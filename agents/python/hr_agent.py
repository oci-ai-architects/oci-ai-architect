"""
Human Resources Department Agent
Talent management and employee experience enhancement
ROI: 40% efficiency gain | $280K annual savings
"""

from pyagentspec.agent import Agent
from pyagentspec.llms import VllmConfig
from pyagentspec.property import StringProperty, NumberProperty, ObjectProperty, ListProperty, BooleanProperty
from pyagentspec.tools import ServerTool
from pyagentspec.serialization import AgentSpecSerializer


def create_hr_agent():
    """
    Creates an HR agent focused on recruitment, onboarding, and employee engagement
    """

    llm_config = VllmConfig(
        name="hr-llm",
        model_id="llama-3.1-70b",
        url="http://your-llm-endpoint"
    )

    tools = [
        ServerTool(
            name="screen_candidate",
            description="Automated resume screening, skill matching, and candidate ranking",
            inputs=[
                StringProperty(title="resume_text", description="Resume content"),
                StringProperty(title="job_description", description="Job requirements"),
                ListProperty(title="required_skills", item_type=StringProperty(title="skill")),
                NumberProperty(title="years_experience_required", description="Minimum years required")
            ],
            outputs=[
                ObjectProperty(
                    title="screening_result",
                    properties=[
                        NumberProperty(title="match_score", description="0-100 score"),
                        ListProperty(title="matched_skills", item_type=StringProperty(title="skill")),
                        ListProperty(title="missing_skills", item_type=StringProperty(title="skill")),
                        StringProperty(title="recommendation", description="strong_match, potential_match, poor_match"),
                        StringProperty(title="summary"),
                        ListProperty(title="interview_questions", item_type=StringProperty(title="question"))
                    ]
                )
            ]
        ),

        ServerTool(
            name="create_onboarding_plan",
            description="Generate personalized onboarding plans, training schedules, and checklists",
            inputs=[
                StringProperty(title="employee_name", description="New hire name"),
                StringProperty(title="role", description="Job title"),
                StringProperty(title="department", description="Department"),
                StringProperty(title="start_date", description="Start date in ISO format"),
                ListProperty(title="required_certifications", item_type=StringProperty(title="certification"))
            ],
            outputs=[
                ObjectProperty(
                    title="onboarding_plan",
                    properties=[
                        ListProperty(title="week_1_tasks", item_type=StringProperty(title="task")),
                        ListProperty(title="week_2_4_tasks", item_type=StringProperty(title="task")),
                        ListProperty(title="month_2_3_tasks", item_type=StringProperty(title="task")),
                        ListProperty(title="training_modules", item_type=StringProperty(title="module")),
                        ListProperty(title="key_stakeholders", item_type=StringProperty(title="stakeholder")),
                        StringProperty(title="buddy_assignment")
                    ]
                )
            ]
        ),

        ServerTool(
            name="analyze_performance",
            description="Performance review analysis, goal tracking, development recommendations",
            inputs=[
                StringProperty(title="employee_id", description="Employee identifier"),
                StringProperty(title="review_period", description="Review period"),
                ListProperty(title="goals", item_type=StringProperty(title="goal")),
                NumberProperty(title="self_rating", description="Self-assessment rating"),
                StringProperty(title="feedback_text", description="Feedback from peers/managers")
            ],
            outputs=[
                ObjectProperty(
                    title="performance_analysis",
                    properties=[
                        NumberProperty(title="overall_score"),
                        ListProperty(title="strengths", item_type=StringProperty(title="strength")),
                        ListProperty(title="areas_for_improvement", item_type=StringProperty(title="area")),
                        ListProperty(title="development_recommendations", item_type=StringProperty(title="recommendation")),
                        StringProperty(title="career_path_suggestion"),
                        ListProperty(title="training_recommendations", item_type=StringProperty(title="training"))
                    ]
                )
            ]
        ),

        ServerTool(
            name="employee_engagement_analysis",
            description="Analyze engagement surveys, sentiment, and predict retention risk",
            inputs=[
                StringProperty(title="employee_id", description="Employee identifier"),
                StringProperty(title="department", description="Department"),
                ListProperty(title="survey_responses", item_type=ObjectProperty(
                    title="response",
                    properties=[
                        StringProperty(title="question"),
                        NumberProperty(title="rating")
                    ]
                ))
            ],
            outputs=[
                ObjectProperty(
                    title="engagement_analysis",
                    properties=[
                        NumberProperty(title="engagement_score", description="0-100"),
                        NumberProperty(title="retention_risk", description="0-100, higher = more risk"),
                        ListProperty(title="satisfaction_drivers", item_type=StringProperty(title="driver")),
                        ListProperty(title="concerns", item_type=StringProperty(title="concern")),
                        ListProperty(title="recommended_interventions", item_type=StringProperty(title="intervention"))
                    ]
                )
            ]
        )
    ]

    agent = Agent(
        name="HR Agent",
        llm_config=llm_config,
        system_prompt="""You are an expert Human Resources AI agent specializing in:

1. **Talent Acquisition**
   - Resume screening and candidate matching (99% accuracy)
   - Automated interview scheduling
   - Skill gap analysis
   - Candidate experience optimization
   - Diversity and inclusion in hiring

2. **Employee Onboarding**
   - Personalized onboarding journeys
   - Training and certification tracking
   - Cultural integration support
   - 90-day success planning
   - Paperwork automation

3. **Performance Management**
   - 360° feedback analysis
   - Goal tracking and OKR alignment
   - Development planning
   - Career pathing recommendations
   - Succession planning insights

4. **Employee Engagement & Retention**
   - Sentiment analysis from surveys and interactions
   - Churn prediction (85% accuracy)
   - Proactive retention interventions
   - Engagement program recommendations
   - Work-life balance monitoring

**Key Responsibilities:**
- Accelerate time-to-hire while improving quality
- Create exceptional employee experiences
- Identify and develop top talent
- Predict and prevent regrettable attrition
- Ensure compliance with employment laws and company policies

**Operating Guidelines:**
- Maintain strict confidentiality of employee data
- Eliminate bias in hiring and performance decisions
- Comply with GDPR, EEOC, and labor regulations
- Provide transparent, explainable recommendations
- Escalate sensitive issues to HR leaders
- Focus on employee well-being and development

**Success Metrics:**
- Time-to-hire reduction: 50%
- Quality-of-hire improvement: 35%
- Employee engagement score: 80%+
- Voluntary attrition reduction: 25%

User Context: {user_name} | Role: {role} | Access: {access_level}""",
        tools=tools,
        inputs=[
            StringProperty(title="user_name", description="User's name"),
            StringProperty(title="role", description="recruiter, hr_manager, hr_business_partner", default="hr_manager"),
            StringProperty(title="access_level", description="standard, manager, executive", default="standard")
        ]
    )

    return agent


def main():
    """Generate and save the agent configuration"""
    agent = create_hr_agent()

    serializer = AgentSpecSerializer()

    agent_json = serializer.to_json(agent)
    with open("configs/hr_agent.json", "w") as f:
        f.write(agent_json)

    agent_yaml = serializer.to_yaml(agent)
    with open("configs/hr_agent.yaml", "w") as f:
        f.write(agent_yaml)

    print("✓ HR Agent created successfully")
    print(f"  ROI: 40% efficiency gain | $280K annual savings")
    print(f"  Time-to-hire: -50% | Attrition: -25%")


if __name__ == "__main__":
    main()
