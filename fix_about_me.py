from bs4 import BeautifulSoup
import copy

with open('about-me.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

experiences = [
    {
        "title": "SENIOR UX DESIGNER",
        "company": "Lowe's India Pvt. Ltd, Bangalore",
        "desc": "Conducted comprehensive user research, created enterprise-wide design systems, and executed usability testing for Shop by Job feature.",
        "year": "Mar 2024 – Present"
    },
    {
        "title": "SENIOR UX DESIGNER",
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
        "title": "ART DIRECTOR",
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
        "school": "from UC San Diego",
        "year": "Mar 2022 – Dec 2022"
    },
    {
        "title": "UX Design Professional Certificate",
        "school": "from Google",
        "year": "Jul 2021 – Jan 2022"
    },
    {
        "title": "UI/UX Design Principles Certificate",
        "school": "from Meta",
        "year": "Jul 2021 – Jan 2022"
    },
    {
        "title": "Advanced Diploma in Graphic Design & Multimedia",
        "school": "from Lalani Computer Academy",
        "year": "Feb 2012 – Jan 2015"
    },
    {
        "title": "Project Management Certificate",
        "school": "from Google, Coursera",
        "year": "Jul 2021 – Jan 2022"
    },
    {
        "title": "BCA",
        "school": "from Kazi Nazrul Islam University",
        "year": "Apr 2015 – Jan 2018"
    }
]

headers = soup.find_all('h2', class_='reveal-type')
exp_header = None
edu_header = None
for hr in headers:
    if 'Work' in hr.text and 'experience' in hr.text:
        exp_header = hr
    elif 'Education' in hr.text:
        edu_header = hr

def replace_list(header, items, is_edu=False):
    container = header.find_parent('div', class_='mxd-pinned-universal__static').find_next_sibling('div', class_='mxd-pinned-universal__scroll')
    res_list = container.find('div', class_='mxd-res-list')
    template_item = res_list.find('div', class_='mxd-res-list__item')
    
    res_list.clear() # remove old items
    
    for item in items:
        new_item = copy.copy(template_item)
        new_item.find('h4').string = item['title']
        
        # company/school
        source_p = new_item.find('p', class_='mxd-res-list__source')
        source_p.string = '\n' + ("from " if is_edu else "at ") + item.get('school', item.get('company', '')) + '\n'
        
        # description
        descr_div = new_item.find('div', class_='mxd-res-list__descr')
        if descr_div:
            if 'desc' in item:
                descr_div.find('p').string = item['desc']
            else:
                descr_div.decompose() # remove it if no description needed
                
        # year
        year_div = new_item.find('div', class_='mxd-res-list__year')
        year_div.find('p').string = item['year']
        
        res_list.append(new_item)

if exp_header:
    replace_list(exp_header, experiences, is_edu=False)
if edu_header:
    replace_list(edu_header, educations, is_edu=True)

with open('about-me.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Successfully replaced Experience and Education.")

