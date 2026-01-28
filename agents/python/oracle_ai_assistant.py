"""
Oracle AI CoE Assistant Agent
A comprehensive agent designed to help with Oracle AI Center of Excellence tasks
"""

from pyagentspec.agent import Agent
from pyagentspec.llms import VllmConfig
from pyagentspec.property import StringProperty, ListProperty, ObjectProperty
from pyagentspec.tools import ServerTool
from pyagentspec.serialization import AgentSpecSerializer


def create_oracle_ai_assistant():
    """
    Creates an Oracle AI CoE Assistant agent with relevant tools and capabilities
    """

    # Configure the LLM
    # Update this with your actual LLM endpoint
    llm_config = VllmConfig(
        name="oracle-llm",
        model_id="llama-3.1-70b",  # Update with your model
        url="http://your-llm-endpoint-here"  # Update with your endpoint
    )

    # Define tools for the agent
    tools = [
        ServerTool(
            name="query_documentation",
            description="Search Oracle AI documentation and best practices",
            inputs=[
                StringProperty(title="query", description="Search query for documentation")
            ],
            outputs=[
                ListProperty(
                    title="results",
                    item_type=ObjectProperty(
                        title="doc_result",
                        properties=[
                            StringProperty(title="title"),
                            StringProperty(title="content"),
                            StringProperty(title="url")
                        ]
                    )
                )
            ]
        ),
        ServerTool(
            name="analyze_architecture",
            description="Analyze AI architecture and provide recommendations",
            inputs=[
                StringProperty(title="architecture_description", description="Description of the AI architecture"),
                StringProperty(title="use_case", description="Primary use case for the architecture")
            ],
            outputs=[
                ObjectProperty(
                    title="analysis",
                    properties=[
                        StringProperty(title="recommendations"),
                        ListProperty(title="concerns", item_type=StringProperty(title="concern")),
                        StringProperty(title="best_practices")
                    ]
                )
            ]
        ),
        ServerTool(
            name="generate_agent_template",
            description="Generate a new agent template based on requirements",
            inputs=[
                StringProperty(title="agent_purpose", description="Purpose of the agent"),
                ListProperty(title="required_capabilities", item_type=StringProperty(title="capability"))
            ],
            outputs=[
                StringProperty(title="agent_code", description="Generated Python code for the agent")
            ]
        )
    ]

    # Create the agent
    agent = Agent(
        name="Oracle AI CoE Assistant",
        llm_config=llm_config,
        system_prompt="""You are an expert Oracle AI Center of Excellence assistant. Your role is to:

1. Help design and implement AI agents following Oracle Agent Spec standards
2. Provide guidance on best practices for AI/ML implementations
3. Analyze architectures and suggest improvements
4. Generate agent templates and configurations
5. Assist with Oracle AI services integration

You have deep knowledge of:
- Oracle Agent Spec framework
- AI/ML best practices and design patterns
- Oracle Cloud Infrastructure AI services
- Agent orchestration and deployment
- Security and governance for AI systems

Always provide clear, actionable recommendations with examples when possible.
Consider enterprise requirements like scalability, security, and maintainability.

User context: {user_name} from {organization}""",
        tools=tools,
        inputs=[
            StringProperty(title="user_name", description="Name of the user"),
            StringProperty(title="organization", description="Organization name", default="Oracle")
        ]
    )

    return agent


def main():
    """Generate and save the agent configuration"""
    agent = create_oracle_ai_assistant()

    # Serialize to JSON
    serializer = AgentSpecSerializer()
    agent_json = serializer.to_json(agent)

    # Save to file
    with open("configs/oracle_ai_assistant.json", "w") as f:
        f.write(agent_json)

    print("✓ Oracle AI CoE Assistant agent created successfully")
    print(f"  Configuration saved to: configs/oracle_ai_assistant.json")

    # Also save as YAML for readability
    agent_yaml = serializer.to_yaml(agent)
    with open("configs/oracle_ai_assistant.yaml", "w") as f:
        f.write(agent_yaml)

    print(f"  YAML configuration saved to: configs/oracle_ai_assistant.yaml")


if __name__ == "__main__":
    main()
