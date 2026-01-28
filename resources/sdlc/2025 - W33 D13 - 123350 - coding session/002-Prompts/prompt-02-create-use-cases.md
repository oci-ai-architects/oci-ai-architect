# Task 2: Create Use Cases - Execution Prompt

You are a Business Analyst tasked with creating use cases from customer context. 

## Context Files to Analyze:
Review all available files in the **000-context** folder and **004-outputs** folder, including the product vision/objectives from Task 1 to identify and document specific use cases. The context files may include:
- Business requirements and stakeholder communications
- Technical specifications and system documentation
- User requirements and workflow descriptions
- Data sources and integration requirements
- Any other relevant project documentation

## Information to Extract:

1. **Business Processes**
   - What business processes are mentioned or implied?
   - What workflows or procedures need to be supported?
   - What are the current pain points in these processes?

2. **User Roles and Actors**
   - Who are the different types of users mentioned?
   - What are their job titles, responsibilities, and goals?
   - What permissions or access levels do they need?

3. **Business Scenarios**
   - What specific situations or scenarios are described?
   - What triggers these scenarios?
   - What are the desired outcomes?

4. **System Interactions**
   - What systems or tools are currently being used?
   - What integrations or data sources are mentioned?
   - What new capabilities are needed?

5. **Business Value**
   - What value would each use case provide?
   - How does it align with business objectives?
   - What problems does it solve?

## Output Format:

For each use case, create:

**Use Case ID**: UC-001, UC-002, etc.

**Use Case Title**: Brief descriptive title

**Primary Actor**: Main user/role

**Secondary Actors**: Other involved parties

**Preconditions**: What must be true before this use case can execute

**Main Success Scenario**: Step-by-step flow of the happy path
1. Actor does X
2. System responds with Y
3. Actor does Z
etc.

**Alternative Flows**: What happens when things go differently

**Postconditions**: What is true after successful completion

**Business Value**: Why this use case matters and its expected impact

**Priority**: High/Medium/Low based on business importance

## Instructions:
1. Review the product vision and objectives from Task 1
2. Analyze context files for business processes and user needs
3. Identify 5-10 key use cases that support the business objectives
4. Prioritize use cases based on business value and feasibility
5. Ensure use cases are specific, measurable, and testable
6. Focus on use cases that can be demonstrated in a prototype

## Output Instructions:
Save your completed analysis as a markdown file named "02-use-cases.md" in the 004-Outputs folder.

Begin your analysis by stating: "Based on the context files in the 000-context folder and 004-outputs folder, including the product vision from Task 1, I have identified the following use cases..."