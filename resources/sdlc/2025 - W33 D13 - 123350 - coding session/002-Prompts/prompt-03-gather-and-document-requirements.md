# Task 3: Gather and Document Requirements - Execution Prompt

You are a Business Analyst tasked with gathering requirements and translating them into user stories. 

## Context Files to Analyze:
Review all available files in the **000-context** folder and **004-outputs** folder, along with the product vision from Task 1 and use cases from Task 2 to extract and document requirements. The context files may include:
- Business requirements and functional specifications
- User workflow documentation
- Technical constraints and system requirements
- Data requirements and integration specifications
- Any other relevant project documentation

## Information to Extract:

1. **Functional Requirements**
   - What specific features or capabilities are needed?
   - What actions must users be able to perform?
   - What business rules or logic must be implemented?
   - What data needs to be captured, stored, or displayed?

2. **Non-Functional Requirements**
   - Performance requirements (speed, response time)
   - Security requirements (authentication, authorization, data protection)
   - Usability requirements (accessibility, user experience)
   - Integration requirements (APIs, data sources, external systems)
   - Scalability and reliability requirements

3. **Data Requirements**
   - What data sources are mentioned?
   - What data fields or attributes are needed?
   - What data formats or standards must be supported?
   - What data validation rules apply?

4. **User Interface Requirements**
   - What screens or views are needed?
   - What user interactions are required?
   - What information must be displayed?
   - What input methods are needed?

5. **Business Logic Requirements**
   - What calculations or processing is needed?
   - What workflows or approval processes exist?
   - What business rules must be enforced?
   - What notifications or alerts are required?

## Output Format:

Create user stories in this format:

**Epic**: [High-level feature area]

**User Story ID**: US-001, US-002, etc.

**User Story**: As a [user role], I want [functionality] so that [business value]

**Acceptance Criteria**:
- Given [precondition]
- When [action]
- Then [expected result]

**Priority**: High/Medium/Low

**Estimated Effort**: Small/Medium/Large

**Dependencies**: Other user stories or external factors

**Notes**: Additional context, assumptions, or constraints

## Instructions:
1. Review product vision, use cases, and context files
2. Extract both functional and non-functional requirements
3. Group related requirements into epics
4. Write clear, testable user stories with acceptance criteria
5. Prioritize stories based on business value and prototype feasibility
6. Focus on requirements that can be demonstrated in a prototype
7. Note any assumptions about missing requirements

## Output Instructions:
Save your completed analysis as a markdown file named "03-requirements-and-user-stories.md" in the 004-Outputs folder.

Begin your analysis by stating: "Based on the context files in the 000-context folder and 004-outputs folder, product vision from Task 1, and use cases from Task 2, I have identified the following requirements and translated them into user stories..."