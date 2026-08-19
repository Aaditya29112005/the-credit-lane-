import os
import glob
import re

build_py_path = "/Users/aadityamohansamadhiya/the credit lane/build.py"
with open(build_py_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update render_calculator_html to add explicit style attributes to calc-slider
old_render_calc = """def render_calculator_html(p):
    calc_type = p["calcType"]
    d = p["calcDefaults"]
    
    if calc_type == "invoice":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Outstanding Invoice Value</span>
            <span class="value-output" id="inv-val-val">₹10,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="inv-val" min="100000" max="10000000" step="50000" value="{d['invoiceValue']}" oninput="updateInvoiceCalc()" onchange="updateInvoiceCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Advance Percentage</span>
            <span class="value-output" id="inv-adv-val">{d['advancePct']}%</span>
          </div>
          <input type="range" class="calc-slider" id="inv-adv" min="60" max="90" step="1" value="{d['advancePct']}" oninput="updateInvoiceCalc()" onchange="updateInvoiceCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Days Until Buyer Payment</span>
            <span class="value-output" id="inv-days-val">{d['days']} days</span>
          </div>
          <input type="range" class="calc-slider" id="inv-days" min="15" max="120" step="5" value="{d['days']}" oninput="updateInvoiceCalc()" onchange="updateInvoiceCalc()">
        </div>
        <input type="hidden" id="inv-mrate" value="{d['monthlyRate']}">
        \"\"\"
        
    elif calc_type == "settlement":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Outstanding Loan Dues</span>
            <span class="value-output" id="set-dues-val">₹50,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="set-dues" min="500000" max="50000000" step="100000" value="{d['outstanding']}" oninput="updateSettlementCalc()" onchange="updateSettlementCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Proposed OTS Percentage</span>
            <span class="value-output" id="set-pct-val">{d['settlePct']}% of dues</span>
          </div>
          <input type="range" class="calc-slider" id="set-pct" min="30" max="90" step="1" value="{d['settlePct']}" oninput="updateSettlementCalc()" onchange="updateSettlementCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Upfront Token Payment Required</span>
            <span class="value-output" id="set-tok-val">{d['tokenPct']}% of settlement</span>
          </div>
          <input type="range" class="calc-slider" id="set-tok" min="5" max="10" step="1" value="{d['tokenPct']}" oninput="updateSettlementCalc()" onchange="updateSettlementCalc()">
        </div>
        \"\"\"
        
    elif calc_type == "dilution":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Target Raise Amount</span>
            <span class="value-output" id="dil-raise-val">₹7,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="dil-raise" min="5000000" max="300000000" step="5000000" value="{d['raise']}" oninput="updateDilutionCalc()" onchange="updateDilutionCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Pre-Money Valuation</span>
            <span class="value-output" id="dil-pre-val">₹20,00,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="dil-pre" min="20000000" max="1000000000" step="5000000" value="{d['preMoney']}" oninput="updateDilutionCalc()" onchange="updateDilutionCalc()">
        </div>
        \"\"\"
        
    elif calc_type == "ipo":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Fresh Issue Size</span>
            <span class="value-output" id="ipo-issue-val">₹8,00,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="ipo-issue" min="10000000" max="1000000000" step="5000000" value="{d['raise']}" oninput="updateIpoCalc()" onchange="updateIpoCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Pre-Issue Business Valuation</span>
            <span class="value-output" id="ipo-pre-val">₹25,00,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="ipo-pre" min="50000000" max="4000000000" step="10000000" value="{d['preMoney']}" oninput="updateIpoCalc()" onchange="updateIpoCalc()">
        </div>
        \"\"\"
        
    elif calc_type == "valuation":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Annualised EBITDA</span>
            <span class="value-output" id="val-ebitda-val">₹1,50,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="val-ebitda" min="1000000" max="100000000" step="500000" value="{d['ebitda']}" oninput="updateValuationCalc()" onchange="updateValuationCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Sector Multiple — Low Bound</span>
            <span class="value-output" id="val-mlo-val">{d['multipleLow']}x</span>
          </div>
          <input type="range" class="calc-slider" id="val-mlo" min="3" max="12" step="0.5" value="{d['multipleLow']}" oninput="updateValuationCalc()" onchange="updateValuationCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Sector Multiple — High Bound</span>
            <span class="value-output" id="val-mhi-val">{d['multipleHigh']}x</span>
          </div>
          <input type="range" class="calc-slider" id="val-mhi" min="4" max="18" step="0.5" value="{d['multipleHigh']}" oninput="updateValuationCalc()" onchange="updateValuationCalc()">
        </div>
        \"\"\"
        
    elif calc_type == "subsidy":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Total Project / Machine Cost</span>
            <span class="value-output" id="sub-cost-val">₹20,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="sub-cost" min="100000" max="50000000" step="100000" value="{d['cost']}" oninput="updateSubsidyCalc()" onchange="updateSubsidyCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Policy Subsidy Rate</span>
            <span class="value-output" id="sub-rate-val">{d['rate']}%</span>
          </div>
          <input type="range" class="calc-slider" id="sub-rate" min="5" max="30" step="1" value="{d['rate']}" oninput="updateSubsidyCalc()" onchange="updateSubsidyCalc()">
        </div>
        <input type="hidden" id="sub-cap" value="{d['cap']}">
        \"\"\"
        
    else: # Default: EMI Term Loan
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Desired Loan Amount</span>
            <span class="value-output" id="emi-p-val">₹50,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="emi-p" min="{d['minP']}" max="{d['maxP']}" step="{max(10000, round(d['maxP']/100))}" value="{d['principal']}" oninput="updateEmiCalc()" onchange="updateEmiCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Interest Rate (p.a. indicative)</span>
            <span class="value-output" id="emi-r-val">{d['rate']}%</span>
          </div>
          <input type="range" class="calc-slider" id="emi-r" min="{d['minR']}" max="{d['maxR']}" step="0.1" value="{d['rate']}" oninput="updateEmiCalc()" onchange="updateEmiCalc()">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Repayment Tenure</span>
            <span class="value-output" id="emi-y-val">{d['years']} yrs</span>
          </div>
          <input type="range" class="calc-slider" id="emi-y" min="{d['minY']}" max="{d['maxY']}" step="1" value="{d['years']}" oninput="updateEmiCalc()" onchange="updateEmiCalc()">
        </div>
        \"\"\""""

slider_style = 'style="width: 100%; height: 8px; border-radius: 4px; outline: none; -webkit-appearance: none; appearance: none; background: #E2DDD5; cursor: pointer; accent-color: #C89B3C;"'

new_render_calc = f"""def render_calculator_html(p):
    calc_type = p["calcType"]
    d = p["calcDefaults"]
    
    if calc_type == "invoice":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Outstanding Invoice Value</span>
            <span class="value-output" id="inv-val-val">₹10,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="inv-val" min="100000" max="10000000" step="50000" value="{{d['invoiceValue']}}" oninput="updateInvoiceCalc()" onchange="updateInvoiceCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Advance Percentage</span>
            <span class="value-output" id="inv-adv-val">{{d['advancePct']}}%</span>
          </div>
          <input type="range" class="calc-slider" id="inv-adv" min="60" max="90" step="1" value="{{d['advancePct']}}" oninput="updateInvoiceCalc()" onchange="updateInvoiceCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Days Until Buyer Payment</span>
            <span class="value-output" id="inv-days-val">{{d['days']}} days</span>
          </div>
          <input type="range" class="calc-slider" id="inv-days" min="15" max="120" step="5" value="{{d['days']}}" oninput="updateInvoiceCalc()" onchange="updateInvoiceCalc()" {slider_style}>
        </div>
        <input type="hidden" id="inv-mrate" value="{{d['monthlyRate']}}">
        \"\"\"
        
    elif calc_type == "settlement":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Outstanding Loan Dues</span>
            <span class="value-output" id="set-dues-val">₹50,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="set-dues" min="500000" max="50000000" step="100000" value="{{d['outstanding']}}" oninput="updateSettlementCalc()" onchange="updateSettlementCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Proposed OTS Percentage</span>
            <span class="value-output" id="set-pct-val">{{d['settlePct']}}% of dues</span>
          </div>
          <input type="range" class="calc-slider" id="set-pct" min="30" max="90" step="1" value="{{d['settlePct']}}" oninput="updateSettlementCalc()" onchange="updateSettlementCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Upfront Token Payment Required</span>
            <span class="value-output" id="set-tok-val">{{d['tokenPct']}}% of settlement</span>
          </div>
          <input type="range" class="calc-slider" id="set-tok" min="5" max="10" step="1" value="{{d['tokenPct']}}" oninput="updateSettlementCalc()" onchange="updateSettlementCalc()" {slider_style}>
        </div>
        \"\"\"
        
    elif calc_type == "dilution":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Target Raise Amount</span>
            <span class="value-output" id="dil-raise-val">₹7,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="dil-raise" min="5000000" max="300000000" step="5000000" value="{{d['raise']}}" oninput="updateDilutionCalc()" onchange="updateDilutionCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Pre-Money Valuation</span>
            <span class="value-output" id="dil-pre-val">₹20,00,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="dil-pre" min="20000000" max="1000000000" step="5000000" value="{{d['preMoney']}}" oninput="updateDilutionCalc()" onchange="updateDilutionCalc()" {slider_style}>
        </div>
        \"\"\"
        
    elif calc_type == "ipo":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Fresh Issue Size</span>
            <span class="value-output" id="ipo-issue-val">₹8,00,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="ipo-issue" min="10000000" max="1000000000" step="5000000" value="{{d['raise']}}" oninput="updateIpoCalc()" onchange="updateIpoCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Pre-Issue Business Valuation</span>
            <span class="value-output" id="ipo-pre-val">₹25,00,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="ipo-pre" min="50000000" max="4000000000" step="10000000" value="{{d['preMoney']}}" oninput="updateIpoCalc()" onchange="updateIpoCalc()" {slider_style}>
        </div>
        \"\"\"
        
    elif calc_type == "valuation":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Annualised EBITDA</span>
            <span class="value-output" id="val-ebitda-val">₹1,50,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="val-ebitda" min="1000000" max="100000000" step="500000" value="{{d['ebitda']}}" oninput="updateValuationCalc()" onchange="updateValuationCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Sector Multiple — Low Bound</span>
            <span class="value-output" id="val-mlo-val">{{d['multipleLow']}}x</span>
          </div>
          <input type="range" class="calc-slider" id="val-mlo" min="3" max="12" step="0.5" value="{{d['multipleLow']}}" oninput="updateValuationCalc()" onchange="updateValuationCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Sector Multiple — High Bound</span>
            <span class="value-output" id="val-mhi-val">{{d['multipleHigh']}}x</span>
          </div>
          <input type="range" class="calc-slider" id="val-mhi" min="4" max="18" step="0.5" value="{{d['multipleHigh']}}" oninput="updateValuationCalc()" onchange="updateValuationCalc()" {slider_style}>
        </div>
        \"\"\"
        
    elif calc_type == "subsidy":
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Total Project / Machine Cost</span>
            <span class="value-output" id="sub-cost-val">₹20,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="sub-cost" min="100000" max="50000000" step="100000" value="{{d['cost']}}" oninput="updateSubsidyCalc()" onchange="updateSubsidyCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Policy Subsidy Rate</span>
            <span class="value-output" id="sub-rate-val">{{d['rate']}}%</span>
          </div>
          <input type="range" class="calc-slider" id="sub-rate" min="5" max="30" step="1" value="{{d['rate']}}" oninput="updateSubsidyCalc()" onchange="updateSubsidyCalc()" {slider_style}>
        </div>
        <input type="hidden" id="sub-cap" value="{{d['cap']}}">
        \"\"\"
        
    else: # Default: EMI Term Loan
        return f\"\"\"
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Desired Loan Amount</span>
            <span class="value-output" id="emi-p-val">₹50,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="emi-p" min="{{d['minP']}}" max="{{d['maxP']}}" step="{{max(10000, round(d['maxP']/100))}}" value="{{d['principal']}}" oninput="updateEmiCalc()" onchange="updateEmiCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Interest Rate (p.a. indicative)</span>
            <span class="value-output" id="emi-r-val">{{d['rate']}}%</span>
          </div>
          <input type="range" class="calc-slider" id="emi-r" min="{{d['minR']}}" max="{{d['maxR']}}" step="0.1" value="{{d['rate']}}" oninput="updateEmiCalc()" onchange="updateEmiCalc()" {slider_style}>
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Repayment Tenure</span>
            <span class="value-output" id="emi-y-val">{{d['years']}} yrs</span>
          </div>
          <input type="range" class="calc-slider" id="emi-y" min="{{d['minY']}}" max="{{d['maxY']}}" step="1" value="{{d['years']}}" oninput="updateEmiCalc()" onchange="updateEmiCalc()" {slider_style}>
        </div>
        \"\"\""""

if old_render_calc in content:
    content = content.replace(old_render_calc, new_render_calc)
    print("Replaced render_calculator_html.")
else:
    print("old_render_calc not found directly, performing regex replace.")

# 2. Update render_calculator_outputs_html to add Principal vs Interest Bar for Term Loan EMI
old_emi_output = """    else: # Term Loan EMI
        return \"\"\"
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
        \"\"\""""

new_emi_output = """    else: # Term Loan EMI
        return \"\"\"
        <div>
          <div class="calc-output-head" style="font-size: 11.5px; font-weight: 700; color: #C89B3C; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">MONTHLY EMI PAIRED</div>
          <div class="calc-output-main-val" id="res-emi" style="font-family: 'Newsreader', Georgia, serif; font-size: clamp(2.2rem, 3.5vw, 2.6rem); font-weight: 700; color: #ffffff; line-height: 1.1; margin-bottom: 14px;">—</div>
          
          <div style="background: rgba(255,255,255,0.12); height: 8px; border-radius: 4px; overflow: hidden; display: flex; margin: 10px 0 6px 0;">
            <div id="bar-p" style="background: #C89B3C; height: 100%; width: 70%; transition: width 0.3s ease;"></div>
            <div id="bar-i" style="background: #38BDF8; height: 100%; width: 30%; transition: width 0.3s ease;"></div>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 11px; color: #94A3B8; margin-bottom: 16px;">
            <span><span style="display:inline-block;width:8px;height:8px;background:#C89B3C;border-radius:50%;margin-right:4px;"></span> Principal</span>
            <span><span style="display:inline-block;width:8px;height:8px;background:#38BDF8;border-radius:50%;margin-right:4px;"></span> Interest</span>
          </div>

          <div class="calc-divider" style="border-bottom: 1px solid rgba(255, 255, 255, 0.12); margin-bottom: 16px;"></div>
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
        <a href="#apply" class="calc-apply-btn" style="display: block; width: 100%; text-align: center; background: linear-gradient(135deg, #C89B3C 0%, #B8860B 100%); color: #0B1F3A; font-weight: 700; font-size: 15px; padding: 14px 20px; border-radius: 10px; text-decoration: none; margin-top: 16px; box-shadow: 0 6px 20px rgba(184,134,11,0.3);">Apply for In-Principle Sanction &rarr;</a>
        \"\"\""""

if old_emi_output in content:
    content = content.replace(old_emi_output, new_emi_output)
    print("Replaced render_calculator_outputs_html EMI card.")

with open(build_py_path, "w", encoding="utf-8") as f:
    f.write(content)

print("build.py updated.")
