import os
import glob
import re

theme_pages_dir = "/Users/aadityamohansamadhiya/the credit lane/credit-lane-theme/pages"
php_files = glob.glob(os.path.join(theme_pages_dir, "*.php"))

form_replacement = """<div class="lead-card" id="apply" style="position: sticky; top: 100px; background: #ffffff; border: 1px solid #E2DDD5; border-top: 4px solid #C89B3C; border-radius: 18px; padding: 28px 22px; box-shadow: 0 12px 35px rgba(11, 31, 58, 0.08);">
                  <h3 style="font-family: var(--font-serif); font-size: 22px; color: #0B1F3A; margin-bottom: 8px;">Check Eligibility</h3>
                  <p style="font-size: 13.5px; color: #3E5372; margin-bottom: 20px; line-height: 1.4;">Submit details. Our desk reviews profile variables and calls you back the same working day.</p>
                  
                  <form class="lead-form" action="https://formsubmit.co/Info@thecreditlane.in" method="POST" style="display: flex; flex-direction: column; gap: 12px;">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="hidden" name="_template" value="table">
                    <input type="hidden" name="_subject" value="New Service Lead - The Credit Lane">
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 4px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 2px;">Full Name *</label>
                      <input type="text" name="Full Name" placeholder="Your full name" required style="width: 100%; padding: 11px 14px; border-radius: 8px; border: 1.5px solid #E2DDD5; font-size: 14px; color: #0B1F3A; background: #F7F5EF; outline: none;">
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 4px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 2px;">Company Name *</label>
                      <input type="text" name="Company Name" placeholder="Company name" required style="width: 100%; padding: 11px 14px; border-radius: 8px; border: 1.5px solid #E2DDD5; font-size: 14px; color: #0B1F3A; background: #F7F5EF; outline: none;">
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 4px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 2px;">Phone Number *</label>
                      <input type="tel" name="Phone Number" placeholder="+91" required style="width: 100%; padding: 11px 14px; border-radius: 8px; border: 1.5px solid #E2DDD5; font-size: 14px; color: #0B1F3A; background: #F7F5EF; outline: none;">
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 4px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 2px;">Email *</label>
                      <input type="email" name="Email" placeholder="you@company.com" required style="width: 100%; padding: 11px 14px; border-radius: 8px; border: 1.5px solid #E2DDD5; font-size: 14px; color: #0B1F3A; background: #F7F5EF; outline: none;">
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 4px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 2px;">City *</label>
                      <input type="text" name="City" placeholder="e.g. Ghaziabad" required style="width: 100%; padding: 11px 14px; border-radius: 8px; border: 1.5px solid #E2DDD5; font-size: 14px; color: #0B1F3A; background: #F7F5EF; outline: none;">
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 4px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 2px;">Business Type *</label>
                      <select name="Business Type" required style="width: 100%; padding: 11px 14px; border-radius: 8px; border: 1.5px solid #E2DDD5; font-size: 14px; color: #0B1F3A; background: #F7F5EF; outline: none;">
                        <option value="">Select your type</option>
                        <option value="Manufacturing / Industrial">Manufacturing / Industrial</option>
                        <option value="Real Estate Developer">Real Estate Developer</option>
                        <option value="Healthcare / Hospital">Healthcare / Hospital</option>
                        <option value="Education / Trust">Education / Trust</option>
                        <option value="Hospitality / Hotel">Hospitality / Hotel</option>
                        <option value="Infrastructure Contractor">Infrastructure Contractor</option>
                        <option value="B2B Trade & Services">B2B Trade &amp; Services</option>
                      </select>
                    </div>
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 4px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 2px;">Funding Size Required *</label>
                      <select name="Funding Size Required" required style="width: 100%; padding: 11px 14px; border-radius: 8px; border: 1.5px solid #E2DDD5; font-size: 14px; color: #0B1F3A; background: #F7F5EF; outline: none;">
                        <option value="">Select size</option>
                        <option value="Under ₹10 Lakh">Under ₹10 Lakh</option>
                        <option value="₹10 Lakh – ₹50 Lakh">₹10 Lakh – ₹50 Lakh</option>
                        <option value="₹50 Lakh – ₹1 Crore">₹50 Lakh – ₹1 Crore</option>
                        <option value="₹1 Crore – ₹5 Crore">₹1 Crore – ₹5 Crore</option>
                        <option value="Above ₹5 Crore">Above ₹5 Crore</option>
                      </select>
                    </div>
                    
                    <label class="form-consent" style="display: flex; align-items: flex-start; gap: 8px; font-size: 12px; color: #3E5372; line-height: 1.4; margin: 4px 0 8px; cursor: pointer;">
                      <input type="checkbox" name="Consent" required style="margin-top: 2px; width: 16px; height: 16px; accent-color: #C89B3C;">
                      I agree to the disclosure terms and authorise The Credit Lane to contact me regarding this enquiry.
                    </label>
                    <button class="btn btn-primary form-submit-btn" type="submit" style="width: 100%; padding: 14px 20px; border-radius: 8px; background: linear-gradient(135deg, #C89B3C 0%, #B8860B 100%); color: #ffffff; font-size: 15px; font-weight: 700; border: none; cursor: pointer; box-shadow: 0 6px 20px rgba(184,134,11,0.3); display: flex; align-items: center; justify-content: center; gap: 8px;">Submit Request &rarr;</button>
                  </form>
                </div>"""

calc_outputs_pattern = re.compile(r'<div class="calc-outputs">', re.IGNORECASE)
calc_outputs_replacement = '<div class="calc-outputs" style="background: #071529 !important; color: #FFFFFF !important; padding: 36px 32px; display: flex; flex-direction: column; justify-content: center; gap: 24px; border-left: 1px solid rgba(255, 255, 255, 0.1);">'

count = 0
for filepath in php_files:
    if os.path.basename(filepath) in ["about.php", "contact.php", "loans.php", "equity.php", "incentives.php"]:
        continue
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace lead-card block
    if '<div class="lead-card"' in content:
        start_idx = content.find('<div class="lead-card"')
        end_idx = content.find('</div>\n              </div>', start_idx)
        if end_idx != -1:
            old_card = content[start_idx:end_idx+6]
            content = content[:start_idx] + form_replacement + content[end_idx+6:]
    
    # Replace calc-outputs
    content = calc_outputs_pattern.sub(calc_outputs_replacement, content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    count += 1

print(f"Updated {count} WordPress page templates in credit-lane-theme/pages/")
