import os
import glob
import re

theme_pages_dir = "/Users/aadityamohansamadhiya/the credit lane/credit-lane-theme/pages"
php_files = glob.glob(os.path.join(theme_pages_dir, "*.php"))

# Common clean calculator template for term loan EMI
emi_calc_clean = """<div class="calc-container">
                    <div class="calc-grid">
                      <!-- Left Inputs -->
                      <div class="calc-inputs">
                        <div class="calc-input-group">
                          <div class="calc-input-label">
                            <span>Desired Loan Amount</span>
                            <span class="value-output" id="emi-p-val">₹50,00,000</span>
                          </div>
                          <input type="range" class="calc-slider" id="emi-p" min="500000" max="100000000" step="500000" value="5000000" oninput="updateEmiCalc()" onchange="updateEmiCalc()">
                        </div>
                        <div class="calc-input-group">
                          <div class="calc-input-label">
                            <span>Interest Rate (p.a. indicative)</span>
                            <span class="value-output" id="emi-r-val">12%</span>
                          </div>
                          <input type="range" class="calc-slider" id="emi-r" min="8" max="24" step="0.1" value="12" oninput="updateEmiCalc()" onchange="updateEmiCalc()">
                        </div>
                        <div class="calc-input-group">
                          <div class="calc-input-label">
                            <span>Repayment Tenure</span>
                            <span class="value-output" id="emi-y-val">5 yrs</span>
                          </div>
                          <input type="range" class="calc-slider" id="emi-y" min="1" max="15" step="1" value="5" oninput="updateEmiCalc()" onchange="updateEmiCalc()">
                        </div>
                      </div>
                      
                      <!-- Right Outputs -->
                      <div class="calc-outputs">
                        <div>
                          <div class="calc-output-head">MONTHLY EMI PAIRED</div>
                          <div class="calc-output-main-val" id="res-emi">—</div>
                          <div class="calc-divider"></div>
                          <div class="calc-metrics-row">
                            <div class="calc-metric-item">
                              <div class="m-label">Total Interest</div>
                              <div class="m-val" id="res-interest">—</div>
                            </div>
                            <div class="calc-metric-item">
                              <div class="m-label">Total Payable</div>
                              <div class="m-val" id="res-total">—</div>
                            </div>
                          </div>
                        </div>
                        <a href="#apply" class="calc-apply-btn">Apply for In-Principle Sanction &rarr;</a>
                      </div>
                    </div>
                    <div class="calc-disclaimer">
                      <b>* Notice:</b> Calculated figures are for simulation purposes only. Sizing, interest rate margins, security discount factors, and subsidy tranches depend on credit metrics and final sanction letters.
                    </div>
                  </div>"""

updated_count = 0
for filepath in php_files:
    filename = os.path.basename(filepath)
    if filename in ["about.php", "contact.php", "loans.php", "equity.php", "incentives.php", "partner-with-us.php"]:
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if file has calculator block
    if '<div class="calc-container">' in content:
        # Replace the entire calc-container block with a clean block
        start_pos = content.find('<div class="calc-container">')
        # Find closing of calc-container
        depth = 1
        pos = start_pos + len('<div class="calc-container">')
        while depth > 0 and pos < len(content):
            if content[pos:pos+4] == '<div':
                depth += 1
            elif content[pos:pos+6] == '</div>':
                depth -= 1
                if depth == 0:
                    break
            pos += 1
        
        if depth == 0:
            # Check if this page has specific calculator type (e.g. invoice, settlement, dilution, ipo, valuation, subsidy)
            # If default term loan EMI:
            if filename not in ["invoice-finance.php", "npa-funding.php", "pre-ipo-funding.php", "sme-ipo.php", "main-board-ipo.php", "valuation-services.php", "up-tus-scheme.php", "up-msme-scheme.php", "up-msmy-scheme.php"]:
                content = content[:start_pos] + emi_calc_clean + content[pos+6:]
                with open(filepath, 'w') as f:
                    f.write(content)
                updated_count += 1
                print(f"Cleaned calculator in {filename}")

print(f"Cleaned calculators across {updated_count} PHP templates.")
