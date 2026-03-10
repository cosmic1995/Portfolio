import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# 1. Update Logo Text
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # Logo Replacement
    content = re.sub(
        r'<span class="mxd-logo__text">.*?</span>',
        '<span class="mxd-logo__text" style="text-transform: uppercase;">BY</span>',
        content,
        flags=re.DOTALL
    )

    with open(file, 'w') as f:
        f.write(content)

# 2. Update About Me Stats
about_me_file = 'about-me.html'
with open(about_me_file, 'r') as f:
    about_text = f.read()

about_text = about_text.replace('PaytmInsider-Logo', 'Lowes-India-Logo')
about_text = about_text.replace('District-logo', 'Omnicom-Logo')
about_text = about_text.replace('District by Zomato', 'Lowe\'s India')
about_text = about_text.replace('Paytm Insider', 'Omnicom Media Group')
about_text = about_text.replace('Years - Built event ticketing at Omnicom Media Group and now shaping it at Lowe\'s India.', 'Years - Crafting enterprise experiences at Lowe\'s India and Omnicom Media Group.')

# Update counter numbers in about-me script
# statsCounter2 was 4, making it 2 (Dec 2022 -> 2024 is ~2 yrs)
about_text = re.sub(
    r'const statsCounter2 = new countUp\.CountUp\("stats-counter-2", 4, optionsPlus\);',
    r'const statsCounter2 = new countUp.CountUp("stats-counter-2", 2, optionsPlus);',
    about_text
)
# statsCounter1 to 9
about_text = re.sub(
    r'const statsCounter1 = new countUp\.CountUp\("stats-counter-1", \d+, optionsPlus\);',
    r'const statsCounter1 = new countUp.CountUp("stats-counter-1", 9, optionsPlus);',
    about_text
)

with open(about_me_file, 'w') as f:
    f.write(about_text)

# 3. Update Projects in workfolio.html
workfolio_file = 'workfolio.html'
with open(workfolio_file, 'r') as f:
      work_text = f.read()

projects_html = """                  <!-- portfolio gallery title -->
                  <div class="col-12 col-xl-6 mxd-projects-masonry__title headline-title">
                    <div class="mxd-block__inner-headline">
                      <h1 class="inner-headline__title headline-img-before headline-img-07">Projects</h1>
                    </div>
                  </div>

                  <!-- Item 1 -->
                  <div class="col-12 col-xl-6 mxd-project-item mxd-projects-masonry__item">
                    <a class="mxd-project-item__media masonry-media" href="#0">
                      <div class="mxd-project-item__preview masonry-preview parallax-img-small" style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Lowe's+Automation)">
                      </div>
                      <div class="mxd-project-item__tags">
                        <span class="tag tag-default tag-permanent">Lowe's India</span>
                        <span class="tag tag-default tag-permanent">UX Design</span>
                      </div>
                    </a>
                    <div class="mxd-project-item__promo">
                      <div class="mxd-project-item__name">
                        <a href="#0"><span>Case Study</span> Design Automation Solution</a>
                        <p>Built custom Figma automation plugin for creative ads design production, eliminating recurring errors and optimizing workflow.</p>
                      </div>
                    </div>
                  </div>

                  <!-- Item 2 -->
                  <div class="col-12 col-xl-6 mxd-project-item mxd-projects-masonry__item">
                    <a class="mxd-project-item__media masonry-media" href="#0">
                      <div class="mxd-project-item__preview masonry-preview parallax-img-small" style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Backyard+Design+System)">
                      </div>
                      <div class="mxd-project-item__tags">
                        <span class="tag tag-default tag-permanent">Lowe's India</span>
                        <span class="tag tag-default tag-permanent">Design Systems</span>
                      </div>
                    </a>
                    <div class="mxd-project-item__promo masonry-promo">
                      <div class="mxd-project-item__name">
                        <a href="#0"><span>Case Study</span> Backyard Design System 4</a>
                        <p>Contributed to Lowe's Backyard Design System tokens and guidelines ensuring consistent user experiences across websites and applications.</p>
                      </div>
                    </div>
                  </div>

                  <!-- Item 3 -->
                  <div class="col-12 col-xl-6 mxd-project-item mxd-projects-masonry__item">
                    <a class="mxd-project-item__media masonry-media" href="#0">
                      <div class="mxd-project-item__preview masonry-preview parallax-img-small" style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Shop+By+Job)">
                      </div>
                      <div class="mxd-project-item__tags">
                        <span class="tag tag-default tag-permanent">Lowe's India</span>
                        <span class="tag tag-default tag-permanent">Product Design</span>
                      </div>
                    </a>
                    <div class="mxd-project-item__promo masonry-promo">
                      <div class="mxd-project-item__name">
                        <a href="#0"><span>Case Study</span> Shop by Job Feature</a>
                        <p>Led end-to-end design for Pro customers, streamlined workflows, and reduced friction in journeys resulting in 20% increase in completions.</p>
                      </div>
                    </div>
                  </div>

                  <!-- Item 4 -->
                  <div class="col-12 col-xl-6 mxd-project-item mxd-projects-masonry__item">
                    <a class="mxd-project-item__media masonry-media" href="#0">
                      <div class="mxd-project-item__preview masonry-preview parallax-img-small" style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Guardian+Shields+UX)">
                      </div>
                      <div class="mxd-project-item__tags">
                        <span class="tag tag-default tag-permanent">Omnicom</span>
                        <span class="tag tag-default tag-permanent">Healthcare UX</span>
                      </div>
                    </a>
                    <div class="mxd-project-item__promo">
                      <div class="mxd-project-item__name">
                        <a href="#0"><span>Case Study</span> Guardian's Shields UX</a>
                        <p>Redesigned healthcare product combining user research with accessibility standards, resulting in 50% engagement increase.</p>
                      </div>
                    </div>
                  </div>

                  <!-- Item 5 -->
                  <div class="col-12 col-xl-6 mxd-project-item mxd-projects-masonry__item">
                    <a class="mxd-project-item__media masonry-media" href="#0">
                      <div class="mxd-project-item__preview masonry-preview parallax-img-small" style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Consumer+Brands)">
                      </div>
                      <div class="mxd-project-item__tags">
                        <span class="tag tag-default tag-permanent">Omnicom</span>
                        <span class="tag tag-default tag-permanent">Digital Experience</span>
                      </div>
                    </a>
                    <div class="mxd-project-item__promo">
                      <div class="mxd-project-item__name">
                        <a href="#0"><span>Case Study</span> Consumer Brand Experiences</a>
                        <p>Created interactive prototypes for major consumer brands like BMW, McDonald's, Bacardi, applying design thinking methodologies.</p>
                      </div>
                    </div>
                  </div>"""

pattern_gallery = re.compile(r'<!-- Portfolio Gallery Start -->.*?<!-- Portfolio Gallery End -->', re.DOTALL)
replacement_gallery_full = f'<!-- Portfolio Gallery Start -->\n                <div class="row g-0 mxd-projects-masonry__gallery" data-masonry=\'{{"percentPosition": true }}\'>\n{projects_html}\n                </div>\n                <!-- Portfolio Gallery End -->'

work_text = pattern_gallery.sub(replacement_gallery_full, work_text, count=1)
with open(workfolio_file, 'w') as f:
      f.write(work_text)

# Also update index.html project list similarly (index.html projects wrap is similar)
index_file = 'index.html'
with open(index_file, 'r') as f:
      index_text = f.read()

index_text = pattern_gallery.sub(replacement_gallery_full, index_text, count=1)
with open(index_file, 'w') as f:
      f.write(index_text)

print("Update script finished.")
