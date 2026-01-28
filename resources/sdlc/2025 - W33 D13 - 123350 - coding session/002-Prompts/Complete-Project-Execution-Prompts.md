# Complete Project Execution Prompts
## Solidarity Insurance AI Use Cases - Prototype Development

This document contains all execution prompts needed to systematically complete the entire project from vision to final presentation. Each prompt can be copied and pasted to execute the corresponding task sequentially.

---

## PROMPT 1: Define Product Vision and Objectives
**Task**: Task-01-Define-Product-Vision-and-Objectives  
**Role**: Product Manager  
**Context**: Read files in 000-context, execute task-01 using prompt-01 and save the file in 004-outputs

<prompt1>
You are a Product Manager tasked with defining the product vision and business objectives. Analyze the provided context files and extract the following information:

## Information to Extract:

1. **Business Context**
   - What industry or domain is this for?
   - What is the customer's current business situation?
   - What challenges or pain points are they facing?

2. **Stakeholder Information**
   - Who are the key stakeholders mentioned?
   - What are their roles and responsibilities?
   - What are their specific needs or concerns?

3. **Business Goals**
   - What business outcomes does the customer want to achieve?
   - Are there any specific metrics or KPIs mentioned?
   - What is the expected timeline or urgency?

4. **Solution Context**
   - What type of solution is being considered?
   - Are there any technology preferences or constraints?
   - What is the scope of the solution?

5. **Success Criteria**
   - How will success be measured?
   - What would constitute a successful outcome?
   - Are there any specific requirements or must-haves?

## Output Format:

Create a document with the following sections:

**Product Vision Statement**
- A clear, concise vision statement (1-2 sentences) that captures the essence of what we're building and why

**Business Objectives**
- Primary objective (main business goal)
- Secondary objectives (supporting goals)
- Success metrics (how we'll measure achievement)

**Context Summary**
- Industry/domain context
- Key stakeholders and their needs
- Current challenges being addressed
- Solution scope and constraints

## Instructions:
1. Read through all provided context files carefully
2. Extract relevant information using the categories above
3. Synthesize the information into a coherent vision and objectives
4. Ensure the vision is inspiring yet achievable
5. Make objectives specific, measurable, and time-bound where possible
6. If information is missing, note what assumptions you're making

Begin your analysis by stating: "Based on the provided context files, I have extracted the following information for defining the product vision and objectives..."

Save output as: Task-01-Product-Vision-and-Objectives-Output.md
</prompt1>

---

## PROMPT 2: Create Use Cases
**Task**: Task-02-Create-Use-Cases  
**Role**: Business Analyst  
**Dependencies**: Requires Task 1 output

<prompt2>
You are a Business Analyst tasked with creating use cases from customer context. Analyze the provided context files and the product vision/objectives from Task 1 to identify and document specific use cases.

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

Begin your analysis by stating: "Based on the context files and product vision, I have identified the following use cases..."

Save output as: Task-02-Use-Cases-Output.md
</prompt2>

---

## PROMPT 3: Gather and Document Requirements
**Task**: Task-03-Gather-and-Document-Requirements  
**Role**: Business Analyst  
**Dependencies**: Requires Task 1 and Task 2 outputs

<prompt3>
You are a Business Analyst tasked with gathering requirements and translating them into user stories. Analyze the provided context files, product vision from Task 1, and use cases from Task 2 to extract and document requirements.

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

Begin your analysis by stating: "Based on the context files, product vision, and use cases, I have identified the following requirements and translated them into user stories..."

Save output as: Task-03-Requirements-and-User-Stories-Output.md
</prompt3>

---

## PROMPT 4: Define User Stories and Acceptance Criteria
**Task**: Task-04-Define-User-Stories-and-Acceptance-Criteria  
**Role**: Product Manager  
**Dependencies**: Requires Task 3 output

<prompt4>
You are a Product Manager tasked with refining user stories and defining detailed acceptance criteria. Review the initial user stories from Task 3 and enhance them with comprehensive acceptance criteria for development and testing.

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

Begin your analysis by stating: "Based on the initial user stories from Task 3, I have refined and enhanced them with detailed acceptance criteria..."

Save output as: Task-04-Detailed-User-Stories-and-Acceptance-Criteria-Output.md
</prompt4>

---

## PROMPT 5: Create Wireframes and Design Mockups
**Task**: Task-05-Create-Wireframes-and-Design-Mockups  
**Role**: UI/UX Designer  
**Dependencies**: Requires Tasks 1-4 outputs

<prompt5>
You are a UI/UX Designer tasked with creating wireframes and high-fidelity mockups. Analyze the use cases, user stories, and acceptance criteria from previous tasks to design an intuitive user interface that supports the customer's business processes.

## Information to Extract:

1. **User Interface Requirements**
   - What screens or pages are needed based on user stories?
   - What information must be displayed on each screen?
   - What user actions need to be supported?
   - What navigation patterns are implied?

2. **User Experience Flow**
   - What is the typical user journey through the application?
   - What are the key decision points or branching paths?
   - Where might users need help or guidance?
   - What are the most critical user tasks?

3. **Data Display Requirements**
   - What data needs to be shown to users?
   - How should data be organized and prioritized?
   - What filtering, sorting, or search capabilities are needed?
   - What data entry forms are required?

4. **Interaction Patterns**
   - What buttons, links, and controls are needed?
   - What feedback should users receive for their actions?
   - What validation and error messages are required?
   - What responsive behavior is needed for different devices?

5. **Business Process Support**
   - How do the designs support the identified use cases?
   - What workflow steps need visual representation?
   - Where are approval or review processes needed?
   - What reporting or dashboard views are required?

## Output Format:

**Design System Elements**:
- Color palette and branding guidelines
- Typography specifications
- Button and form element styles
- Icon library and usage guidelines

**Wireframes** (for each major screen):
- **Screen Name**: [Descriptive name]
- **Purpose**: [What this screen accomplishes]
- **User Story Reference**: [Related user stories]
- **Layout**: [Describe the wireframe layout]
  - Header: [Navigation, branding, user info]
  - Main Content: [Primary content area layout]
  - Sidebar: [Secondary navigation or information]
  - Footer: [Additional links or information]
- **Key Elements**: [List of major UI components]
- **User Actions**: [Available actions on this screen]
- **Navigation**: [How users get to/from this screen]

**High-Fidelity Mockups** (for priority screens):
- **Screen Name**: [Same as wireframe]
- **Visual Design**: [Detailed description of colors, typography, spacing]
- **Interactive Elements**: [Buttons, forms, controls with specific styling]
- **Content Examples**: [Sample data or realistic content]
- **Responsive Considerations**: [How design adapts to different screen sizes]
- **Accessibility Features**: [Color contrast, keyboard navigation, screen reader support]

**User Flow Diagrams**:
- **Flow Name**: [e.g., "User Registration Flow"]
- **Starting Point**: [Where the flow begins]
- **Steps**: [Each step in the user journey]
- **Decision Points**: [Where users make choices]
- **End Points**: [Possible outcomes]

## Instructions:
1. Review use cases, user stories, and acceptance criteria from previous tasks
2. Identify all required screens and user interface elements
3. Create low-fidelity wireframes focusing on layout and functionality
4. Design high-fidelity mockups for the most critical screens
5. Ensure designs support all identified user stories
6. Consider responsive design for different device sizes
7. Include accessibility considerations in your designs
8. Document design decisions and rationale

Begin your analysis by stating: "Based on the use cases and user stories, I have identified the following screens and user interface requirements for the wireframes and mockups..."

Save output as: Task-05-Wireframes-and-Mockups-Output.md
</prompt5>

---

## PROMPT 6: Implement HTML Structure
**Task**: Task-06-Implement-HTML-Structure  
**Role**: Frontend Developer  
**Dependencies**: Requires Task 5 output

<prompt6>
You are a Frontend Developer tasked with implementing the HTML structure for the prototype. Analyze the wireframes and mockups from Task 5, along with the user stories and acceptance criteria, to create semantic HTML that supports all required functionality.

## Information to Extract:

1. **Page Structure Requirements**
   - What pages/screens need to be created based on wireframes?
   - What is the overall site navigation structure?
   - What common elements appear across multiple pages?
   - What unique elements are needed for specific pages?

2. **Content Organization**
   - What content sections are defined in the wireframes?
   - How should content be hierarchically organized?
   - What headings and subheadings are needed?
   - What content blocks or components are repeated?

3. **Form and Input Requirements**
   - What forms are needed based on user stories?
   - What input fields, types, and validation are required?
   - What buttons and actions need to be implemented?
   - What data capture requirements exist?

4. **Data Display Requirements**
   - What tables, lists, or data grids are needed?
   - What dynamic content areas require placeholder structure?
   - What media elements (images, videos) need to be supported?
   - What interactive elements need HTML foundation?

5. **Accessibility and SEO Requirements**
   - What semantic HTML elements should be used?
   - What ARIA labels and roles are needed?
   - What meta tags and structured data are required?
   - What keyboard navigation support is needed?

## Output Format:

**File Structure**:
```
/prototype
  /index.html
  /pages
    /[page-name].html
  /components
    /[component-name].html
  /assets
    /css (placeholder)
    /js (placeholder)
    /images (placeholder)
```

**For Each HTML File**:

**File**: [filename.html]
**Purpose**: [What this page accomplishes]
**User Stories Supported**: [List of relevant user story IDs]

**HTML Structure**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags, title, and links -->
</head>
<body>
    <!-- Semantic HTML structure -->
</body>
</html>
```

**Key Elements**:
- **Header**: Navigation, branding, user controls
- **Main Content**: Primary page content with semantic sections
- **Sidebar**: Secondary navigation or information panels
- **Footer**: Additional links and information
- **Forms**: All required input forms with proper labels and validation attributes
- **Data Tables**: Structured data display with proper headers
- **Interactive Elements**: Buttons, links, and controls with appropriate attributes

**Accessibility Features**:
- Semantic HTML5 elements (header, nav, main, section, article, aside, footer)
- Proper heading hierarchy (h1-h6)
- Form labels and fieldsets
- Alt text placeholders for images
- ARIA labels where needed
- Keyboard navigation support

## Instructions:
1. Review wireframes, mockups, and user stories from previous tasks
2. Create a logical file structure for the prototype
3. Implement semantic HTML for each identified page
4. Include all forms, tables, and interactive elements
5. Add proper accessibility attributes and structure
6. Use placeholder content that reflects real use cases
7. Ensure HTML validates and follows best practices
8. Include comments explaining complex sections

Begin your implementation by stating: "Based on the wireframes and user stories, I will create the following HTML structure for the prototype..."

Save output as: Task-06-HTML-Structure-Output.md (plus actual HTML files)
</prompt6>

---

## PROMPT 7: Add Interactivity with JavaScript
**Task**: Task-07-Add-Interactivity-with-JavaScript  
**Role**: Frontend Developer  
**Dependencies**: Requires Tasks 4 and 6 outputs

<prompt7>
You are a Frontend Developer tasked with adding JavaScript interactivity to the prototype. Analyze the user stories, acceptance criteria, and use cases from previous tasks to implement dynamic functionality that demonstrates the core business processes and user workflows.

## Information to Extract:

1. **User Interaction Requirements**
   - What button clicks and form submissions need to be handled?
   - What navigation and page transitions are required?
   - What user input validation and feedback is needed?
   - What modal dialogs or popup interactions are specified?

2. **Data Management Requirements**
   - What data needs to be captured, stored, or retrieved?
   - What calculations or data processing is required?
   - What filtering, sorting, or search functionality is needed?
   - What data persistence is required for the prototype?

3. **Dynamic Content Requirements**
   - What content needs to be dynamically updated or displayed?
   - What conditional logic affects what users see?
   - What real-time updates or notifications are needed?
   - What progressive disclosure or show/hide functionality is required?

4. **Business Logic Requirements**
   - What workflows or multi-step processes need to be implemented?
   - What validation rules and business constraints must be enforced?
   - What approval or review processes need to be simulated?
   - What reporting or dashboard functionality is required?

5. **Integration and API Requirements**
   - What external data sources need to be simulated or mocked?
   - What API calls or data exchanges are implied by the use cases?
   - What third-party services or integrations are mentioned?
   - What data formats or protocols need to be supported?

## Output Format:

**JavaScript File Structure**:
```
/assets/js/
  /main.js (application initialization)
  /modules/
    /navigation.js
    /forms.js
    /data-manager.js
    /ui-components.js
  /utils/
    /helpers.js
    /validators.js
    /api-mock.js
  /data/
    /mock-data.js
```

**For Each JavaScript Module**:

**Module Name**: [e.g., Form Handler]
**Purpose**: [What functionality this module provides]
**User Stories Supported**: [List of relevant user story IDs]

**Key Functions**:
```javascript
// Function documentation with purpose and parameters
function functionName(parameters) {
    // Implementation with comments
}
```

**Event Handlers**:
- **Event**: [e.g., form submission, button click]
- **Trigger**: [What causes this event]
- **Action**: [What happens when event occurs]
- **Validation**: [What validation is performed]
- **Feedback**: [What feedback is provided to user]

**Data Structures**:
```javascript
// Mock data structures that simulate real data
const mockData = {
    // Sample data that reflects actual use cases
};
```

**Business Logic Implementation**:
- **Process Name**: [e.g., User Registration]
- **Steps**: [Each step in the process]
- **Validation Rules**: [What rules are enforced]
- **Error Handling**: [How errors are managed]
- **Success Actions**: [What happens on successful completion]

## Instructions:
1. Review user stories, acceptance criteria, and use cases from previous tasks
2. Identify all interactive elements that need JavaScript functionality
3. Create modular JavaScript code that's easy to maintain and extend
4. Implement form validation and user feedback mechanisms
5. Add dynamic content updates and state management
6. Create mock data and API responses that reflect real use cases
7. Implement business logic and workflow processes
8. Add error handling and edge case management
9. Ensure accessibility with keyboard navigation and screen reader support
10. Test all interactive functionality across different browsers

Begin your implementation by stating: "Based on the user stories and acceptance criteria, I will implement the following JavaScript functionality to create an interactive prototype..."

Save output as: Task-07-JavaScript-Interactivity-Output.md (plus actual JS files)
</prompt7>

---

## PROMPT 8: Test and Refine Prototype
**Task**: Task-08-Test-and-Refine-Prototype  
**Role**: QA Engineer  
**Dependencies**: Requires Tasks 4, 6, and 7 outputs

<prompt8>
You are a QA Engineer tasked with testing and refining the prototype. Analyze the user stories, acceptance criteria, and use cases from previous tasks to create comprehensive test plans and validate that the prototype meets all specified requirements.

## Information to Extract:

1. **Functional Testing Requirements**
   - What user stories need to be validated?
   - What acceptance criteria must be verified?
   - What business processes need to be tested end-to-end?
   - What edge cases and error conditions should be tested?

2. **Usability Testing Requirements**
   - What user workflows need to be validated for ease of use?
   - What accessibility requirements need to be tested?
   - What responsive design behavior needs validation?
   - What user feedback and error messaging should be evaluated?

3. **Technical Testing Requirements**
   - What browser compatibility needs to be verified?
   - What performance benchmarks should be met?
   - What security considerations need to be tested?
   - What data validation and integrity checks are required?

4. **Integration Testing Requirements**
   - What data flows between components need validation?
   - What mock API responses need to be tested?
   - What external system integrations should be verified?
   - What data persistence and retrieval functions need testing?

5. **User Acceptance Testing Requirements**
   - What scenarios reflect real customer use cases?
   - What business value demonstrations are needed?
   - What stakeholder feedback should be collected?
   - What success criteria from the original vision need validation?

## Output Format:

**Test Plan Overview**:
- **Testing Scope**: [What will be tested]
- **Testing Approach**: [How testing will be conducted]
- **Success Criteria**: [What constitutes successful testing]
- **Test Environment**: [Browsers, devices, conditions]

**Test Cases** (for each user story):

**Test Case ID**: TC-001
**User Story Reference**: US-001
**Test Scenario**: [Brief description of what's being tested]
**Preconditions**: [What must be true before testing]
**Test Steps**:
1. [Action to perform]
2. [Next action]
3. [Continue...]
**Expected Results**: [What should happen]
**Actual Results**: [What actually happened - to be filled during testing]
**Status**: [Pass/Fail/Blocked - to be filled during testing]
**Priority**: [High/Medium/Low]
**Notes**: [Additional observations or issues]

**Usability Test Scenarios**:
**Scenario Name**: [e.g., "New User Registration"]
**User Profile**: [Type of user performing this scenario]
**Context**: [Situation or environment]
**Tasks**: [Specific tasks user should complete]
**Success Metrics**: [How to measure success]
**Observations**: [Usability issues or positive feedback]

**Technical Test Results**:
**Browser Compatibility**:
- Chrome: [Version tested, results]
- Firefox: [Version tested, results]
- Safari: [Version tested, results]
- Edge: [Version tested, results]

**Performance Testing**:
- Page Load Times: [Results]
- Interactive Response Times: [Results]
- Mobile Performance: [Results]

**Accessibility Testing**:
- Keyboard Navigation: [Results]
- Screen Reader Compatibility: [Results]
- Color Contrast: [Results]
- WCAG Compliance: [Results]

**Issues and Refinements**:
**Issue ID**: BUG-001
**Severity**: [Critical/High/Medium/Low]
**Description**: [What the issue is]
**Steps to Reproduce**: [How to recreate the issue]
**Expected vs Actual**: [What should happen vs what does happen]
**Proposed Fix**: [How to resolve the issue]
**Status**: [Open/In Progress/Fixed/Closed]

## Instructions:
1. Review all user stories, acceptance criteria, and use cases from previous tasks
2. Create comprehensive test cases covering functional, usability, and technical requirements
3. Execute tests systematically and document results
4. Identify and prioritize issues based on severity and impact
5. Work with development team to implement fixes and refinements
6. Conduct regression testing after fixes are implemented
7. Validate that the prototype demonstrates business value
8. Prepare summary report with recommendations for next steps

Begin your testing by stating: "Based on the user stories and acceptance criteria, I have created the following test plan to validate the prototype functionality..."

Save output as: Task-08-Testing-and-Refinement-Output.md
</prompt8>

---

## PROMPT 9: Document and Present Prototype
**Task**: Task-09-Document-and-Present-Prototype  
**Role**: Technical Writer  
**Dependencies**: Requires all previous task outputs

<prompt9>
You are a Technical Writer tasked with documenting the prototype and preparing presentation materials. Analyze all deliverables from previous tasks to create comprehensive documentation that demonstrates the business value and technical implementation of the solution.

## Information to Extract:

1. **Business Context Documentation**
   - What was the original business problem or opportunity?
   - What use cases and user stories were implemented?
   - How does the prototype address the customer's needs?
   - What business value does the solution provide?

2. **Technical Implementation Documentation**
   - What technologies and approaches were used?
   - How is the prototype structured and organized?
   - What key features and functionality are implemented?
   - What integrations or data sources are supported?

3. **User Experience Documentation**
   - What user workflows are supported?
   - How do users interact with the system?
   - What accessibility features are included?
   - What responsive design considerations were implemented?

4. **Testing and Validation Documentation**
   - What testing was performed and what were the results?
   - How were user stories and acceptance criteria validated?
   - What issues were identified and resolved?
   - What performance and usability metrics were achieved?

5. **Presentation and Demo Requirements**
   - What key messages need to be communicated to stakeholders?
   - What demonstrations will best show the business value?
   - What questions or concerns might stakeholders have?
   - What next steps or recommendations should be presented?

## Output Format:

**Prototype Documentation**:

**Executive Summary**
- **Business Problem**: [What challenge was addressed]
- **Solution Overview**: [High-level description of the prototype]
- **Key Benefits**: [Primary value propositions]
- **Recommendations**: [Suggested next steps]

**Business Requirements Summary**
- **Use Cases Implemented**: [List of key use cases with brief descriptions]
- **User Stories Delivered**: [Summary of implemented user stories]
- **Business Objectives Met**: [How prototype addresses original objectives]
- **Success Metrics**: [Measurable outcomes achieved]

**Technical Architecture**
- **Technology Stack**: [HTML, CSS, JavaScript, frameworks used]
- **File Structure**: [Organization of prototype files]
- **Key Components**: [Major functional components]
- **Data Model**: [How data is structured and managed]
- **Integration Points**: [External systems or APIs]

**User Experience Guide**
- **User Workflows**: [Step-by-step user journeys]
- **Screen Descriptions**: [Purpose and functionality of each screen]
- **Interactive Features**: [How users interact with the system]
- **Accessibility Features**: [Inclusive design elements]
- **Responsive Design**: [Multi-device support]

**Testing Results Summary**
- **Test Coverage**: [What was tested and validation results]
- **Performance Metrics**: [Load times, responsiveness]
- **Browser Compatibility**: [Supported browsers and devices]
- **Accessibility Compliance**: [WCAG standards met]
- **Issues Resolved**: [Problems found and fixed]

**User Guide**
- **Getting Started**: [How to access and begin using the prototype]
- **Feature Walkthrough**: [How to use key features]
- **Common Tasks**: [Step-by-step instructions for typical workflows]
- **Troubleshooting**: [Common issues and solutions]

**Presentation Materials**:

**Stakeholder Presentation Outline**:
1. **Business Context** (2-3 slides)
   - Problem statement and opportunity
   - Success criteria and objectives

2. **Solution Overview** (3-4 slides)
   - Key use cases implemented
   - User experience highlights
   - Technical approach

3. **Live Demonstration** (10-15 minutes)
   - Guided walkthrough of key workflows
   - Interactive features showcase
   - Business value demonstration

4. **Results and Validation** (2-3 slides)
   - Testing results and metrics
   - User feedback and validation
   - Performance achievements

5. **Next Steps and Recommendations** (2-3 slides)
   - Proposed development roadmap
   - Resource requirements
   - Timeline and milestones

**Demo Script**:
**Scenario**: [Business scenario being demonstrated]
**Duration**: [Estimated time for this demo section]
**Setup**: [What needs to be prepared]
**Script**: [Step-by-step narration and actions]
**Key Messages**: [Important points to emphasize]
**Potential Questions**: [Likely stakeholder questions and responses]

## Instructions:
1. Review all deliverables from Tasks 1-9
2. Create comprehensive documentation that tells the complete story
3. Prepare presentation materials tailored to stakeholder needs
4. Develop demo scripts that showcase business value
5. Include technical details for development teams
6. Provide user-friendly guides for end users
7. Document lessons learned and recommendations
8. Prepare for stakeholder questions and feedback collection

Begin your documentation by stating: "Based on all previous tasks and deliverables, I will create comprehensive documentation and presentation materials that demonstrate the business value and technical implementation of the prototype..."

Save output as: Task-09-Documentation-and-Presentation-Output.md
</prompt9>

---

## EXECUTION SEQUENCE SUMMARY

To complete the entire project, execute the prompts in this order:

1. **PROMPT 1** → Product Vision and Objectives
2. **PROMPT 2** → Use Cases (requires Task 1 output)
3. **PROMPT 3** → Requirements and Initial User Stories (requires Tasks 1-2)
4. **PROMPT 4** → Detailed User Stories and Acceptance Criteria (requires Task 3)
5. **PROMPT 5** → Wireframes and Design Mockups (requires Tasks 1-4)
6. **PROMPT 6** → HTML Structure Implementation (requires Task 5)
7. **PROMPT 7** → CSS Styling (requires Tasks 5-6)
8. **PROMPT 8** → JavaScript Interactivity (requires Tasks 4, 6-7)
9. **PROMPT 9** → Testing and Refinement (requires Tasks 4, 6-8)
10. **PROMPT 10** → Documentation and Presentation (requires all previous tasks)

Each prompt builds upon the outputs of previous tasks, creating a comprehensive prototype development workflow from initial vision to final presentation.

## CONTEXT REFERENCE

All prompts reference the Solidarity Insurance AI Use Cases context from the 000-context directory, specifically:
- **Primary Context**: Solidarity Insurance - AI Use Cases.md
- **Supporting Context**: Big Data Roadmap.pdf (when accessible)

The project focuses on creating a prototype that demonstrates AI-powered insurance solutions for Solidarity Insurance, a Bahrain-based motor insurance company undergoing digital transformation.

---

## BONUS PROMPT: Create Interactive HTML Mock-ups
**Task**: Create-Interactive-HTML-Mockups  
**Role**: Frontend Developer  
**Dependencies**: All output files from Tasks 1-9

<mockup-prompt>
Create comprehensive HTML mock-ups with CSS and JavaScript based on the detailed specifications provided in the output files. Generate interactive prototypes that demonstrate the complete user experience and functionality described in the documentation.

## Task Overview
Analyze all output files from the project to extract:
- Screen specifications and wireframes
- User stories and acceptance criteria  
- Technical requirements and functionality
- Design system elements and styling guidelines
- Interactive behaviors and user workflows

Create fully functional HTML mock-ups that bring these specifications to life with realistic data, interactive elements, and professional styling.

## File Structure Requirements
```
/prototype
├── [screen-name]-mockup.html       # One file per major screen/interface
├── /assets
│   ├── /css
│   │   └── mockup-styles.css      # Shared styling system
│   ├── /js
│   │   └── mockup-interactions.js # Shared JavaScript functionality
│   └── /data
│       └── mock-data.js           # Realistic sample data
```

## Implementation Requirements

### 1. Extract Design Specifications
From the output files, identify and implement:
- **Color palette** and branding guidelines
- **Typography** specifications and hierarchy
- **Component library** (buttons, forms, cards, panels)
- **Layout patterns** and responsive breakpoints
- **Accessibility requirements** (WCAG compliance level)
- **Interactive states** (hover, focus, active, disabled)

### 2. Implement Core Functionality
For each screen identified in the specifications:
- **Static content** matching wireframes and mockups
- **Interactive elements** based on user stories and acceptance criteria
- **Data visualization** components (charts, tables, dashboards)
- **Form handling** with validation and feedback
- **Navigation patterns** between screens and workflows
- **Loading states** and progress indicators

### 3. Create Realistic Sample Data
Generate comprehensive mock data that reflects:
- **Business context** from the project domain
- **User personas** and realistic scenarios
- **Data relationships** between different entities
- **Edge cases** and various data states
- **Localization** appropriate for the target market
- **Compliance requirements** (data masking, privacy)

### 4. Implement Interactive Behaviors
Based on user stories and acceptance criteria:
- **User workflows** with step-by-step interactions
- **State management** for complex interfaces
- **Real-time updates** and dynamic content
- **Error handling** and user feedback
- **Performance optimization** for smooth interactions
- **Cross-browser compatibility** for target browsers

### 5. Ensure Accessibility and Usability
- **Semantic HTML** structure with proper landmarks
- **ARIA labels** and roles for screen readers
- **Keyboard navigation** support throughout
- **Focus management** for complex interactions
- **Color contrast** meeting accessibility standards
- **Responsive design** for multiple device types

## Technical Implementation Guidelines

### HTML Structure
- Use semantic HTML5 elements
- Implement proper heading hierarchy
- Include meta tags for responsive design
- Add structured data where appropriate
- Ensure valid, well-formed markup

### CSS Architecture
- Mobile-first responsive design approach
- CSS custom properties for consistent theming
- Component-based styling methodology
- Efficient selector usage for performance
- Print-friendly styles where relevant

### JavaScript Functionality
- Modern ES6+ syntax and features
- Modular code organization
- Event delegation for dynamic content
- Performance optimization techniques
- Error handling and graceful degradation

### Data Management
- Realistic, contextually appropriate sample data
- Consistent data formats and structures
- Proper data validation and sanitization
- Simulation of API responses and delays
- State persistence where appropriate

## Quality Assurance Requirements

### Testing Considerations
- **Functional testing** of all interactive elements
- **Usability testing** of key user workflows
- **Accessibility testing** with screen readers and keyboard navigation
- **Performance testing** for load times and responsiveness
- **Cross-browser testing** on target browsers and devices

### Documentation
- **Code comments** explaining complex functionality
- **README file** with setup and usage instructions
- **Component documentation** for reusable elements
- **Data schema documentation** for mock data structures
- **Browser compatibility notes** and known limitations

## Deliverable Specifications

### Each Mock-up Should Include
- **Complete visual implementation** matching design specifications
- **Full interactivity** demonstrating user workflows
- **Realistic content** appropriate to the business context
- **Responsive behavior** across device sizes
- **Accessibility features** meeting compliance requirements
- **Performance optimization** for smooth user experience

### Shared Assets Should Provide
- **Consistent styling system** used across all mock-ups
- **Reusable JavaScript modules** for common functionality
- **Comprehensive mock data** supporting all use cases
- **Utility functions** for common operations
- **Configuration options** for easy customization

## Success Criteria
The completed mock-ups should:
- Accurately represent all specifications from the output files
- Demonstrate complete user workflows and interactions
- Provide realistic preview of the final product experience
- Meet all accessibility and performance requirements
- Serve as effective demonstration tools for stakeholders
- Provide clear foundation for development implementation

Execute this prompt by analyzing the provided output files and creating comprehensive, interactive HTML mock-ups that bring the documented specifications to life with professional quality and attention to detail.
</mockup-prompt>