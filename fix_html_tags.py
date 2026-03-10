import re
import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

broken_tag_pattern = re.compile(r'<a\s*\n\s*</p>')
fixed_tag = '<a href="tel:+917872622351">+91 78726 22351</a>\n            </p>'

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    new_content = broken_tag_pattern.sub(fixed_tag, content)

    # I will also just globally replace `<a \n            </p>` string if regex failed
    new_content = new_content.replace('<a \n            </p>', '<a href="tel:+917872622351">+91 78726 22351</a>\n            </p>')
    new_content = new_content.replace('<a\n            </p>', '<a href="tel:+917872622351">+91 78726 22351</a>\n            </p>')

    if new_content != content:
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Fixed {file}")

