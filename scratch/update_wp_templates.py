import os
import glob

theme_pages_dir = "/Users/aadityamohansamadhiya/the credit lane/credit-lane-theme/pages"
php_files = glob.glob(os.path.join(theme_pages_dir, "*.php"))

calc_outputs_replacement = """<div class="calc-outputs" style="background: #08192E !important; color: #FFFFFF !important; padding: 36px 32px; border-radius: 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
                        <div>
                          <div class="calc-output-head" style="font-size: 11.5px; font-weight: 700; color: #C89B3C; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">MONTHLY EMI PAIRED</div>
                          <div class="calc-output-main-val" id="res-emi" style="font-family: 'Newsreader', Georgia, serif; font-size: clamp(2.2rem, 3.5vw, 2.6rem); font-weight: 700; color: #ffffff; line-height: 1.1; margin-bottom: 16px;">—</div>
                          <div class="calc-divider" style="border-bottom: 1px solid rgba(255, 255, 255, 0.12); margin-bottom: 20px;"></div>
                          <div class="calc-metrics-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                            <div class="calc-metric-item">
                              <div class="m-label" style="font-size: 12px; color: #94A3B8; margin-bottom: 4px;">Total Interest</div>
                              <div class="m-val" id="res-interest" style="font-size: 18px; font-weight: 700; color: #ffffff;">—</div>
                            </div>
                            <div class="calc-metric-item">
                              <div class="m-label" style="font-size: 12px; color: #94A3B8; margin-bottom: 4px;">Total Payable</div>
                              <div class="m-val" id="res-total" style="font-size: 18px; font-weight: 700; color: #ffffff;">—</div>
                            </div>
                          </div>
                        </div>
                        <a href="#apply" class="calc-apply-btn" style="display: block; width: 100%; text-align: center; background: #C89B3C; color: #0B1F3A; font-weight: 700; font-size: 15px; padding: 14px 20px; border-radius: 10px; text-decoration: none; margin-top: 16px;">Apply for In-Principle Sanction &rarr;</a>
                      </div>"""

count = 0
for filepath in php_files:
    if os.path.basename(filepath) in ["about.php", "contact.php", "loans.php", "equity.php", "incentives.php"]:
        continue
    with open(filepath, 'r') as f:
        content = f.read()
    
    if '<div class="calc-outputs"' in content:
        start_idx = content.find('<div class="calc-outputs"')
        end_idx = content.find('</div>', start_idx)
        # Find closing div of calc-outputs block
        depth = 1
        pos = start_idx + 25
        while depth > 0 and pos < len(content):
            if content[pos:pos+5] == '<div':
                depth += 1
            elif content[pos:pos+6] == '</div>':
                depth -= 1
                if depth == 0:
                    break
            pos += 1
        if depth == 0:
            content = content[:start_idx] + calc_outputs_replacement + content[pos+6:]
    
    with open(filepath, 'w') as f:
        f.write(content)
    count += 1

print(f"Updated {count} WordPress page templates in credit-lane-theme/pages/")
