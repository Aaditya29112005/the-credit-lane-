import os, re

base_dir = "/Users/aadityamohansamadhiya/the credit lane"
old_url = "https://script.google.com/macros/s/AKfycbzaSs_XJESePwtNQJZDAGWiyHISLA66LCuXEhPCeLhVWp58g472FDNjuJPH75gxPTNw/exec"
new_url = "https://script.google.com/macros/s/AKfycbzaSs_XJESePwtNQJZDAGWiyHISLA66LCuXEhPCeLhVWp58g472FDNjuJPH75gxPTNw/exec"

count = 0
for root, dirs, files in os.walk(base_dir):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.php') or f.endswith('.html') or f.endswith('.py') or f.endswith('.js'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if old_url in content:
                new_content = content.replace(old_url, new_url)
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                count += 1
                print(f"Updated {f}")

print(f"Total files updated with new CRM URL: {count}")
