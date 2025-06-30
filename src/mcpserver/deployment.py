from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Addition Demo")

def add_two_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    """
    return a + b

