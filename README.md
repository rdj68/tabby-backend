# Gemini Backend

This repository builds a server for the tabbyML clients (VSCode, Vim, IntelliJ). The code is written in Python and uses FastAPI for HTTP request handling. It utilizes the Gemini API to fetch code snippets.

## Getting Started

To run this project, follow these steps:

1. **Create a Python Virtual Environment:**
   ```bash
   python -m venv .venv
   ```

   This command creates a Python virtual environment in the `.venv` folder.

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   This command installs the required dependencies for the project.

3. **Run the Server:**
   ```bash
   uvicorn server:app
   ```

   This command starts the server using Uvicorn.

## Contributing

If you would like to contribute to this project, please follow the [contribution guidelines](CONTRIBUTING.md).