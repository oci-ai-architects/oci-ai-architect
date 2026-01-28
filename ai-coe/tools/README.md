# Custom Tools Library

This directory contains reusable tool definitions that can be used across multiple agents.

## Tool Categories

### 1. Oracle Cloud Integration Tools
Tools for interacting with Oracle Cloud Infrastructure services.

### 2. Documentation Tools
Tools for searching, retrieving, and managing documentation.

### 3. Code Analysis Tools
Tools for analyzing, generating, and reviewing code.

### 4. Data Processing Tools
Tools for data analysis and transformation.

## Creating a Custom Tool

Example structure:

```python
from pyagentspec.tools import ServerTool
from pyagentspec.property import StringProperty, ObjectProperty

def create_my_tool():
    return ServerTool(
        name="tool_name",
        description="Clear description of what the tool does",
        inputs=[
            StringProperty(title="input_param", description="What this parameter does")
        ],
        outputs=[
            ObjectProperty(
                title="result",
                properties=[
                    StringProperty(title="output_field")
                ]
            )
        ]
    )
```

## Best Practices

1. **Single Responsibility**: Each tool should do one thing well
2. **Clear Documentation**: Describe inputs, outputs, and behavior
3. **Error Handling**: Consider edge cases and failure modes
4. **Reusability**: Design for use across multiple agents
5. **Testing**: Include unit tests for each tool
