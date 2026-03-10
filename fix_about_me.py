from bs4 import BeautifulSoup
import copy

with open('about-me.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

experiences = [
    {
        "title": "Senior UX Designer",
        "company": "Lowe's India Pvt. Ltd, Bangalore",
        "desc": "Conducted comprehensive user research, created enterprise-wide design systems, and executed usability testing for Shop by Job feature.",
        "year": "Mar 2024 – Present"
    },
    {
        "title": "Senior UX Designer",
        "company": "Omnicom Media Group, Bangalore",
        "desc": "Established in-house UX capabilities, redesigned healthcare websites causing a 50% engagement increase, and created interactive prototypes for major global brands.",
        "year": "Dec 2022 – Mar 2024"
    },
    {
        "title": "Senior UX Designer",
        "company": "Bridge Tower Media Network / WPP",
        "desc": "Built comprehensive design system and visual guidelines, standardized design workflows, and improved brand recognition by 30%.",
        "year": "Mar 2022 – Dec 2022"
    },
    {
        "title": "Art Director",
        "company": "Glow Magic Events & Studio, Kolkata, India",
        "desc": "Directed comprehensive branding campaigns using user feedback and design thinking methodology, increasing digital reach by 30%.",
        "year": "Jan 2019 – Dec 2022"
    },
    {
        "title": "Creative Designer",
        "company": "Veda Hospitality, Kolkata",
        "desc": "Developed user-centered design solutions for hospitality and consumer brands, enhancing engagement by 20%.",
        "year": "Jan 2017 – Dec 2019"
    },
    {
        "title": "Graphic Designer",
        "company": "Park Hotels Group, Kolkata",
        "desc": "Created comprehensive visual design solutions, contributing to revenue growth through effective problem-solving.",
        "year": "Jan 2015 – Dec 2017"
    }
]

educations = [
    {
        "title": "Interaction Design Specialization",
        "school": "UC San Diego",
        "year": "Mar 2022 – Dec 2022"
    },
    {
        "title": "UX Design Professional Certificate",
        "school": "Google",
        "year": "Jul 2021 – Jan 2022"
    },
    {
        "title": "UI/UX Design Principles Certificate",
        "school": "Meta",
        "year": "Jul 2021 – Jan 2022"
    },
    {
        "title": "Advanced Diploma in Graphic Design & Multimedia",
        "school": "Lalani Computer Academy",
        "year": "Feb 2012 – Jan 2015"
    },
    {
        "title": "Project Management Certificate",
        "school": "Google, Coursera",
        "year": "Jul 2021 – Jan 2022"
    },
    {
        "title": "BCA",
        "school": "Kazi Nazrul Islam University",
        "year": "Apr 2015 – Jan 2018"
    }
]

headers = soup.find_all('h2', class_='reveal-type')
exp_header = None
edu_header = None
for hr in headers:
    text = hr.get_text(separator=' ')
    if 'Work' in text and 'experience' in text:
        exp_header = hr
    elif 'Education' in text:
        edu_header = hr

def replace_list(header, items, is_edu=False):
    container_inner = header.find_parent('div', class_='mxd-pinned-universal__static').find_next_sibling('div', class_='mxd-pinned-universal__scroll')
    res_list = container_inner.find('div', class_='mxd-res-list')
    template_item = res_list.find('div', class_='mxd-res-list__item')
    
    # Store a copy of the template
    new_items = []
    
    for item in items:
        # Create a new item from template
        new_item = copy.copy(template_item)
        new_item.find('h4').string = item['title']
        
        # company/school
        source_p = new_item.find('p', class_='mxd-res-list__source')
        source_p.string = '\n' + ("from " if is_edu else "at ") + item.get('school', item.get('company', '')) + '\n'
        
        # description
        descr_div = new_item.find('div', class_='mxd-res-list__descr')
        if descr_div:
            if 'desc' in item:
                # Need to find the inner <p>
                if descr_div.find('p'):
                    descr_div.find('p').string = item['desc']
            else:
                descr_div.decompose() # remove it if no description needed
                
        # year
        year_div = new_item.find('div', class_='mxd-res-list__year')
        year_div.find('p').string = item['year']
        
        new_items.append(new_item)

    res_list.clear() # remove old items
    for ni in new_items:
        res_list.append(ni)

if exp_header:
    replace_list(exp_header, experiences, is_edu=False)
else:
    print("Work experience header not found.")

if edu_header:
    replace_list(edu_header, educations, is_edu=True)
else:
    print("Education header not found.")

with open('about-me.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Successfully replaced Experience and Education.")
