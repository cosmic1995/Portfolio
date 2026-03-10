import re
import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# 1. Fix Logo Styling in all files (especially about-me.html)
logo_pattern = r'<span class="mxd-logo__text" style="text-transform: uppercase;">BY</span>'
logo_fixed = '<span class="mxd-logo__text" style="text-transform: uppercase; font-weight: 800; font-size: 1.4rem; letter-spacing: 1px;">BY</span>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(logo_pattern, logo_fixed)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed logo in {file}")

# 2. Update Core Competencies in about-me.html
about_me_file = 'about-me.html'
if os.path.exists(about_me_file):
    with open(about_me_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new content for the approach list (Core Competencies)
    competencies = [
        {
            "title": "UX Research & Strategy",
            "descr": "User Research and Analysis, User Personas, User Journey Mapping, User Flows, Wireframing, Interactive Prototyping, Usability Testing, User Feedback Sessions, Information Architecture, Design Thinking, Human-Computer Interaction, User-Centered Design."
        },
        {
            "title": "Visual Design & Branding",
            "descr": "Brand Identity Development, Art Direction, Typography & Layout, Print & Digital Campaigns, Marketing Collateral Design, Visual Storytelling, Creative Strategy, Brand Guidelines."
        },
        {
            "title": "Design Tools & Software",
            "descr": "Figma (SME), Sketch, Adobe Creative Suite (Photoshop, Illustrator, InDesign), Adobe XD, Miro, Mural, Microsoft Whiteboard, InVision, Axure RP."
        },
        {
            "title": "Technical & Process",
            "descr": "HTML, CSS, Responsive & Mobile-First Design, Accessibility (WCAG), Design Systems, Component Libraries, Agile Methodologies, Scrum, Cross-functional Collaboration, Stakeholder Management, Project Management, Design Documentation."
        }
    ]

    # Replacing the current items in the mxd-approach-list
    # The structure found earlier:
    # <div class="mxd-approach-list__title anim-uni-in-up">
    # <h6>Strategy</h6>
    # </div>
    # ...
    # <div class="mxd-approach-list__descr anim-uni-in-up">
    # <p>...</p><br/>
    # <h6>The output is clarity.</h6>
    # </div>

    # I'll use a more targeted replacement per block if possible, or just replace the whole section.
    # The section is between <!-- Block - Approach and Philosophy List Start --> and <!-- Block - Approach and Philosophy List End -->
    
    # Let's try to replace the titles and descriptions sequentially.
    titles = ["Strategy", "Design", "Development Collaboration", "Quality Assurance"]
    for i, old_title in enumerate(titles):
        if i < len(competencies):
            # Replace title
            content = content.replace(f'<h6>{old_title}</h6>', f'<h6>{competencies[i]["title"]}</h6>')
            
            # Replace description - this is trickier because the text is long. 
            # I will look for the specific strings found in the file view.
            if old_title == "Strategy":
                old_descr = "Before designing anything, we make sure we’re solving the right problem. This phase may include: Product and business discovery, Market and competitor analysis, User understanding and pain-point mapping, Defining goals, constraints, and success metrics."
                content = content.replace(old_descr, competencies[i]["descr"])
                content = content.replace("<h6>The output is clarity.</h6>", "")
            elif old_title == "Design":
                old_descr = "Once direction is clear, I move into problem-solving through design. This includes: User flows and information architecture, Wireframes, Interaction design, High-fidelity pixel-perfect UI, Prototypes that simulate real product behavior"
                content = content.replace(old_descr, competencies[i]["descr"])
                content = content.replace("<h6>Design decisions are always tied back to user needs and business goals.</h6>", "")
            elif old_title == "Development Collaboration":
                old_descr = "I work closely with engineering teams to ensure designs are built exactly as intended. Clear handoffs and documentation, Design QA during development and Front-end support for web projects when needed."
                content = content.replace(old_descr, competencies[i]["descr"])
                content = content.replace("<h6>Because I understand code, collaboration stays smooth and practical.</h6>", "")
            elif old_title == "Quality Assurance":
                old_descr = "Design doesn’t stop at delivery. Regular check-ins and transparent progress, Feedback-driven iterations, Optional user testing with real customers and Refinement based on data and insights."
                content = content.replace(old_descr, competencies[i]["descr"])
                content = content.replace("<h6>The goal is confidence — for you and your users.</h6>", "")

    # Cleanup any leftover empty tags if needed, but the replaces should be fine.
    
    with open(about_me_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Core Competencies in about-me.html")

# 3. Final scrub of "District" and "Zomato" in descriptive text and meta tags
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace references to District by Zomato with Omnicom or Lowe's depending on context
    # Usually it's Omnicom for the older projects or Lowe's for the new ones.
    # The user's resume says Omnicom for Guardian's Shields and Lowe's for Shop by Job.
    
    content = content.replace("District by Zomato", "Omnicom Media Group")
    content = content.replace("District by zomato", "Omnicom Media Group")
    content = content.replace("at District", "at Omnicom")
    
    if "Paytm Insider" in content:
        content = content.replace("Paytm Insider", "Omnicom Media Group")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Final cleanup finished.")
