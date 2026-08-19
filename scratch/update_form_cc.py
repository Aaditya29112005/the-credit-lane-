import os, re

theme_dir = "/Users/aadityamohansamadhiya/the credit lane/credit-lane-theme"

for root, dirs, files in os.walk(theme_dir):
    for f in files:
        if f.endswith('.php'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if 'formsubmit.co' in content and '_cc' not in content:
                # Add hidden _cc field inside form
                new_content = re.sub(
                    r'(<form[^>]*action="https://formsubmit\.co/[^"]*"[^>]*>)',
                    r'\1\n          <input type="hidden" name="_cc" value="creditlaneindia@gmail.com">',
                    content
                )
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Updated {f}")
