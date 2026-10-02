// Lógica pura do navegador: ler o MAPA.md, calcular o perímetro, montar o
// recorte local e o prompt do PANORAMA. Sem `$`: testável à parte.

export type No = {
  id: string
  nome: string
  pai: string | null
  estado: string
  dono: string
  logica: string
  divisao: string
  mandato: string
  thread: string
  ficheiros: string[]
}

export type Mapa = { activo: string | null; nos: No[] }

export type NomeModo = 'geral' | 'governo' | 'arquitecto' | 'thread'

export const ESTADOS = ['por abrir', 'em curso', 'resolvido', 'em pausa']

// Um nó é um cabeçalho de nível 2 a 6: `## <ID> — <nome>`. O nível 1 é o título do ficheiro.
const CABECALHO = /^#{2,6}\s+([A-Z][A-Za-z0-9.]{0,11})\s+[—–-]\s+(.+?)\s*$/
const CAMPO = /^-?\s*(pai|estado|dono|l[óo]gica|divis[ãa]o|mandato|thread|ficheiros)\s*:\s*(.*)$/i

const chave = (s: string) =>
  s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')

const vazio = (s: string) => s === '' || s === '—' || s === '-'

export function lerMapa(texto: string): Mapa {
  const linhas = texto.split(/\r?\n/)
  let activo: string | null = null
  let i = 0
  if (linhas[0]?.trim() === '---') {
    for (i = 1; i < linhas.length && (linhas[i] ?? '').trim() !== '---'; i++) {
      const m = /^activo\s*:\s*(\S+)/.exec(linhas[i] ?? '')
      if (m) activo = m[1] ?? null
    }
    i++
  }
  const nos: No[] = []
  let actual: No | null = null
  let ultimo: string | null = null
  for (; i < linhas.length; i++) {
    const linha = linhas[i] ?? ''
    const cab = CABECALHO.exec(linha)
    if (cab) {
      const novo: No = {
        id: cab[1] ?? '', nome: cab[2] ?? '', pai: null, estado: 'por abrir', dono: '',
        logica: '', divisao: '', mandato: '', thread: '', ficheiros: [],
      }
      actual = novo
      nos.push(novo)
      ultimo = null
      continue
    }
    if (!actual) continue
    const campo = CAMPO.exec(linha)
    if (campo) {
      const k = chave(campo[1] ?? '')
      const v = (campo[2] ?? '').trim()
      ultimo = k
      if (k === 'pai') actual.pai = vazio(v) ? null : v
      else if (k === 'estado') actual.estado = v
      else if (k === 'dono') actual.dono = v
      else if (k === 'logica') actual.logica = v
      else if (k === 'divisao') actual.divisao = v
      else if (k === 'mandato') actual.mandato = v
      else if (k === 'thread') actual.thread = vazio(v) ? '' : v
      else if (k === 'ficheiros')
        actual.ficheiros = vazio(v) ? [] : v.split(',').map(f => f.trim()).filter(Boolean)
      continue
    }
    // Continuação de um campo de texto: linha indentada.
    if (ultimo && /^\s{2,}\S/.test(linha)) {
      const v = linha.trim()
      if (ultimo === 'logica') actual.logica += ' ' + v
      else if (ultimo === 'divisao') actual.divisao += ' ' + v
      else if (ultimo === 'mandato') actual.mandato += ' ' + v
    } else if (linha.trim() !== '') {
      ultimo = null
    }
  }
  return { activo, nos }
}

export const noPorId = (m: Mapa, id: string | null) =>
  id === null ? undefined : m.nos.find(n => n.id === id)

export const filhos = (m: Mapa, id: string) => m.nos.filter(n => n.pai === id)

export function caminho(m: Mapa, id: string | null): No[] {
  const out: No[] = []
  const vistos = new Set<string>()
  let no = noPorId(m, id)
  while (no && !vistos.has(no.id)) {
    out.unshift(no)
    vistos.add(no.id)
    no = noPorId(m, no.pai)
  }
  return out
}

export function profundidade(m: Mapa, id: string): number {
  return Math.max(0, caminho(m, id).length - 1)
}

/** Ordem de árvore: cada nó seguido dos filhos, raízes pela ordem do ficheiro. */
export function emArvore(m: Mapa): No[] {
  const out: No[] = []
  const vistos = new Set<string>()
  const visita = (n: No) => {
    if (vistos.has(n.id)) return
    vistos.add(n.id)
    out.push(n)
    filhos(m, n.id).forEach(visita)
  }
  m.nos.filter(n => n.pai === null || !noPorId(m, n.pai)).forEach(visita)
  return out
}

/** Problemas de forma que o mapa não pode ter: o PANORAMA e o painel mostram-nos. */
export function defeitos(m: Mapa): string[] {
  const out: string[] = []
  const ids = new Set<string>()
  for (const n of m.nos) {
    if (ids.has(n.id)) out.push(`${n.id} está repetido`)
    ids.add(n.id)
    if (n.pai !== null && !noPorId(m, n.pai)) out.push(`${n.id}: pai ${n.pai} não existe`)
    if (n.pai !== null && n.logica === '') out.push(`${n.id} não tem lógica`)
    if (filhos(m, n.id).length > 0 && n.divisao === '')
      out.push(`${n.id} divide-se mas não diz porquê (divisão)`)
  }
  if (m.activo !== null && !noPorId(m, m.activo)) out.push(`activo ${m.activo} não existe`)
  return out
}

// ---------------------------------------------------------------- perímetro

export const SEMPRE = ['CLAUDE.md']

export function baseDoModo(modo: NomeModo | null, pastaThread: string | null): string[] {
  switch (modo) {
    case 'governo':
      return ['FLUXO-DE-PROJECTO.md', 'BRANCHES.md', '30-THREADS/_TEMPLATE/**', '30-THREADS/*/CLAUDE.md']
    case 'arquitecto':
      return ['ESTADO.md', 'REJEICOES.md', 'INBOX.md', 'THREADS.md', 'THREAD-MENSAGENS.md',
        'HANDOFF.md', 'REGISTO-DOCUMENTOS.md', 'Jardim.html']
    case 'thread':
      return ['THREADS.md', 'INBOX.md', 'THREAD-MENSAGENS.md', 'REGISTO-DOCUMENTOS.md',
        ...(pastaThread ? [`30-THREADS/${pastaThread}/**`] : [])]
    default:
      return []
  }
}

/** Uma pasta escrita como `X/` vale `X/**`. */
export const normalizarPadrao = (p: string) =>
  p.replace(/^\.\//, '').replace(/^\/+/, '').replace(/\/$/, '/**')

function padraoParaRegex(p: string): RegExp {
  let r = ''
  for (let i = 0; i < p.length; i++) {
    const c = p[i] ?? ''
    if (c === '*' && p[i + 1] === '*') {
      r += '.*'
      i++
      if (p[i + 1] === '/') i++
    } else if (c === '*') r += '[^/]*'
    else if (c === '?') r += '[^/]'
    else r += c.replace(/[.+^${}()|[\]\\]/g, '\\$&')
  }
  return new RegExp(`^${r}$`)
}

/** Um ficheiro (ou pasta) relativo à raiz está dentro do perímetro? */
export function dentro(rel: string, padroes: string[]): boolean {
  const alvo = rel.replace(/\/+$/, '')
  return padroes.map(normalizarPadrao).some(p => {
    if (padraoParaRegex(p).test(alvo)) return true
    // Uma pasta conta quando é a base de um `X/**` ou fica abaixo dela.
    if (p.endsWith('/**')) {
      const base = p.slice(0, -3)
      if (!/[*?]/.test(base) && (alvo === base || alvo.startsWith(base + '/'))) return true
    }
    return false
  })
}

/** Caminho absoluto ou relativo → relativo à raiz; null se fica fora dela. */
export function relativo(caminhoFicheiro: string, raiz: string): string | null {
  const abs = caminhoFicheiro.startsWith('/') ? caminhoFicheiro : `${raiz}/${caminhoFicheiro}`
  const partes: string[] = []
  for (const s of abs.split('/')) {
    if (s === '' || s === '.') continue
    if (s === '..') partes.pop()
    else partes.push(s)
  }
  const norm = '/' + partes.join('/')
  const r = raiz.replace(/\/+$/, '')
  if (norm === r) return ''
  return norm.startsWith(r + '/') ? norm.slice(r.length + 1) : null
}

// ---------------------------------------------------------------- bash

const GIT_SEGURO = new Set([
  'status', 'log', 'add', 'commit', 'push', 'pull', 'fetch', 'branch', 'checkout',
  'switch', 'worktree', 'rev-parse', 'remote', 'restore', 'merge', 'tag',
])

/** Parte um comando em segmentos por `&&`, `||`, `;`, `|`, respeitando aspas. */
export function segmentos(cmd: string): string[] {
  const out: string[] = []
  let cur = ''
  let aspa: string | null = null
  for (let i = 0; i < cmd.length; i++) {
    const c = cmd[i] ?? ''
    if (aspa) {
      cur += c
      if (c === aspa) aspa = null
      continue
    }
    if (c === '"' || c === "'") { aspa = c; cur += c; continue }
    if (c === '\n' || c === ';' || c === '|' || (c === '&' && cmd[i + 1] === '&')) {
      if (cur.trim()) out.push(cur.trim())
      cur = ''
      if ((c === '&' || c === '|') && cmd[i + 1] === c) i++
      continue
    }
    cur += c
  }
  if (cur.trim()) out.push(cur.trim())
  return out
}

/** Bash permitido sem «bash livre»: só git que não mostra conteúdo, ls, pwd, claude plugin. */
export function bashSeguro(cmd: string): { ok: true } | { ok: false; motivo: string } {
  // Entre aspas duplas a shell ainda avalia $( ) e ` `: só as simples os neutralizam.
  if (/\$\(|`/.test(cmd.replace(/'[^']*'/g, "''")))
    return { ok: false, motivo: 'substituição de comando' }
  if (/<<|>|</.test(cmd.replace(/"[^"]*"|'[^']*'/g, '""')))
    return { ok: false, motivo: 'heredoc ou redireccionamento' }
  for (const seg of segmentos(cmd)) {
    const pal = seg.split(/\s+/)
    const p0 = pal[0] ?? ''
    const p1 = pal[1] ?? ''
    if (p0 === 'cd' || p0 === 'pwd' || p0 === 'ls') continue
    if (p0 === 'claude' && p1 === 'plugin') continue
    if (p0 === 'git') {
      const sub = pal.slice(1).find(w => !w.startsWith('-')) ?? ''
      if (GIT_SEGURO.has(sub)) continue
      if (sub === 'diff' && pal.some(w => /^--(stat|name-only|shortstat|name-status)$/.test(w))) continue
      return { ok: false, motivo: `git ${sub} mostra conteúdo de ficheiros` }
    }
    return { ok: false, motivo: `\`${p0}\` não está na lista segura` }
  }
  return { ok: true }
}

// ---------------------------------------------------------------- texto para o modelo

const linhaNo = (n: No, comLogica: boolean) =>
  `- ${n.id} — ${n.nome} [${n.estado}${n.dono ? ' · ' + n.dono : ''}]` +
  (comLogica && n.logica ? `\n  lógica: ${n.logica}` : '')

/** O que o modelo sabe em cada turno: o nó activo e, do pai, só a divisão. */
export function contexto(m: Mapa, modo: string, perimetro: string[]): string {
  const no = noPorId(m, m.activo)
  const l: string[] = ['# Navegador', `Modo: ${modo}.`]
  if (!no) {
    l.push('Nenhum nó activo no MAPA.md. Pede ao David para escolher um (/activo <id>).')
  } else {
    l.push(`Tarefa activa: ${no.id} — ${no.nome} [${no.estado}${no.dono ? ' · ' + no.dono : ''}]`)
    if (no.logica) l.push(`Porque existe: ${no.logica}`)
    if (no.mandato) l.push(`Mandato: ${no.mandato}`)
    if (no.thread) l.push(`Thread: ${no.thread}`)
    const pai = noPorId(m, no.pai)
    if (pai) l.push(`Pai ${pai.id} — ${pai.nome}. Porque se divide assim: ${pai.divisao || '(não declarado)'}`)
    const fs = filhos(m, no.id)
    if (fs.length) l.push('Filhos:', ...fs.map(f => linhaNo(f, false)))
  }
  l.push(
    `Perímetro (só isto podes ler ou escrever no repositório): ${perimetro.join(', ') || '(vazio)'}.`,
    'Fora dele o navegador recusa. Se precisares de mais, pede ao David que o seleccione em /mapa. O MAPA.md não se lê directamente.',
  )
  return l.join('\n')
}

/** O prompt do PANORAMA: o recorte local e as perguntas, por ordem. */
export function panorama(m: Mapa, opts: {
  visiveis: string[]
  mandatoThread: string | null
  defeitos: string[]
}): string {
  const no = noPorId(m, m.activo)
  const l: string[] = [
    'PANORAMA — pára o que estás a fazer. Não executes nenhuma ferramenta antes de responder.',
    '',
  ]
  if (!no) {
    l.push('Não há nó activo no MAPA.md. Diz isso ao David e pára.')
    return l.join('\n')
  }
  const pai = noPorId(m, no.pai)
  l.push('## O que vês (só isto)')
  if (pai) {
    l.push(`**Pai** ${pai.id} — ${pai.nome}`, `- porque se divide assim: ${pai.divisao || '(não declarado)'}`)
    const irmaos = filhos(m, pai.id).filter(n => n.id !== no.id)
    l.push('**Irmãos**', ...(irmaos.length ? irmaos.map(n => linhaNo(n, true)) : ['- (nenhum)']))
  } else {
    l.push('**Pai** — (este nó é a raiz)')
  }
  l.push(
    `**Tu** ${no.id} — ${no.nome} [${no.estado}${no.dono ? ' · ' + no.dono : ''}]`,
    `- lógica: ${no.logica || '(não declarada)'}`,
    `- mandato: ${no.mandato || '(não declarado)'}`,
  )
  if (no.thread) l.push(`- thread: ${no.thread}`)
  if (opts.mandatoThread) l.push('- mandato da thread (thread.md):', ...opts.mandatoThread.split('\n').map(s => '  ' + s))
  const fs = filhos(m, no.id)
  l.push('**Filhos**', ...(fs.length ? fs.map(n => linhaNo(n, true)) : ['- (nenhum)']))
  const extra = opts.visiveis
    .map(id => noPorId(m, id))
    .filter((n): n is No => !!n && n.id !== no.id && n.id !== pai?.id && n.pai !== no.id && n.pai !== pai?.id)
  if (extra.length) l.push('**Seleccionados pelo David**', ...extra.map(n => linhaNo(n, true)))
  if (opts.defeitos.length) l.push('**Defeitos de forma do mapa**', ...opts.defeitos.map(d => `- ${d}`))
  l.push(
    '',
    '## Responde por esta ordem. Não passes ao passo seguinte sem fechar o anterior.',
    '1. **Ainda sigo uma lógica no que estou a fazer, ou já derivei em relação à tarefa?** Confronta o que fizeste desde o último PANORAMA (ou desde o início da tarefa) com o mandato. Dá exemplos concretos.',
    '2. **Sei reformular toda a lógica do que estou a fazer?** Do pai até à tarefa, por palavras tuas: porque o pai existe dividido assim, porque esta tarefa é a parte que é, e o que o trabalho actual entrega a ela. Se não souberes, diz que não sabes — isso já é a conclusão.',
    '3. Só depois: **manter, reordenar ou reestruturar**, com justificação. Não alteres nada no mapa: propõe, o David decide.',
  )
  return l.join('\n')
}

/** Extrai do thread.md a secção do mandato (até ao próximo cabeçalho), cortada. */
export function mandatoDoThread(texto: string, max = 1500): string | null {
  const linhas = texto.split(/\r?\n/)
  const ini = linhas.findIndex(s => /^#{1,6}\s.*mandato/i.test(s))
  if (ini < 0) return null
  const nivel = (/^#+/.exec(linhas[ini] ?? '')?.[0] ?? '#').length
  const corpo: string[] = []
  for (let i = ini + 1; i < linhas.length; i++) {
    const linha = linhas[i] ?? ''
    const h = /^(#+)\s/.exec(linha)
    if (h && (h[1] ?? '').length <= nivel) break
    corpo.push(linha)
  }
  const t = corpo.join('\n').trim()
  if (!t) return null
  return t.length > max ? t.slice(0, max) + ' […]' : t
}

/** Reescreve o `activo:` do front matter. */
export function definirActivo(texto: string, id: string): string {
  if (/^---\r?\n[\s\S]*?^activo\s*:.*$/m.test(texto))
    return texto.replace(/^activo\s*:.*$/m, `activo: ${id}`)
  if (texto.startsWith('---')) return texto.replace(/^---\r?\n/, `---\nactivo: ${id}\n`)
  return `---\nactivo: ${id}\n---\n${texto}`
}

/** Reescreve o `estado:` do nó `id`. */
export function definirEstado(texto: string, id: string, estado: string): string | null {
  const linhas = texto.split('\n')
  let dentroNo = false
  for (let i = 0; i < linhas.length; i++) {
    const linha = linhas[i] ?? ''
    const cab = CABECALHO.exec(linha)
    if (cab) { dentroNo = cab[1] === id; continue }
    if (dentroNo && /^-?\s*estado\s*:/i.test(linha)) {
      linhas[i] = linha.replace(/(estado\s*:\s*).*$/i, `$1${estado}`)
      return linhas.join('\n')
    }
  }
  return null
}

export function lerModo(texto: string): { nome: NomeModo; thread: string | null } | null {
  const t = chave(texto.trim()).replace(/[.!]$/, '')
  const m = /^(?:modo\s+)?(geral|governo|arquitecto|arquiteto|thread)(?:\s+(t?\d{1,3}))?$/.exec(t)
  if (!m) return null
  const nome = (m[1] === 'arquiteto' ? 'arquitecto' : m[1]) as NomeModo
  const n = m[2]?.replace(/^t/, '')
  return { nome, thread: nome === 'thread' && n ? `T${n.padStart(3, '0')}` : null }
}
