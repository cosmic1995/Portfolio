import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# 1. Update Logo Text size and weight
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # Logo Replacement (it either has style="text-transform: uppercase;" or similar)
    # The previous script replaced it with: <span class="mxd-logo__text" style="text-transform: uppercase;">BY</span>
    
    content = re.sub(
        r'<span class="mxd-logo__text" style="text-transform: uppercase;">BY</span>',
        '<span class="mxd-logo__text" style="text-transform: uppercase; font-weight: 800; font-size: 1.4rem; letter-spacing: 1px;">BY</span>',
        content
    )
    # Just in case it missed some:
    content = re.sub(
        r'<span class="mxd-logo__text">BY</span>',
        '<span class="mxd-logo__text" style="text-transform: uppercase; font-weight: 800; font-size: 1.4rem; letter-spacing: 1px;">BY</span>',
        content
    )

    with open(file, 'w') as f:
        f.write(content)

# 2. Update About Me Intro
about_me_file = 'about-me.html'
with open(about_me_file, 'r') as f:
    about_text = f.read()

old_p1 = r'<p class="inner-headline__text t-large t-bright loading__item">👋 Hey! I’m Binay — a product designer based in India, born and raised in Jalandhar, Punjab. I work across product design, brand identity, UI/UX, and web development, with a strong technical foundation and a fine sense of visual balance \(plus a subtle hint of humour where it fits\).</p>'
new_p1 = r'<p class="inner-headline__text t-large t-bright loading__item">👋 Hey! I’m Binay — a results-driven UX Designer with 9+ years of experience creating user-friendly, engaging digital experiences for consumer brands and healthcare platforms.</p>'

old_p2 = r'<p class="inner-headline__text t-bright loading__item">I’m deeply passionate about building clear, usable, and scalable experiences, especially in complex, high-stakes environments where design decisions directly impact trust, usability, and business outcomes.</p>'
new_p2 = r'<p class="inner-headline__text t-bright loading__item">Expert across the end-to-end design process—from user research and analysis to visual execution and usability testing. Proven record of improving user satisfaction by 25–60% while supporting digital transformation initiatives and delivering solutions that meet stakeholder expectations.</p>'

about_text = re.sub(old_p1, new_p1, about_text)
about_text = re.sub(old_p2, new_p2, about_text)

with open(about_me_file, 'w') as f:
    f.write(about_text)

print("Update script finished.")
