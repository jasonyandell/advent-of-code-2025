#!/bin/bash
# One-stop setup: creates venv if needed, activates, installs deps

if [ ! -d ".venv" ]; then
    echo "Creating .venv..."
    python3 -m venv .venv
fi

source .venv/bin/activate
pip install -q -r requirements.txt
