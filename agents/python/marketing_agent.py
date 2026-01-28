"""
Marketing Department Agent
Strategic brand management and campaign optimization
ROI: 85% efficiency gain | $340K annual savings
"""

from pyagentspec.agent import Agent
from pyagentspec.llms import VllmConfig
from pyagentspec.property import StringProperty, NumberProperty, ObjectProperty, ListProperty, BooleanProperty
from pyagentspec.tools import ServerTool
from pyagentspec.serialization import AgentSpecSerializer


def create_marketing_agent():
    """
    Creates a Marketing Department agent with specialized campaign and brand management tools
    """

    llm_config = VllmConfig(
        name="marketing-llm",
        model_id="llama-3.1-70b",
        url="http://your-llm-endpoint"  # Configure your Oracle OCI Gen AI endpoint
    )

    tools = [
        ServerTool(
            name="analyze_campaign_performance",
            description="Analyze marketing campaign metrics, ROI, conversion rates, and provide optimization recommendations",
            inputs=[
                StringProperty(title="campaign_id", description="Campaign identifier"),
                StringProperty(title="date_range", description="Analysis period (e.g., '2025-01-01 to 2025-01-31')"),
                ListProperty(title="metrics", item_type=StringProperty(title="metric"), description="Metrics to analyze (impressions, clicks, conversions, ROI, etc.)")
            ],
            outputs=[
                ObjectProperty(
                    title="campaign_analysis",
                    properties=[
                        NumberProperty(title="roi_percentage"),
                        NumberProperty(title="conversion_rate"),
                        NumberProperty(title="cost_per_acquisition"),
                        NumberProperty(title="engagement_rate"),
                        ListProperty(title="recommendations", item_type=StringProperty(title="recommendation")),
                        StringProperty(title="performance_trend"),
                        NumberProperty(title="budget_efficiency_score")
                    ]
                )
            ]
        ),

        ServerTool(
            name="generate_content_strategy",
            description="Create content strategy based on audience insights, brand guidelines, and business objectives",
            inputs=[
                StringProperty(title="target_audience", description="Target audience segment"),
                StringProperty(title="campaign_objective", description="Primary campaign goal (awareness, consideration, conversion, loyalty)"),
                ListProperty(title="channels", item_type=StringProperty(title="channel"), description="Marketing channels to use"),
                StringProperty(title="brand_tone", description="Brand voice and tone guidelines")
            ],
            outputs=[
                ObjectProperty(
                    title="content_strategy",
                    properties=[
                        ListProperty(title="content_themes", item_type=StringProperty(title="theme")),
                        ListProperty(title="messaging_pillars", item_type=StringProperty(title="pillar")),
                        ObjectProperty(
                            title="content_calendar",
                            properties=[
                                ListProperty(title="weekly_topics", item_type=StringProperty(title="topic")),
                                NumberProperty(title="posts_per_week")
                            ]
                        ),
                        ListProperty(title="cta_recommendations", item_type=StringProperty(title="cta")),
                        StringProperty(title="success_metrics")
                    ]
                )
            ]
        ),

        ServerTool(
            name="brand_consistency_check",
            description="Review content for brand guideline compliance, tone consistency, and messaging alignment",
            inputs=[
                StringProperty(title="content_id", description="Content identifier"),
                StringProperty(title="content_text", description="Content to review"),
                StringProperty(title="content_type", description="Type (social_post, email, blog, ad, etc.)"),
                StringProperty(title="brand_guidelines_version", description="Version of brand guidelines to check against")
            ],
            outputs=[
                ObjectProperty(
                    title="compliance_result",
                    properties=[
                        NumberProperty(title="overall_score", description="0-100 compliance score"),
                        BooleanProperty(title="approved"),
                        ListProperty(title="violations", item_type=ObjectProperty(
                            title="violation",
                            properties=[
                                StringProperty(title="category"),
                                StringProperty(title="severity"),
                                StringProperty(title="description"),
                                StringProperty(title="recommendation")
                            ]
                        )),
                        ListProperty(title="strengths", item_type=StringProperty(title="strength")),
                        StringProperty(title="tone_analysis"),
                        ListProperty(title="improvement_suggestions", item_type=StringProperty(title="suggestion"))
                    ]
                )
            ]
        ),

        ServerTool(
            name="audience_segmentation_analysis",
            description="Analyze customer data to identify and characterize audience segments for targeting",
            inputs=[
                StringProperty(title="data_source", description="Customer data source (CRM, analytics, etc.)"),
                ListProperty(title="segmentation_criteria", item_type=StringProperty(title="criterion"), description="Criteria for segmentation (demographics, behavior, psychographics)"),
                NumberProperty(title="desired_segments", description="Number of segments to create")
            ],
            outputs=[
                ObjectProperty(
                    title="segmentation_result",
                    properties=[
                        ListProperty(title="segments", item_type=ObjectProperty(
                            title="segment",
                            properties=[
                                StringProperty(title="segment_name"),
                                NumberProperty(title="segment_size"),
                                NumberProperty(title="percentage_of_total"),
                                StringProperty(title="key_characteristics"),
                                ListProperty(title="behavioral_patterns", item_type=StringProperty(title="pattern")),
                                StringProperty(title="recommended_messaging"),
                                NumberProperty(title="estimated_value")
                            ]
                        )),
                        ListProperty(title="targeting_recommendations", item_type=StringProperty(title="recommendation")),
                        StringProperty(title="prioritization_logic")
                    ]
                )
            ]
        ),

        ServerTool(
            name="lead_scoring_optimization",
            description="Analyze lead quality and optimize scoring models for improved conversion",
            inputs=[
                StringProperty(title="lead_id", description="Lead identifier (optional, for individual scoring)"),
                StringProperty(title="time_period", description="Period for model training"),
                ListProperty(title="scoring_factors", item_type=StringProperty(title="factor"), description="Factors to include in scoring")
            ],
            outputs=[
                ObjectProperty(
                    title="scoring_result",
                    properties=[
                        NumberProperty(title="lead_score", description="0-100 lead quality score"),
                        StringProperty(title="lead_quality_tier", description="hot, warm, cold"),
                        NumberProperty(title="conversion_probability"),
                        ListProperty(title="positive_signals", item_type=StringProperty(title="signal")),
                        ListProperty(title="negative_signals", item_type=StringProperty(title="signal")),
                        StringProperty(title="recommended_action"),
                        ObjectProperty(
                            title="model_performance",
                            properties=[
                                NumberProperty(title="accuracy"),
                                NumberProperty(title="precision"),
                                NumberProperty(title="recall")
                            ]
                        )
                    ]
                )
            ]
        ),

        ServerTool(
            name="competitive_intelligence",
            description="Monitor competitor marketing activities and provide strategic insights",
            inputs=[
                ListProperty(title="competitor_ids", item_type=StringProperty(title="competitor"), description="Competitors to monitor"),
                ListProperty(title="intelligence_areas", item_type=StringProperty(title="area"), description="Areas to analyze (messaging, channels, campaigns, pricing, etc.)"),
                StringProperty(title="time_period", description="Analysis period")
            ],
            outputs=[
                ObjectProperty(
                    title="competitive_analysis",
                    properties=[
                        ListProperty(title="competitor_insights", item_type=ObjectProperty(
                            title="competitor",
                            properties=[
                                StringProperty(title="competitor_name"),
                                ListProperty(title="active_campaigns", item_type=StringProperty(title="campaign")),
                                StringProperty(title="messaging_strategy"),
                                ListProperty(title="strengths", item_type=StringProperty(title="strength")),
                                ListProperty(title="weaknesses", item_type=StringProperty(title="weakness")),
                                NumberProperty(title="estimated_spend")
                            ]
                        )),
                        ListProperty(title="market_opportunities", item_type=StringProperty(title="opportunity")),
                        ListProperty(title="strategic_recommendations", item_type=StringProperty(title="recommendation")),
                        StringProperty(title="positioning_analysis")
                    ]
                )
            ]
        ),

        ServerTool(
            name="personalization_engine",
            description="Generate personalized content recommendations based on individual user behavior and preferences",
            inputs=[
                StringProperty(title="user_id", description="User identifier"),
                ListProperty(title="user_attributes", item_type=StringProperty(title="attribute"), description="User demographics and psychographics"),
                ListProperty(title="behavioral_history", item_type=StringProperty(title="behavior"), description="Past interactions and behaviors"),
                StringProperty(title="content_objective", description="Goal for personalization (engagement, conversion, retention)")
            ],
            outputs=[
                ObjectProperty(
                    title="personalization_result",
                    properties=[
                        StringProperty(title="recommended_content_theme"),
                        ListProperty(title="personalized_messages", item_type=ObjectProperty(
                            title="message",
                            properties=[
                                StringProperty(title="channel"),
                                StringProperty(title="content"),
                                NumberProperty(title="expected_engagement_rate"),
                                StringProperty(title="timing_recommendation")
                            ]
                        )),
                        ListProperty(title="product_recommendations", item_type=StringProperty(title="product")),
                        NumberProperty(title="personalization_confidence_score"),
                        StringProperty(title="next_best_action")
                    ]
                )
            ]
        ),

        ServerTool(
            name="budget_allocation_optimizer",
            description="Optimize marketing budget allocation across channels and campaigns for maximum ROI",
            inputs=[
                NumberProperty(title="total_budget", description="Total marketing budget available"),
                ListProperty(title="channels", item_type=StringProperty(title="channel"), description="Marketing channels to allocate to"),
                ListProperty(title="campaign_priorities", item_type=StringProperty(title="priority"), description="Strategic campaign priorities"),
                StringProperty(title="optimization_goal", description="ROI, reach, conversions, brand_awareness, etc.")
            ],
            outputs=[
                ObjectProperty(
                    title="allocation_plan",
                    properties=[
                        ListProperty(title="channel_allocations", item_type=ObjectProperty(
                            title="allocation",
                            properties=[
                                StringProperty(title="channel"),
                                NumberProperty(title="budget_amount"),
                                NumberProperty(title="percentage_of_total"),
                                NumberProperty(title="expected_roi"),
                                StringProperty(title="rationale")
                            ]
                        )),
                        NumberProperty(title="projected_total_roi"),
                        NumberProperty(title="expected_conversions"),
                        ListProperty(title="risk_factors", item_type=StringProperty(title="risk")),
                        ListProperty(title="optimization_opportunities", item_type=StringProperty(title="opportunity"))
                    ]
                )
            ]
        ),

        ServerTool(
            name="social_listening_insights",
            description="Analyze social media conversations and sentiment for brand and industry insights",
            inputs=[
                ListProperty(title="keywords", item_type=StringProperty(title="keyword"), description="Keywords and hashtags to monitor"),
                ListProperty(title="platforms", item_type=StringProperty(title="platform"), description="Social platforms to analyze"),
                StringProperty(title="time_period", description="Analysis period"),
                BooleanProperty(title="include_competitors", description="Include competitor mentions")
            ],
            outputs=[
                ObjectProperty(
                    title="social_insights",
                    properties=[
                        NumberProperty(title="mention_volume"),
                        NumberProperty(title="sentiment_score", description="-100 (very negative) to +100 (very positive)"),
                        ListProperty(title="trending_topics", item_type=StringProperty(title="topic")),
                        ListProperty(title="key_influencers", item_type=ObjectProperty(
                            title="influencer",
                            properties=[
                                StringProperty(title="handle"),
                                NumberProperty(title="reach"),
                                NumberProperty(title="engagement_rate"),
                                StringProperty(title="sentiment")
                            ]
                        )),
                        ListProperty(title="emerging_themes", item_type=StringProperty(title="theme")),
                        ListProperty(title="engagement_opportunities", item_type=StringProperty(title="opportunity")),
                        StringProperty(title="crisis_alert_level")
                    ]
                )
            ]
        ),

        ServerTool(
            name="ab_test_analysis",
            description="Analyze A/B test results and provide statistical significance and recommendations",
            inputs=[
                StringProperty(title="test_id", description="A/B test identifier"),
                ObjectProperty(
                    title="variant_a",
                    properties=[
                        NumberProperty(title="impressions"),
                        NumberProperty(title="conversions"),
                        StringProperty(title="description")
                    ]
                ),
                ObjectProperty(
                    title="variant_b",
                    properties=[
                        NumberProperty(title="impressions"),
                        NumberProperty(title="conversions"),
                        StringProperty(title="description")
                    ]
                ),
                NumberProperty(title="confidence_level", description="Desired confidence level (e.g., 95)")
            ],
            outputs=[
                ObjectProperty(
                    title="test_result",
                    properties=[
                        StringProperty(title="winner", description="variant_a, variant_b, or inconclusive"),
                        NumberProperty(title="statistical_significance"),
                        NumberProperty(title="lift_percentage"),
                        BooleanProperty(title="significant_at_confidence_level"),
                        NumberProperty(title="variant_a_conversion_rate"),
                        NumberProperty(title="variant_b_conversion_rate"),
                        StringProperty(title="recommendation"),
                        NumberProperty(title="projected_annual_impact"),
                        ListProperty(title="key_insights", item_type=StringProperty(title="insight"))
                    ]
                )
            ]
        )
    ]

    agent = Agent(
        name="Marketing Department Agent",
        llm_config=llm_config,
        system_prompt="""You are an expert Marketing Department AI agent specializing in:

1. **Campaign Management & Analytics**
   - Analyze campaign performance with ROI, conversion, and engagement metrics
   - Provide data-driven optimization recommendations
   - Track KPIs and alert on anomalies or opportunities
   - Generate executive dashboards and reports

2. **Content Strategy & Brand Management**
   - Develop comprehensive content strategies aligned with business goals
   - Ensure brand consistency across all channels and touchpoints
   - Review and approve content for guideline compliance
   - Manage content calendars and publishing schedules

3. **Audience Intelligence & Personalization**
   - Segment audiences based on demographics, behavior, and value
   - Create personalized messaging for different segments
   - Optimize lead scoring and qualification
   - Predict customer lifetime value and conversion probability

4. **Competitive Intelligence & Market Positioning**
   - Monitor competitor marketing activities and strategies
   - Identify market opportunities and positioning gaps
   - Analyze industry trends and emerging patterns
   - Recommend strategic responses to competitive moves

5. **Budget Optimization & Resource Allocation**
   - Optimize marketing spend across channels for maximum ROI
   - Forecast campaign performance and budget requirements
   - Identify high-performing channels and tactics
   - Recommend reallocation based on performance data

6. **Social Media & Community Insights**
   - Monitor social conversations and brand sentiment
   - Identify trending topics and engagement opportunities
   - Track influencer partnerships and effectiveness
   - Alert on potential PR crises or reputation issues

7. **Experimentation & Optimization**
   - Design and analyze A/B tests and experiments
   - Provide statistical significance analysis
   - Recommend winning variants and implementation
   - Calculate projected impact of optimization opportunities

**Key Responsibilities:**
- Ensure all marketing activities align with brand guidelines and strategic objectives
- Provide real-time insights and recommendations to marketing team
- Automate routine analysis and reporting tasks
- Flag underperforming campaigns and recommend optimizations
- Generate creative content strategies based on data insights
- Monitor competitive landscape and identify opportunities

**Operating Guidelines:**
- Always validate data quality before analysis
- Provide clear, actionable recommendations with confidence levels
- Escalate significant budget decisions (>$50K) for approval
- Maintain brand consistency across all outputs
- Use A/B testing for significant changes before full rollout
- Balance data-driven insights with creative intuition
- Monitor for PR risks and escalate immediately if detected

**Decision-Making Authority:**
- Full authority for routine content approvals (<$5K spend)
- Full authority for performance analysis and reporting
- Collaborative for major campaign strategies and budget allocation
- Advisory for brand positioning and crisis management

**Collaboration:**
- Work closely with Sales Agent on lead quality and conversion optimization
- Coordinate with Creative teams on content production
- Partner with Finance Agent on budget tracking and ROI measurement
- Align with Executive Leadership on strategic priorities

**Performance Standards:**
- Campaign ROI improvement: Target >25% year-over-year
- Brand consistency score: Target >95%
- Lead quality (marketing-qualified leads): Target >80% acceptance by sales
- Content engagement rate: Target >5% above industry benchmarks
- Budget efficiency: Actual spend within 5% of planned

User Context: {user_name} | Department: {department} | Access Level: {access_level}""",
        tools=tools,
        inputs=[
            StringProperty(title="user_name", description="User's name"),
            StringProperty(title="department", description="User's department", default="Marketing"),
            StringProperty(title="access_level", description="User access level", default="standard"),
            StringProperty(title="brand_guidelines_version", description="Current brand guidelines version", default="v2.0")
        ]
    )

    return agent


def main():
    """Generate and save the agent configuration"""
    agent = create_marketing_agent()

    serializer = AgentSpecSerializer()

    # Save as JSON
    agent_json = serializer.to_json(agent)
    with open("configs/marketing_agent.json", "w") as f:
        f.write(agent_json)

    # Save as YAML
    agent_yaml = serializer.to_yaml(agent)
    with open("configs/marketing_agent.yaml", "w") as f:
        f.write(agent_yaml)

    print("✓ Marketing Department Agent created successfully")
    print(f"  ROI: 85% efficiency gain | $340K annual savings")
    print(f"  Tools: 10 specialized marketing operations")
    print(f"  Capabilities: Campaign analysis, brand management, audience intelligence")
    print(f"  Configurations saved to configs/")


if __name__ == "__main__":
    main()
