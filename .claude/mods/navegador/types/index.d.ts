export type Modo = {
  nome: 'geral' | 'governo' | 'arquitecto' | 'thread' | null
  thread: string | null
}

declare module 'claude-code' {
  interface PluginState {
    navegador: {
      modo: Modo
      extras: string[]
      nosVisiveis: string[]
      bashLivre: boolean
      versao: number
    }
  }
}
