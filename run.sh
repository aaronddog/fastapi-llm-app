#!/bin/bash

# Load environment variables from .env file
set -a
source .env
set +a

echo "Activating virtual environment"
source venv/bin/activate

echo "Installing dependencies"
pip install -r requirements.txt

echo "Starting FastAPI application"
# Run FastAPI application
uvicorn main:app --host 0.0.0.0 --port 8000 --reload