import os
import re

# Define calcTitle and calcLabels for all 19 products
CALC_CUSTOMIZATIONS = {
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

print("Customization dict ready with", len(CALC_CUSTOMIZATIONS), "products.")
