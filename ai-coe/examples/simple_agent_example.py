"""
Simple Agent Example
A basic example to demonstrate Oracle Agent Spec usage
"""

from pyagentspec.agent import Agent
from pyagentspec.llms import VllmConfig
from pyagentspec.property import StringProperty
from pyagentspec.serialization import AgentSpecSerializer


def create_simple_assistant():
    """Create a simple writing assistant agent"""

    # Configure LLM
    llm_config = VllmConfig(
        name="simple-llm",
        model_id="llama-3.1-8b",
        url="http://localhost:8000"  # Update with your endpoint
    )

    # Create agent without tools for simplicity
    agent = Agent(
        name="Simple Writing Assistant",
        llm_config=llm_config,
        system_prompt="""You are a helpful writing assistant.
Help users improve their writing with clear suggestions and corrections.
Be concise and friendly.""",
        inputs=[
            StringProperty(title="user_name", description="User's name")
        ]
    )

    return agent


if __name__ == "__main__":
    agent = create_simple_assistant()
    serializer = AgentSpecSerializer()

    # Print as JSON
    print("Simple Agent Configuration (JSON):")
    print(serializer.to_json(agent))
