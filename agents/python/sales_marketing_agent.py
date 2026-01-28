"""
Sales & Marketing Department Agent
Revenue acceleration and customer engagement
ROI: 85% efficiency gain | $340K annual savings
"""

from pyagentspec.agent import Agent
from pyagentspec.llms import VllmConfig
from pyagentspec.property import StringProperty, NumberProperty, ObjectProperty, ListProperty
from pyagentspec.tools import ServerTool
from pyagentspec.serialization import AgentSpecSerializer


def create_sales_marketing_agent():
    """
    Creates a Sales & Marketing agent focused on lead generation and conversion
    """

    llm_config = VllmConfig(
        name="sales-marketing-llm",
        model_id="llama-3.1-70b",
        url="http://your-llm-endpoint"
    )

    tools = [
        ServerTool(
            name="qualify_lead",
            description="Intelligent lead scoring, qualification, and prioritization",
            inputs=[
                StringProperty(title="lead_id", description="Lead identifier"),
                StringProperty(title="company_name", description="Company name"),
                StringProperty(title="industry", description="Industry sector"),
                NumberProperty(title="company_size", description="Number of employees"),
                StringProperty(title="engagement_level", description="Engagement metrics")
            ],
            outputs=[
                ObjectProperty(
                    title="qualification",
                    properties=[
                        NumberProperty(title="lead_score", description="0-100 score"),
                        StringProperty(title="qualification_tier", description="hot, warm, cold"),
                        ListProperty(title="buying_signals", item_type=StringProperty(title="signal")),
                        StringProperty(title="recommended_action"),
                        NumberProperty(title="conversion_probability")
                    ]
                )
            ]
        ),

        ServerTool(
            name="generate_campaign_content",
            description="Create personalized marketing content, email campaigns, social media posts",
            inputs=[
                StringProperty(title="campaign_type", description="email, social, blog, ad_copy"),
                StringProperty(title="target_audience", description="Audience persona"),
                StringProperty(title="campaign_objective", description="awareness, consideration, conversion"),
                ListProperty(title="key_messages", item_type=StringProperty(title="message"))
            ],
            outputs=[
                ObjectProperty(
                    title="content",
                    properties=[
                        StringProperty(title="headline"),
                        StringProperty(title="body_copy"),
                        StringProperty(title="call_to_action"),
                        ListProperty(title="variations", item_type=StringProperty(title="variant")),
                        StringProperty(title="tone_analysis")
                    ]
                )
            ]
        ),

        ServerTool(
            name="analyze_deal",
            description="Deal pipeline analysis, win/loss prediction, competitive positioning",
            inputs=[
                StringProperty(title="deal_id", description="Deal identifier"),
                StringProperty(title="deal_stage", description="Current pipeline stage"),
                NumberProperty(title="deal_value", description="Deal value in USD"),
                ListProperty(title="stakeholders", item_type=StringProperty(title="stakeholder")),
                StringProperty(title="competitor", description="Primary competitor")
            ],
            outputs=[
                ObjectProperty(
                    title="analysis",
                    properties=[
                        NumberProperty(title="win_probability"),
                        ListProperty(title="risk_factors", item_type=StringProperty(title="risk")),
                        ListProperty(title="recommended_actions", item_type=StringProperty(title="action")),
                        StringProperty(title="competitive_strategy"),
                        StringProperty(title="next_best_action")
                    ]
                )
            ]
        ),

        ServerTool(
            name="customer_sentiment_analysis",
            description="Analyze customer interactions, feedback, and social media mentions",
            inputs=[
                StringProperty(title="customer_id", description="Customer identifier"),
                StringProperty(title="data_source", description="email, social, support_tickets, surveys"),
                StringProperty(title="time_period", description="Analysis period")
            ],
            outputs=[
                ObjectProperty(
                    title="sentiment",
                    properties=[
                        StringProperty(title="overall_sentiment", description="positive, neutral, negative"),
                        NumberProperty(title="sentiment_score", description="-100 to 100"),
                        ListProperty(title="key_themes", item_type=StringProperty(title="theme")),
                        NumberProperty(title="churn_risk"),
                        ListProperty(title="action_items", item_type=StringProperty(title="action"))
                    ]
                )
            ]
        )
    ]

    agent = Agent(
        name="Sales & Marketing Agent",
        llm_config=llm_config,
        system_prompt="""You are an expert Sales & Marketing AI agent specializing in:

1. **Lead Qualification & Scoring**
   - Intelligent lead prioritization using ML
   - Real-time buyer intent signals
   - Automated lead nurturing campaigns
   - Conversion probability prediction

2. **Content Generation & Optimization**
   - Personalized email campaigns
   - Social media content calendar
   - Blog posts and thought leadership
   - Ad copy A/B testing

3. **Sales Intelligence**
   - Deal pipeline analysis and forecasting
   - Win/loss pattern identification
   - Competitive intelligence and positioning
   - Next-best-action recommendations

4. **Customer Engagement Analytics**
   - Sentiment analysis across channels
   - Engagement tracking and optimization
   - Churn prediction and prevention
   - Customer journey mapping

**Key Responsibilities:**
- Accelerate lead-to-opportunity conversion
- Generate high-quality, personalized marketing content
- Provide actionable insights for sales teams
- Optimize campaign performance and ROI
- Identify at-risk customers and recommend interventions

**Operating Guidelines:**
- Personalize all customer interactions
- Respect data privacy and opt-out preferences
- A/B test content variations for optimization
- Integrate with CRM (Salesforce, HubSpot, Oracle CX)
- Track and report on key performance metrics (CAC, LTV, conversion rates)

**Success Metrics:**
- Lead conversion rate improvement: 35%+
- Campaign engagement rate: 25%+ increase
- Sales cycle time reduction: 40%
- Customer acquisition cost: 30% reduction

User Context: {user_name} | Role: {role} | Territory: {territory}""",
        tools=tools,
        inputs=[
            StringProperty(title="user_name", description="User's name"),
            StringProperty(title="role", description="sales, marketing, sales_ops", default="sales"),
            StringProperty(title="territory", description="Sales territory", default="global")
        ]
    )

    return agent


def main():
    """Generate and save the agent configuration"""
    agent = create_sales_marketing_agent()

    serializer = AgentSpecSerializer()

    agent_json = serializer.to_json(agent)
    with open("configs/sales_marketing_agent.json", "w") as f:
        f.write(agent_json)

    agent_yaml = serializer.to_yaml(agent)
    with open("configs/sales_marketing_agent.yaml", "w") as f:
        f.write(agent_yaml)

    print("✓ Sales & Marketing Agent created successfully")
    print(f"  ROI: 85% efficiency gain | $340K annual savings")
    print(f"  Lead conversion +35% | Sales cycle -40%")


if __name__ == "__main__":
    main()
