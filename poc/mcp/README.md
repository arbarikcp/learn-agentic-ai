

``` # linux/mac
python -m venv --help
sudo apt-get install python3-venv #install venv - optional
python3 -m venv agent-env

source agent-env/bin/activate # activae the virtual environment

pip3 install mcp
pip3 install "mcp[cli]"
pip3 install uv

pip show mcp

pip freeze > requirements.txt
 or 
pip install package-name && pip freeze > requirements.txt

```
### mcp config for windsurf
- Here we have configured mcp servers for calculator and postgresql. Calculator is our custom server and postgresql is provided by mcp.
```
{
  "mcpServers": {
    "calculator": {
      "command": "/Users/username/workspace/learn-agentic-ai/poc/mcp/agent-env/bin/python3",
      "args": [
        "/Users/username/workspace/learn-agentic-ai/poc/mcp/calculator.py"
      ],
      "env": {
        "CALCULATOR_ENV": "LOCAL"
      }
    },
    "postgresql": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://root:root@localhost:5432/root"
      ]
    }
  }
} 
```

