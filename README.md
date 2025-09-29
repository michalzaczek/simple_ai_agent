# AI Agent

A Python-based AI coding agent that uses Google's Gemini API to perform file operations and execute Python code within a secure, sandboxed environment.

## Overview

This project implements an AI agent that can interact with files and execute Python code through a set of predefined functions. The agent uses Google's Gemini 2.0 Flash model to understand user requests and perform various file system operations safely within a constrained working directory.

## Features

- **File Operations**: List, read, and write files within a secure working directory
- **Python Execution**: Run Python files with optional command-line arguments
- **Security**: All operations are constrained to the working directory to prevent unauthorized access
- **AI Integration**: Uses Google's Gemini API for natural language processing and task planning
- **Calculator Module**: Includes a sample calculator implementation with infix expression evaluation

## Project Structure

```
ai_agent/
├── main.py                 # Main AI agent application
├── config.py              # Configuration settings and system prompt
├── pyproject.toml         # Project dependencies and metadata
├── functions/             # Core function implementations
│   ├── get_files_info.py  # List files and directories
│   ├── get_file_content.py # Read file contents
│   ├── run_python_file.py # Execute Python files
│   ├── write_file.py      # Write files
│   ├── call_function.py   # Function call handler
│   └── file_utils.py      # Utility functions
├── calculator/            # Sample calculator module
│   ├── main.py           # Calculator demo
│   ├── pkg/
│   │   ├── calculator.py # Calculator class implementation
│   │   └── render.py     # Rendering utilities
│   └── tests.py          # Calculator unit tests
└── tests.py              # Integration tests
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai_agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -e .
   ```
   
   Or using uv (recommended):
   ```bash
   uv sync
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

### Basic Usage

Run the AI agent with a natural language prompt:

```bash
python main.py "your prompt here"
```

### Verbose Mode

Add `--verbose` flag for detailed output including token usage:

```bash
python main.py "your prompt here" --verbose
```

### Example Commands

```bash
# List files in the current directory
python main.py "list all files in the current directory"

# Read a specific file
python main.py "read the calculator.py file"

# Run a Python file
python main.py "run the calculator tests"

# Write a new file
python main.py "create a new file called hello.py with print('Hello, World!')"
```

## Available Functions

The AI agent has access to the following functions:

### 1. `get_files_info`
- **Purpose**: Lists files and directories with their sizes
- **Parameters**: `directory` (optional, defaults to current directory)
- **Security**: Constrained to working directory

### 2. `get_file_content`
- **Purpose**: Reads file contents
- **Parameters**: `file_path` (required)
- **Security**: Constrained to working directory, content truncated at 10,000 characters
- **Returns**: File content or error message

### 3. `run_python_file`
- **Purpose**: Executes Python files with optional arguments
- **Parameters**: `file_path` (required), `args` (optional array)
- **Security**: Only Python files within working directory, 30-second timeout
- **Returns**: STDOUT, STDERR, and exit code

### 4. `write_file`
- **Purpose**: Writes content to files
- **Parameters**: `file_path` (required), `content` (required)
- **Security**: Constrained to working directory, creates directories as needed
- **Returns**: Success message with character count

## Calculator Module

The project includes a sample calculator implementation that demonstrates:

- **Infix Expression Evaluation**: Handles operator precedence correctly
- **Basic Operations**: Addition, subtraction, multiplication, division
- **Error Handling**: Invalid tokens, insufficient operands, malformed expressions
- **Unit Tests**: Comprehensive test coverage

### Calculator Usage

```python
from calculator.pkg.calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 5 * 2")  # Returns 13
```

## Configuration

### Model Settings
- **Model**: `gemini-2.0-flash-001`
- **Max Characters**: 10,000 (for file content)
- **Max Iterations**: 20 (prevents infinite loops)

### System Prompt
The agent is configured with a system prompt that defines its capabilities and constraints, ensuring it operates within the defined security boundaries.

## Security Features

- **Path Validation**: All file operations are restricted to the working directory
- **Timeout Protection**: Python execution limited to 30 seconds
- **Content Limits**: File reading truncated to prevent memory issues
- **Error Handling**: Comprehensive error messages for debugging

## Testing

Run the integration tests:

```bash
python tests.py
```

Run the calculator unit tests:

```bash
python calculator/tests.py
```

## Dependencies

- `google-genai==1.12.1` - Google Gemini API client
- `python-dotenv==1.1.0` - Environment variable management
- Python 3.13+

## Development

### Adding New Functions

1. Create a new function file in the `functions/` directory
2. Define the function schema using Google's `types.FunctionDeclaration`
3. Implement the function with proper error handling and security checks
4. Add the schema to the `available_functions` list in `main.py`
5. Update the system prompt if needed

### Security Considerations

- Always validate file paths against the working directory
- Use absolute paths internally, relative paths for user interface
- Implement proper error handling and timeouts
- Test security boundaries thoroughly

## License

This project is part of a coding bootcamp curriculum and is intended for educational purposes.

## Contributing

This is an educational project. For questions or issues, please refer to the course materials or instructor.
