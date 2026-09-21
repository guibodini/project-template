# project-template

Project template for data scientists who works with project development using python with AI-assisted development. The main goal is to optmize the first steps when starting a new project.

## Setup

```bash
./setup.sh
```

Ajuste `pyproject.toml` (`[project].name`) e `CLAUDE.md` (comandos, guardrails)
para o projeto real. A estrutura de `src/` (subpastas, módulos) só deve ser
criada quando o formato do projeto pedir — ver `arquitetura-projeto.md` nas
regras globais (ML clássico vs. pipeline híbrido).

## Estrutura

```
experimenting/       # EDA, scripts exploratórios e testes iniciais
src/                  # código do pacote (import src) — cresce conforme o projeto pede
tests/                # espelha src/
configs/              # hiperparâmetros e paths de experimento (YAML)
data/                 # input/ (dado bruto) e output/ (resultado gerado)
models/               # artefatos treinados
reports/figures/      # saídas geradas para relatórios
```

## Uso

<!-- comando real de execução do pipeline — preencher ao começar o projeto -->

## Comandos de dev

```bash
pytest              # suite de testes
ruff check .         # lint
ruff format .        # formatação
```
