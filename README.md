# project-template

Project template for data scientists who works with project development using python with AI-assisted development. The main goal is to optmize the first steps when starting a new project.

## Setup

```bash
./setup.sh
```

Renomeie `src/project_name/` para o nome do seu pacote e ajuste `pyproject.toml`
(`[project].name`), `README.md` e `CLAUDE.md` de acordo.

## Estrutura

```
src/project_name/   # código do pacote (data/features/models/evaluation)
tests/               # espelha src/
configs/             # hiperparâmetros e paths de experimento (YAML)
data/                # raw/interim/processed/external — raw é somente leitura
models/              # artefatos treinados
notebooks/           # exploração — nunca fonte de verdade
reports/figures/     # saídas geradas para relatórios
```

## Uso

<!-- comando real de execução do pipeline — preencher ao começar o projeto -->

## Comandos de dev

```bash
pytest              # suite de testes
ruff check .         # lint
ruff format .        # formatação
```
