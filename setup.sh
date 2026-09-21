#!/bin/bash

python -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -e .
pip install ruff pre-commit pytest

pre-commit install

echo "Setup completo ✅"
