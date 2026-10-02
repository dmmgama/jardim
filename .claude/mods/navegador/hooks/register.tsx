import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { Modo } from '../types'
import {
  ESTADOS, SEMPRE, baseDoModo, bashSeguro, caminho, contexto, defeitos, definirActivo,
  definirEstado, dentro, emArvore, lerMapa, lerModo, mandatoDoThread, noPorId, normalizarPadrao,
  panorama, profundidade, relativo,
} from './mapa'
import type { Mapa } from './mapa'

const MAPA = 'MAPA.md'
const PANE = 'navegador-mapa'

const modo = atom({ plugin: 'navegador', key: 'modo' } as const, { nome: null, thread: null } as Modo)
const extras = atom({ plugin: 'navegador', key: 'extras' } as const, [] as string[])
const nosVisiveis = atom({ plugin: 'navegador', key: 'nosVisiveis' } as const, [] as string[])
const bashLivre = atom({ plugin: 'navegador', key: 'bashLivre' } as const, false)
// Sobe a cada escrita do MAPA.md feita pelo mod, para redesenhar quem o lê.
const versao = atom({ plugin: 'navegador', key: 'versao' } as const, 0)

type Ctx = {
  raiz: string
  mapa: Mapa
  modo: Modo
  pastaThread: string | null
  perimetro: string[]
}

/** null quando não há MAPA.md na raiz: aí o navegador não governa nada. */
async function carregar($: EngineInterface): Promise<Ctx | null> {
  const raiz = (await $.session.cwd()).replace(/\/+$/, '')
  const texto = await $.fs.read(`${raiz}/${MAPA}`).catch(() => null)
  if (typeof texto !== 'string') return null
  const mapa = lerMapa(texto)
  const m = await read($, modo)
  const pastaThread = m.thread ? await pastaDaThread($, raiz, m.thread) : null
  const no = noPorId(mapa, mapa.activo)
  const perimetro = [
    ...SEMPRE,
    ...baseDoModo(m.nome, pastaThread),
    ...(no?.ficheiros ?? []),
    ...(await read($, extras)),
  ].map(normalizarPadrao)
  return { raiz, mapa, modo: m, pastaThread, perimetro: [...new Set(perimetro)] }
}

async function pastaDaThread($: EngineInterface, raiz: string, id: string): Promise<string | null> {
  const lista = await $.fs.list(`${raiz}/30-THREADS`).catch(() => [])
  return lista.find(e => e.kind === 'dir' && e.name.startsWith(id))?.name ?? null
}

const nomeModo = (m: Modo) =>
  m.nome === null ? 'por definir' : m.nome.toUpperCase() + (m.thread ? ` ${m.thread}` : '')

function linhaEstado(c: Ctx): string {
  const passos = caminho(c.mapa, c.mapa.activo).map(n => n.id)
  const no = noPorId(c.mapa, c.mapa.activo)
  return `◉ ${passos.join(' › ') || 'sem nó activo'}${no ? ' ' + no.nome : ''} · ${nomeModo(c.modo)}`
}

async function refrescarEstado($: EngineInterface) {
  const c = await carregar($)
  $.ui.status(c ? linhaEstado(c) : undefined)
}

async function escreverMapa($: EngineInterface, fn: (t: string) => string | null): Promise<boolean> {
  const raiz = (await $.session.cwd()).replace(/\/+$/, '')
  const texto = await $.fs.read(`${raiz}/${MAPA}`).catch(() => null)
  if (typeof texto !== 'string') return false
  const novo = fn(texto)
  if (novo === null) return false
  await $.fs.write(`${raiz}/${MAPA}`, novo)
  await update($, versao, v => v + 1)
  await refrescarEstado($)
  return true
}

async function enviarPanorama($: EngineInterface): Promise<string> {
  const c = await carregar($)
  if (!c) return 'Não há MAPA.md na raiz.'
  const no = noPorId(c.mapa, c.mapa.activo)
  let mandatoThread: string | null = null
  if (no?.thread) {
    const pasta = await pastaDaThread($, c.raiz, no.thread.split(/\s/)[0] ?? no.thread)
    const t = pasta ? await $.fs.read(`${c.raiz}/30-THREADS/${pasta}/thread.md`).catch(() => null) : null
    if (typeof t === 'string') mandatoThread = mandatoDoThread(t)
  }
  const texto = panorama(c.mapa, {
    visiveis: await read($, nosVisiveis),
    mandatoThread,
    defeitos: defeitos(c.mapa),
  })
  await $.prompt.submit({ text: texto })
  return 'PANORAMA enviado.'
}

const FALHA = 'navegador: erro interno ao verificar o perímetro — recusado por precaução.'

/** Decide se um caminho do repositório pode ser tocado. Em erro, recusa (o motor deixaria passar). */
async function guarda($: EngineInterface, alvo: string | undefined, accao: string): Promise<string | null> {
  try {
    return await guardaSemRede($, alvo, accao)
  } catch {
    return FALHA
  }
}

async function guardaSemRede($: EngineInterface, alvo: string | undefined, accao: string) {
  const c = await carregar($)
  if (!c) return null
  const rel = relativo(alvo ?? c.raiz, c.raiz)
  if (rel === null) return null // fora do repositório: não é connosco
  const mapaAberto = (await read($, extras)).map(normalizarPadrao).includes(MAPA)
  if (rel === MAPA && !mapaAberto)
    return `navegador: o ${MAPA} não se ${accao} directamente. Vês o recorte que te é dado; para mudar o nó activo ou um estado, o David usa /activo e /estado.`
  if (rel === '' || !dentro(rel, c.perimetro))
    return `navegador: «${rel || '(raiz do repositório)'}» está fora do perímetro de ${c.mapa.activo ?? '(sem nó activo)'} em modo ${nomeModo(c.modo)}. Perímetro: ${c.perimetro.join(', ')}. Pede ao David que o seleccione em /mapa.`
  return null
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'mapa', description: 'Navegador: árvore, selecção de nós e ficheiros, perímetro' })
    await $.command.register({ name: 'panorama', description: 'Navegador: parar e rever a lógica do que se está a fazer' })
    await $.command.register({ name: 'activo', description: 'Navegador: /activo <id> muda o nó activo' })
    await $.command.register({ name: 'estado', description: `Navegador: /estado <id> <${ESTADOS.join(' | ')}>` })
    await $.command.register({ name: 'modo', description: 'Navegador: /modo geral | governo | arquitecto | thread <N>' })
    await refrescarEstado($)
    return next(e)
  })

  // ------------------------------------------------------------ modo de sessão

  on('prompt.submit', async ($, e, next) => {
    const m = lerModo(e.text)
    if (m) {
      await update($, modo, () => m)
      await refrescarEstado($)
    }
    return next(e)
  })

  on('command.run', { command: 'modo' }, async ($, e) => {
    const m = lerModo(e.args)
    if (!m) return { text: 'Usa: /modo geral | governo | arquitecto | thread <N>' }
    await update($, modo, () => m)
    await refrescarEstado($)
    return { text: `Modo ${nomeModo(m)}.` }
  })

  // ------------------------------------------------------------ perímetro

  on('tool.call', { tool: 'Read' }, async ($, e, next) => {
    const deny = await guarda($, e.file_path, 'lê')
    return deny ? { deny } : next(e)
  })
  on('tool.call', { tool: 'Edit' }, async ($, e, next) => {
    const deny = await guarda($, e.file_path, 'edita')
    return deny ? { deny } : next(e)
  })
  on('tool.call', { tool: 'Write' }, async ($, e, next) => {
    const deny = await guarda($, e.file_path, 'escreve')
    return deny ? { deny } : next(e)
  })
  on('tool.call', { tool: 'NotebookEdit' }, async ($, e, next) => {
    const deny = await guarda($, e.notebook_path, 'edita')
    return deny ? { deny } : next(e)
  })
  on('tool.call', { tool: 'Glob' }, async ($, e, next) => {
    const deny = await guarda($, e.path, 'lista')
    return deny ? { deny } : next(e)
  })
  on('tool.call', { tool: 'Grep' }, async ($, e, next) => {
    const deny = await guarda($, e.path, 'pesquisa')
    return deny ? { deny } : next(e)
  })
  on('tool.call', { tool: 'Bash' }, async ($, e, next) => {
    const c = await carregar($).catch(() => 'erro' as const)
    if (c === 'erro') return { deny: FALHA }
    if (!c || (await read($, bashLivre))) return next(e)
    const r = bashSeguro(e.command)
    return r.ok
      ? next(e)
      : { deny: `navegador: Bash restrito (${r.motivo}). Usa Read/Edit dentro do perímetro, ou pede ao David que ligue «Bash livre» em /mapa.` }
  })

  // ------------------------------------------------------------ o que o modelo sabe

  on('prompt.compose', async ($, e, next) => {
    const r = await next(e)
    const c = await carregar($)
    if (!c) return r
    return {
      sections: [...r.sections, { id: 'navegador:contexto', text: contexto(c.mapa, nomeModo(c.modo), c.perimetro), scope: 'session' }],
    }
  })

  // ------------------------------------------------------------ comandos

  on('command.run', { command: 'panorama' }, async $ => ({ text: await enviarPanorama($) }))

  on('command.run', { command: 'mapa' }, async $ => {
    await $.ui.open({ id: PANE, title: 'Mapa', focus: true })
    return { text: 'Mapa aberto.' }
  })

  on('command.run', { command: 'activo' }, async ($, e) => {
    const id = e.args.trim()
    const c = await carregar($)
    if (!c) return { text: 'Não há MAPA.md na raiz.' }
    if (!noPorId(c.mapa, id)) return { text: `Não existe o nó «${id}».` }
    await escreverMapa($, t => definirActivo(t, id))
    return { text: `Nó activo: ${id}.` }
  })

  on('command.run', { command: 'estado' }, async ($, e) => {
    const [id = '', ...resto] = e.args.trim().split(/\s+/)
    const estado = resto.join(' ').toLowerCase()
    if (!ESTADOS.includes(estado)) return { text: `Estado inválido. Usa: ${ESTADOS.join(' | ')}.` }
    const ok = await escreverMapa($, t => definirEstado(t, id, estado))
    return { text: ok ? `${id}: ${estado}.` : `Não encontrei o campo estado do nó «${id}».` }
  })

  // ------------------------------------------------------------ desenho

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    if (e.props.hasSurvey) return next(e)
    await read($, versao)
    await read($, modo)
    const c = await carregar($)
    if (!c) return next(e)
    const { Box, Button, Text } = $.ui.resolve(e)
    return (
      <Box>
        <Text dimColor>{linhaEstado(c)} </Text>
        <Button key="panorama" label="⏸ PANORAMA" variant="primary" onPress={() => void enviarPanorama($)} />
        <Text> </Text>
        <Button key="mapa" label="Mapa" onPress={() => void $.ui.open({ id: PANE, title: 'Mapa', focus: true })} />
      </Box>
    )
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const tabela = $.ui.resolve(e)
    const { Box, Button, Text } = tabela
    // O telemóvel não tem Input: aí a caixa de ficheiros não aparece.
    const Input = 'Input' in tabela ? tabela.Input : null
    await read($, versao)
    const c = await carregar($)
    if (!c) return <Text>Não há MAPA.md na raiz do repositório.</Text>
    const vis = await read($, nosVisiveis)
    const ext = await read($, extras)
    const livre = await read($, bashLivre)
    const mapaAberto = ext.map(normalizarPadrao).includes(MAPA)
    const erros = defeitos(c.mapa)

    return (
      <Box flexDirection="column">
        <Text bold>Modo {nomeModo(c.modo)}</Text>
        <Text dimColor>Nós: «ver» põe o nó no PANORAMA do Claude. «activar» torna-o a tarefa activa.</Text>
        {emArvore(c.mapa).map(n => {
          const activo = n.id === c.mapa.activo
          const visto = vis.includes(n.id)
          return (
            <Box key={`no-${n.id}`}>
              <Text bold={activo}>
                {'  '.repeat(profundidade(c.mapa, n.id))}{activo ? '◉' : '○'} {n.id} — {n.nome} [{n.estado}]{' '}
              </Text>
              <Button
                key={`ver-${n.id}`}
                label={visto ? '✓ vê' : 'ver'}
                dimColor={!visto}
                onPress={() => void update($, nosVisiveis, l => (l.includes(n.id) ? l.filter(x => x !== n.id) : [...l, n.id]))}
              />
              {!activo && (
                <Button key={`act-${n.id}`} label="activar" dimColor onPress={() => void escreverMapa($, t => definirActivo(t, n.id))} />
              )}
            </Box>
          )
        })}
        {erros.length > 0 && <Text color="yellow">Defeitos: {erros.join(' · ')}</Text>}

        <Text bold> </Text>
        <Text bold>Perímetro do Claude</Text>
        <Text dimColor>{c.perimetro.join(', ')}</Text>

        <Text bold> </Text>
        <Text bold>Ficheiros extra (só nesta sessão)</Text>
        {ext.length === 0 && <Text dimColor>(nenhum)</Text>}
        {ext.map(f => (
          <Box key={`ext-${f}`}>
            <Text>{f} </Text>
            <Button key={`rm-${f}`} label="tirar" dimColor onPress={() => void update($, extras, l => l.filter(x => x !== f))} />
          </Box>
        ))}
        {Input && <Input
          key="novo-extra"
          label="Adicionar: "
          placeholder="caminho ou padrão, ex. 10-LOCAL/** ou ESTADO.md"
          submitLabel="adicionar"
          onSubmit={(v: string) => {
            const p = normalizarPadrao(v.trim())
            if (p) void update($, extras, l => (l.includes(p) ? l : [...l, p]))
          }}
        />}
        <Box>
          <Button
            key="mapa-aberto"
            label={mapaAberto ? '✓ MAPA.md aberto ao Claude' : 'Abrir MAPA.md ao Claude'}
            dimColor={!mapaAberto}
            onPress={() => void update($, extras, l => (l.includes(MAPA) ? l.filter(x => x !== MAPA) : [...l, MAPA]))}
          />
          <Text> </Text>
          <Button
            key="bash"
            label={livre ? '✓ Bash livre' : 'Bash livre'}
            dimColor={!livre}
            onPress={() => void update($, bashLivre, b => !b)}
          />
          <Text> </Text>
          <Button key="limpar" label="Limpar selecção" dimColor onPress={() => {
            void update($, extras, () => [])
            void update($, nosVisiveis, () => [])
            void update($, bashLivre, () => false)
          }} />
        </Box>
      </Box>
    )
  })
}
