# FastAPI App

A FastAPI application integrated with OpenAI

## Setup

### 1. Create and Activate Virtual Environment

Create a virtual environment to isolate project dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when the virtual environment is active.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Add the following to your `.env` file:

```bash
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Running the Application

Use the provided script:

```bash
./run.sh
```

This script will:
- Load environment variables from `.env`
- Activate the virtual environment
- Run the FastAPI app


## API Endpoints

- `GET /` - Returns a joke from OpenAI
- `GET /health` - Health check endpoint
- `GET /items/{item_id}` - Get item by ID with optional query parameter
