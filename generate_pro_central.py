import re

TEMPLATE = "case-study-woobly.html"

p = {
    "file": "case-study-pro-central.html",
    "title": "Pro Central",
    "company": "Lowe's India"
}

with open(TEMPLATE, "r") as f:
    content = f.read()

content = re.sub(
    r'<title>.*?</title>',
    f'<title>{p["title"]} - Binay Yadav Portfolio</title>',
    content
)
content = re.sub(
    r'<meta property="og:title" content=".*?">',
    f'<meta property="og:title" content="{p["title"]} - Case Study">',
    content
)
content = re.sub(
    r'<h1 class="inner-headline__title">.*?</h1>',
    f'<h1 class="inner-headline__title">{p["title"]}</h1>',
    content
)
content = re.sub(
    r'<p class="mxd-data-list__content">Woobly</p>',
    f'<p class="mxd-data-list__content">{p["company"]}</p>',
    content
)

with open(p["file"], "w") as f:
    f.write(content)

print("Generated case-study-pro-central.html successfully.")
