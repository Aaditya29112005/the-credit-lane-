import os
import glob
import re

theme_pages_dir = "/Users/aadityamohansamadhiya/the credit lane/credit-lane-theme/pages"
php_files = glob.glob(os.path.join(theme_pages_dir, "*.php"))

slider_style = 'style="width: 100%; height: 8px; border-radius: 4px; outline: none; -webkit-appearance: none; appearance: none; background: #E2DDD5; cursor: pointer; accent-color: #C89B3C;"'
outputs_style = 'style="background: #08192E !important; color: #FFFFFF !important; padding: 32px 28px !important; border-radius: 18px !important; display: flex; flex-direction: column; justify-content: space-between; gap: 20px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); width: 100%; box-sizing: border-box;"'

updated_count = 0

for filepath in php_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content

    # Add inline slider styles if missing
    def replace_slider(match):
        slider_tag = match.group(0)
        if "style=" in slider_tag:
            return slider_tag
        return slider_tag[:-1] + f' {slider_style}>'

    content = re.sub(r'<input\s+type="range"\s+class="calc-slider"[^>]*>', replace_slider, content)

    # Add inline outputs styles if missing
    content = re.sub(r'<div\s+class="calc-outputs"(?![^>]*style=)[^>]*>', f'<div class="calc-outputs" {outputs_style}>', content)

    # Add Principal vs Interest bar to EMI calculator outputs if missing
    if "res-emi" in content and "bar-p" not in content:
        old_emi_block = '<div class="calc-output-main-val" id="res-emi" style="font-family: \'Newsreader\', Georgia, serif; font-size: clamp(2.2rem, 3.5vw, 2.6rem); font-weight: 700; color: #ffffff; line-height: 1.1; margin-bottom: 16px;">—</div>'
        new_emi_block = '''<div class="calc-output-main-val" id="res-emi" style="font-family: 'Newsreader', Georgia, serif; font-size: clamp(2.2rem, 3.5vw, 2.6rem); font-weight: 700; color: #ffffff; line-height: 1.1; margin-bottom: 14px;">—</div>
          <div style="background: rgba(255,255,255,0.12); height: 8px; border-radius: 4px; overflow: hidden; display: flex; margin: 10px 0 6px 0;">
            <div id="bar-p" style="background: #C89B3C; height: 100%; width: 70%; transition: width 0.3s ease;"></div>
            <div id="bar-i" style="background: #38BDF8; height: 100%; width: 30%; transition: width 0.3s ease;"></div>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 11px; color: #94A3B8; margin-bottom: 16px;">
            <span><span style="display:inline-block;width:8px;height:8px;background:#C89B3C;border-radius:50%;margin-right:4px;"></span> Principal</span>
            <span><span style="display:inline-block;width:8px;height:8px;background:#38BDF8;border-radius:50%;margin-right:4px;"></span> Interest</span>
          </div>'''
        content = content.replace(old_emi_block, new_emi_block)

    if content != orig_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1
        print(f"Updated WP template: {os.path.basename(filepath)}")

print(f"Total WP templates updated: {updated_count}")
