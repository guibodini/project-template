# {{nome_do_projeto}} — Índice de Comandos e Guardas

Este arquivo é operacional, não de convenção de estilo — estilo/design de
código já vive nas regras globais do usuário (`~/.claude/CLAUDE.md` e
`rules/*.md`, citando Código Limpo/Python Fluente/Effective Python). O que
vai aqui é só o que é específico deste repo: comando real, caminho que não
se toca, ação que precisa confirmação. Preencha as seções abaixo ao usar
este template como ponto de partida de um projeto novo.

## Comandos de dev

```bash
pytest                          # suite de testes completa (tests/)
pytest tests/test_x.py -v       # um arquivo específico
ruff check .                    # lint — deve passar sem erro
ruff format .                   # formatação
pip install -e .                # instala o pacote em modo editável (src layout)
# python main.py ...            # comando real de execução do pipeline — preencher
```

## Nunca editar à mão

- `.env` — nunca ler o conteúdo (credenciais, chaves de API). Existência do
  arquivo pode ser checada; valor não. Perguntar ao usuário se precisar de
  algum valor.
- `models/` — artefato treinado, não código; troca de modelo é decisão de
  treino, não edição manual.
- <!-- adicionar aqui outros artefatos gerados/encriptados específicos deste projeto -->

## Guardrails de ação

- **Git**: push da branch + abrir PR no GitHub — nunca `git merge` ou
  `push origin main` direto, a menos que pedido explicitamente.
- **Produção**: nunca rodar comandos que escrevem em ambiente de
  produção (banco, storage compartilhado) sem pedido explícito — mesmo
  para auditoria/checagem pontual.
- <!-- adicionar aqui guardrails específicos deste projeto (paths de output, custo de API, etc.) -->

## Revisão de código

Antes de considerar uma mudança em `.py` pronta, rodar o subagente
`code-reviewer` (`.claude/agents/code-reviewer.md`) — julga design/clareza
contra Código Limpo/Python Fluente/Effective Python; `ruff` já cobre estilo
automaticamente (via hook em `.claude/hooks/ruff_check.py`), isso aqui não.
