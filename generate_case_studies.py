import re

TEMPLATE = "case-study-woobly.html"

projects = [
    {
        "file": "case-study-design-automation.html",
        "title": "Design Automation Solution",
        "company": "Lowe's India"
    },
    {
        "file": "case-study-backyard-design-system.html",
        "title": "Backyard Design System 4",
        "company": "Lowe's India"
    },
    {
        "file": "case-study-shop-by-job.html",
        "title": "Shop by Job Feature",
        "company": "Lowe's India"
    },
    {
        "file": "case-study-guardians-shields.html",
        "title": "Guardian's Shields UX",
        "company": "Omnicom"
    },
    {
        "file": "case-study-consumer-brand.html",
        "title": "Consumer Brand Experiences",
        "company": "Omnicom"
    }
]

with open(TEMPLATE, "r") as f:
    template_content = f.read()

for p in projects:
    content = template_content
    
    # Update Title tag
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{p["title"]} - Binay Yadav Portfolio</title>',
        content
    )
    
    # Update og:title
    content = re.sub(
        r'<meta property="og:title" content=".*?">',
        f'<meta property="og:title" content="{p["title"]} - Case Study">',
        content
    )
    
    # Update main headline - The actual class in woobly is inner-headline__title
    content = re.sub(
        r'<h1 class="inner-headline__title">.*?</h1>',
        f'<h1 class="inner-headline__title">{p["title"]}</h1>',
        content
    )
    
    # Update Client/Company Name in Info Block
    content = re.sub(
        r'<p class="mxd-data-list__content">Woobly \| Smarter Dining Experiences</p>',
        f'<p class="mxd-data-list__content">{p["company"]}</p>',
        content
    )
    
    # The role description is also there: "<p class="mxd-data-list__content">Lowe's India</p>" if already replaced, let's just make sure.
    # In pristine woobly template: "Woobly"
    # Actually wait, in original woobly template it is:
    # <div class="mxd-data-list__item">
    #   <p class="mxd-data-list__name">For</p>
    #   <p class="mxd-data-list__content">Woobly</p>
    # </div>
    # Let's target the exact line.
    content = re.sub(
        r'<p class="mxd-data-list__content">Woobly</p>',
        f'<p class="mxd-data-list__content">{p["company"]}</p>',
        content
    )
    
    with open(p["file"], "w") as f:
        f.write(content)

print("Generated case studies successfully.")
