import re

with open("build.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update PRODUCTS definitions with calcTitle & calcLabels
customizations = {
    "unsecured-business-loan-dod": {
        "calcTitle": "Unsecured Working Capital & Drop-Line OD Estimator",
        "calcLabels": {
            "pLabel": "Turnover / Working Capital Credit Limit",
            "rLabel": "Unsecured Interest Rate (p.a. indicative)",
            "yLabel": "Repayment / OD Limit Tenure",
            "outHead": "ESTIMATED MONTHLY EMI / OD INTEREST"
        }
    },
    "commercial-industrial-purchase-loan": {
        "calcTitle": "Commercial & Industrial Property Purchase Loan Calculator",
        "calcLabels": {
            "pLabel": "Commercial Property Valuation / Price",
            "rLabel": "Commercial Loan Interest Rate (% p.a.)",
            "yLabel": "Commercial Property Loan Tenure",
            "outHead": "ESTIMATED MONTHLY PROPERTY EMI"
        }
    },
    "machine-loan-sidbi": {
        "calcTitle": "SIDBI SPEED & SPEED Plus Machinery Finance Estimator",
        "calcLabels": {
            "pLabel": "New Machinery Invoice Outlay",
            "rLabel": "SIDBI Scheme Rate (% p.a.)",
            "yLabel": "Machinery Loan Tenure",
            "outHead": "ESTIMATED SIDBI MACHINERY EMI"
        }
    },
    "machine-loan-bank": {
        "calcTitle": "Bank Equipment & Machinery Purchase Loan Calculator",
        "calcLabels": {
            "pLabel": "Total Machinery Invoice Value",
            "rLabel": "Bank Loan Interest Rate (% p.a.)",
            "yLabel": "Machinery Loan Tenure",
            "outHead": "ESTIMATED BANK MACHINERY EMI"
        }
    },
    "invoice-finance": {
        "calcTitle": "Supply Chain Invoice & Receivable Discounting Estimator",
        "calcLabels": {
            "pLabel": "Outstanding Approved Invoice Value",
            "rLabel": "Upfront Advance Percentage",
            "yLabel": "Credit Due Period (Days)",
            "outHead": "IMMEDIATE LIQUID CASH ADVANCE"
        }
    },
    "school-college-funding": {
        "calcTitle": "Educational Campus Expansion & Building Loan Estimator",
        "calcLabels": {
            "pLabel": "Campus Infrastructure Project Outlay",
            "rLabel": "Institutional Loan Rate (% p.a.)",
            "yLabel": "Infrastructure Loan Tenure",
            "outHead": "ESTIMATED INSTITUTIONAL EMI"
        }
    },
    "builder-real-estate-funding": {
        "calcTitle": "Real Estate Construction & Builder Debt Sizing Estimator",
        "calcLabels": {
            "pLabel": "Project Construction Outlay",
            "rLabel": "Construction Debt Rate (% p.a.)",
            "yLabel": "Construction Loan Tenure",
            "outHead": "ESTIMATED MONTHLY PROJECT EMI"
        }
    },
    "hospital-funding": {
        "calcTitle": "Hospital Medical Equipment & Building Expansion Finance Estimator",
        "calcLabels": {
            "pLabel": "Medical Equipment & Facility Outlay",
            "rLabel": "Healthcare Loan Rate (% p.a.)",
            "yLabel": "Healthcare Loan Tenure",
            "outHead": "ESTIMATED HEALTHCARE EMI"
        }
    },
    "hotel-resort-funding": {
        "calcTitle": "Hospitality & Resort Infrastructure Finance Calculator",
        "calcLabels": {
            "pLabel": "Hotel Property Purchase / Renovation Cost",
            "rLabel": "Hospitality Loan Rate (% p.a.)",
            "yLabel": "Hospitality Repayment Tenure",
            "outHead": "ESTIMATED HOSPITALITY EMI"
        }
    },
    "npa-funding": {
        "calcTitle": "NPA One-Time Settlement (OTS) Savings & Debt Restructuring Estimator",
        "calcLabels": {
            "pLabel": "Total Outstanding Bank Dues (Principal + Interest)",
            "rLabel": "Target OTS Settlement Percentage (% of Dues)",
            "yLabel": "Upfront Token Payment Required (% of OTS)",
            "outHead": "ESTIMATED OTS SETTLEMENT AMOUNT"
        }
    },
    "infrastructure-funding": {
        "calcTitle": "Infrastructure & Solar Renewable Project Debt Calculator",
        "calcLabels": {
            "pLabel": "Total Infrastructure Project Outlay",
            "rLabel": "Project Debt Interest Rate (% p.a.)",
            "yLabel": "Project Finance Tenure",
            "outHead": "ESTIMATED INFRASTRUCTURE EMI"
        }
    },
    "venture-funding": {
        "calcTitle": "Venture Equity Raise & Growth Dilution Estimator",
        "calcLabels": {
            "pLabel": "Target Growth Capital Raise",
            "rLabel": "Agreed Pre-Money Valuation",
            "outHead": "POST-MONEY ENTERPRISE VALUATION"
        }
    },
    "sme-ipo": {
        "calcTitle": "SME Public Listing (IPO) Fresh Issue Valuation Estimator",
        "calcLabels": {
            "pLabel": "Fresh Issue Capital Sizing",
            "rLabel": "Pre-Issue Business Valuation",
            "outHead": "POST-ISSUE SME LISTING VALUATION"
        }
    },
    "main-board-ipo": {
        "calcTitle": "Mainboard Public IPO Capital Issue & Valuation Calculator",
        "calcLabels": {
            "pLabel": "Public Issue Size (Fresh Issue + OFS)",
            "rLabel": "Pre-Issue Enterprise Valuation",
            "outHead": "POST-IPO ENTERPRISE VALUATION"
        }
    },
    "valuation-services": {
        "calcTitle": "EBITDA Multiple Corporate Valuation Calculator",
        "calcLabels": {
            "pLabel": "Normalized Annualised EBITDA",
            "rLabel": "Sector Multiple — Low Bound",
            "yLabel": "Sector Multiple — High Bound",
            "outHead": "ESTIMATED ENTERPRISE VALUATION (LOW)"
        }
    },
    "up-tus-scheme": {
        "calcTitle": "UP TUS 50% Capital Subsidy Claim Estimator",
        "calcLabels": {
            "pLabel": "Total Machinery Purchase Invoice Cost",
            "rLabel": "Policy Subsidy Claim Rate",
            "outHead": "MAXIMUM TUS SUBSIDY CLAIMABLE"
        }
    },
    "up-msme-scheme": {
        "calcTitle": "UP MSME Promotion Policy Capital Grant Calculator",
        "calcLabels": {
            "pLabel": "Total Industrial Plant / Project Outlay",
            "rLabel": "Subsidy Percentage Category",
            "outHead": "ESTIMATED CAPITAL SUBSIDY CLAIM"
        }
    },
    "up-msmy-scheme": {
        "calcTitle": "UP Mukhyamantri Yuva Swarojgar Yojana (MSMY) Grant Estimator",
        "calcLabels": {
            "pLabel": "Micro-Unit Project Outlay",
            "rLabel": "State Margin Money Subsidy Rate",
            "outHead": "MARGIN MONEY SUBSIDY GRANT"
        }
    }
}

for pid, cdata in customizations.items():
    # Insert calcTitle and calcLabels into each product entry right after calcDefaults
    calc_title_str = f'"calcTitle": "{cdata["calcTitle"]}",\n        "calcLabels": {repr(cdata["calcLabels"])},'
    pattern = f'("id": "{pid}".*?"calcDefaults": \\{{.*?\\}},)'
    code = re.sub(pattern, f'\\1\n        {calc_title_str}', code, flags=re.DOTALL)

# 2. Update render_calculator_html(p)
old_render_calc = """def render_calculator_html(p):
    calc_type = p["calcType"]
    d = p["calcDefaults"]"""

new_render_calc = """def render_calculator_html(p):
    calc_type = p["calcType"]
    d = p["calcDefaults"]
    l = p.get("calcLabels", {})"""

code = code.replace(old_render_calc, new_render_calc)

# Replace label texts in render_calculator_html
code = code.replace('<span>Outstanding Invoice Value</span>', '<span>{l.get("pLabel", "Outstanding Invoice Value")}</span>')
code = code.replace('<span>Advance Percentage</span>', '<span>{l.get("rLabel", "Advance Percentage")}</span>')
code = code.replace('<span>Days Until Buyer Payment</span>', '<span>{l.get("yLabel", "Days Until Buyer Payment")}</span>')

code = code.replace('<span>Outstanding Loan Dues</span>', '<span>{l.get("pLabel", "Outstanding Loan Dues")}</span>')
code = code.replace('<span>Proposed OTS Percentage</span>', '<span>{l.get("rLabel", "Proposed OTS Percentage")}</span>')
code = code.replace('<span>Upfront Token Payment Required</span>', '<span>{l.get("yLabel", "Upfront Token Payment Required")}</span>')

code = code.replace('<span>Target Raise Amount</span>', '<span>{l.get("pLabel", "Target Raise Amount")}</span>')
code = code.replace('<span>Pre-Money Valuation</span>', '<span>{l.get("rLabel", "Pre-Money Valuation")}</span>')

code = code.replace('<span>Fresh Issue Size</span>', '<span>{l.get("pLabel", "Fresh Issue Size")}</span>')
code = code.replace('<span>Pre-Issue Business Valuation</span>', '<span>{l.get("rLabel", "Pre-Issue Business Valuation")}</span>')

code = code.replace('<span>Annualised EBITDA</span>', '<span>{l.get("pLabel", "Annualised EBITDA")}</span>')
code = code.replace('<span>Sector Multiple — Low Bound</span>', '<span>{l.get("rLabel", "Sector Multiple — Low Bound")}</span>')
code = code.replace('<span>Sector Multiple — High Bound</span>', '<span>{l.get("yLabel", "Sector Multiple — High Bound")}</span>')

code = code.replace('<span>Total Project / Machine Cost</span>', '<span>{l.get("pLabel", "Total Project / Machine Cost")}</span>')
code = code.replace('<span>Policy Subsidy Rate</span>', '<span>{l.get("rLabel", "Policy Subsidy Rate")}</span>')

code = code.replace('<span>Desired Loan Amount</span>', '<span>{l.get("pLabel", "Desired Loan Amount")}</span>')
code = code.replace('<span>Interest Rate (p.a. indicative)</span>', '<span>{l.get("rLabel", "Interest Rate (p.a. indicative)")}</span>')
code = code.replace('<span>Repayment Tenure</span>', '<span>{l.get("yLabel", "Repayment Tenure")}</span>')

# Update output header in render_calculator_outputs_html(p)
old_out_emi = '<div class="calc-output-head" style="font-size: 11.5px; font-weight: 700; color: #C89B3C; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">MONTHLY EMI PAIRED</div>'
new_out_emi = '<div class="calc-output-head" style="font-size: 11.5px; font-weight: 700; color: #C89B3C; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">{p.get("calcLabels", {}).get("outHead", "MONTHLY EMI PAIRED")}</div>'

code = code.replace(old_out_emi, new_out_emi)

# Update calc_title resolution in generate_servicepage
old_calc_title_res = 'calc_title = calc_titles.get(p["calcType"], "Indicative Repayment (EMI) Calculator")'
new_calc_title_res = 'calc_title = p.get("calcTitle", calc_titles.get(p["calcType"], "Indicative Repayment (EMI) Calculator"))'

code = code.replace(old_calc_title_res, new_calc_title_res)

with open("build.py", "w", encoding="utf-8") as f:
    f.write(code)

print("build.py successfully updated with custom calcTitle & calcLabels for all products!")
