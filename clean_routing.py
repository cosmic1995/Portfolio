import os

files_to_update = [
    "index.html",
    "about-me.html",
    "case-study-tata-ipl-2025-ticketing-system.html",
    "case-study-virtual-queue-experience.html",
    "case-study-woobly.html",
    "contact.html",
    "workfolio.html"
]

replacements = {
    # Revert to clean URLs to match the expected routing of a real website
    'href="about-me.html"': 'href="about-me"',
    'href="workfolio.html"': 'href="workfolio"',
    'href="contact.html"': 'href="contact"',
    'href="case-study-tata-ipl-2025-ticketing-system.html"': 'href="case-study-tata-ipl-2025-ticketing-system"',
    'href="case-study-virtual-queue-experience.html"': 'href="case-study-virtual-queue-experience"',
    'href="case-study-cashless-event-experience.html"': 'href="case-study-cashless-event-experience"',
    'href="case-study-ticket-transfer.html"': 'href="case-study-ticket-transfer"',
    'href="case-study-woobly.html"': 'href="case-study-woobly"',
    
    # We also need to fix href="index.html" if it exists, it should probably be "/"
    'href="index.html"': 'href="/"',
    
    # Also fix some issues from earlier replace where we still had 'case-study-xyz.html' internally
}

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Internal navigation updated to clean routes.")
