import re

with open('about-me.html', 'r') as f:
    html = f.read()

# Replace Experience
exp_start = '                      <div class="mxd-res-list">\n                        <!-- item -->\n                        <div class="mxd-res-list__item">'
exp_end = '                        </div>                       \n                      </div>'

new_exp = """                      <div class="mxd-res-list">
                        <!-- item -->
                        <div class="mxd-res-list__item">
                          <div class="mxd-res-list__divider anim-uni-in-up"></div>
                          <div class="mxd-res-list__content">
                            <div class="mxd-res-list__data">
                              <div class="mxd-res-list__title">
                                <h4 class="anim-uni-in-up">Senior UX Designer</h4>
                                <p class="mxd-res-list__source anim-uni-in-up">
                                  at Lowe's India Pvt. Ltd
                                </p>
                              </div>
                              <div class="mxd-res-list__descr">
                                <p class="anim-uni-in-up">Led end-to-end design for Shop by Job feature, conducted extensive user research, and developed enterprise-wide design systems, increasing user satisfaction by 25%.</p>
                              </div>
                            </div>
                            <div class="mxd-res-list__year">
                              <p class="anim-uni-in-up">Mar 2024 – Present</p>
                            </div>
                          </div>
                          <div class="mxd-res-list__divider anim-uni-in-up"></div>
                        </div>
                        <!-- item -->
                        <div class="mxd-res-list__item">
                          <div class="mxd-res-list__divider anim-uni-in-up"></div>
                          <div class="mxd-res-list__content">
                            <div class="mxd-res-list__data">
                              <div class="mxd-res-list__title">
                                <h4 class="anim-uni-in-up">Senior UX Designer</h4>
                                <p class="mxd-res-list__source anim-uni-in-up">
                                  at Omnicom Media Group
                                </p>
                              </div>
                              <div class="mxd-res-list__descr">
                                <p class="anim-uni-in-up">Established in-house UX capabilities, redesigned healthcare websites causing a 50% engagement increase, and created interactive prototypes for major global brands.</p>
                              </div>
                            </div>
                            <div class="mxd-res-list__year">
                              <p class="anim-uni-in-up">Dec 2022 – Mar 2024</p>
                            </div>
                          </div>
                          <div class="mxd-res-list__divider anim-uni-in-up"></div>
                        </div>
                      </div>"""

# Find the location of experience list
pattern_exp = re.compile(re.escape(exp_start) + r'.*?' + re.escape(exp_end), re.DOTALL)
html = pattern_exp.sub(new_exp, html, count=1)

with open('about-me.html', 'w') as f:
    f.write(html)
