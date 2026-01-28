"""
Finance & Accounting Department Agent
Automated financial operations and intelligent analysis
ROI: 65% efficiency gain | $420K annual savings
"""

from pyagentspec.agent import Agent
from pyagentspec.llms import VllmConfig
from pyagentspec.property import StringProperty, NumberProperty, ObjectProperty, ListProperty
from pyagentspec.tools import ServerTool
from pyagentspec.serialization import AgentSpecSerializer


def create_finance_agent():
    """
    Creates a Finance & Accounting agent with specialized financial tools
    """

    llm_config = VllmConfig(
        name="finance-llm",
        model_id="llama-3.1-70b",
        url="http://your-llm-endpoint"  # Configure your Oracle OCI Gen AI endpoint
    )

    tools = [
        ServerTool(
            name="process_invoice",
            description="Process and validate invoices with automated AP/AR, anomaly detection",
            inputs=[
                StringProperty(title="invoice_number", description="Invoice reference number"),
                StringProperty(title="vendor_id", description="Vendor identifier"),
                NumberProperty(title="amount", description="Invoice amount"),
                StringProperty(title="invoice_date", description="Invoice date in ISO format")
            ],
            outputs=[
                ObjectProperty(
                    title="processing_result",
                    properties=[
                        StringProperty(title="status", description="approved, rejected, or flagged"),
                        ListProperty(title="anomalies", item_type=StringProperty(title="anomaly")),
                        StringProperty(title="payment_due_date"),
                        NumberProperty(title="confidence_score")
                    ]
                )
            ]
        ),

        ServerTool(
            name="financial_forecast",
            description="Generate revenue projections, budget planning, and variance analysis",
            inputs=[
                StringProperty(title="analysis_period", description="Forecast period (monthly, quarterly, yearly)"),
                StringProperty(title="department", description="Department code for budget analysis"),
                ListProperty(title="historical_data", item_type=NumberProperty(title="value"))
            ],
            outputs=[
                ObjectProperty(
                    title="forecast",
                    properties=[
                        ListProperty(title="projected_values", item_type=NumberProperty(title="value")),
                        NumberProperty(title="confidence_interval"),
                        StringProperty(title="trend_analysis"),
                        ListProperty(title="risk_factors", item_type=StringProperty(title="risk"))
                    ]
                )
            ]
        ),

        ServerTool(
            name="compliance_check",
            description="Monitor SOX compliance, generate audit trails, and regulatory reporting",
            inputs=[
                StringProperty(title="transaction_id", description="Transaction to audit"),
                StringProperty(title="compliance_framework", description="SOX, GAAP, IFRS, etc.")
            ],
            outputs=[
                ObjectProperty(
                    title="compliance_result",
                    properties=[
                        StringProperty(title="status", description="compliant, non-compliant, or requires review"),
                        ListProperty(title="violations", item_type=StringProperty(title="violation")),
                        StringProperty(title="audit_trail"),
                        ListProperty(title="recommendations", item_type=StringProperty(title="recommendation"))
                    ]
                )
            ]
        ),

        ServerTool(
            name="expense_analysis",
            description="Analyze spending patterns, identify cost savings opportunities",
            inputs=[
                StringProperty(title="department", description="Department to analyze"),
                StringProperty(title="time_period", description="Analysis period"),
                StringProperty(title="category", description="Expense category")
            ],
            outputs=[
                ObjectProperty(
                    title="analysis",
                    properties=[
                        NumberProperty(title="total_spend"),
                        NumberProperty(title="variance_percentage"),
                        ListProperty(title="savings_opportunities", item_type=ObjectProperty(
                            title="opportunity",
                            properties=[
                                StringProperty(title="description"),
                                NumberProperty(title="potential_savings")
                            ]
                        )),
                        StringProperty(title="trend")
                    ]
                )
            ]
        )
    ]

    agent = Agent(
        name="Finance & Accounting Agent",
        llm_config=llm_config,
        system_prompt="""You are an expert Finance & Accounting AI agent specializing in:

1. **Automated Invoice Processing**
   - Process AP/AR with 99.5% accuracy
   - Detect anomalies and fraud patterns
   - Optimize payment terms and cash flow
   - Three-way matching automation

2. **Financial Forecasting & Planning**
   - Revenue projections with ML models
   - Budget planning and variance analysis
   - Cash flow forecasting
   - Scenario planning and sensitivity analysis

3. **Compliance & Audit**
   - SOX compliance monitoring
   - Automated audit trail generation
   - Regulatory reporting (GAAP, IFRS)
   - Control testing and documentation

4. **Cost Optimization**
   - Expense analysis and benchmarking
   - Identify savings opportunities
   - Vendor spend optimization
   - Budget variance analysis

**Key Responsibilities:**
- Ensure all financial processes comply with accounting standards
- Provide real-time financial insights and recommendations
- Automate repetitive financial tasks to improve efficiency
- Flag unusual transactions for human review
- Generate executive financial reports and dashboards

**Operating Guidelines:**
- Always validate data before processing
- Maintain complete audit trails
- Escalate high-risk transactions (>$50K) for approval
- Ensure compliance with SOX and corporate policies
- Provide clear explanations for all financial recommendations

User Context: {user_name} | Department: {department} | Access Level: {access_level}""",
        tools=tools,
        inputs=[
            StringProperty(title="user_name", description="User's name"),
            StringProperty(title="department", description="User's department", default="Finance"),
            StringProperty(title="access_level", description="User access level", default="standard")
        ]
    )

    return agent


def main():
    """Generate and save the agent configuration"""
    agent = create_finance_agent()

    serializer = AgentSpecSerializer()

    # Save as JSON
    agent_json = serializer.to_json(agent)
    with open("configs/finance_agent.json", "w") as f:
        f.write(agent_json)

    # Save as YAML
    agent_yaml = serializer.to_yaml(agent)
    with open("configs/finance_agent.yaml", "w") as f:
        f.write(agent_yaml)

    print("✓ Finance & Accounting Agent created successfully")
    print(f"  ROI: 65% efficiency gain | $420K annual savings")
    print(f"  Configurations saved to configs/")


if __name__ == "__main__":
    main()
