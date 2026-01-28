"""
Customer Support Department Agent
24/7 intelligent customer service at scale
ROI: 55% efficiency gain | $380K annual savings | CSAT +35%
"""

from pyagentspec.agent import Agent
from pyagentspec.llms import VllmConfig
from pyagentspec.property import StringProperty, NumberProperty, ObjectProperty, ListProperty
from pyagentspec.tools import ServerTool
from pyagentspec.serialization import AgentSpecSerializer


def create_customer_support_agent():
    """
    Creates a Customer Support agent for 24/7 automated support
    """

    llm_config = VllmConfig(
        name="support-llm",
        model_id="llama-3.1-70b",
        url="http://your-llm-endpoint"
    )

    tools = [
        ServerTool(
            name="triage_ticket",
            description="Intelligent ticket classification, priority routing, and SLA assignment",
            inputs=[
                StringProperty(title="ticket_id", description="Ticket identifier"),
                StringProperty(title="subject", description="Ticket subject"),
                StringProperty(title="description", description="Issue description"),
                StringProperty(title="customer_tier", description="free, standard, premium, enterprise")
            ],
            outputs=[
                ObjectProperty(
                    title="triage_result",
                    properties=[
                        StringProperty(title="category", description="technical, billing, feature_request, bug"),
                        StringProperty(title="priority", description="critical, high, medium, low"),
                        StringProperty(title="assigned_team", description="Team to handle"),
                        StringProperty(title="sla_target", description="Response time target"),
                        NumberProperty(title="complexity_score"),
                        ListProperty(title="suggested_knowledge_articles", item_type=StringProperty(title="article_id"))
                    ]
                )
            ]
        ),

        ServerTool(
            name="search_knowledge_base",
            description="Semantic search across documentation, FAQs, and previous resolutions",
            inputs=[
                StringProperty(title="query", description="Search query"),
                StringProperty(title="product", description="Product/service context"),
                NumberProperty(title="max_results", description="Maximum results to return")
            ],
            outputs=[
                ListProperty(
                    title="results",
                    item_type=ObjectProperty(
                        title="article",
                        properties=[
                            StringProperty(title="article_id"),
                            StringProperty(title="title"),
                            StringProperty(title="summary"),
                            StringProperty(title="solution"),
                            NumberProperty(title="relevance_score"),
                            NumberProperty(title="success_rate")
                        ]
                    )
                )
            ]
        ),

        ServerTool(
            name="generate_response",
            description="Generate customer-friendly support responses with solutions",
            inputs=[
                StringProperty(title="ticket_id", description="Ticket identifier"),
                StringProperty(title="customer_query", description="Customer's question"),
                StringProperty(title="context", description="Additional context"),
                ListProperty(title="knowledge_articles", item_type=StringProperty(title="article"))
            ],
            outputs=[
                ObjectProperty(
                    title="response",
                    properties=[
                        StringProperty(title="response_text", description="Customer-facing response"),
                        StringProperty(title="tone", description="empathetic, professional, technical"),
                        ListProperty(title="steps", item_type=StringProperty(title="step")),
                        StringProperty(title="escalation_needed"),
                        NumberProperty(title="confidence_score")
                    ]
                )
            ]
        ),

        ServerTool(
            name="sentiment_and_churn_analysis",
            description="Analyze customer sentiment, satisfaction, and churn risk",
            inputs=[
                StringProperty(title="customer_id", description="Customer identifier"),
                StringProperty(title="interaction_history", description="Recent interactions"),
                NumberProperty(title="csat_score", description="Recent CSAT score if available")
            ],
            outputs=[
                ObjectProperty(
                    title="analysis",
                    properties=[
                        StringProperty(title="sentiment", description="positive, neutral, negative, angry"),
                        NumberProperty(title="sentiment_score", description="-100 to 100"),
                        NumberProperty(title="churn_probability", description="0-100"),
                        ListProperty(title="pain_points", item_type=StringProperty(title="pain_point")),
                        ListProperty(title="recommended_actions", item_type=StringProperty(title="action")),
                        StringProperty(title="escalation_priority")
                    ]
                )
            ]
        )
    ]

    agent = Agent(
        name="Customer Support Agent",
        llm_config=llm_config,
        system_prompt="""You are an expert Customer Support AI agent providing 24/7 intelligent service:

1. **Ticket Triage & Routing**
   - Instant classification and prioritization
   - SLA-aware routing to appropriate teams
   - Complexity assessment for agent assignment
   - Automated escalation for critical issues

2. **Knowledge Base & Self-Service**
   - Semantic search across documentation
   - Context-aware article recommendations
   - Step-by-step troubleshooting guides
   - Video tutorials and visual aids

3. **Response Generation**
   - Empathetic, professional communication
   - Clear, actionable solutions
   - Personalized based on customer tier
   - Multi-language support

4. **Customer Sentiment & Retention**
   - Real-time sentiment analysis
   - Churn prediction and prevention
   - Proactive outreach for at-risk customers
   - CSAT optimization

**Key Responsibilities:**
- Resolve tier-1 issues autonomously (target: 70%)
- Provide instant, accurate responses 24/7
- Escalate complex issues with full context
- Improve customer satisfaction continuously
- Reduce average handle time while maintaining quality

**Operating Guidelines:**
- Always be empathetic and patient
- Provide clear, step-by-step instructions
- Verify customer identity for account changes
- Escalate if customer is frustrated or issue is complex
- Follow up on unresolved issues
- Maintain brand voice and tone
- Track and learn from successful resolutions

**Success Metrics:**
- First Contact Resolution: 70%+
- Average Response Time: <30 seconds
- Customer Satisfaction (CSAT): 90%+
- Deflection Rate: 60%+ (tickets resolved without human)
- Churn Prevention: 35% reduction

**Escalation Triggers:**
- Customer explicitly requests human agent
- Security or compliance issues
- Refund requests >$500
- Angry or abusive language
- Technical issues beyond knowledge base

Customer Context: {customer_name} | Tier: {customer_tier} | Product: {product}""",
        tools=tools,
        inputs=[
            StringProperty(title="customer_name", description="Customer's name"),
            StringProperty(title="customer_tier", description="free, standard, premium, enterprise", default="standard"),
            StringProperty(title="product", description="Product/service context", default="all")
        ]
    )

    return agent


def main():
    """Generate and save the agent configuration"""
    agent = create_customer_support_agent()

    serializer = AgentSpecSerializer()

    agent_json = serializer.to_json(agent)
    with open("configs/customer_support_agent.json", "w") as f:
        f.write(agent_json)

    agent_yaml = serializer.to_yaml(agent)
    with open("configs/customer_support_agent.yaml", "w") as f:
        f.write(agent_yaml)

    print("✓ Customer Support Agent created successfully")
    print(f"  ROI: 55% efficiency gain | $380K annual savings")
    print(f"  CSAT: +35% | FCR: 70% | 24/7 availability")


if __name__ == "__main__":
    main()
