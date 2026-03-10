import re

index_file = 'index.html'
with open(index_file, 'r') as f:
    index_text = f.read()

# The projects in index.html should be the following:
projects_html = """
                    <!-- item 1 -->
                    <div class="mxd-project-item">
                      <a class="mxd-project-item__media anim-uni-in-up" href="case-study-design-automation.html">
                        <div class="mxd-project-item__preview parallax-img-small"
                          style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Lowe's+Automation)">
                        </div>
                        <div class="mxd-project-item__tags">
                          <span class="tag tag-default tag-permanent">Lowe's India</span>
                          <span class="tag tag-default tag-permanent">UX Design</span>
                        </div>
                      </a>
                      <div class="mxd-project-item__promo">
                        <div class="mxd-project-item__name">
                          <a class="anim-uni-in-up" href="case-study-design-automation.html"><span>Case Study</span> Design Automation Solution</a>
                          <p>Built custom Figma automation plugin for creative ads design production, eliminating recurring errors and optimizing workflow.</p>
                        </div>
                      </div>
                    </div>

                    <!-- item 2 -->
                    <div class="mxd-project-item">
                      <a class="mxd-project-item__media anim-uni-in-up" href="case-study-backyard-design-system.html">
                        <div class="mxd-project-item__preview parallax-img-small"
                          style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Backyard+Design+System)">
                        </div>
                        <div class="mxd-project-item__tags">
                          <span class="tag tag-default tag-permanent">Lowe's India</span>
                          <span class="tag tag-default tag-permanent">Design Systems</span>
                        </div>
                      </a>
                      <div class="mxd-project-item__promo">
                        <div class="mxd-project-item__name">
                          <a class="anim-uni-in-up" href="case-study-backyard-design-system.html"><span>Case Study</span> Backyard Design System 4</a>
                          <p>Contributed to Lowe's Backyard Design System tokens and guidelines ensuring consistent user experiences across websites and applications.</p>
                        </div>
                      </div>
                    </div>

                    <!-- item 3 -->
                    <div class="mxd-project-item">
                      <a class="mxd-project-item__media anim-uni-in-up" href="case-study-shop-by-job.html">
                        <div class="mxd-project-item__preview parallax-img-small"
                          style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Shop+By+Job)">
                        </div>
                        <div class="mxd-project-item__tags">
                          <span class="tag tag-default tag-permanent">Lowe's India</span>
                          <span class="tag tag-default tag-permanent">Product Design</span>
                        </div>
                      </a>
                      <div class="mxd-project-item__promo">
                        <div class="mxd-project-item__name">
                          <a class="anim-uni-in-up" href="case-study-shop-by-job.html"><span>Case Study</span> Shop by Job Feature</a>
                          <p>Led end-to-end design for Pro customers, streamlined workflows, and reduced friction in journeys resulting in 20% increase in completions.</p>
                        </div>
                      </div>
                    </div>

                    <!-- item 4 -->
                    <div class="mxd-project-item">
                      <a class="mxd-project-item__media anim-uni-in-up" href="case-study-guardians-shields.html">
                        <div class="mxd-project-item__preview parallax-img-small"
                          style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Guardian+Shields+UX)">
                        </div>
                        <div class="mxd-project-item__tags">
                          <span class="tag tag-default tag-permanent">Omnicom</span>
                          <span class="tag tag-default tag-permanent">Healthcare UX</span>
                        </div>
                      </a>
                      <div class="mxd-project-item__promo">
                        <div class="mxd-project-item__name">
                          <a class="anim-uni-in-up" href="case-study-guardians-shields.html"><span>Case Study</span> Guardian's Shields UX</a>
                          <p>Redesigned healthcare product combining user research with accessibility standards, resulting in 50% engagement increase.</p>
                        </div>
                      </div>
                    </div>

                    <!-- item 5 -->
                    <div class="mxd-project-item">
                      <a class="mxd-project-item__media anim-uni-in-up" href="case-study-consumer-brand.html">
                        <div class="mxd-project-item__preview parallax-img-small"
                          style="background-image:url(https://placehold.co/1000x1000/1d1d1d/ffffff?text=Consumer+Brands)">
                        </div>
                        <div class="mxd-project-item__tags">
                          <span class="tag tag-default tag-permanent">Omnicom</span>
                          <span class="tag tag-default tag-permanent">Digital Experience</span>
                        </div>
                      </a>
                      <div class="mxd-project-item__promo">
                        <div class="mxd-project-item__name">
                          <a class="anim-uni-in-up" href="case-study-consumer-brand.html"><span>Case Study</span> Consumer Brand Experiences</a>
                          <p>Created interactive prototypes for major consumer brands like BMW, McDonald's, Bacardi, applying design thinking methodologies.</p>
                        </div>
                      </div>
                    </div>
"""

pattern = re.compile(r'(<div class="mxd-pinned-projects__scroll-inner mxd-grid-item no-margin">).*?(</div>\s+</div>\s+</div>\s+</div>\s+</div>\s+</div>)', re.DOTALL)
index_text = pattern.sub(r'\1' + '\n' + projects_html + r'\2', index_text)

with open(index_file, 'w') as f:
    f.write(index_text)

print("Index projects updated.")
