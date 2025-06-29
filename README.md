# Lesson 1 - Building Your First MCP Server with Python

Welcome to our first lesson on Model Context Protocol! In this short tutorial, we'll build the tiniest possible MCP server using FastMCP in Python, and test it with mcp-cli. By the end of this lesson, you'll see a complete round-trip from MCP server creation to JSON response.

First, we need to create our hello_mcp.py file. This will contain our minimal MCP server implementation.

Now let's write our MCP server code. We'll start by importing the FastMCP library.

```python
from fastmcp import FastMCP
```

Next, we'll instantiate our server and give our tool a namespace called 'hello'. This groups actions so the model can pick the right capability.

```python
from fastmcp import FastMCP

# 1. Instantiate a server and give our tool a namespace
```

Now we'll create our action. The @mcp.tool decorator turns our greet function into an action that the LLM can call.

```python
from fastmcp import FastMCP

# 1. Instantiate a server and give our tool a namespace
mcp = FastMCP("hello")

# 2. Expose a single action
```

Finally, we'll add the runtime code that starts our JSON-over-stdio server using the built-in transport.

```python
from fastmcp import FastMCP

# 1. Instantiate a server and give our tool a namespace
mcp = FastMCP("hello")

# 2. Expose a single action
@mcp.tool
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! 👋"

# 3. Run with the built-in stdio transport (works with any client)
```

Perfect! Our MCP server is ready. Let's save the file and run it to see it in action.

```python
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
```

Let's open up a terminal.

We can run the MCP server in the background by running the Python file.

```shell
nohup python hello_mcp.py &
```

```shell
🚀 MCP server "hello" listening on STDIN/STDOUT
```

Excellent! Our server is now running and listening on STDIN/STDOUT. This means it's ready to receive MCP protocol messages.

Now we'll test our MCP server using mcp-cli, a Node utility that forwards stdin to any MCP stdio server. We'll send a JSON message to call our greet action.

```shell
echo '{ "tool": "hello", "action": "greet", "params": { "name": "world" } }' | npx mcp-cli call -
```

```shell
{ "status": "ok", "result": "Hello, world! 👋" }
```

Perfect! We just completed our first MCP round-trip. The server received our JSON request, processed it through our greet function, and returned a JSON response with our friendly greeting.

Congratulations! You've just built and tested your first MCP server. Let me explain the key concepts we just demonstrated.

First, the Tool - that's our 'hello' namespace that groups actions so models can pick the right capability.

Second, the Action - that's our 'greet' function that executes real work with typed parameters and returns.

Third, the Server - that's our FastMCP runtime that bridges your logic with any MCP-aware client.

And finally, the Client - that's mcp-cli in our case, but it could be ChatGPT, Claude, LangChain, Gemini, or any other model. You now understand the fundamentals of the Model Context Protocol and how to create servers that can integrate with AI systems!

From here, the possibilities are endless - throughout the MCP Masterclass, we'll learn more advanced things like adding website context to tool calls, returning images directly in the chat, and even conducting advanced decision-tree workflows.

In the next lesson, we'll see how to create the same server but using TypeScript with Anthropic's TypeScript SDK. See you there!