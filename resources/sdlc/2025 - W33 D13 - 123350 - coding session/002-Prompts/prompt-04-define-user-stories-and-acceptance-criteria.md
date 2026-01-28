# Task 4: Define User Stories and Acceptance Criteria - Execution Prompt

You are a Product Manager tasked with refining user stories and defining detailed acceptance criteria. 

## Context Files to Reference:
Review all available files in the **000-context** folder and **004-outputs** folder, including the initial user stories from Task 3 to enhance them with comprehensive acceptance criteria for development and testing. The context files may provide additional details on:
- Business rules and validation requirements
- User experience expectations
- Technical constraints and performance requirements
- Integration and data requirements
- Any other relevant specifications

## Information to Extract:

1. **User Story Refinement**
   - Are the user stories clear and unambiguous?
   - Do they follow the "As a... I want... So that..." format?
   - Is the business value clearly articulated?
   - Are they appropriately sized for development?

2. **Acceptance Criteria Details**
   - What are the specific conditions that must be met?
   - What are the expected behaviors and outcomes?
   - What edge cases or error conditions need to be handled?
   - What validation rules must be enforced?

3. **User Experience Requirements**
   - What should the user interface look like?
   - How should users interact with the system?
   - What feedback should users receive?
   - What accessibility requirements apply?

4. **Data and Integration Requirements**
   - What data must be displayed or captured?
   - How should data be formatted or validated?
   - What integrations or API calls are needed?
   - What happens when external systems are unavailable?

5. **Performance and Quality Requirements**
   - What response time expectations exist?
   - What error handling is required?
   - What security considerations apply?
   - What browser or device compatibility is needed?

## Output Format:

For each refined user story:

**Epic**: [Feature area]

**User Story ID**: US-001

**Title**: [Brief descriptive title]

**User Story**: As a [specific user role], I want [specific functionality] so that [clear business benefit]

**Priority**: High/Medium/Low

**Story Points**: [Estimation for development effort]

**Acceptance Criteria**:
**Scenario 1**: [Happy path]
- Given [initial state/preconditions]
- When [user action or trigger]
- Then [expected system response]
- And [additional expected outcomes]

**Scenario 2**: [Alternative flow]
- Given [different initial state]
- When [different action]
- Then [different expected response]

**Scenario 3**: [Error handling]
- Given [error condition]
- When [action that triggers error]
- Then [error handling behavior]

**Definition of Done**:
- [ ] Functionality works as specified
- [ ] All acceptance criteria pass
- [ ] UI matches design requirements
- [ ] Error handling implemented
- [ ] Performance requirements met
- [ ] Security requirements met

**Dependencies**: [Other stories or external dependencies]

**Notes**: [Additional context, assumptions, or technical considerations]

## Instructions:
1. Review and refine user stories from Task 3
2. Break down large stories into smaller, manageable pieces
3. Write comprehensive acceptance criteria covering happy path, alternative flows, and error cases
4. Ensure acceptance criteria are testable and measurable
5. Prioritize stories for prototype development
6. Add technical notes for developers where needed
7. Validate that stories align with use cases and business objectives

## Output Instructions:
Save your completed analysis as a markdown file named "04-refined-user-stories-and-acceptance-criteria.md" in the 004-Outputs folder.

Begin your analysis by stating: "Based on the context files in the 000-context folder and 004-outputs folder, including the initial user stories from Task 3, I have refined and enhanced them with detailed acceptance criteria..."