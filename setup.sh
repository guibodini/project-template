#!/bin/bash

python -m venv .venv
source .venv/bin/activate

python.exe -m pip install --upgrade pip
pip install ruff pre-commit pytest

pre-commit install

echo "Setup completo ✅"
