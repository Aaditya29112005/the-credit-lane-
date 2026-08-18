import os
import glob

theme_pages_dir = "/Users/aadityamohansamadhiya/the credit lane/credit-lane-theme/pages"
php_files = glob.glob(os.path.join(theme_pages_dir, "*.php"))

sidebar_form_replacement = """<div class="lead-card" id="apply" style="position: sticky; top: 100px; background: #FAF8F5; border: 1px solid #E2DDD5; border-top: 4px solid #C89B3C; border-radius: 20px; padding: 32px 26px; box-shadow: 0 10px 30px rgba(11, 31, 58, 0.06);">
                  <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 700; color: #0B1F3A; margin-bottom: 6px;">Check Eligibility</h3>
                  <p style="font-size: 13.5px; color: #5B6472; line-height: 1.5; margin-bottom: 22px;">Submit details. Our desk reviews profile variables and calls you back the same working day.</p>
                  
                  <form class="lead-form" action="https://formsubmit.co/Info@thecreditlane.in" method="POST" style="display: flex; flex-direction: column; gap: 14px;">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="hidden" name="_template" value="table">
                    <input type="hidden" name="_subject" value="New Service Lead - The Credit Lane">
                    
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 0;">Full Name *</label>
                      <input type="text" name="Full Name" placeholder="Your full name" required style="width: 100%; padding: 12px 14px; border-radius: 10px; border: 1px solid #DFD9CE; font-size: 14px; color: #0B1F3A; background: #F2EFE9; outline: none;">
                    </div>
                    
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 0;">Company Name *</label>
                      <input type="text" name="Company Name" placeholder="Company name" required style="width: 100%; padding: 12px 14px; border-radius: 10px; border: 1px solid #DFD9CE; font-size: 14px; color: #0B1F3A; background: #F2EFE9; outline: none;">
                    </div>
                    
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 0;">Phone Number *</label>
                      <input type="tel" name="Phone Number" placeholder="+91" required style="width: 100%; padding: 12px 14px; border-radius: 10px; border: 1px solid #DFD9CE; font-size: 14px; color: #0B1F3A; background: #F2EFE9; outline: none;">
                    </div>
                    
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 0;">Email *</label>
                      <input type="email" name="Email" placeholder="you@company.com" required style="width: 100%; padding: 12px 14px; border-radius: 10px; border: 1px solid #DFD9CE; font-size: 14px; color: #0B1F3A; background: #F2EFE9; outline: none;">
                    </div>
                    
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 0;">City *</label>
                      <input type="text" name="City" placeholder="e.g. Ghaziabad" required style="width: 100%; padding: 12px 14px; border-radius: 10px; border: 1px solid #DFD9CE; font-size: 14px; color: #0B1F3A; background: #F2EFE9; outline: none;">
                    </div>
                    
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 0;">Business Type *</label>
                      <select name="Business Type" required style="width: 100%; padding: 12px 14px; border-radius: 10px; border: 1px solid #DFD9CE; font-size: 14px; color: #0B1F3A; background: #F2EFE9; outline: none;">
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
                    
                    <div class="form-group" style="display: flex; flex-direction: column; gap: 6px;">
                      <label style="display: block; font-size: 13px; font-weight: 700; color: #0B1F3A; margin-bottom: 0;">Funding Size Required *</label>
                      <select name="Funding Size Required" required style="width: 100%; padding: 12px 14px; border-radius: 10px; border: 1px solid #DFD9CE; font-size: 14px; color: #0B1F3A; background: #F2EFE9; outline: none;">
                        <option value="">Select size</option>
                        <option value="Under ₹10 Lakh">Under ₹10 Lakh</option>
                        <option value="₹10 Lakh – ₹50 Lakh">₹10 Lakh – ₹50 Lakh</option>
                        <option value="₹50 Lakh – ₹1 Crore">₹50 Lakh – ₹1 Crore</option>
                        <option value="₹1 Crore – ₹5 Crore">₹1 Crore – ₹5 Crore</option>
                        <option value="Above ₹5 Crore">Above ₹5 Crore</option>
                      </select>
                    </div>
                    
                    <label class="form-consent" style="display: flex; align-items: flex-start; gap: 8px; font-size: 12px; color: #5B6472; line-height: 1.45; margin: 6px 0 14px; cursor: pointer;">
                      <input type="checkbox" name="Consent" required style="margin-top: 2px; width: 16px; height: 16px; accent-color: #C89B3C; flex-shrink: 0;">
                      I agree to the disclosure terms and authorise The Credit Lane to contact me regarding this enquiry.
                    </label>

                    <button type="submit" class="btn btn-primary" style="width: 100%; padding: 14px 20px; font-size: 15px; font-weight: 700; border-radius: 10px; background: linear-gradient(135deg, #C89B3C 0%, #B8860B 100%); color: #FFFFFF; border: none; cursor: pointer; box-shadow: 0 6px 20px rgba(184, 134, 11, 0.3);">
                      Submit Requirement &rarr;
                    </button>
                  </form>
                </div>"""

count = 0
for filepath in php_files:
    if os.path.basename(filepath) in ["about.php", "contact.php", "loans.php", "equity.php", "incentives.php", "partner-with-us.php"]:
        continue
    with open(filepath, 'r') as f:
        content = f.read()
    
    if '<div class="lead-card"' in content:
        start_idx = content.find('<div class="lead-card"')
        # Find closing div of lead-card block
        depth = 1
        pos = start_idx + 22
        while depth > 0 and pos < len(content):
            if content[pos:pos+4] == '<div':
                depth += 1
            elif content[pos:pos+6] == '</div>':
                depth -= 1
                if depth == 0:
                    break
            pos += 1
        if depth == 0:
            content = content[:start_idx] + sidebar_form_replacement + content[pos+6:]
    
    with open(filepath, 'w') as f:
        f.write(content)
    count += 1

print(f"Updated sidebar lead forms across {count} WordPress page templates in credit-lane-theme/pages/")
