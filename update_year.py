import os
import glob

def update_copyright_year():
    html_files = glob.glob('*.html')
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the overlay menu year
        content = content.replace('                2021\n', '                2026\n')
        content = content.replace('              2025\n', '              2026\n')
        
        # Replace the footer copyright year
        content = content.replace('</i> 2021', '</i> 2026')
        content = content.replace('</i> 2025', '</i> 2026')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")

if __name__ == '__main__':
    update_copyright_year()
