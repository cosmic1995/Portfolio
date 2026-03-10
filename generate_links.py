import re

projects = [
    {"file": "case-study-design-automation.html"},
    {"file": "case-study-backyard-design-system.html"},
    {"file": "case-study-shop-by-job.html"},
    {"file": "case-study-guardians-shields.html"},
    {"file": "case-study-consumer-brand.html"}
]

# Process index.html and workfolio.html
for filepath in ["index.html", "workfolio.html"]:
    with open(filepath, "r") as f:
        content = f.read()
    
    # Let's find each item block:
    # <div class="col-12 col-xl-6 mxd-project-item mxd-projects-masonry__item">
    # We want to replace the FIRST two href="#0" inside each item block.
    
    parts = content.split('mxd-project-item mxd-projects-masonry__item')
    new_parts = [parts[0]]
    
    # parts[1] is item 1, parts[2] is item 2, etc. (up to 5 items)
    for i in range(1, len(parts)):
        if i <= len(projects):
            proj_file = projects[i-1]["file"]
            # Replace the first two href="#0" in this part
            modified_part = parts[i].replace('href="#0"', f'href="{proj_file}"', 2)
            new_parts.append(modified_part)
        else:
            new_parts.append(parts[i])
            
    content = 'mxd-project-item mxd-projects-masonry__item'.join(new_parts)
    
    with open(filepath, "w") as f:
        f.write(content)

print("Links updated")
