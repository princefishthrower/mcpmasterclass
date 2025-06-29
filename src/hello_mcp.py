from fastmcp import FastMCP

# 1. Instantiate a server and give our tool a namespace
mcp = FastMCP("hello")

# 2. Expose a single action
@mcp.tool
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! 👋"

# 3. Run with the built-in stdio transport (works with any client)
if __name__ == "__main__":
    mcp.run()