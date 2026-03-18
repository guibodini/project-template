#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install ruff pre-commit pytest

pre-commit install

echo "Setup completo ✅"