# Getting Started with Oracle Agent Spec

## Quick Start Tutorial

### Step 1: Environment Setup

1. **Install Python 3.8+**
   ```bash
   python --version
   ```

2. **Install PyAgentSpec**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   python -c "import pyagentspec; print(pyagentspec.__version__)"
   ```

### Step 2: Run Your First Example

1. **Run the simple agent example:**
   ```bash
   python examples/simple_agent_example.py
   ```

2. **Review the output:**
   - JSON configuration of the agent
   - Agent structure and properties

### Step 3: Create the Oracle AI Assistant

1. **Generate the agent:**
   ```bash
   python agents/oracle_ai_assistant.py
   ```

2. **Check generated configs:**
   ```bash
   ls configs/
   cat configs/oracle_ai_assistant.json
   ```

### Step 4: Customize for Your LLM

Edit `agents/oracle_ai_assistant.py` and update:

```python
llm_config = VllmConfig(
    name="your-llm-name",
    model_id="your-model-id",  # e.g., "llama-3.1-70b"
    url="your-llm-endpoint"    # e.g., "http://your-server:8000"
)
```

### Step 5: Explore the Documentation

1. **Open index.html in your browser:**
   - View the Agent Catalog
   - Review Best Practices
   - Check the Development Roadmap

2. **Read the README.md:**
   - Understand the strategy
   - Review the development workflow
   - Learn about best practices

## Next Steps

### Learn by Example
- Study `examples/simple_agent_example.py`
- Analyze `agents/oracle_ai_assistant.py`
- Experiment with modifications

### Build Your First Agent
1. Define your use case
2. Create a new file in `agents/`
3. Define tools if needed
4. Test and iterate
5. Add to index.html catalog

### Contribute
- Share your agents
- Improve documentation
- Report issues
- Suggest enhancements

## Common Tasks

### Generate Agent Configuration
```python
from pyagentspec.serialization import AgentSpecSerializer

serializer = AgentSpecSerializer()
json_config = serializer.to_json(agent)
yaml_config = serializer.to_yaml(agent)
```

### Add a Tool to an Agent
```python
from pyagentspec.tools import ServerTool
from pyagentspec.property import StringProperty

tool = ServerTool(
    name="my_tool",
    description="What it does",
    inputs=[StringProperty(title="input")],
    outputs=[StringProperty(title="output")]
)

agent = Agent(
    name="My Agent",
    llm_config=llm_config,
    system_prompt="...",
    tools=[tool]  # Add your tool here
)
```

### Add Context Variables
```python
agent = Agent(
    name="My Agent",
    llm_config=llm_config,
    system_prompt="Hello {user_name}, you work at {company}",
    inputs=[
        StringProperty(title="user_name"),
        StringProperty(title="company", default="Oracle")
    ]
)
```

## Troubleshooting

### Import Errors
```bash
pip install --upgrade pyagentspec
```

### LLM Connection Issues
- Verify your endpoint URL is correct
- Check network connectivity
- Ensure the LLM service is running

### Configuration Errors
- Validate JSON/YAML syntax
- Check required fields are present
- Review property types

## Resources

- [Oracle Agent Spec Docs](https://oracle.github.io/agent-spec)
- [How-to Guides](https://oracle.github.io/agent-spec/howtoguides/)
- [Project README](../README.md)
- [Interactive Docs](../index.html)

## Support

For questions or issues:
1. Check the documentation
2. Review examples
3. Contact Oracle AI CoE team
