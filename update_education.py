import re

about_me_file = 'about-me.html'
with open(about_me_file, 'r') as f:
    about_text = f.read()

edu_items = [
    ("Interaction Design Specialization", "UC San Diego", "Mar 2022–Dec 2022"),
    ("UX Design Professional Certificate", "Google", "Jul 2021–Jan 2022"),
    ("UI/UX Design Principles Certificate", "Meta", "Jul 2021–Jan 2022"),
    ("Advanced Diploma in Graphic Design & Multimedia", "Lalani Computer Academy", "Feb 2012–Jan 2015"),
    ("Project Management Certificate", "Google, Coursera", "Jul 2021–Jan 2022"),
    ("BCA", "Kazi Nazrul Islam University", "Apr 2015–Jan 2018")
]

new_list_html = '<div class="mxd-res-list">\n'
for title, source, year in edu_items:
    new_list_html += f"""                      <!-- item -->
                      <div class="mxd-res-list__item">
                        <div class="mxd-res-list__divider anim-uni-in-up"></div>
                        <div class="mxd-res-list__content">
                          <div class="mxd-res-list__data">
                            <div class="mxd-res-list__title">
                              <h4 class="anim-uni-in-up">{title}</h4>
                              <p class="mxd-res-list__source anim-uni-in-up">
                                from {source}
                              </p>
                            </div>
                          </div>
                          <div class="mxd-res-list__year">
                            <p class="anim-uni-in-up">{year}</p>
                          </div>
                        </div>
                        <div class="mxd-res-list__divider anim-uni-in-up"></div>
                      </div>\n"""
new_list_html += '                    </div>'

pattern_edu = re.compile(r'<div class="mxd-res-list">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*<!-- Block - Stack Universal Pinned Block with Section Title Start -->', re.DOTALL)

# Let's find exactly lines 914 to 957 string
target_start = '<div class="mxd-res-list">'
target_end = '</div>\n                  </div>\n                </div>\n              </div>' # end of scroll
# To be safe, let's use a non-greedy regex just for the mxd-res-list div
pattern = re.compile(r'<div class="mxd-res-list">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)

# Try replacing
def replace_between(text, start_str, end_str, replacement):
    start_idx = text.find(start_str)
    if start_idx == -1: return text
    
    # We want the </div> after the last item. 
    # Current text has 2 items.
    # It's safer to just split string.
    
    return text

# Actually, the python string `replace` or `sub`
# Let's just find the exact block and replace
content = open(about_me_file).read()
import traceback
try:
    start_str = '                    <div class="mxd-res-list">'
    end_str = '                    </div>\n                  </div>\n                </div>'
    start = content.index(start_str)
    # The end_str will match the closing of mxd-res-list
    end = content.index(end_str, start) + len('                    </div>')
    new_content = content[:start] + '                    ' + new_list_html + content[end:]
    open(about_me_file, 'w').write(new_content)
    print("Education updated")
except Exception as e:
    print(e)
    traceback.print_exc()

