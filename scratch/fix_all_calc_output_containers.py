import glob
import re

php_files = glob.glob("credit-lane-theme/pages/*.php")
style_attr = 'style="background: #0B1D33 !important; color: #FFFFFF !important; padding: 36px 32px !important; border-radius: 20px !important; border: 1.5px solid rgba(200, 155, 60, 0.4) !important; box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3) !important; display: flex !important; flex-direction: column !important; justify-content: space-between !important;"'

for filepath in php_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace <div class="calc-outputs"> or existing inline style on calc-outputs
    new_content = re.sub(
        r'<div\s+class="calc-outputs"[^>]*>',
        f'<div class="calc-outputs" {style_attr}>',
        content
    )

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filepath}")

print("All PHP page calculator output containers updated with explicit dark navy inline styles.")
