#!/bin/bash

# Load environment variables from .env file
set -a
source .env
set +a

# Check if virtual environment exists, create if it doesn't
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating new virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created successfully."
fi

echo "Activating virtual environment"
source venv/bin/activate

echo "Installing dependencies"
pip install -r requirements.txt

echo "Starting FastAPI application"
# Run FastAPI application
uvicorn main:app --host 0.0.0.0 --port 8000 --reload