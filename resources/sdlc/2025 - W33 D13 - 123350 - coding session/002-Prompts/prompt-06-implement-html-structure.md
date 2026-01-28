# Task 6: Implement HTML Structure - Execution Prompt

You are a Frontend Developer tasked with implementing the HTML structure for the prototype. 

## Context Files to Reference:
Review all available files in the **000-context** folder and **004-outputs** folder along with the wireframes and mockups from Task 5, user stories, and acceptance criteria to create semantic HTML that supports all required functionality. The context files may provide additional details on:
- Technical requirements and constraints
- Content structure and organization
- Accessibility and compliance requirements
- Integration requirements with existing systems
- Any other relevant technical specifications

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

## Output Instructions:
Save your completed implementation as a markdown file named "06-html-structure-implementation.md" in the 004-Outputs folder. Include all HTML code, file structure, and implementation notes.

Begin your implementation by stating: "Based on the context files in the 000-context folder and 004-outputs folder, wireframes from Task 5, and user stories from previous tasks, I will create the following HTML structure for the prototype..."