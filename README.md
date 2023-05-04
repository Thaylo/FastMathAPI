# A Math Problem-Solving REST API

A simple REST API to solve mathematical equations using Python, Flask, and SymPy. It features an LRU cache to improve performance for repeated requests.

## Features

- Solve mathematical equations with a single variable.
- LRU cache implementation to handle repeated requests efficiently.
- Docker support for easy deployment.

## Requirements

- Python 3.6+
- Flask 2.1.1
- SymPy 1.9
- cachetools 4.2.4
- Docker (optional)

## Installation

1. Clone this repository:
```
git clone https://github.com/Thaylo/FastMathAPI.git
cd math-api
```

2. (Optional) Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```


3. Install the required Python packages:
```
pip install -r requirements.txt
```

## Running the API

### Using the deployment script (requires Docker)
The script below will create the docker image and run it on localhost:8000.
```
./install_dependencies.sh
```

## Testing the API
Open a new terminal interface and run the command:
```
python client.py
```
Follow instructions.

## Usage

Send a POST request to the `/solve` endpoint with a JSON payload containing the `equation` and `variable` fields.

- `equation`: A string representing a mathematical equation, where the expression is set equal to zero. For example, "x+3-2" (which represents "x+3=2").
- `variable`: A string representing the variable to be solved for in the equation. For example, "x".

Example JSON payload:

```
json
{
    "equation": "x+3-2",
    "variable": "x"
}
```
## License
This project is licensed under the MIT License. 

Copyright 2023 Thaylo X. de Freitas

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
