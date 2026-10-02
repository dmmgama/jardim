import { describe, expect, test } from 'claude-code/testing'

import {
  bashSeguro, contexto, defeitos, definirActivo, definirEstado, dentro, lerMapa, lerModo,
  panorama, relativo,
} from '../hooks/mapa'

const MAPA = `---
activo: B1
---
# MAPA

## A — Raiz
- pai: —
- estado: em curso
- divisão: divide-se em B e C porque sim
- mandato: resolver tudo

## B — Ramo B
- pai: A
- estado: por abrir
- lógica: B cobre metade
- divisão: B1 e B2 são as duas partes de B

## B1 — Folha B1
- pai: B
- estado: em curso
- dono: @Claude
- lógica: B1 é a primeira parte
  e continua aqui
- mandato: entregar o B1
- ficheiros: docs/b1/, notas.md

## B2 — Folha B2
- pai: B
- lógica: B2 é a segunda parte

## C — Ramo C
- pai: A
- lógica: C cobre a outra metade
- divisão: C só tem X

## X — Segredo
- pai: C
- lógica: não devia aparecer
`

const RAIZ = '/repo'

describe('MAPA.md', () => {
  test('lê nós, campos e continuação', () => {
    const m = lerMapa(MAPA)
    expect(m.activo).toBe('B1')
    expect(m.nos.map(n => n.id)).toEqual(['A', 'B', 'B1', 'B2', 'C', 'X'])
    const b1 = m.nos[2]!
    expect(b1.pai).toBe('B')
    expect(b1.logica).toBe('B1 é a primeira parte e continua aqui')
    expect(b1.ficheiros).toEqual(['docs/b1/', 'notas.md'])
    expect(defeitos(m)).toEqual([])
  })

  test('assinala nó sem lógica e divisão por declarar', () => {
    const m = lerMapa('## A — a\n- pai: —\n## B — b\n- pai: A\n')
    expect(defeitos(m)).toEqual(['A divide-se mas não diz porquê (divisão)', 'B não tem lógica'])
  })

  test('muda o activo e o estado sem tocar no resto', () => {
    const t = definirEstado(definirActivo(MAPA, 'C'), 'B', 'resolvido')!
    const m = lerMapa(t)
    expect(m.activo).toBe('C')
    expect(m.nos.find(n => n.id === 'B')!.estado).toBe('resolvido')
    expect(m.nos.find(n => n.id === 'B1')!.estado).toBe('em curso')
  })

  test('o estado de um nó sem campo estado não se inventa', () => {
    expect(definirEstado(MAPA, 'C', 'resolvido')).toBe(null)
  })
})

describe('perímetro', () => {
  const p = ['CLAUDE.md', 'docs/b1/', 'notas.md', '30-THREADS/*/CLAUDE.md']

  test('permite o que está declarado e nega o resto', () => {
    expect(dentro('notas.md', p)).toBe(true)
    expect(dentro('docs/b1/x/y.md', p)).toBe(true)
    expect(dentro('docs/b1', p)).toBe(true)
    expect(dentro('30-THREADS/T004-geometria/CLAUDE.md', p)).toBe(true)
    expect(dentro('30-THREADS/T004-geometria/thread.md', p)).toBe(false)
    expect(dentro('docs', p)).toBe(false)
    expect(dentro('docs/b10/z.md', p)).toBe(false)
    expect(dentro('ESTADO.md', p)).toBe(false)
  })

  test('caminhos relativos à raiz, com .. resolvido', () => {
    expect(relativo('/repo/a/b.md', RAIZ)).toBe('a/b.md')
    expect(relativo('/repo/docs/b1/../../ESTADO.md', RAIZ)).toBe('ESTADO.md')
    expect(relativo('a.md', RAIZ)).toBe('a.md')
    expect(relativo('/repo', RAIZ)).toBe('')
    expect(relativo('/tmp/x', RAIZ)).toBe(null)
    expect(relativo('/repository/x', RAIZ)).toBe(null)
  })
})

describe('bash', () => {
  test('git que não mostra conteúdo passa', () => {
    expect(bashSeguro('git status && git add -A && git commit -m "a; b | c"')).toEqual({ ok: true })
    expect(bashSeguro('git diff --stat')).toEqual({ ok: true })
    expect(bashSeguro('ls 30-THREADS')).toEqual({ ok: true })
  })

  test('leituras de conteúdo são recusadas', () => {
    expect(bashSeguro('cat ESTADO.md').ok).toBe(false)
    expect(bashSeguro('git status; grep x ESTADO.md').ok).toBe(false)
    expect(bashSeguro('git show HEAD:ESTADO.md').ok).toBe(false)
    expect(bashSeguro('git diff ESTADO.md').ok).toBe(false)
    expect(bashSeguro('git commit -m "$(cat ESTADO.md)"').ok).toBe(false)
    expect(bashSeguro("git commit -m '$(nada)'").ok).toBe(true)
    expect(bashSeguro('git log > out.txt').ok).toBe(false)
    expect(bashSeguro('echo `cat ESTADO.md`').ok).toBe(false)
  })
})

describe('modo', () => {
  test('reconhece a resposta à pergunta de arranque', () => {
    expect(lerModo('Geral')).toEqual({ nome: 'geral', thread: null })
    expect(lerModo('arquiteto')).toEqual({ nome: 'arquitecto', thread: null })
    expect(lerModo('thread 4')).toEqual({ nome: 'thread', thread: 'T004' })
    expect(lerModo('modo thread T005')).toEqual({ nome: 'thread', thread: 'T005' })
    expect(lerModo('geral, e já agora...')).toBe(null)
  })
})

describe('o que o modelo vê', () => {
  test('contexto: do pai só a divisão; nada de irmãos nem do resto', () => {
    const t = contexto(lerMapa(MAPA), 'GERAL', ['CLAUDE.md'])
    expect(t).toContain('Tarefa activa: B1 — Folha B1')
    expect(t).toContain('B1 e B2 são as duas partes de B')
    expect(t).not.toContain('B cobre metade')
    expect(t).not.toContain('Folha B2')
    expect(t).not.toContain('Raiz')
    expect(t).not.toContain('Segredo')
  })

  test('PANORAMA: pai, irmãos, filhos e tarefa; o resto só se seleccionado', () => {
    const m = lerMapa(MAPA)
    const t = panorama(m, { visiveis: [], mandatoThread: null, defeitos: [] })
    expect(t).toContain('B1 e B2 são as duas partes de B')
    expect(t).toContain('B2 — Folha B2')
    expect(t).toContain('mandato: entregar o B1')
    expect(t).not.toContain('Segredo')
    expect(t).not.toContain('Raiz')
    expect(t.indexOf('1. **Ainda sigo')).toBeLessThan(t.indexOf('2. **Sei reformular'))
    expect(t.indexOf('2. **Sei reformular')).toBeLessThan(t.indexOf('3. Só depois'))
    const comX = panorama(m, { visiveis: ['X'], mandatoThread: null, defeitos: [] })
    expect(comX).toContain('X — Segredo')
  })
})

describe('hook de perímetro (integração)', () => {
  const comRepo = (on: Parameters<Parameters<typeof test>[1] & ((...a: any[]) => any)>[1]) => {
    on('session.cwd', () => ({ value: RAIZ }))
    on('fs.read', ($: unknown, e: { path: string }) => {
      if (e.path === `${RAIZ}/MAPA.md`) return { value: MAPA }
      throw new Error('ENOENT')
    })
    on('fs.list', () => ({ value: [] }))
    on('tool.call', () => ({ result: 'lido' }))
  }

  test('lê dentro do perímetro do nó activo', async ($, on) => {
    comRepo(on)
    const r = await $.tool.call({ tool: 'Read', file_path: `${RAIZ}/docs/b1/a.md` })
    expect(r.deny).toBe(undefined)
  })

  test('recusa fora do perímetro e o próprio MAPA.md', async ($, on) => {
    comRepo(on)
    const fora = await $.tool.call({ tool: 'Read', file_path: `${RAIZ}/ESTADO.md` })
    expect(String(fora.deny)).toContain('fora do perímetro')
    const mapa = await $.tool.call({ tool: 'Edit', file_path: `${RAIZ}/MAPA.md`, old_string: 'a', new_string: 'b' })
    expect(String(mapa.deny)).toContain('não se edita directamente')
    const grep = await $.tool.call({ tool: 'Grep', pattern: 'x' })
    expect(String(grep.deny)).toContain('raiz do repositório')
  })

  test('fora do repositório não é com o navegador', async ($, on) => {
    comRepo(on)
    const r = await $.tool.call({ tool: 'Read', file_path: '/tmp/x.md' })
    expect(r.deny).toBe(undefined)
  })

  test('bash restrito por omissão', async ($, on) => {
    comRepo(on)
    const r = await $.tool.call({ tool: 'Bash', command: 'cat ESTADO.md' })
    expect(String(r.deny)).toContain('Bash restrito')
    const ok = await $.tool.call({ tool: 'Bash', command: 'git status' })
    expect(ok.deny).toBe(undefined)
  })
})
