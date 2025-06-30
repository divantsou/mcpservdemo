To run the server add the following to your mcp config file:

```
{
  "mcpServers": {
    "Addition": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "git+https://github.com/divantsou/mcpservdemo.git",
        "mcp-server"
      ]
    }
  }
}
```