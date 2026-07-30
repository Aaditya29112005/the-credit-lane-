import os
import shutil

# 1. DEFINE THE SERVICE DATA
PRODUCTS = [
    {
        "id": "unsecured-business-loan-dod",
        "category": "Loans",
        "subcategory": "Business & Working Capital",
        "eyebrow": "Loans / Working Capital",
        "name": "Unsecured Business Loan & DOD Limit",
        "headline": "Working Capital, Without Pledging Collateral",
        "sub": "Unsecured term loans and drop-line overdraft limits sized to your GST turnover — in-principle approval in as little as 24 hours.",
        "tag": "#FundedOnYourTurnover",
        "stats": [["₹5L – ₹5Cr", "Loan amount"], ["14% – 26% p.a.", "Interest rate*"], ["12 – 60 mo", "Tenure"]],
        "statNote": "*Unsecured NBFC pricing. CGTMSE-backed schemes can bring eligible borrowers down to 10.5–13% p.a.",
        "brief": [
            "An unsecured business loan gives your company working capital without pledging property, machinery or inventory — sanctioned on the strength of your GST turnover, banking conduct and credit history rather than a fixed asset.",
            "Because no collateral backs the exposure, pricing runs higher than secured credit: unsecured NBFC loans in the current market typically fall between 14% and 26% per annum, though government-backed CGTMSE schemes can bring select borrowers down to 10.5–13%.",
            "A drop-line overdraft (DOD) limit works alongside or instead of a term loan — you draw only what you need against a sanctioned ceiling, and interest accrues solely on the drawn balance, which keeps carrying cost low for seasonal cash gaps."
        ],
        "whoIntro": "This product fits businesses that value speed and flexibility over chasing the lowest possible rate.",
        "whoSummary": [
            "Best for: established firms needing fast, asset-free working capital.",
            "Think twice if: you can pledge property or machinery for a materially lower secured rate."
        ],
        "qualify": [
            "Business vintage of 2+ years with stable GST filings",
            "Need working capital for inventory, payroll or short-term cash gaps",
            "Want to avoid mortgaging property or machinery",
            "Existing bank relationship but no fresh collateral to offer"
        ],
        "features": [
            ["01", "No collateral required", "Sanctioned purely against turnover, banking and credit profile."],
            ["02", "Drop-line overdraft option", "Interest charged only on the amount drawn, not the full limit."],
            ["03", "Multi-lender comparison", "Your file is run across 15+ banks and NBFCs for the sharpest rate."],
            ["04", "CGTMSE eligibility check", "We check government-backed guarantee schemes that can cut your rate."]
        ],
        "process": [
            ["Document pickup", "Share GST, bank and ITR data — digitised the same day."],
            ["Lender matching", "Your file is matched against live rate cards from our panel."],
            ["Sanction & terms", "Compare 2–3 sanction letters side by side before you choose."],
            ["Disbursal", "Funds credited directly to your current account."]
        ],
        "calcType": "emi",
        "calcDefaults": {"principal": 2000000, "rate": 18, "years": 3, "minP": 200000, "maxP": 50000000, "minR": 10.5, "maxR": 26, "minY": 1, "maxY": 5},
        "reviews": {
            "rating": 4.6,
            "count": 212,
            "items": [
                ["Ankit Verma", "Ghaziabad", "We needed ₹80L before the festive season with no time to mortgage anything. Sanction letter in three days."],
                ["Priya Sharma", "Noida", "Compared quotes from four lenders side by side — ended up 3% cheaper than my bank's first offer."],
                ["Ravi Kant", "Sahibabad", "The DOD limit meant I stopped paying interest on money I wasn't even using."]
            ]
        },
        "faqs": [
            ["Is any collateral needed at all?", "No. Sanction is based on turnover, banking conduct and credit score — not fixed assets."],
            ["How is a DOD limit different from a term loan?", "A term loan disburses the full amount upfront with fixed EMIs. A DOD limit is a revolving line — you draw and repay within the limit and pay interest only on the utilised amount."],
            ["What CIBIL score is typically required?", "700+ is preferred by most lenders, though a strong banking profile can offset a slightly lower score."],
            ["Can I get a lower rate through a government scheme?", "CGTMSE-backed schemes can bring eligible MSME borrowers down to roughly 10.5–13% p.a. — we check this alongside your standard application."]
        ]
    },
    {
        "id": "commercial-industrial-purchase-loan",
        "category": "Loans",
        "subcategory": "Asset & Equipment Finance",
        "eyebrow": "Loans / Property",
        "name": "Commercial or Industrial Purchase Loan",
        "headline": "Own the Premises You Currently Rent",
        "sub": "Structured finance to purchase commercial shops, offices or industrial plots — repaid over a tenure that matches your business cycle.",
        "tag": "#StopPayingSomeoneElsesEMI",
        "stats": [["50% – 75%", "Loan-to-value"], ["8.5% – 14% p.a.", "Interest rate*"], ["Up to 15 yrs", "Tenure"]],
        "statNote": "*Public/private banks typically price 8.5–11%; NBFCs and HFCs 10–14%, depending on profile and property type.",
        "brief": [
            "A commercial or industrial purchase loan lets a business acquire operating premises without depleting working capital, with the property itself serving as security.",
            "Loan-to-value generally runs 50–75% of the registered property value, with banks pricing at the lower end (around 8.5–11% p.a.) and NBFCs typically 10–14% depending on borrower profile, property type and loan size.",
            "Because tenure can stretch to 15 years, EMIs are often lower than the rent a business would otherwise pay — converting a recurring cost into a growing asset."
        ],
        "whoIntro": "Best suited to businesses ready to trade a long-term EMI for ownership of the space they operate from.",
        "whoSummary": [
            "Best for: businesses currently renting premises, ready to own instead.",
            "Think twice if: you need the property's full value unlocked quickly — LTV caps at 75%."
        ],
        "qualify": [
            "Currently paying rent for business premises and want to own instead",
            "Buying an industrial plot or shed to relocate or expand operations",
            "Need a loan structured against both business and property cash flows",
            "Looking to free up working capital instead of paying cash for property"
        ],
        "features": [
            ["01", "High loan-to-value", "Finance up to 75% of the registered property value."],
            ["02", "Balance transfer support", "Move an existing commercial property loan to a lower rate."],
            ["03", "Flexible end-use", "Applies to shops, showrooms, offices, warehouses and industrial plots."],
            ["04", "Co-applicant structuring", "Combine promoter and firm income to maximise eligibility."]
        ],
        "process": [
            ["Property vetting", "Legal team checks title, encumbrance and zoning before you commit."],
            ["Valuation", "Empanelled valuers assess fair market value for loan sizing."],
            ["Sanction", "Lender issues terms based on property value and business income."],
            ["Registration & disbursal", "Funds released in sync with registration and legal formalities."]
        ],
        "calcType": "emi",
        "calcDefaults": {"principal": 10000000, "rate": 11, "years": 10, "minP": 2000000, "maxP": 100000000, "minR": 8.5, "maxR": 14, "minY": 3, "maxY": 15},
        "reviews": {
            "rating": 4.7,
            "count": 158,
            "items": [
                ["Sanjay Gupta", "Loni", "Buying our shed outright would have locked up all our capital. This let us keep working capital free."],
                ["Meena Aggarwal", "Ghaziabad", "EMI came in lower than the rent we were paying for the same shop. Should have done this years ago."],
                ["Deepak Chawla", "Modinagar", "The legal vetting caught a title issue our own lawyer missed. Saved us a bad purchase."]
            ]
        },
        "faqs": [
            ["Can I include renovation cost in the loan?", "Yes, most lenders allow a top-up for fit-out or renovation once the base purchase loan is sanctioned."],
            ["Is a co-applicant mandatory?", "Not mandatory, but adding a co-applicant (partner/promoter) often improves eligibility and rate."],
            ["What happens if the property has unclear title?", "We flag title issues during legal vetting before applying — resolving these upfront avoids sanction delays later."],
            ["Bank or NBFC — which is cheaper?", "Banks are typically cheaper (8.5–11%) but slower and stricter on documentation; NBFCs move faster at 10–14%. We benchmark both before you decide."]
        ]
    },
    {
        "id": "machine-loan-sidbi",
        "category": "Loans",
        "subcategory": "Asset & Equipment Finance",
        "eyebrow": "Loans / Machinery",
        "name": "Machine Loan from SIDBI",
        "headline": "Machinery Finance on SIDBI's SME-First Terms",
        "sub": "Access SIDBI's SPEED and SPEED Plus machinery schemes — built specifically for MSMEs, with pricing banks rarely match.",
        "tag": "#BuiltForMSMEs",
        "stats": [["8.80% – 10.50% p.a.", "Interest rate (SPEED Plus)"], ["Up to 100%", "Machine cost financed"], ["2 – 5 yrs", "Tenure"]],
        "statNote": "Rates and financing % per SIDBI's SPEED / SPEED Plus schemes; internal rating-based, subject to change.",
        "brief": [
            "SIDBI runs machinery finance as part of its core MSME mandate through the SPEED and SPEED Plus schemes, which fund up to 100% of machinery cost — up to ₹1 crore for new borrowers and ₹2–3 crore for existing SIDBI customers.",
            "Pricing reflects that mandate: SPEED Plus carries interest of roughly 8.80–10.50% per annum based on internal rating, meaningfully below what a general-purpose bank loan typically offers for a comparable profile.",
            "Because SIDBI schemes are frequently paired with state incentive programmes, we cross-check your eligibility for a capital subsidy at the same time as filing the loan — often reducing the effective cost of the machine further."
        ],
        "whoIntro": "Purpose-built for registered MSMEs buying new machinery who want scheme-linked pricing rather than standard bank rates.",
        "whoSummary": [
            "Best for: Udyam-registered MSMEs buying new or upgraded machinery.",
            "Think twice if: your unit isn't manufacturing/processing-classified — scheme eligibility varies by activity."
        ],
        "qualify": [
            "Registered MSME looking to buy new or upgrade existing machinery",
            "Want scheme-linked pricing rather than standard bank rates",
            "Manufacturing or processing unit expanding capacity",
            "Prefer a lender specialising in SME machinery finance"
        ],
        "features": [
            ["01", "MSME-first pricing", "SIDBI's mandate is SME lending, reflected in preferential 8.8–10.5% rates."],
            ["02", "Up to 100% funding", "Machinery cost financed in full for eligible new borrowers up to ₹1Cr."],
            ["03", "Scheme stacking", "We check TUS/MSME subsidy eligibility alongside the loan for compounded savings."],
            ["04", "Vendor-direct disbursal", "Payment made directly to the machine supplier against invoice."]
        ],
        "process": [
            ["Scheme mapping", "We identify whether SPEED or SPEED Plus fits your machine category and unit size."],
            ["Application filing", "Documentation compiled and filed through our SIDBI channel."],
            ["Technical appraisal", "SIDBI reviews the machine specification and vendor credentials."],
            ["Sanction & vendor payment", "Approved amount paid directly against the vendor invoice."]
        ],
        "calcType": "emi",
        "calcDefaults": {"principal": 5000000, "rate": 9.5, "years": 5, "minP": 500000, "maxP": 30000000, "minR": 8.8, "maxR": 10.5, "minY": 2, "maxY": 5},
        "reviews": {
            "rating": 4.8,
            "count": 96,
            "items": [
                ["Harish Bansal", "Ghaziabad", "Our bank quoted 2 points higher than what SIDBI sanctioned for the same CNC machine."],
                ["Sunita Rathi", "Sahibabad", "Didn't know SPEED Plus existed until Credit Lane flagged it — funded 100% of our machine cost."],
                ["Vikram Oberoi", "Loni", "Scheme mapping saved us weeks of applying to the wrong SIDBI product."]
            ]
        },
        "faqs": [
            ["Can this be used for second-hand machinery?", "Select schemes allow it, subject to valuation and residual life certification — we confirm scheme-specific rules during mapping."],
            ["Is SIDBI finance only for manufacturing units?", "Primarily manufacturing and allied processing units, though eligibility varies by scheme — we verify this against your unit's activity code."],
            ["How does this differ from a bank machine loan?", "SIDBI's mandate is dedicated MSME lending, which means sharper pricing (8.8–10.5% vs 9–13% at banks) and higher LTV for a comparable profile."],
            ["What's the difference between SPEED and SPEED Plus?", "SPEED funds up to ₹1Cr for new borrowers at ~9.25–10% p.a.; SPEED Plus extends financing to ₹2–3Cr at a marginally lower 8.80–10.50% band for stronger-rated borrowers."]
        ]
    },
    {
        "id": "machine-loan-bank",
        "category": "Loans",
        "subcategory": "Asset & Equipment Finance",
        "eyebrow": "Loans / Machinery",
        "name": "Machine Loan from Bank",
        "headline": "Bank-Funded Machinery Loans, on Your Existing Relationship",
        "sub": "When you'd rather finance new machinery through your existing bank, we structure the file and negotiate terms on your behalf.",
        "tag": "#YourBankCanDoBetter",
        "stats": [["9% – 13% p.a.", "Interest rate"], ["Up to 80%", "Machine cost financed"], ["3 – 7 yrs", "Tenure"]],
        "statNote": "Typical secured machinery loan pricing from scheduled banks; final rate depends on relationship and credit profile.",
        "brief": [
            "A standard bank machine loan is often the fastest route when a business already holds a banking relationship, since much of the KYC and credit assessment reuses existing records.",
            "Pricing typically runs 9–13% per annum, secured against the machinery itself, with up to 80% of invoice value financed and tenure stretching 3–7 years depending on the asset's useful life.",
            "Where this route differs from SIDBI or scheme-linked finance is flexibility — banks can structure tenure, moratorium and repayment around your specific cash flow rather than a fixed scheme template."
        ],
        "whoIntro": "Fits businesses that want to keep financing within an existing bank relationship rather than route through a scheme.",
        "whoSummary": [
            "Best for: businesses with an existing bank relationship wanting a faster, familiar process.",
            "Think twice if: you qualify for SIDBI's SPEED scheme — that route is usually cheaper."
        ],
        "qualify": [
            "Have an existing current account or credit relationship with a bank",
            "Prefer a single-bank relationship over multi-lender scheme routes",
            "Buying machinery where SIDBI scheme criteria don't apply",
            "Need faster turnaround using an existing banking file"
        ],
        "features": [
            ["01", "Relationship-based pricing", "Leverages your existing banking history to negotiate rate and tenure."],
            ["02", "Broad machine coverage", "Applicable across manufacturing, printing, textile, food-processing and more."],
            ["03", "Moratorium structuring", "Repayment holiday negotiated for machines with a commissioning lag."],
            ["04", "Multi-bank rate check", "We benchmark your primary bank's offer against 3–4 alternatives before you sign."]
        ],
        "process": [
            ["Rate benchmarking", "We pull comparative quotes from your bank and 3 alternatives."],
            ["File preparation", "Financials and machine specs compiled into the lender's format."],
            ["Sanction", "Bank issues terms; we negotiate rate, tenure and moratorium if needed."],
            ["Disbursal", "Payment released to vendor on invoice, machine delivery confirmed."]
        ],
        "calcType": "emi",
        "calcDefaults": {"principal": 4000000, "rate": 11, "years": 5, "minP": 500000, "maxP": 20000000, "minR": 9, "maxR": 13, "minY": 3, "maxY": 7},
        "reviews": {
            "rating": 4.5,
            "count": 134,
            "items": [
                ["Manoj Tyagi", "Sahibabad", "Assumed my bank's first quote was final — Credit Lane got them to revise it once they saw a competing offer."],
                ["Reena Malhotra", "Ghaziabad", "Moratorium structuring meant we didn't pay EMI until the machine was actually running."],
                ["Ashok Jindal", "Modinagar", "Filed with my existing bank but they still shopped three other lenders — worth it."]
            ]
        },
        "faqs": [
            ["Does staying with my existing bank guarantee the best rate?", "Not automatically — we still benchmark against other lenders, and use competing offers to negotiate your bank's terms."],
            ["Can I get a moratorium before EMIs start?", "Yes, particularly if the machine needs installation or commissioning time before it generates revenue."],
            ["What if my bank rejects the file?", "We re-route the same file to an alternate bank or NBFC in our panel without restarting documentation from scratch."],
            ["How does this compare with SIDBI's rates?", "SIDBI's SPEED/SPEED Plus schemes (8.8–10.5%) typically undercut standard bank machine loans (9–13%) for eligible MSMEs — we check SIDBI eligibility first."]
        ]
    },
    {
        "id": "invoice-finance",
        "category": "Loans",
        "subcategory": "Business & Working Capital",
        "eyebrow": "Loans / Trade Finance",
        "name": "Sale Invoice Finance / Purchase Invoice Finance",
        "headline": "Unlock Cash Tied Up in Unpaid Invoices",
        "sub": "Convert receivables into immediate working capital, or finance purchases against upcoming payables — without waiting out your buyer's credit cycle.",
        "tag": "#DontWaitToGetPaid",
        "stats": [["75% – 90%", "Of invoice value advanced"], ["From 12% p.a.", "Discounting cost*"], ["24 – 72 hrs", "Funds against invoice"]],
        "statNote": "*Discounting typically priced 1.5–3% per month of invoice value depending on buyer credit strength and tenor.",
        "brief": [
            "Sale invoice finance advances cash against confirmed receivables, letting a business collect early instead of waiting out a buyer's payment cycle — particularly useful when selling to large corporates with long standard credit terms.",
            "Advances typically run 75–90% of invoice value, with the discounting cost priced at roughly 1.5–3% per month depending on your buyer's credit strength — cheaper than most unsecured working capital because the receivable itself is the security.",
            "Purchase invoice finance works in reverse, funding payment to your suppliers against a confirmed purchase order, which helps maintain supplier relationships and unlock early-payment discounts."
        ],
        "whoIntro": "Fits businesses selling on credit terms to reputable buyers, where the payment gap — not creditworthiness — is the constraint.",
        "whoSummary": [
            "Best for: B2B sellers with 30–90 day buyer credit terms and strong receivables.",
            "Think twice if: your buyers are small/unrated — pricing depends heavily on buyer credit quality."
        ],
        "qualify": [
            "Selling to large corporates or PSUs on 30–90 day credit terms",
            "Cash flow is stretched between delivery and payment realisation",
            "Need to pay suppliers before your own receivables come in",
            "Want financing tied to transactions, not a fixed term loan"
        ],
        "features": [
            ["01", "Receivables unlocked fast", "Advance released within 24–72 hours of invoice acceptance."],
            ["02", "Buyer-credit based pricing", "Rate often reflects your buyer's credit strength, not just yours."],
            ["03", "Purchase-side cover", "Finance supplier payments against confirmed purchase orders."],
            ["04", "Revolving structure", "Repeat draws as new invoices are raised, without fresh sanction each time."]
        ],
        "process": [
            ["Invoice/PO review", "We assess buyer credit quality and invoice authenticity."],
            ["Facility sanction", "A revolving limit is set based on projected monthly invoice volume."],
            ["Draw-down", "Submit invoices as raised; funds advanced within days."],
            ["Settlement", "Facility is repaid as the buyer/you settle the underlying invoice."]
        ],
        "calcType": "invoice",
        "calcDefaults": {"invoiceValue": 1000000, "advancePct": 85, "monthlyRate": 2, "days": 60},
        "reviews": {
            "rating": 4.7,
            "count": 87,
            "items": [
                ["Nitin Sabharwal", "Noida", "Our biggest client pays on a strict 75-day cycle. This closed the gap so we stopped delaying our own supplier payments."],
                ["Kavita Bhalla", "Ghaziabad", "85% advance within two days of raising the invoice — genuinely changed how we manage cash flow."],
                ["Rajeev Malik", "Sahibabad", "Purchase invoice financing let us take an early-payment discount from our steel supplier for the first time."]
            ]
        },
        "faqs": [
            ["Does my buyer need to be involved in the process?", "Some structures require buyer acknowledgement of the invoice; others don't — we confirm which applies to your buyer base."],
            ["Is this the same as a cash credit limit?", "No — it's transaction-linked and tied to specific invoices/POs, rather than a general-purpose revolving limit against stock and receivables."],
            ["What if a buyer delays payment beyond the invoice term?", "Terms vary by facility — we structure this upfront so you know exactly how delays are handled before drawing down."],
            ["How is the discounting cost calculated?", "Typically 1.5–3% per month on the advanced amount, prorated for the actual number of days outstanding — you're not charged for the full tenor if the buyer pays early."]
        ]
    },
    {
        "id": "school-college-funding",
        "category": "Loans",
        "subcategory": "Sector-Specific Funding",
        "eyebrow": "Loans / Institutional",
        "name": "School & College Funding",
        "headline": "Infrastructure Finance for Educational Institutions",
        "sub": "Term loans for campus construction, hostel blocks, labs and equipment — structured against fee-cycle cash flows.",
        "tag": "#BuiltAroundYourAcademicCalendar",
        "stats": [["Up to ₹25Cr", "Loan size"], ["10.5% – 14% p.a.", "Interest rate*"], ["Up to 15 yrs", "Tenure"]],
        "statNote": "*Institutional infrastructure lending, assessed case-by-case against enrolment, fee income and trust financials.",
        "brief": [
            "Educational institution funding differs from a standard business loan in one key respect: cash flow arrives in seasonal fee cycles rather than continuous revenue, so lenders structure repayment schedules accordingly rather than defaulting to flat monthly EMIs.",
            "Pricing for trust/society-backed institutional infrastructure loans generally falls in the 10.5–14% per annum range, comparable to secured commercial term lending, with tenure extending up to 15 years for larger campus projects.",
            "Trust and society borrowers also face different documentation requirements than companies — governing body resolutions and trust deed compliance are central to the sanction process, which is where institutional lending expertise matters most."
        ],
        "whoIntro": "Built for registered trusts and societies funding physical expansion, not day-to-day operating costs.",
        "whoSummary": [
            "Best for: established trusts/societies expanding campus, hostel or lab infrastructure.",
            "Think twice if: you're a first-year institution — most lenders want 5+ years of enrolment history."
        ],
        "qualify": [
            "Registered trust/society running a school or college",
            "Expanding campus, building a new block, or upgrading facilities",
            "Need funding structured around academic-year fee inflows",
            "Established institution with a multi-year enrolment track record"
        ],
        "features": [
            ["01", "Fee-cycle repayment", "EMI/quarterly structuring aligned to admission and fee-collection cycles."],
            ["02", "Long tenure", "Extended repayment periods suited to infrastructure-grade assets."],
            ["03", "Equipment & construction combined", "One facility can cover civil construction plus lab/IT equipment."],
            ["04", "Trust/society structuring", "Documentation built around trust deed and governing body approvals."]
        ],
        "process": [
            ["Institutional assessment", "Enrolment trends, fee structure and governance reviewed."],
            ["Project appraisal", "Construction or equipment plan evaluated against loan sizing."],
            ["Sanction", "Terms structured around the academic fee-collection calendar."],
            ["Phased disbursal", "Funds released in stages tied to construction or procurement milestones."]
        ],
        "calcType": "emi",
        "calcDefaults": {"principal": 20000000, "rate": 12, "years": 10, "minP": 2000000, "maxP": 250000000, "minR": 10.5, "maxR": 14, "minY": 3, "maxY": 15},
        "reviews": {
            "rating": 4.6,
            "count": 41,
            "items": [
                ["Anita Malhotra", "Ghaziabad", "The bank's standard EMI ignored our seasonal fee income. Credit Lane restructured it around our actual collection months."],
                ["S.K. Tripathi", "Loni", "Trust deed compliance was the part we understood least — they handled it end to end."],
                ["Rekha Bhatia", "Modinagar", "Funded our new lab block and hostel in one facility instead of two separate loans."]
            ]
        },
        "faqs": [
            ["Can this fund a hostel block specifically?", "Yes, hostel and residential infrastructure are commonly financed alongside academic blocks."],
            ["Do government-aided schools qualify differently?", "Aided institutions have additional documentation around grant-in-aid status — we assess this case by case."],
            ["Is equipment (labs, computers) financed separately from construction?", "It can be combined into one facility or split, depending on procurement timing and vendor invoicing."],
            ["What repayment tenure is realistic for a large campus project?", "Larger infrastructure projects commonly run 10–15 years, matched to the scale of construction and projected fee growth."]
        ]
    },
    {
        "id": "builder-real-estate-funding",
        "category": "Loans",
        "subcategory": "Sector-Specific Funding",
        "eyebrow": "Loans / Real Estate",
        "name": "Builder and Real Estate Developers Funding",
        "headline": "Construction Finance, Structured Around Your Project Timeline",
        "sub": "Project-linked funding for developers — from land acquisition and approvals through construction-linked disbursal.",
        "tag": "#MilestonesNotLumpSums",
        "stats": [["Up to 70%", "Of project cost financed*"], ["11% – 16% p.a.", "Interest rate"], ["Up to 5 yrs", "Project tenure"]],
        "statNote": "*Excludes land cost; disbursal released against construction milestones, not upfront.",
        "brief": [
            "Developer funding is structured fundamentally differently from a standard business loan — disbursal is tied to construction milestones rather than released upfront, which controls interest cost and aligns with RERA-mandated escrow practices.",
            "Financing typically covers up to 70% of construction cost (excluding land), priced at roughly 11–16% per annum depending on project risk, developer track record and location, with tenure generally capped at 5 years for a single project cycle.",
            "Because project risk is assessed on title clarity, approval status and developer track record together, early-stage due diligence is often the difference between a smooth sanction and a stalled one — this is where we front-load the work."
        ],
        "whoIntro": "For developers with an approved plan ready to break ground, not early-stage land speculation.",
        "whoSummary": [
            "Best for: developers with clear title and an approved plan, seeking milestone-linked funds.",
            "Think twice if: your project lacks RERA registration — most lenders require it before sanction."
        ],
        "qualify": [
            "Developer with an approved layout/building plan ready to break ground",
            "Need funding across land, approvals or construction — not just one stage",
            "Project has clear title and RERA registration in progress or complete",
            "Looking for disbursal tied to construction milestones, not lump sum"
        ],
        "features": [
            ["01", "Milestone-linked disbursal", "Funds released in stages as construction progresses, reducing idle interest cost."],
            ["02", "RERA-aligned structuring", "Facility documentation built to align with RERA escrow requirements."],
            ["03", "Land + construction coverage", "Single relationship can span acquisition, approval costs and construction."],
            ["04", "Exit-linked repayment", "Repayment structured against projected unit sales/collections."]
        ],
        "process": [
            ["Project due diligence", "Title, approvals and developer track record verified."],
            ["Facility structuring", "Loan sized and staged against the construction timeline."],
            ["Sanction", "Terms finalised including escrow and milestone conditions."],
            ["Milestone disbursal", "Tranches released as each construction stage is certified complete."]
        ],
        "calcType": "emi",
        "calcDefaults": {"principal": 50000000, "rate": 13, "years": 5, "minP": 5000000, "maxP": 500000000, "minR": 11, "maxR": 16, "minY": 1, "maxY": 5},
        "reviews": {
            "rating": 4.5,
            "count": 33,
            "items": [
                ["Anil Chaudhary", "Ghaziabad", "Lump-sum disbursal would have meant paying interest on idle money before we broke ground. Milestone funding matched our actual spend."],
                ["Poonam Saxena", "Noida", "RERA escrow structuring was the one thing our previous lender didn't understand. This one did."],
                ["Rajat Bhargava", "Loni", "Title diligence flagged an encumbrance early — avoided a costly delay mid-project."]
            ]
        },
        "faqs": [
            ["Can this fund land acquisition before construction begins?", "Yes, though land-only funding typically carries a shorter tenure and stricter title requirements than construction-linked tranches."],
            ["How does RERA escrow affect disbursal?", "A portion of buyer collections must stay in a RERA-designated account for construction — we structure loan disbursal to work alongside this, not around it."],
            ["What if the project timeline slips?", "Milestone-linked facilities typically allow renegotiation of tranche timing — we flag this during structuring so it isn't a surprise mid-project."],
            ["Why is the rate higher than a property purchase loan?", "Construction finance carries higher execution risk than a purchase against a completed asset, which is reflected in the 11–16% pricing band versus 8.5–14% for purchase loans."]
        ]
    },
    {
        "id": "hospital-funding",
        "category": "Loans",
        "subcategory": "Sector-Specific Funding",
        "eyebrow": "Loans / Healthcare",
        "name": "Hospital Funding",
        "headline": "Capital for Beds, Equipment and Expansion",
        "sub": "Funding for hospital construction, medical equipment and working capital — sized against patient revenue and insurance receivables.",
        "tag": "#EquipYourNextExpansion",
        "stats": [["Up to ₹15Cr", "Loan size"], ["8.75% – 16% p.a.", "Interest rate*"], ["Up to 7 yrs", "Equipment tenure"]],
        "statNote": "*Banks ~8.25–9.5% for established hospitals with collateral; NBFCs 9–16%+ with faster turnaround.",
        "brief": [
            "Hospital funding sits at the intersection of infrastructure and equipment finance, since most facilities need both civil construction and high-value medical equipment financed together or in close sequence.",
            "Established multi-specialty hospitals with adequate collateral can access bank pricing around 8.25–9.5% per annum; NBFCs charge more (9–16%+) but process in 3–7 days versus 10–20 days for banks and often accept equipment hypothecation instead of additional property collateral.",
            "Because a meaningful share of hospital revenue is delayed through insurance and TPA settlement cycles, working capital facilities for healthcare providers are typically sized with that lag built in, rather than assuming immediate cash realisation."
        ],
        "whoIntro": "Fits registered clinical establishments financing equipment, bed capacity or both — not personal medical loans.",
        "whoSummary": [
            "Best for: hospitals/diagnostic centres adding equipment or bed capacity.",
            "Think twice if: you need funds faster than 3 days — bank-priced facilities take longer to sanction."
        ],
        "qualify": [
            "Setting up a new facility or adding bed capacity",
            "Purchasing high-value diagnostic or surgical equipment",
            "Managing receivables delays from insurance/TPA settlements",
            "Established practice looking to formalise into a larger facility"
        ],
        "features": [
            ["01", "Equipment-specific financing", "Dedicated lines for diagnostic, ICU and surgical equipment with vendor-direct payment."],
            ["02", "Receivables-aware structuring", "Working capital sized with insurance/TPA settlement delays factored in."],
            ["03", "Expansion + infra combined", "Single relationship spans new construction and equipment procurement."],
            ["04", "Licensing-stage support", "Documentation guidance for facilities still completing regulatory approvals."]
        ],
        "process": [
            ["Facility assessment", "Current capacity, licensing status and expansion plan reviewed."],
            ["Sizing", "Loan structured against equipment cost, construction estimate or both."],
            ["Sanction", "Terms finalised with vendor-direct payment for equipment tranches."],
            ["Disbursal", "Funds released to vendors/contractors per procurement or construction stage."]
        ],
        "calcType": "emi",
        "calcDefaults": {"principal": 7500000, "rate": 11, "years": 7, "minP": 1000000, "maxP": 150000000, "minR": 8.75, "maxR": 16, "minY": 1, "maxY": 7},
        "reviews": {
            "rating": 4.7,
            "count": 64,
            "items": [
                ["Dr. Alok Mehra", "Ghaziabad", "Needed a new MRI unit but our TPA receivables ran 60 days behind. The structure accounted for that lag from the start."],
                ["Dr. Shalini Bose", "Noida", "NBFC route took 5 days against the bank's 3-week estimate — worth the marginally higher rate."],
                ["Dr. Ramesh Iyer", "Sahibabad", "Equipment hypothecation instead of extra property collateral was the deciding factor for us."]
            ]
        },
        "faqs": [
            ["Can equipment and construction be financed under one facility?", "Yes, they're commonly combined, with separate tranches and vendor-direct payment for equipment."],
            ["Does TPA receivable delay affect loan eligibility?", "It's factored into working capital sizing rather than treated as a red flag — this is standard for the sector."],
            ["Is this available for diagnostic centres, not just full hospitals?", "Yes, diagnostic and specialty centres qualify under the same equipment and infrastructure lines."],
            ["Bank or NBFC — which should I choose?", "Banks are cheaper (8.25–9.5%) if you have collateral and can wait 2–3 weeks; NBFCs (9–16%) fund in days and accept equipment as security — we help you weigh the trade-off."]
        ]
    },
    {
        "id": "hotel-resort-funding",
        "category": "Loans",
        "subcategory": "Sector-Specific Funding",
        "eyebrow": "Loans / Hospitality",
        "name": "Hotel & Resort Funding",
        "headline": "Finance Built for Hospitality's Seasonal Cash Cycle",
        "sub": "Construction, renovation and working capital finance for hotels and resorts — structured around occupancy seasonality, not flat monthly EMIs.",
        "tag": "#SeasonalEMIsThatFlex",
        "stats": [["Up to 70%", "Of project cost financed*"], ["9% – 14% p.a.", "Interest rate"], ["Up to 12 yrs", "Tenure"]],
        "statNote": "*Excludes land cost. Banks typically price ~9–11%; NBFCs up to ~14% with faster turnaround.",
        "brief": [
            "Hospitality projects carry a cash flow pattern that standard term loans handle poorly — occupancy and revenue swing seasonally, so repayment structuring needs to flex accordingly rather than assume flat monthly income.",
            "Pricing generally runs 9–14% per annum — banks around 9–11% for well-collateralised projects, NBFCs up to 14% with materially faster approval — with construction finance covering up to 70% of project cost excluding land.",
            "Beyond room construction, hotels and resorts often need financing for banquet halls, F&B outlets and amenity infrastructure that drive non-room revenue — this is typically bundled into the same facility rather than financed separately."
        ],
        "whoIntro": "Fits hospitality operators whose revenue genuinely swings by season, not businesses wanting a generic construction loan.",
        "whoSummary": [
            "Best for: hotels/resorts needing EMIs that flex with occupancy season.",
            "Think twice if: your property has flat year-round demand — a standard term loan may be simpler."
        ],
        "qualify": [
            "Building a new property or renovating an existing hotel/resort",
            "Revenue is seasonal and a flat EMI schedule doesn't fit cash flow",
            "Need working capital to bridge low-occupancy months",
            "Expanding room inventory or adding banquet/F&B infrastructure"
        ],
        "features": [
            ["01", "Seasonality-matched EMIs", "Higher repayment in peak season, lower in off-season — not a flat schedule."],
            ["02", "Renovation + new-build coverage", "Applies equally to greenfield construction and existing property upgrades."],
            ["03", "F&B and banquet financing", "Covers ancillary revenue infrastructure, not just room inventory."],
            ["04", "Brand-tie-up consideration", "Loan terms can reflect projected revenue uplift from franchise/management tie-ups."]
        ],
        "process": [
            ["Property & market review", "Location, competing supply and occupancy potential assessed."],
            ["Project sizing", "Loan structured against construction/renovation cost and revenue projection."],
            ["Sanction", "Seasonal repayment schedule finalised against projected occupancy curve."],
            ["Phased disbursal", "Funds released against construction milestones or renovation stages."]
        ],
        "calcType": "emi",
        "calcDefaults": {"principal": 30000000, "rate": 11, "years": 10, "minP": 2500000, "maxP": 300000000, "minR": 9, "maxR": 14, "minY": 2, "maxY": 12},
        "reviews": {
            "rating": 4.6,
            "count": 29,
            "items": [
                ["Karan Bedi", "near Delhi NCR", "Our previous lender wanted the same EMI in July as December, despite occupancy swinging by half. This flexes with our season."],
                ["Nisha Kapoor", "Delhi NCR", "Banquet hall financing was bundled into the same facility — one relationship instead of two."],
                ["Farhan Sheikh", "Ghaziabad", "NBFC route closed in under two weeks; our bank was still asking for documents at that point."]
            ]
        },
        "faqs": [
            ["Can this fund renovation of an existing property, not just new builds?", "Yes — renovation financing follows the same seasonality-matched structuring as new construction."],
            ["How is the seasonal EMI schedule decided?", "Based on historical or projected occupancy data for the specific location and property category."],
            ["Does a management/franchise tie-up improve loan terms?", "It can — projected revenue uplift from an established brand affiliation is factored into sizing and pricing where relevant."],
            ["Why is NBFC pricing higher than bank pricing here?", "NBFCs price in the speed and flexibility they offer — often closing in under two weeks against 4–12 weeks for a bank, which matters for seasonal construction windows."]
        ]
    },
    {
        "id": "npa-funding",
        "category": "Loans",
        "subcategory": "Special Situation & Growth Capital",
        "eyebrow": "Loans / Stressed Assets",
        "name": "NPA Funding",
        "headline": "Resolve a Stressed Account Before It Escalates",
        "sub": "Structured refinancing and One-Time Settlement (OTS) support for businesses whose accounts have slipped into NPA — aimed at resolution, not just extension.",
        "tag": "#ResolutionNotJustExtension",
        "stats": [["5% – 10%", "Typical token payment*"], ["3 – 12 mo", "OTS settlement window"], ["Case-by-case", "Loan sizing"]],
        "statNote": "*Token payment made to the no-lien account to obtain an OTS letter and demonstrate settlement intent, per standard bank practice.",
        "brief": [
            "An NPA classification isn't necessarily the end of a lending relationship — many accounts are resolvable through a negotiated One-Time Settlement (OTS) or structured refinancing, provided the underlying business retains operational viability.",
            "In a typical OTS, the borrower proposes a settlement figure, pays a token amount — usually 5–10% of the proposed sum — into a no-lien account to obtain an OTS letter, and then settles within a window of roughly 3 months to a year depending on transaction size.",
            "This is deliberately the most case-specific product in our portfolio: every NPA situation carries a different history with the existing lender, which is why resolution strategy is built account-by-account rather than templated."
        ],
        "whoIntro": "For businesses with a genuine turnaround story, not accounts flagged for wilful default or fraud.",
        "whoSummary": [
            "Best for: viable businesses with an NPA-tagged account and a real repayment source.",
            "Not applicable if: the account involves wilful default or fraud — RBI guidelines exclude these from OTS."
        ],
        "qualify": [
            "Existing loan account classified as NPA or approaching classification",
            "Business is fundamentally viable but hit a temporary cash crunch",
            "Looking to negotiate a One-Time Settlement (OTS) with the current lender",
            "Need bridge funding to regularise an account before it escalates further"
        ],
        "features": [
            ["01", "OTS negotiation support", "We help structure and negotiate settlement terms with the existing lender."],
            ["02", "Bridge refinancing", "Fresh funding structured to clear or regularise the stressed account."],
            ["03", "Turnaround assessment", "Honest viability check before committing to a resolution path."],
            ["04", "New-lender onboarding", "Where viable, we identify lenders willing to take on a post-resolution account."]
        ],
        "process": [
            ["Account review", "We assess how the account slipped and what resolution path is realistic."],
            ["Resolution strategy", "OTS negotiation, refinancing, or a combination is proposed."],
            ["Lender engagement", "We coordinate directly with the existing lender on settlement terms."],
            ["Closure & fresh start", "Account regularised or settled; fresh credit access rebuilt where possible."]
        ],
        "calcType": "settlement",
        "calcDefaults": {"outstanding": 5000000, "settlePct": 60, "tokenPct": 8},
        "reviews": {
            "rating": 4.5,
            "count": 22,
            "items": [
                ["Suresh Nanda", "Ghaziabad", "Assumed once tagged NPA there was no way back. They negotiated an OTS that let us close the chapter and refinance."],
                ["Vandana Kapoor", "Sahibabad", "Honest about our chances before we spent a rupee — didn't oversell a resolution that wasn't realistic."],
                ["Mahesh Tandon", "Loni", "Direct coordination with the bank meant we weren't going back and forth ourselves."]
            ]
        },
        "faqs": [
            ["Can any NPA account be refinanced?", "Not every account is viable — we assess the underlying business honestly before proposing a path, rather than promising resolution upfront."],
            ["What is an OTS and how is it negotiated?", "A One-Time Settlement is a negotiated reduced payoff that closes the loan account. We represent the borrower in structuring and negotiating these terms with the existing lender."],
            ["Will this affect my CIBIL record?", "An OTS is typically reported as 'settled' rather than fully closed, which does affect credit history — we explain these trade-offs before you commit to a path."],
            ["How much of a token payment is usually required upfront?", "Typically 5–10% of the proposed settlement amount, paid into a no-lien account to obtain the OTS letter and demonstrate genuine intent."]
        ]
    },
    {
        "id": "infrastructure-funding",
        "category": "Loans",
        "subcategory": "Sector-Specific Funding",
        "eyebrow": "Loans / Infrastructure",
        "name": "Infrastructure Companies Funding",
        "headline": "Project and Working Capital Finance for Infrastructure Contractors",
        "sub": "Funding structured around EPC contracts, mobilisation needs and milestone billing cycles typical of infrastructure execution.",
        "tag": "#BuiltAroundYourBillingCycle",
        "stats": [["Up to ₹50Cr", "Project loan size"], ["10.5% – 15% p.a.", "Interest rate*"], ["Milestone-linked", "Disbursal & repayment"]],
        "statNote": "*Indicative EPC/infra project finance band; actual pricing depends on contract quality and client (govt/PSU/private).",
        "brief": [
            "Infrastructure contractors face a specific cash flow pattern: mobilisation costs are incurred upfront, billing happens at milestones, and client payment — especially from government and PSU clients — often lags well behind billing.",
            "Funding for this sector is structured around the project's actual execution and billing calendar rather than treated as a generic business loan, typically priced 10.5–15% per annum with mobilisation advances and milestone-linked working capital as the core components.",
            "Where relevant, we also support arranging the bid and performance bank guarantees required to participate in and execute tenders — a standard requirement infrastructure contractors face that general business lending doesn't address."
        ],
        "whoIntro": "For registered contractors executing or bidding EPC/infrastructure work, not general SME borrowers.",
        "whoSummary": [
            "Best for: EPC contractors with a signed work order and a billing-cycle cash gap.",
            "Think twice if: you lack a verifiable work order — most lenders require one before structuring."
        ],
        "qualify": [
            "Executing or bidding for EPC/infrastructure contracts",
            "Need mobilisation advance or equipment finance ahead of project start",
            "Cash flow gap between milestone billing and client payment realisation",
            "Government or PSU contracts with standard payment delays"
        ],
        "features": [
            ["01", "Mobilisation advance", "Upfront funding to cover site setup, equipment mobilisation and initial procurement."],
            ["02", "Bank guarantee facilitation", "Support in arranging performance and bid guarantees required for tenders."],
            ["03", "Milestone billing-linked WC", "Working capital sized against the project's billing schedule, not flat turnover."],
            ["04", "Equipment finance bundled", "Heavy machinery and equipment loans structured alongside project funding."]
        ],
        "process": [
            ["Contract review", "Work order terms, client payment history and project scope assessed."],
            ["Facility structuring", "Mobilisation advance, WC and equipment lines sized against the project plan."],
            ["Sanction", "Terms finalised, including any bank guarantee support required."],
            ["Milestone-linked release", "Funds and WC limits track the project's actual billing and execution stages."]
        ],
        "calcType": "emi",
        "calcDefaults": {"principal": 30000000, "rate": 13, "years": 5, "minP": 5000000, "maxP": 500000000, "minR": 10.5, "maxR": 15, "minY": 1, "maxY": 7},
        "reviews": {
            "rating": 4.4,
            "count": 19,
            "items": [
                ["Deepak Rawal", "NCR", "Government payment cycles run 90 days behind our billing. The working capital line was sized around that gap instead of ignoring it."],
                ["Sameer Khosla", "Ghaziabad", "Bank guarantee support for a tender we'd have otherwise skipped bidding on."],
                ["Vinod Sethi", "Noida", "Mobilisation advance meant we didn't dip into other project reserves to start site setup."]
            ]
        },
        "faqs": [
            ["What is a mobilisation advance?", "Upfront funding to cover initial site setup, equipment deployment and procurement before milestone billing begins generating cash inflow."],
            ["Can this help with bid or performance bank guarantees?", "Yes, we assist in arranging the guarantees typically required to participate in and execute tenders."],
            ["Does this apply to subcontractors, or only main EPC contractors?", "Both, provided there's a verifiable work order or contract establishing the scope and payment terms."],
            ["Why does government/PSU client payment take so long?", "Standard bill certification and treasury release cycles for government works commonly run 60–120 days — we size working capital facilities with this delay factored in rather than assuming prompt payment."]
        ]
    },
    {
        "id": "venture-funding",
        "category": "Loans",
        "subcategory": "Special Situation & Growth Capital",
        "eyebrow": "Equity / Growth Capital",
        "name": "Venture Funding",
        "headline": "Growth Capital for Businesses Ready to Scale",
        "sub": "Structured introductions to venture and growth-stage investors for businesses with a scalable model and a clear use of capital.",
        "tag": "#EquityNotEMI",
        "stats": [["₹4Cr – ₹15Cr", "Typical seed raise"], ["15% – 25%", "Typical dilution"], ["Seed – Series B", "Stages covered"]],
        "statNote": "India seed/Series A benchmarks; actual raise size and dilution depend on traction, sector and investor demand.",
        "brief": [
            "Venture funding is fundamentally different from our lending products — it's equity capital in exchange for ownership, aimed at businesses whose growth trajectory justifies dilution rather than debt servicing.",
            "Indian seed rounds typically raise ₹4–15 crore (most commonly ₹7–8 crore) at 15–25% dilution; Series A rounds run considerably larger — commonly $10–25 million — at a broadly similar 18–25% dilution band.",
            "Our role here is advisory and introduction-based: preparing a business to be investor-ready, curating relevant investor introductions, and supporting negotiation through to a closed term sheet."
        ],
        "whoIntro": "For companies with real traction seeking growth capital, not idea-stage concepts.",
        "whoSummary": [
            "Best for: Pvt Ltd companies with traction, raising seed through Series B.",
            "Not applicable if: you want to retain full ownership — this route requires equity dilution."
        ],
        "qualify": [
            "Scalable business model with demonstrable traction",
            "Raising capital for growth, not just working capital",
            "Need investor introductions, not just loan-based funding",
            "Ready for equity dilution in exchange for growth capital"
        ],
        "features": [
            ["01", "Investor matchmaking", "Introductions curated to funds actively investing in your sector and stage."],
            ["02", "Pitch & data-room prep", "Support structuring the pitch deck, financial model and data room."],
            ["03", "Valuation guidance", "Realistic valuation benchmarking against comparable recent rounds."],
            ["04", "Term sheet negotiation", "Support reviewing and negotiating investor term sheets before signing."]
        ],
        "process": [
            ["Readiness assessment", "Business model, traction and materials reviewed for investor readiness."],
            ["Materials preparation", "Pitch deck, financial model and data room built or refined."],
            ["Investor outreach", "Curated introductions made to funds matching sector and stage."],
            ["Term sheet to close", "Support through negotiation, due diligence and final documentation."]
        ],
        "calcType": "dilution",
        "calcDefaults": {"raise": 70000000, "preMoney": 200000000},
        "reviews": {
            "rating": 4.8,
            "count": 17,
            "items": [
                ["Aditya Rao", "Delhi NCR (B2B SaaS)", "Strong product but a weak pitch deck. Their prep work was the difference between polite rejections and a term sheet."],
                ["Neha Chandran", "Gurugram (D2C)", "Valuation guidance kept us from underselling the round — closed 20% above our first draft ask."],
                ["Ishaan Kohli", "Noida (Fintech)", "Investor introductions were genuinely relevant to our stage, not a generic mass email list."]
            ]
        },
        "faqs": [
            ["How is this different from a business loan?", "A loan is debt that must be repaid with interest; venture funding is equity capital exchanged for ownership stake, with no fixed repayment obligation."],
            ["What stage of business is eligible?", "Primarily seed through Series B — businesses with some traction and a credible growth story, rather than pure idea-stage concepts."],
            ["Do you charge success fees on the raise?", "Fee structures are discussed upfront during the readiness assessment, before any investor outreach begins."],
            ["What's typical dilution at seed vs Series A?", "Both bands run broadly similar in India — roughly 15–25% at seed and 18–25% at Series A — though the absolute cheque size is materially larger at Series A."]
        ]
    },
    {
        "id": "valuation-services",
        "category": "Equity",
        "subcategory": "Advisory & Valuation",
        "eyebrow": "Equity / Advisory",
        "name": "Valuation Services",
        "headline": "Defensible Valuations for Every Statutory Purpose",
        "sub": "Registered Valuer and SEBI Merchant Banker reports for share issuance, ESOPs, M&A and FEMA pricing — matched to the right method and the right professional.",
        "tag": "#TheRightNumberOnPaper",
        "stats": [["₹25k – ₹2L+", "Fee range*"], ["4 – 8 business days", "Turnaround"], ["DCF / NAV / Market", "Methods applied"]],
        "statNote": "*Single-purpose Registered Valuer reports from ~₹25,000; Merchant Banker DCF reports from ~₹65,000; multi-framework engagements (Companies Act + FEMA + Income Tax together) can run ₹2,00,000+.",
        "brief": [
            "Not every valuation need calls for the same professional or method — Companies Act and IBC valuations require an IBBI Registered Valuer, Income Tax Rule 11UA valuations need a SEBI-registered Merchant Banker for the DCF route (or a Chartered Accountant for NAV), and FEMA pricing for foreign investment accepts either a Merchant Banker or a practising CA.",
            "Getting this match wrong is the single most common reason a valuation report gets rejected by a regulator or auditor — so we start by identifying the exact statutory purpose before assigning the professional and method.",
            "Under IBBI valuation standards, three approaches — Income, Market and Asset — must all be considered for a defensible report, even where one method ultimately drives the concluded value. For ESOP perquisite tax purposes specifically, the Merchant Banker FMV certificate must be dated within 180 days of exercise."
        ],
        "whoIntro": "For any transaction or filing that requires a certified, regulator-ready value on a business or its shares.",
        "whoSummary": [
            "Best for: share issuance at premium, ESOP FMV, M&A, FEMA pricing, succession planning.",
            "Think twice if: you only need an informal indicative number — a lighter internal estimate may suffice."
        ],
        "qualify": [
            "Issuing shares at a premium and need a Section 56(2)(viib)-compliant valuation",
            "Setting or revising ESOP strike price and need a certified FMV",
            "Structuring an M&A, buyback or family settlement requiring a fairness opinion",
            "Receiving foreign investment and need FEMA-compliant pricing"
        ],
        "features": [
            ["01", "Purpose-matched professional", "Registered Valuer, Merchant Banker or CA — assigned to what the filing actually requires."],
            ["02", "Multi-framework reports", "One engagement can satisfy Companies Act, FEMA and Income Tax requirements together."],
            ["03", "IBBI three-approach standard", "Income, Market and Asset approaches considered for a defensible conclusion."],
            ["04", "ESOP-ready certification", "FMV certificates issued within the 180-day validity window exercise requires."]
        ],
        "process": [
            ["Purpose identification", "We confirm exactly which regulator/filing the valuation must satisfy."],
            ["Professional assignment", "Registered Valuer, Merchant Banker or CA engaged per the applicable rule."],
            ["Data & financials collection", "Financials, cap table and business data compiled for analysis."],
            ["Valuation & report", "DCF/NAV/market approaches applied; report issued in the required format."]
        ],
        "calcType": "valuation",
        "calcDefaults": {"ebitda": 15000000, "multipleLow": 6, "multipleHigh": 10},
        "reviews": {
            "rating": 4.7,
            "count": 38,
            "items": [
                ["Rohit Sablani", "Ghaziabad", "Needed both a Companies Act and a FEMA valuation for the same funding round — one engagement covered both."],
                ["Priyanka Dass", "Noida", "ESOP FMV certificate came in well within the 180-day window our auditor needed."],
                ["Gurpreet Anand", "Delhi NCR", "First valuation firm that explained why we need a Merchant Banker and not just a CA."]
            ]
        },
        "faqs": [
            ["Do I need a Registered Valuer or a Merchant Banker?", "It depends on the filing: Companies Act/IBC needs an IBBI Registered Valuer; Income Tax Rule 11UA DCF valuations need a SEBI Merchant Banker; FEMA pricing accepts either a Merchant Banker or a CA."],
            ["How long is a valuation report valid for?", "Validity depends on the purpose — ESOP FMV certificates must be within 180 days of exercise; other reports are typically used within the same financial year or transaction window."],
            ["Can one report cover multiple statutory purposes?", "Yes, a multi-framework report can address Companies Act, FEMA and Income Tax requirements together, which is usually more cost-efficient than three separate engagements."],
            ["What information do I need to provide?", "Audited financials, cap table, business projections and details of the transaction the valuation supports — we provide a checklist upfront."]
        ]
    },
    {
        "id": "pre-ipo-funding",
        "category": "Equity",
        "subcategory": "Public Market Readiness",
        "eyebrow": "Equity / Growth Capital",
        "name": "Pre-IPO Funding",
        "headline": "Bridge Capital for the Last Mile Before Listing",
        "sub": "Structured mezzanine and pre-IPO capital for companies 6 months to 2 years from a listing, from PE funds, family offices and HNIs.",
        "tag": "#TheRunwayBeforeTheBell",
        "stats": [["6 mo – 2 yrs", "Window before listing"], ["CCD / OCD / Pref", "Common instruments"], ["PE / Family / HNI", "Investor base"]],
        "statNote": "Pre-IPO rounds are privately negotiated; pricing and structure vary by company stage, sector and investor appetite.",
        "brief": [
            "A pre-IPO investment is late-stage capital raised roughly six months to two years before a listing, aimed at strengthening the balance sheet, funding expansion and tightening corporate governance ahead of public-market scrutiny.",
            "These rounds are typically structured as private placements, secondary share sales, or instruments like compulsorily/optionally convertible debentures and preference shares — often carrying warrants that let the investor convert to equity on defined milestones.",
            "Investors at this stage are usually private equity funds, family offices and high-net-worth individuals seeking exposure to a company nearing a liquidity event, rather than early-stage venture funds."
        ],
        "whoIntro": "For companies with a credible listing timeline that need capital or governance runway to get there.",
        "whoSummary": [
            "Best for: companies 6–24 months from a realistic IPO, needing balance sheet or governance strengthening.",
            "Think twice if: your listing timeline is beyond 2 years — venture or growth equity may fit better."
        ],
        "qualify": [
            "Targeting an IPO within the next 6–24 months",
            "Need capital to strengthen the balance sheet ahead of listing",
            "Corporate governance or board structure needs tightening before scrutiny",
            "Want investor introductions to PE funds, family offices or HNIs specifically"
        ],
        "features": [
            ["01", "Listing-stage investor access", "Introductions to PE funds, family offices and HNIs focused on pre-IPO stage."],
            ["02", "Instrument structuring", "CCDs, OCDs and preference shares structured to fit your cap table and timeline."],
            ["03", "Governance readiness", "Support tightening board composition and compliance ahead of public scrutiny."],
            ["04", "Valuation continuity", "Round pricing benchmarked to support, not undercut, your eventual IPO pricing."]
        ],
        "process": [
            ["Listing-readiness assessment", "Governance, financials and timeline reviewed against IPO-readiness benchmarks."],
            ["Instrument structuring", "Appropriate instrument (CCD/OCD/preference shares) proposed for the raise."],
            ["Investor outreach", "Curated introductions to PE, family office and HNI investors."],
            ["Negotiation & close", "Support through term sheet negotiation, due diligence and closing."]
        ],
        "calcType": "dilution",
        "calcDefaults": {"raise": 150000000, "preMoney": 600000000},
        "reviews": {
            "rating": 4.6,
            "count": 14,
            "items": [
                ["Vivek Chhabra", "Delhi NCR (Manufacturing)", "We were 18 months from listing and needed governance fixes as much as capital — they helped with both."],
                ["Alka Nair", "Gurugram (Healthcare)", "Instrument structuring meant the round didn't complicate our cap table ahead of the DRHP."],
                ["Tarun Wadhwa", "Noida (Consumer)", "Investor introductions were genuinely pre-IPO-stage investors, not generic growth VCs."]
            ]
        },
        "faqs": [
            ["How is pre-IPO funding different from a regular equity round?", "It's specifically timed and structured around an upcoming listing — instruments and investor base are chosen to support IPO governance and valuation continuity, not just growth capital."],
            ["What instruments are typically used?", "Compulsorily or optionally convertible debentures and preference shares are common, often with conversion triggers tied to listing milestones."],
            ["Who typically invests at this stage?", "Private equity funds, family offices and high-net-worth individuals seeking exposure to a near-term liquidity event."],
            ["Does this delay or complicate the eventual IPO?", "Not if structured correctly — we benchmark round pricing and instrument terms to support rather than conflict with your IPO valuation and cap table."]
        ]
    },
    {
        "id": "sme-ipo",
        "category": "Equity",
        "subcategory": "Public Market Readiness",
        "eyebrow": "Equity / Public Markets",
        "name": "SME IPO",
        "headline": "List on BSE SME or NSE Emerge — Built for Growing Businesses",
        "sub": "A lighter-compliance route to public markets for companies with post-issue paid-up capital up to ₹25 crore and a 3-year track record.",
        "tag": "#PublicWithoutTheMainboardWeight",
        "stats": [["≤ ₹25Cr", "Post-issue capital cap"], ["3+ years", "Track record required"], ["4 – 6 months", "Listing timeline"]],
        "statNote": "Per BSE SME / NSE Emerge norms: net worth >=₹1Cr in each of the last 2 years, EBITDA-positive in 2 of the last 3 years, min. 20% promoter contribution.",
        "brief": [
            "BSE SME and NSE Emerge are purpose-built platforms letting smaller companies access public markets without meeting the stricter, costlier mainboard rules — post-issue paid-up capital must not exceed ₹25 crore, with net worth of at least ₹1 crore in each of the preceding two years.",
            "Profitability isn't mandatory, but the company must show operating profit (EBITDA) in at least 2 of the last 3 financial years, backed by 3 years of audited financials that feed directly into the Draft Red Herring Prospectus (DRHP).",
            "The listing process — DRHP filing, exchange review, a site inspection of company facilities, and appearance before the Listing Advisory Committee — typically runs 4–6 months from mandate to listing, with a minimum 20% promoter contribution held in demat form."
        ],
        "whoIntro": "For established SMEs ready for public market discipline without mainboard-scale requirements.",
        "whoSummary": [
            "Best for: companies with 3+ years' track record and post-issue capital under ₹25Cr.",
            "Think twice if: you have pending IBC proceedings or promoter defaults — these disqualify SME listing."
        ],
        "qualify": [
            "Company or promoter with at least 3 years of operating track record",
            "Post-issue paid-up capital fits within the ₹25 crore SME threshold",
            "EBITDA-positive in at least 2 of the last 3 financial years",
            "No pending defaults or IBC proceedings against the company"
        ],
        "features": [
            ["01", "Platform eligibility mapping", "Assessment of BSE SME vs NSE Emerge fit based on your financials and structure."],
            ["02", "DRHP drafting support", "Coordination with merchant banker on prospectus drafting and SEBI-format compliance."],
            ["03", "Exchange process coordination", "Support through site inspection and Listing Advisory Committee presentation."],
            ["04", "Market maker & underwriting coordination", "Arrangement of mandatory market making and underwriting for the issue."]
        ],
        "process": [
            ["Eligibility & platform assessment", "Financials and structure reviewed against BSE SME / NSE Emerge criteria."],
            ["DRHP drafting & filing", "Merchant banker drafts the DRHP; filed with the chosen exchange."],
            ["Exchange review", "Site inspection and promoter interaction before the Listing Advisory Committee."],
            ["Price band & subscription", "In-principle approval received; issue opens for subscription."],
            ["Listing", "Shares allotted and the company lists on BSE SME or NSE Emerge."]
        ],
        "calcType": "ipo",
        "calcDefaults": {"raise": 80000000, "preMoney": 250000000},
        "reviews": {
            "rating": 4.5,
            "count": 21,
            "items": [
                ["Yogesh Kohli", "Ghaziabad (Auto)", "Site inspection and Listing Advisory Committee stage felt daunting until they walked us through exactly what would be asked."],
                ["Simran Oberoi", "Noida (FMCG)", "Went from mandate to listing in just under 5 months — on the timeline we were quoted."],
                ["Naresh Bhatia", "Sahibabad", "Platform assessment correctly steered us to NSE Emerge over BSE SME for our sector."]
            ]
        },
        "faqs": [
            ["What's the difference between BSE SME and NSE Emerge?", "Both are SME-focused platforms with similar eligibility norms; the choice often comes down to sector fit, market maker arrangements and merchant banker relationships — we assess both before recommending one."],
            ["Does my company need to be profitable to list?", "No, profitability isn't mandatory, but EBITDA-positive results in at least 2 of the last 3 financial years are required."],
            ["What is the Listing Advisory Committee?", "An exchange committee that reviews the DRHP, conducts a site inspection and interacts with promoters before granting in-principle listing approval."],
            ["Can an SME-listed company migrate to the mainboard later?", "Yes, companies that outgrow SME thresholds and meet mainboard eligibility criteria can migrate to NSE/BSE mainboard listing."]
        ]
    },
    {
        "id": "main-board-ipo",
        "category": "Equity",
        "subcategory": "Public Market Readiness",
        "eyebrow": "Equity / Public Markets",
        "name": "Main Board IPO",
        "headline": "Take Your Company to NSE and BSE Mainboard",
        "sub": "End-to-end support for large, established companies meeting SEBI's profitability or QIB-route eligibility for a mainboard listing.",
        "tag": "#ReadyForTheMainboard",
        "stats": [["₹10Cr+", "Minimum paid-up capital"], ["₹15Cr", "Avg. operating profit needed*"], ["75% to QIBs", "Under alternate QIB route"]],
        "statNote": "*Profitability route: tangible assets >=₹3Cr and operating profit >=₹15Cr in 3 of last 5 years. Book-built QIB route available if this isn't met.",
        "brief": [
            "A Main Board IPO is reserved for large, established companies — under the standard profitability route, net tangible assets must be at least ₹3 crore in each of the last three years, with average operating profit of at least ₹15 crore in three of the last five years, and net worth exceeding ₹10 crore in each of the preceding three years.",
            "Companies that don't meet this profitability threshold can still list via the book-building QIB route, which requires allocating at least 75% of the net issue to Qualified Institutional Buyers, whose participation itself signals institutional confidence in the offer.",
            "The process runs through a SEBI-registered merchant banker: DRHP filing with SEBI, a formal review and observation cycle, price-band finalisation, book-building and subscription, followed by allotment and listing on NSE and BSE."
        ],
        "whoIntro": "For large, established companies with either a strong 3-5 year profitability record or institutional-grade investor appeal.",
        "whoSummary": [
            "Best for: companies meeting the ₹3Cr/₹15Cr/₹10Cr profitability thresholds, or able to anchor 75% QIB demand.",
            "Think twice if: you're closer to SME-scale — the SME IPO route is faster and less compliance-heavy."
        ],
        "qualify": [
            "Net tangible assets of at least ₹3 crore in each of the last 3 years",
            "Average operating profit of at least ₹15 crore across 3 of the last 5 years",
            "Net worth exceeding ₹10 crore in each of the last 3 preceding years",
            "No debarment against promoters/directors by SEBI or other regulators"
        ],
        "features": [
            ["01", "Dual-route eligibility check", "Assessment of both the profitability route and the QIB book-building route."],
            ["02", "Merchant banker coordination", "End-to-end coordination with lead managers, underwriters and registrars."],
            ["03", "SEBI DRHP observations", "Support through SEBI's review and observation cycle on the draft prospectus."],
            ["04", "Roadshow coordination", "Support structuring investor roadshows ahead of the book-building window."]
        ],
        "process": [
            ["Eligibility assessment", "Financials tested against the profitability route and QIB alternate route."],
            ["Merchant banker & DRHP", "Lead manager appointed; DRHP drafted and filed with SEBI."],
            ["SEBI review observations", "SEBI's observations addressed and the prospectus finalised."],
            ["Book-building & subscription", "Price band set; issue opens for QIB, HNI and retail subscription."],
            ["Allotment & listing", "Shares allotted and the company lists on NSE and BSE mainboard."]
        ],
        "calcType": "ipo",
        "calcDefaults": {"raise": 500000000, "preMoney": 2000000000},
        "reviews": {
            "rating": 4.8,
            "count": 11,
            "items": [
                ["Arvind Kathpalia", "Delhi NCR", "SEBI's observation cycle had two rounds of queries — having someone who'd seen this before saved weeks."],
                ["Meenal Sarin", "Noida", "Dual-route assessment showed us the QIB path was realistic even before we hit the standard profitability numbers."],
                ["Col. R.S. Bakshi", "Ghaziabad", "Roadshow coordination brought in institutional interest we wouldn't have reached on our own."]
            ]
        },
        "faqs": [
            ["What if my company doesn't meet the profitability thresholds?", "You may still qualify via the QIB book-building route, which requires at least 75% of the net issue to be allocated to Qualified Institutional Buyers instead of meeting the standard profitability test."],
            ["How long does SEBI's review of the DRHP typically take?", "This varies by case and the number of observation rounds SEBI raises; we help prepare a DRHP designed to minimise back-and-forth."],
            ["What's the difference between an SME IPO and a Main Board IPO for a company at the threshold?", "Main Board carries materially higher profitability and net worth thresholds and heavier compliance, but offers broader investor access and liquidity than the SME platforms."],
            ["Who are the key parties involved besides the merchant banker?", "Underwriters, registrars, legal counsel and often a syndicate of banks for larger issues — we help coordinate the full syndicate."]
        ]
    },
    {
        "id": "up-tus-scheme",
        "category": "Incentives",
        "subcategory": "Uttar Pradesh Government Incentives",
        "eyebrow": "Incentives / UP Government",
        "name": "UP Govt Technical Upgradation Support (TUS) Scheme",
        "headline": "Subsidised Machinery Upgrades & Certification for UP MSMEs",
        "sub": "Up to ₹15 lakh in state subsidy for machinery, equipment and quality-certification costs — with a further 15% for green and women-led units.",
        "tag": "#UpgradeOnTheStatesRupee",
        "stats": [["₹7.5L micro / ₹15L small", "Maximum subsidy"], ["+15%", "Green / women bonus"], ["3+ years", "Minimum unit age"]],
        "statNote": "Per Uttar Pradesh's Technical Upgradation Support Scheme, administered via the District Industries and Enterprise Promotion Centre (DIEPC).",
        "brief": [
            "The Technical Upgradation Support (TUS) Scheme gives operational micro and small units in Uttar Pradesh direct financial support to buy machinery and equipment or fund quality-improvement interventions — including BIS, FSSAI and management-system certification costs.",
            "Subsidy is capped at ₹7.5 lakh for micro units and ₹15 lakh for small units when applying for multiple items under the scheme, with an additional 15% subsidy layered on for units adopting green solutions — solar, renewable energy, retrofitted devices — or owned by women entrepreneurs.",
            "Applications are processed first-come-first-served through the DIEPC, reviewed by a district-level technical committee and approved by a state-level committee — which makes application timing genuinely material to whether funds are still available."
        ],
        "whoIntro": "For operational micro/small units in UP upgrading machinery or pursuing quality certification, not new units still setting up.",
        "whoSummary": [
            "Best for: micro/small units, 3+ years old, investing in machinery or certification (BIS/FSSAI/ISO).",
            "Not eligible if: you've already received a grant under the UP Industrial Investment Policy 2017 or another state/central scheme for the same purpose."
        ],
        "qualify": [
            "Micro or small unit that has been operational for at least 3 years",
            "Planning to purchase machinery/equipment or pursue quality certification",
            "Have not already received a grant under UP's 2017 industrial policy or a similar scheme",
            "Willing to apply promptly — allocation is first-come-first-served"
        ],
        "features": [
            ["01", "Machinery & equipment subsidy", "Direct support toward the cost of new machinery and equipment purchases."],
            ["02", "Certification cost coverage", "BIS, FSSAI, ISO and management-system certification costs included."],
            ["03", "Green & women-owned bonus", "An additional 15% subsidy for solar/renewable adoption or women-led units."],
            ["04", "Two-tier committee review", "District technical committee plus state-level approval for transparency."]
        ],
        "process": [
            ["Eligibility check", "Unit age, prior grants and planned expenditure verified against scheme rules."],
            ["Application filing", "Online application submitted to the District Industries and Enterprise Promotion Centre."],
            ["District technical review", "District-level technical committee examines the application."],
            ["State approval & disbursal", "State committee approves and the subsidy is disbursed to the unit."]
        ],
        "calcType": "subsidy",
        "calcDefaults": {"cost": 2000000, "rate": 20, "cap": 1500000, "capLabel": "₹15L (small unit cap)"},
        "reviews": {
            "rating": 4.5,
            "count": 26,
            "items": [
                ["Om Prakash Yadav", "Ghaziabad", "Filed within the first week of the window opening — got the full small-unit cap approved."],
                ["Farah Ansari", "Loni", "The green-solution bonus on our solar-linked upgrade wasn't something our accountant even knew existed."],
                ["Devendra Chauhan", "Modinagar", "BIS certification cost being covered under the same subsidy was a pleasant surprise."]
            ]
        },
        "faqs": [
            ["Is this scheme only for buying machinery?", "No — it also covers quality-improvement interventions like BIS, FSSAI and management-system certification, not just equipment purchase."],
            ["What does 'first come first serve' actually mean in practice?", "Applications are processed in the order received once the window opens; once the district/state allocation is exhausted, later applications may not be funded in that cycle — timing your application matters."],
            ["Can a unit that already received a UP 2017 policy grant apply for TUS?", "No, units that have already received benefits under the UP Industrial Investment and Employment Promotion Policy 2017 or a similar scheme are not eligible."],
            ["How is the green/women-owned bonus applied?", "It's an additional 15% subsidy layered on top of the standard TUS support, for units adopting green/renewable solutions or owned by women entrepreneurs."]
        ]
    },
    {
        "id": "up-msme-scheme",
        "category": "Incentives",
        "subcategory": "Uttar Pradesh Government Incentives",
        "eyebrow": "Incentives / UP Government",
        "name": "UP Govt MSME Promotion Policy Scheme",
        "headline": "Capital Subsidy, Stamp Duty & Interest Relief for New UP MSMEs",
        "sub": "Up to 25% capital subsidy, up to 100% stamp duty exemption and 5-year interest subvention for new MSME units under UP's 2022 policy.",
        "tag": "#TheStateSharesTheSetupCost",
        "stats": [["10% – 25%", "Capital subsidy (region-based)"], ["Up to 100%", "Stamp duty exemption*"], ["50% – 60%", "Interest subvention, 5 years"]],
        "statNote": "*100% in Purvanchal/Bundelkhand, 75% in Madhyanchal/Paschimanchal, 50% in Gautam Buddh Nagar & Ghaziabad — 100% for women entrepreneurs statewide. Per UP MSME Promotion Policy 2022.",
        "brief": [
            "Under the UP Micro, Small and Medium Enterprises Promotion Policy 2022, new MSME units get a capital subsidy of 10–25% depending on region — Bundelkhand and Purvanchal sit at the higher 15–25% band, while central and western UP (including the NCR-adjacent districts) are set at 10–20%, capped at ₹4 crore per unit, with a further 2% for SC/ST and women entrepreneurs.",
            "Stamp duty exemption follows the same regional logic: 100% in Purvanchal and Bundelkhand, 75% in Madhyanchal and Paschimanchal, but only 50% in Gautam Buddh Nagar and Ghaziabad specifically — women entrepreneurs get 100% exemption anywhere in the state regardless of region.",
            "New micro units also qualify for interest subvention of 50% on their loan's annual interest (60% for SC/ST and women entrepreneurs) for 5 years, capped at ₹25 lakh per unit, alongside a 7-year infrastructure interest subsidy for eligible projects."
        ],
        "whoIntro": "For new MSME units being set up in UP — the benefit size depends materially on which region you're setting up in.",
        "whoSummary": [
            "Best for: new units in Purvanchal/Bundelkhand (highest subsidy tier) or any women-led unit statewide.",
            "Note: Ghaziabad and Gautam Buddh Nagar units get a reduced 50% stamp duty exemption versus 100% elsewhere."
        ],
        "qualify": [
            "Setting up a new micro, small or medium enterprise in Uttar Pradesh",
            "Want capital subsidy, stamp duty relief or interest subvention — or a combination",
            "Fall under SC/ST or women-entrepreneur categories for enhanced benefits",
            "Need infrastructure interest subsidy support for a new project"
        ],
        "features": [
            ["01", "Region-tiered capital subsidy", "10–25% subsidy on project cost, capped at ₹4Cr, based on district."],
            ["02", "Stamp duty exemption", "Up to 100% exemption on land/property registration, region-dependent."],
            ["03", "5-year interest subvention", "50–60% discount on annual loan interest, capped at ₹25L per unit."],
            ["04", "7-year infra interest subsidy", "Extended interest relief for eligible infrastructure investment."]
        ],
        "process": [
            ["Policy fit assessment", "Region, category (general/SC-ST/women) and project cost mapped to applicable benefit tiers."],
            ["Application via single window", "Application filed through Invest UP / Nivesh Mitra single-window portal."],
            ["Document verification", "Project and eligibility documents verified by the district authority."],
            ["Sanction & disbursal", "Capital subsidy, stamp duty relief and/or interest subvention sanctioned and released."]
        ],
        "calcType": "subsidy",
        "calcDefaults": {"cost": 20000000, "rate": 15, "cap": 4000000, "capLabel": "₹4Cr per-unit cap"},
        "reviews": {
            "rating": 4.6,
            "count": 33,
            "items": [
                ["Shalini Verma", "Ghaziabad", "Knew about the capital subsidy but had no idea our district only got 50% stamp duty relief until they explained the regional split."],
                ["Irfan Qureshi", "Prayagraj", "Full 25% capital subsidy plus 100% stamp duty exemption — the Purvanchal tier made a real difference to our setup cost."],
                ["Kavita Chaturvedi", "Jhansi", "Interest subvention as a woman entrepreneur brought our effective rate down substantially for the first 5 years."]
            ]
        },
        "faqs": [
            ["Why does my subsidy depend on which district I'm in?", "The policy deliberately tiers benefits higher in less-industrialised regions (Purvanchal, Bundelkhand) to encourage investment there, versus already-developed NCR-adjacent districts like Ghaziabad and Gautam Buddh Nagar."],
            ["Can I combine capital subsidy, stamp duty exemption and interest subvention?", "Yes, these are separate benefit heads under the same policy and can typically be availed together, subject to each head's own eligibility and caps."],
            ["Is the 100% stamp duty exemption for women available everywhere, including Ghaziabad?", "Yes — the policy grants 100% stamp duty exemption to women entrepreneurs statewide, overriding the lower regional tier that would otherwise apply."],
            ["How long does the interest subvention last?", "5 years for the standard capital interest subvention on new micro units (up to ₹25 lakh per unit), and 7 years for the separate infrastructure interest subsidy where applicable."]
        ]
    },
    {
        "id": "up-msmy-scheme",
        "category": "Incentives",
        "subcategory": "Uttar Pradesh Government Incentives",
        "eyebrow": "Incentives / UP Government",
        "name": "UP Govt MSMY (Mukhyamantri Yuva Swarozgar Yojana)",
        "headline": "Collateral-Free Startup Capital for UP's Educated Youth",
        "sub": "Margin-money grant and interest support to help educated unemployed youth in Uttar Pradesh set up their first enterprise.",
        "tag": "#YourFirstUnitStartsHere",
        "stats": [["Up to ₹5L", "Loan, largely interest-free*"], ["10%", "Margin money subsidy"], ["Collateral-free", "Security requirement"]],
        "statNote": "*Reflects CM-YUVA alignment; SC/ST and women applicants receive enhanced margin-money and interest support.",
        "brief": [
            "Mukhyamantri Yuva Swarozgar Yojana (MYSY) was created to give Uttar Pradesh's educated but unemployed youth a route into self-employment in the industry and service sectors, through a margin-money grant and interest support rather than a standard commercial loan.",
            "In its current operating form — aligned with the state's broader CM-YUVA push — eligible applicants can access collateral-free financing up to ₹5 lakh with a 10% margin-money subsidy on total project cost, removing the two biggest barriers first-time entrepreneurs face: security and upfront equity.",
            "Special provisions apply for SC/ST and women applicants, who receive enhanced margin-money and interest support beyond the standard terms — reflecting the scheme's explicit focus on widening access to first-generation entrepreneurship."
        ],
        "whoIntro": "For educated, currently-unemployed individuals in UP setting up their very first enterprise — not an expansion or working-capital product.",
        "whoSummary": [
            "Best for: first-time entrepreneurs, educated and unemployed, setting up a new micro-enterprise in UP.",
            "Not applicable if: you're expanding an existing running business — this scheme targets new-unit formation."
        ],
        "qualify": [
            "Educated but currently unemployed resident of Uttar Pradesh",
            "Setting up a new enterprise in the industry or service sector",
            "Have a workable business plan for a first-time venture",
            "Fall under SC/ST or women categories for enhanced scheme benefits"
        ],
        "features": [
            ["01", "Collateral-free financing", "Up to ₹5 lakh in financing without pledging security."],
            ["02", "Margin-money subsidy", "10% of total project cost covered as a subsidy, reducing promoter contribution."],
            ["03", "SC/ST & women enhancements", "Additional margin-money and interest support for eligible categories."],
            ["04", "Business-plan support", "Guidance structuring a bankable plan before the district committee review."]
        ],
        "process": [
            ["Eligibility & plan preparation", "Applicant eligibility confirmed and a business plan drafted for review."],
            ["Online application", "Application submitted via the UP MSME/self-employment portal."],
            ["District committee screening", "District-level committee reviews the plan and applicant eligibility."],
            ["Bank sanction & disbursal", "Empanelled bank sanctions financing; margin-money subsidy credited alongside."]
        ],
        "calcType": "subsidy",
        "calcDefaults": {"cost": 500000, "rate": 10, "cap": 50000, "capLabel": "10% margin-money on a ₹5L project"},
        "reviews": {
            "rating": 4.4,
            "count": 19,
            "items": [
                ["Mohd. Salman", "Ghaziabad", "Collateral-free was the deciding factor — I had zero assets to pledge as a first-time applicant."],
                ["Pooja Rawat", "Modinagar", "Margin-money subsidy meant I didn't need to arrange the full promoter contribution myself."],
                ["Anjali Sirohi", "Loni", "Business plan support before the district committee review made the difference between rejection and approval."]
            ]
        },
        "faqs": [
            ["Who exactly counts as 'educated unemployed youth' for this scheme?", "Eligibility is based on educational qualification and current unemployment status at the time of application — exact age and qualification bands are confirmed during the eligibility check, as they're periodically revised."],
            ["Is this only for men, or can women apply too?", "Women are explicitly eligible, with enhanced margin-money and interest support built into the scheme's special provisions."],
            ["Can I use this to expand an existing business?", "No — this scheme is specifically for setting up a new enterprise, not for working capital or expansion of an already-running unit."],
            ["What happens after the district committee approves my plan?", "An empanelled bank sanctions the financing and the margin-money subsidy is credited alongside disbursal, per the scheme's process."]
        ]
    }
]

# 2. DEFINE GLYPHS FOR ADVISORY bluePRINT VISUALS
GLYPHS = {
    "loans-cat": '<circle cx="100" cy="100" r="42"/><path d="M100 66a34 34 0 1 1-24 10"/><path d="M76 76l0-14 14 4" fill="none"/><text x="100" y="112" font-size="34" fill="#E4C878" stroke="none" text-anchor="middle" font-family="ui-monospace">₹</text>',
    "equity-cat": '<circle cx="100" cy="100" r="44"/><line x1="100" y1="56" x2="100" y2="144"/><line x1="56" y1="100" x2="144" y2="100"/><path d="M70 70l60 60M70 130l60-60"/>',
    "incentives-cat": '<circle cx="85" cy="90" r="24"/><circle cx="120" cy="115" r="18"/><circle cx="85" cy="90" r="6"/><circle cx="120" cy="115" r="4"/>',
    "about-cat": '<rect x="58" y="70" width="84" height="80"/><line x1="100" y1="88" x2="100" y2="116"/><line x1="86" y1="102" x2="114" y2="102"/><line x1="70" y1="150" x2="70" y2="130"/><line x1="130" y1="150" x2="130" y2="130"/>',
    "contact-cat": '<circle cx="100" cy="100" r="46"/><path d="M78 92l16 16 30-30"/><path d="M100 54v10M100 136v10M54 100h10M136 100h10"/>',
    "unsecured-business-loan-dod": '<circle cx="100" cy="100" r="42"/><path d="M100 66a34 34 0 1 1-24 10"/><path d="M76 76l0-14 14 4" fill="none"/><text x="100" y="112" font-size="34" fill="#E4C878" stroke="none" text-anchor="middle" font-family="ui-monospace">₹</text>',
    "commercial-industrial-purchase-loan": '<rect x="55" y="80" width="90" height="70" rx="2"/><path d="M55 80l45-32 45 32"/><rect x="90" y="112" width="20" height="38"/><line x1="70" y1="95" x2="70" y2="105"/><line x1="130" y1="95" x2="130" y2="105"/>',
    "machine-loan-sidbi": '<circle cx="100" cy="100" r="30"/><circle cx="100" cy="100" r="10"/><path d="M100 62v14M100 124v14M62 100h14M124 100h14M75 75l10 10M115 115l10 10M75 125l10-10M115 85l10-10"/>',
    "machine-loan-bank": '<circle cx="100" cy="95" r="26"/><circle cx="100" cy="95" r="8"/><path d="M100 61v12M100 117v12M66 95h12M122 95h12"/><rect x="60" y="140" width="80" height="8"/><path d="M70 140v-8h60v8"/>',
    "invoice-finance": '<rect x="62" y="52" width="76" height="96" rx="2"/><path d="M62 52l20 0 0 20-20 0z"/><line x1="76" y1="90" x2="124" y2="90"/><line x1="76" y1="104" x2="124" y2="104"/><line x1="76" y1="118" x2="108" y2="118"/><path d="M148 100l16 0m0 0l-8-8m8 8l-8 8" stroke-width="2.4"/>',
    "school-college-funding": '<path d="M100 60L45 84l55 24 55-24z"/><path d="M70 96v26c0 8 14 16 30 16s30-8 30-16V96"/><line x1="155" y1="84" x2="155" y2="118"/>',
    "builder-real-estate-funding": '<line x1="70" y1="150" x2="70" y2="55"/><line x1="70" y1="60" x2="140" y2="60"/><line x1="130" y1="60" x2="130" y2="90"/><path d="M126 90h8l-4 8z"/><rect x="55" y="130" width="26" height="20"/><rect x="86" y="112" width="26" height="38"/><rect x="117" y="122" width="26" height="28"/>',
    "hospital-funding": '<rect x="58" y="70" width="84" height="80"/><line x1="100" y1="88" x2="100" y2="116"/><line x1="86" y1="102" x2="114" y2="102"/><line x1="70" y1="150" x2="70" y2="130"/><line x1="130" y1="150" x2="130" y2="130"/>',
    "hotel-resort-funding": '<rect x="60" y="76" width="80" height="74"/><line x1="76" y1="92" x2="86" y2="92"/><line x1="76" y1="108" x2="86" y2="108"/><line x1="76" y1="124" x2="86" y2="124"/><line x1="114" y1="92" x2="124" y2="92"/><line x1="114" y1="108" x2="124" y2="108"/><path d="M50 150q12-10 24 0t24 0 24 0 24 0"/><circle cx="150" cy="62" r="12"/>',
    "npa-funding": '<circle cx="100" cy="100" r="46"/><path d="M78 92l16 16 30-30"/><path d="M100 54v10M100 136v10M54 100h10M136 100h10"/>',
    "infrastructure-funding": '<path d="M50 140h100"/><path d="M60 140V110l20-20 20 20v30"/><path d="M100 140v-40l20-16 20 16v40"/><line x1="150" y1="140" x2="150" y2="84"/><path d="M144 90h12l-6-10z"/>',
    "venture-funding": '<path d="M60 140h80"/><rect x="66" y="112" width="14" height="28"/><rect x="86" y="96" width="14" height="44"/><rect x="106" y="76" width="14" height="64"/><path d="M126 66l16-16 0 12 -12 0z"/><line x1="126" y1="66" x2="142" y2="50"/>',
    "valuation-services": '<rect x="50" y="70" width="100" height="70" rx="3"/><line x1="75" y1="140" x2="75" y2="155"/><line x1="125" y1="140" x2="125" y2="155"/><line x1="60" y1="155" x2="140" y2="155"/><path d="M68 115l20-20 16 12 28-28"/><path d="M120 71h12v12"/>',
    "pre-ipo-funding": '<circle cx="100" cy="100" r="44"/><line x1="100" y1="56" x2="100" y2="144"/><line x1="56" y1="100" x2="144" y2="100"/><path d="M70 70l60 60M70 130l60-60"/>',
    "sme-ipo": '<path d="M50 140V60h40v80z M110 140V90h40v50z"/><line x1="40" y1="140" x2="160" y2="140"/><path d="M70 40l10 10-10 10 M130 70l10 10-10 10"/>',
    "main-board-ipo": '<circle cx="100" cy="90" r="30"/><path d="M100 120v25 M85 145h30"/><path d="M100 75v10 M100 95v15 M85 90h30"/><line x1="60" y1="150" x2="140" y2="150"/>',
    "up-tus-scheme": '<circle cx="85" cy="90" r="24"/><circle cx="120" cy="115" r="18"/><circle cx="85" cy="90" r="6"/><circle cx="120" cy="115" r="4"/>',
    "up-msme-scheme": '<rect x="60" y="60" width="80" height="80" rx="4"/><line x1="80" y1="140" x2="80" y2="150"/><line x1="120" y1="140" x2="120" y2="150"/><path d="M75 105l15-15 15 10 20-20"/>',
    "up-msmy-scheme": '<path d="M100 50l40 30v55H60V80z"/><circle cx="100" cy="95" r="14"/><path d="M86 95h28"/>'
}

# 3. HELPER FOR RELATIVE PATH PREFIXES BASED ON FOLDER DEPTH
def get_prefix(depth):
    return "../" * depth

# 4. BLUEPRINT SVG WRAPPER FOR SERVICE HEROES
def get_blueprint_svg(glyph):
    return f"""<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M20 0H0V20" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
        </pattern>
      </defs>
      <rect width="200" height="200" fill="url(#grid)"/>
      <circle cx="100" cy="100" r="82" fill="none" stroke="rgba(200,155,60,0.18)" stroke-width="1.2" stroke-dasharray="3 4"/>
      <g stroke="#C89B3C" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
        {glyph}
      </g>
    </svg>"""

# 5. RENDER THE DYNAMIC EMI/INPUT CALCULATORS
def render_calculator_html(p):
    calc_type = p["calcType"]
    d = p["calcDefaults"]
    
    if calc_type == "invoice":
        return f"""
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Outstanding Invoice Value</span>
            <span class="value-output" id="inv-val-val">₹10,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="inv-val" min="100000" max="10000000" step="50000" value="{d['invoiceValue']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Advance Percentage</span>
            <span class="value-output" id="inv-adv-val">{d['advancePct']}%</span>
          </div>
          <input type="range" class="calc-slider" id="inv-adv" min="60" max="90" step="1" value="{d['advancePct']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Days Until Buyer Payment</span>
            <span class="value-output" id="inv-days-val">{d['days']} days</span>
          </div>
          <input type="range" class="calc-slider" id="inv-days" min="15" max="120" step="5" value="{d['days']}">
        </div>
        <input type="hidden" id="inv-mrate" value="{d['monthlyRate']}">
        """
        
    elif calc_type == "settlement":
        return f"""
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Outstanding Loan Dues</span>
            <span class="value-output" id="set-dues-val">₹50,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="set-dues" min="500000" max="50000000" step="100000" value="{d['outstanding']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Proposed OTS Percentage</span>
            <span class="value-output" id="set-pct-val">{d['settlePct']}% of dues</span>
          </div>
          <input type="range" class="calc-slider" id="set-pct" min="30" max="90" step="1" value="{d['settlePct']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Upfront Token Payment Required</span>
            <span class="value-output" id="set-tok-val">{d['tokenPct']}% of settlement</span>
          </div>
          <input type="range" class="calc-slider" id="set-tok" min="5" max="10" step="1" value="{d['tokenPct']}">
        </div>
        """
        
    elif calc_type == "dilution":
        return f"""
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Target Raise Amount</span>
            <span class="value-output" id="dil-raise-val">₹7,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="dil-raise" min="5000000" max="300000000" step="5000000" value="{d['raise']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Pre-Money Valuation</span>
            <span class="value-output" id="dil-pre-val">₹20,00,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="dil-pre" min="20000000" max="1000000000" step="5000000" value="{d['preMoney']}">
        </div>
        """
        
    elif calc_type == "ipo":
        return f"""
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Fresh Issue Size</span>
            <span class="value-output" id="ipo-issue-val">₹8,00,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="ipo-issue" min="10000000" max="1000000000" step="5000000" value="{d['raise']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Pre-Issue Business Valuation</span>
            <span class="value-output" id="ipo-pre-val">₹25,00,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="ipo-pre" min="50000000" max="4000000000" step="10000000" value="{d['preMoney']}">
        </div>
        """
        
    elif calc_type == "valuation":
        return f"""
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Annualised EBITDA</span>
            <span class="value-output" id="val-ebitda-val">₹1,50,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="val-ebitda" min="1000000" max="100000000" step="500000" value="{d['ebitda']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Sector Multiple — Low Bound</span>
            <span class="value-output" id="val-mlo-val">{d['multipleLow']}x</span>
          </div>
          <input type="range" class="calc-slider" id="val-mlo" min="3" max="12" step="0.5" value="{d['multipleLow']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Sector Multiple — High Bound</span>
            <span class="value-output" id="val-mhi-val">{d['multipleHigh']}x</span>
          </div>
          <input type="range" class="calc-slider" id="val-mhi" min="4" max="18" step="0.5" value="{d['multipleHigh']}">
        </div>
        """
        
    elif calc_type == "subsidy":
        return f"""
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Total Project / Machine Cost</span>
            <span class="value-output" id="sub-cost-val">₹20,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="sub-cost" min="100000" max="50000000" step="100000" value="{d['cost']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Policy Subsidy Rate</span>
            <span class="value-output" id="sub-rate-val">{d['rate']}%</span>
          </div>
          <input type="range" class="calc-slider" id="sub-rate" min="5" max="30" step="1" value="{d['rate']}">
        </div>
        <input type="hidden" id="sub-cap" value="{d['cap']}">
        """
        
    else: # Default: EMI Term Loan
        return f"""
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Desired Loan Amount</span>
            <span class="value-output" id="emi-p-val">₹50,00,000</span>
          </div>
          <input type="range" class="calc-slider" id="emi-p" min="{d['minP']}" max="{d['maxP']}" step="{max(10000, round(d['maxP']/100))}" value="{d['principal']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Interest Rate (p.a. indicative)</span>
            <span class="value-output" id="emi-r-val">{d['rate']}%</span>
          </div>
          <input type="range" class="calc-slider" id="emi-r" min="{d['minR']}" max="{d['maxR']}" step="0.1" value="{d['rate']}">
        </div>
        <div class="calc-input-group">
          <div class="calc-input-label">
            <span>Repayment Tenure</span>
            <span class="value-output" id="emi-y-val">{d['years']} yrs</span>
          </div>
          <input type="range" class="calc-slider" id="emi-y" min="{d['minY']}" max="{d['maxY']}" step="1" value="{d['years']}">
        </div>
        """

def render_calculator_outputs_html(p):
    calc_type = p["calcType"]
    
    if calc_type == "invoice":
        return """
        <div class="calc-output-item primary-out">
          <div class="label">Immediate Cash Advance (approx)</div>
          <div class="value" id="res-inv-adv">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Factoring / Discounting Fee</div>
          <div class="value" id="res-inv-cost">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Net Balance on Realisation</div>
          <div class="value" id="res-inv-net">—</div>
        </div>
        """
    elif calc_type == "settlement":
        return """
        <div class="calc-output-item primary-out">
          <div class="label">Settlement Amount (OTS)</div>
          <div class="value" id="res-set-amt">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Total Savings Realised</div>
          <div class="value" id="res-set-save">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Token Amount to Secure OTS Letter</div>
          <div class="value" id="res-set-tok">—</div>
        </div>
        """
    elif calc_type == "dilution":
        return """
        <div class="calc-output-item primary-out">
          <div class="label">Post-Money Valuation</div>
          <div class="value" id="res-dil-post">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Equity Dilution (approx)</div>
          <div class="value" id="res-dil-dil">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Promoters Shareholding Retained</div>
          <div class="value" id="res-dil-ret">—</div>
        </div>
        """
    elif calc_type == "ipo":
        return """
        <div class="calc-output-item primary-out">
          <div class="label">Post-Issue Valuation</div>
          <div class="value" id="res-ipo-post">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Public / Float Shareholding</div>
          <div class="value" id="res-ipo-pub">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Promoters Holding Post-Issue</div>
          <div class="value" id="res-ipo-prom">—</div>
        </div>
        """
    elif calc_type == "valuation":
        return """
        <div class="calc-output-item primary-out">
          <div class="label">Indicative Valuation (Low Bound)</div>
          <div class="value" id="res-val-lo">—</div>
        </div>
        <div class="calc-output-item primary-out">
          <div class="label">Indicative Valuation (High Bound)</div>
          <div class="value" id="res-val-hi">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Methodology Applied</div>
          <div class="value" style="font-size: 15px;">Comparable Multiple (EBITDA * multiple)</div>
        </div>
        """
    elif calc_type == "subsidy":
        return """
        <div class="calc-output-item primary-out">
          <div class="label">Estimated Subsidy Claimable</div>
          <div class="value" id="res-sub-amt">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Net Setup Cost After Subsidy</div>
          <div class="value" id="res-sub-net">—</div>
        </div>
        """
    else: # Term Loan EMI
        return """
        <div class="calc-output-item primary-out">
          <div class="label">Monthly Repayment (EMI)</div>
          <div class="value" id="res-emi">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Total Interest Payable</div>
          <div class="value" id="res-interest">—</div>
        </div>
        <div class="calc-output-item">
          <div class="label">Total Capital + Interest Payable</div>
          <div class="value" id="res-total">—</div>
        </div>
        <div class="calc-bar" id="c_bar">
          <div class="calc-bar-p" id="bar-p"></div>
          <div class="calc-bar-i" id="bar-i"></div>
        </div>
        """

# 6. LAYOUT WRAPPER (HEADER, FOOTER, SCRIPTS & CSS PATH RESOLUTION)
def get_layout(content, title, description, url_slug, depth=0):
    pref = get_prefix(depth)
    
    # Filter products for dropdown menus
    loans_items = [p for p in PRODUCTS if p["category"] == "Loans"]
    equity_items = [p for p in PRODUCTS if p["category"] == "Equity"]
    incentives_items = [p for p in PRODUCTS if p["category"] == "Incentives"]

    # Generate Loans Dropdown Grid Items
    loans_menu_html = ""
    for p in loans_items:
        loans_menu_html += f'<a href="{pref}loans/{p["id"]}/index.html" class="mega-item"><span class="title">{p["name"]}</span><span class="desc">{p["headline"]}</span></a>\n'

    # Generate Equity Dropdown Grid Items
    equity_menu_html = ""
    for p in equity_items:
        equity_menu_html += f'<a href="{pref}equity/{p["id"]}/index.html" class="mega-item"><span class="title">{p["name"]}</span><span class="desc">{p["headline"]}</span></a>\n'

    # Generate Incentives Dropdown Grid Items
    incentives_menu_html = ""
    for p in incentives_items:
        incentives_menu_html += f'<a href="{pref}incentives/{p["id"]}/index.html" class="mega-item"><span class="title">{p["name"]}</span><span class="desc">{p["headline"]}</span></a>\n'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | The Credit Lane</title>
  <meta name="description" content="{description}">
  
  <!-- Canonical URL -->
  <link rel="canonical" href="https://thecreditlane.com/{url_slug}">

  <!-- SEO OG Metadata -->
  <meta property="og:title" content="{title} | The Credit Lane">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://thecreditlane.com/{url_slug}">
  <meta property="og:site_name" content="The Credit Lane">

  <!-- Style Sheets -->
  <link rel="stylesheet" href="{pref}css/main.css">
</head>
<body>

  <!-- ============ HEADER / NAV ============ -->
  <header>
    <div class="wrap">
      <a href="{pref}index.html" class="logo">
        <svg viewBox="0 0 100 100" class="logo-svg" style="width: 38px; height: 38px; flex-shrink: 0; display: block;">
          <rect width="100" height="100" rx="22" fill="#0B1F3A"/>
          <rect x="6" y="6" width="88" height="88" rx="16" fill="#FFFFFF"/>
          <circle cx="53" cy="50" r="24" stroke="#0B1F3A" stroke-width="12" fill="none" stroke-dasharray="113.1 37.7" stroke-dashoffset="-18.8"/>
          <path d="M 44,39 L 44,54 Q 44,61 51,61 L 62,61 L 62,54 L 51,54 L 51,39 Z" fill="#0B1F3A"/>
          <text x="86" y="15" font-family="'Public Sans', sans-serif" font-size="9" font-weight="900" fill="#FFFFFF">®</text>
        </svg>
        THE CREDIT LANE
      </a>
      <nav class="mainnav">
        <a href="{pref}index.html" class="{"active" if url_slug == "" else ""}">Home</a>
        <div class="nav-item">
          <span>Loans ▾</span>
          <div class="mega-menu loans-menu">
            <h4>Debt Solutions & Funding</h4>
            <div class="mega-grid">
              {loans_menu_html}
            </div>
          </div>
        </div>
        <div class="nav-item">
          <span>Equity ▾</span>
          <div class="mega-menu">
            <h4>Advisory & Public Listings</h4>
            <div class="mega-grid">
              {equity_menu_html}
            </div>
          </div>
        </div>
        <div class="nav-item">
          <span>Incentives ▾</span>
          <div class="mega-menu">
            <h4>Government Scheme Subsidies</h4>
            <div class="mega-grid">
              {incentives_menu_html}
            </div>
          </div>
        </div>
        <a href="{pref}about/index.html" class="{"active" if url_slug == "about" else ""}">About Us</a>
        <a href="{pref}contact/index.html" class="{"active" if url_slug == "contact" else ""}">Contact Us</a>
      </nav>
      
      <div class="header-cta">
        <span class="phone">📞 8802-905-123</span>
        <a href="{pref}contact/index.html" class="btn btn-primary">Discuss Your Funding Need</a>
      </div>

      <!-- Hamburger mobile icon -->
      <button class="hamburger" aria-label="Toggle Navigation">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>

  <!-- Mobile nav drawer -->
  <div class="mobile-nav">
    <div class="mobile-nav-links">
      <div class="mobile-nav-item">
        <a href="{pref}index.html" style="font-weight: 700; font-size: 16px;">Home</a>
      </div>
      <div class="mobile-nav-item">
        <div class="mobile-nav-title">Loans <span class="arrow-toggle">▾</span></div>
        <div class="mobile-nav-submenu">
          <a href="{pref}loans/index.html" style="font-weight:700;">→ Loans Catalog</a>
          {"".join([f'<a href="{pref}loans/{p["id"]}/index.html">{p["name"]}</a>' for p in loans_items])}
        </div>
      </div>
      <div class="mobile-nav-item">
        <div class="mobile-nav-title">Equity <span class="arrow-toggle">▾</span></div>
        <div class="mobile-nav-submenu">
          <a href="{pref}equity/index.html" style="font-weight:700;">→ Equity Catalog</a>
          {"".join([f'<a href="{pref}equity/{p["id"]}/index.html">{p["name"]}</a>' for p in equity_items])}
        </div>
      </div>
      <div class="mobile-nav-item">
        <div class="mobile-nav-title">Incentives <span class="arrow-toggle">▾</span></div>
        <div class="mobile-nav-submenu">
          <a href="{pref}incentives/index.html" style="font-weight:700;">→ Incentives Catalog</a>
          {"".join([f'<a href="{pref}incentives/{p["id"]}/index.html">{p["name"]}</a>' for p in incentives_items])}
        </div>
      </div>
      <div class="mobile-nav-item">
        <a href="{pref}about/index.html" style="font-weight: 700; font-size: 16px;">About Us</a>
      </div>
      <div class="mobile-nav-item">
        <a href="{pref}contact/index.html" style="font-weight: 700; font-size: 16px;">Contact Us</a>
      </div>
    </div>
    
    <div class="mobile-nav-cta">
      <span class="phone">📞 8802-905-123</span>
      <a href="{pref}contact/index.html" class="btn btn-primary">Discuss Your Funding Need</a>
    </div>
  </div>

  <div class="overlay"></div>

  <!-- Main Content Area -->
  <main>
    {content}
  </main>

  <!-- ============ FOOTER ============ -->
  <footer>
    <div class="footer-top-section">
      <div class="wrap">
        <div class="footer-top-row">
          <div class="footer-tagline">CA &amp; Advocate-led<br>Corporate Finance Desk.</div>
          <div class="footer-cols">
            <div class="footer-col">
              <h5>LOANS</h5>
              <div class="footer-links">
                {"".join([f'<a href="{pref}loans/{p["id"]}/index.html">{p["name"]}</a>' for p in loans_items])}
              </div>
            </div>
            <div class="footer-col">
              <h5>EQUITY</h5>
              <div class="footer-links">
                {"".join([f'<a href="{pref}equity/{p["id"]}/index.html">{p["name"]}</a>' for p in equity_items])}
              </div>
            </div>
            <div class="footer-col">
              <h5>INCENTIVES</h5>
              <div class="footer-links">
                {"".join([f'<a href="{pref}incentives/{p["id"]}/index.html">{p["name"]}</a>' for p in incentives_items])}
              </div>
            </div>
            <div class="footer-col">
              <h5>COMPANY</h5>
              <div class="footer-links">
                <a href="{pref}about/index.html">About Us</a>
                <a href="{pref}contact/index.html">Contact Us</a>
                <a href="{pref}contact/index.html">Partner With Us</a>
                <a href="{pref}contact/index.html">Track Application</a>
              </div>
            </div>
          </div>
        </div>
        <div class="footer-badges-row">
          <div class="footer-badges">
            <span>ISO 9001:2015</span>
            <span>Corporate Finance Desk</span>
            <span>10+ Yrs Experience</span>
          </div>
          <p class="footer-desc">CA, CS and Advocate-led corporate finance desk. We help Indian companies structure and secure the optimal mix of debt, equity, and government subsidies.</p>
        </div>
      </div>
    </div>

    <div class="footer-wordmark-section">
      <div class="footer-wordmark">The Credit Lane</div>
    </div>

    <div class="footer-bottom-bar">
      <div class="wrap">
        <div class="footer-bottom">
          <div>
            <span>© 2026 The Credit Lane. All rights reserved.</span>
            <span class="mono" style="font-size: 11px; color:#5B6472; margin-left: 16px;">HQ: Ghaziabad · Delhi NCR, India</span>
          </div>
          <div class="disclaimer">
            <b>Financial Advisory Disclaimer:</b> The terms, interest rates, dilution limits, and subsidy caps shown on this site are indicative. Final credit approval is subject to underwriting, audit, and sanction by respective banks, investors, or government authorities. The Credit Lane does not charge upfront fees.
          </div>
        </div>
      </div>
    </div>
  </footer>

  <!-- Floating WhatsApp Widget -->
  <a href="https://wa.me/918802905123" target="_blank" class="wa-fab" aria-label="Chat on WhatsApp" title="Chat with us">
    <svg viewBox="0 0 32 32" fill="none"><path d="M16 4C9.4 4 4 9.4 4 16c0 2.4.7 4.6 1.9 6.5L4 28l5.7-1.8C11.5 27.4 13.7 28 16 28c6.6 0 12-5.4 12-12S22.6 4 16 4z" fill="#fff"/><path d="M22.1 19.1c-.3-.2-1.9-1-2.2-1.1-.3-.1-.5-.2-.7.2-.2.3-.8 1.1-1 1.3-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-2-1.8-2.3-.2-.3 0-.5.1-.6.1-.1.3-.4.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.2-.7-1.7-1-2.3-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1.1 2.8 1.2 3c.1.2 2.1 3.3 5.2 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.9-.8 2.1-1.5.3-.7.3-1.4.2-1.5-.1-.1-.3-.2-.6-.3z" fill="#25d366"/></svg>
    <div class="wa-tooltip">Chat with us</div>
  </a>

  <!-- Script Files -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/Observer.min.js"></script>
  <script src="{pref}js/main.js"></script>
</body>
</html>"""

# 6.5. IMAGE MAPPING HELPER FOR SERVICE PAGES
def get_service_image(product):
    pid = product["id"]
    
    # 19 products unique active image mapping
    mapping = {
        "unsecured-business-loan-dod": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=600&auto=format&fit=crop", # Office work B2B
        "commercial-industrial-purchase-loan": "https://images.unsplash.com/photo-1582407947304-fd86f028f716?q=80&w=600&auto=format&fit=crop", # Commercial buildings
        "machine-loan-sidbi": "https://images.unsplash.com/photo-1537462715879-360eeb61a0bc?q=80&w=600&auto=format&fit=crop", # CNC factory machining
        "machine-loan-bank": "https://images.unsplash.com/photo-1565034946487-077786996e27?q=80&w=600&auto=format&fit=crop", # Welding robot arm
        "invoice-finance": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=600&auto=format&fit=crop", # Logistics cargo boxes
        "school-college-funding": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=600&auto=format&fit=crop", # University dome spire
        "builder-real-estate-funding": "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?q=80&w=600&auto=format&fit=crop", # Construction concrete frame
        "hospital-funding": "https://images.unsplash.com/photo-1516549655169-df83a0774514?q=80&w=600&auto=format&fit=crop", # ICU monitor and bed
        "hotel-resort-funding": "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=600&auto=format&fit=crop", # Premium pool hotel front
        "npa-funding": "https://images.unsplash.com/photo-1450133064473-71024230f91b?q=80&w=600&auto=format&fit=crop", # signing OTS document
        "infrastructure-funding": "https://images.unsplash.com/photo-1590069261209-f8e9b8642343?q=80&w=600&auto=format&fit=crop", # Infrastructure concrete bridge
        "venture-funding": "https://images.unsplash.com/photo-1531538606174-0f90ff5dce83?q=80&w=600&auto=format&fit=crop", # Open tech workspace
        "valuation-services": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=600&auto=format&fit=crop", # Analyzing financial chart screens
        "pre-ipo-funding": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=600&auto=format&fit=crop", # Corporate advisor chart board
        "sme-ipo": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=600&auto=format&fit=crop", # Exchange price graphs
        "main-board-ipo": "https://images.unsplash.com/photo-1535320903710-d993d3d77d29?q=80&w=600&auto=format&fit=crop", # Corporate ticker boards
        "up-tus-scheme": "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?q=80&w=600&auto=format&fit=crop", # mill automated loom inspector
        "up-msme-scheme": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?q=80&w=600&auto=format&fit=crop", # manufacturing assembly line packager
        "up-msmy-scheme": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=600&auto=format&fit=crop"  # young local store owner entrepreneur
    }
    
    return mapping.get(pid, "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=600&auto=format&fit=crop")

# 7. HOMEPAGE COMPILER
def generate_homepage():
    # Capital Selector HTML
    stack_lists_html = ""
    for category in ["Loans", "Equity", "Incentives"]:
        active_class = "active" if category == "Loans" else ""
        items = [p for p in PRODUCTS if p["category"] == category]
        
        stack_lists_html += f'<div class="stack-list {active_class}">\n'
        for p in items:
            path = f'{category.lower()}/{p["id"]}/index.html'
            stack_lists_html += f'  <a href="{path}">{p["name"]} <span class="arrow">→</span></a>\n'
        stack_lists_html += '</div>\n'

    # Services Catalog tabs
    catalog_grids_html = ""
    for category in ["Loans", "Equity", "Incentives"]:
        active_class = "active" if category == "Loans" else ""
        items = [p for p in PRODUCTS if p["category"] == category]
        
        catalog_grids_html += f'<div class="catalog-grid {active_class}">\n'
        for p in items:
            path = f'{category.lower()}/{p["id"]}/index.html'
            # Shorten description
            desc = p["sub"] if len(p["sub"]) < 110 else p["sub"][:107] + "..."
            
            # Simple Category tag icons
            icon_char = "OD"
            if category == "Equity":
                icon_char = "EQ"
            elif category == "Incentives":
                icon_char = "IN"
            elif "Machinery" in p["eyebrow"]:
                icon_char = "MC"
            elif "Property" in p["eyebrow"]:
                icon_char = "PR"
            elif "Trade" in p["eyebrow"]:
                icon_char = "TF"
            
            catalog_grids_html += f"""
            <div class="service-card">
              <div class="icon">{icon_char}</div>
              <h4>{p["name"]}</h4>
              <p>{desc}</p>
              <a href="{path}" class="link">Explore solution →</a>
            </div>\n"""
        catalog_grids_html += '</div>\n'

    content = f"""
    <!-- ============ HERO ============ -->
    <section class="hero" style="padding-bottom: 0;">
      <video autoplay muted loop playsinline style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: fill; z-index: 1; opacity: 0.65; pointer-events: none;">
        <source src="about/Screen_Recording_2026-07-30_at_4.54.57_PM.mov" type="video/quicktime">
        <source src="about/Screen_Recording_2026-07-30_at_4.54.57_PM.mov" type="video/mp4">
      </video>
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to right, rgba(8, 21, 39, 0.96) 0%, rgba(8, 21, 39, 0.65) 45%, rgba(8, 21, 39, 0.15) 100%); z-index: 1; pointer-events: none;"></div>
      <div class="wrap" style="padding-top: 40px; padding-bottom: 40px;">
        <div>
          <span class="eyebrow">CA · CS · ADVOCATE-LED CAPITAL ADVISORY — 10+ YEARS · ₹2,500 CR+ RAISED</span>
          <h1>Capital for Your Next Stage of Growth.</h1>
          <p class="lead">Strategic funding, equity advisory and government incentive solutions for ambitious Indian businesses. Access 100+ institutional lenders with the transparency of a premium advisory desk.</p>
          
          <div class="hero-trust">Loans • Equity • Government Incentives</div>
          
          <div class="hero-cta-row">
            <a href="contact/index.html" class="btn btn-primary">Discuss Your Funding Need</a>
            <a href="#selector" class="btn btn-outline">Explore Our Services</a>
          </div>
          
          <div class="hero-stats">
            <div class="stat"><b>₹2,500 Cr+</b><span>Debt & Equity Structured</span></div>
            <div class="stat"><b>100+</b><span>Lending Partners</span></div>
            <div class="stat"><b>1,000+</b><span>SMEs Funded</span></div>
            <div class="stat"><b>10 Years</b><span>On-Ground Execution</span></div>
          </div>
        </div>

        <!-- Interactive Capital Selector -->
        <div class="stack-card" id="selector">
          <div class="stack-tabs">
            <div class="stack-tab active">LOANS</div>
            <div class="stack-tab">EQUITY</div>
            <div class="stack-tab">INCENTIVES</div>
          </div>
          {stack_lists_html}
          <div class="stack-note">
            <span>↻</span>
            Click tabs to explore. Select any option to view the dedicated requirements page.
          </div>
        </div>
      </div>
    </section>

    <!-- ============ TRUST MARQUEE ============ -->
    <div class="marquee-band">
      <div class="marquee-eyebrow">
        <span class="eyebrow">TRUSTED CHANNEL PARTNER TO PLATFORMS</span>
      </div>
      <div class="marquee-track-wrap">
        <div class="marquee-rail" id="marqueeRail">
          <span>HDFC BANK</span>
          <span class="marquee-sep">·</span>
          <span>AXIS BANK</span>
          <span class="marquee-sep">·</span>
          <span>DCB BANK</span>
          <span class="marquee-sep">·</span>
          <span>BAJAJ FINSERV</span>
          <span class="marquee-sep">·</span>
          <span>ADITYA BIRLA</span>
          <span class="marquee-sep">·</span>
          <span>SIDBI CO-LOAN</span>
          <span class="marquee-sep">·</span>
          <span>TATA CAPITAL</span>
          <span class="marquee-sep">·</span>
          <span>HDFC BANK</span>
          <span class="marquee-sep">·</span>
          <span>AXIS BANK</span>
          <span class="marquee-sep">·</span>
          <span>DCB BANK</span>
          <span class="marquee-sep">·</span>
          <span>BAJAJ FINSERV</span>
          <span class="marquee-sep">·</span>
          <span>ADITYA BIRLA</span>
          <span class="marquee-sep">·</span>
          <span>SIDBI CO-LOAN</span>
          <span class="marquee-sep">·</span>
          <span>TATA CAPITAL</span>
          <span class="marquee-sep">·</span>
        </div>
      </div>
    </div>

    <!-- ============ TRUST / AUTHORITY SECTION ============ -->
    <section>
      <div class="wrap">
        <div class="section-head center">
          <span class="eyebrow">THE ADVISORY DIFFERENCE</span>
          <h2>Finance is not one-size-fits-all.</h2>
          <p>Every business possesses a distinct footprint. Sizing and structuring must match your specific realities, not bank algorithms.</p>
        </div>
        
        <div style="font-size: 15px; color: var(--slate); max-width: 800px; margin: -20px auto 40px; text-align: center; line-height: 1.6;">
          Businesses differ in cash-flow velocity, collateral depth, lifecycle stage, capital structures, industry margins, and target execution runways. We diagnose the parameters before we approach a lender.
        </div>

        <div class="pillars">
          <div class="pillar-card">
            <span class="num">01</span>
            <h4>Structured Funding</h4>
            <p>We analyze balance sheets and contracts to build custom structures that reduce capital costs.</p>
          </div>
          <div class="pillar-card">
            <span class="num">02</span>
            <h4>Multi-Route Access</h4>
            <p>Access debt limits, private capital pre-IPO financing, and state incentive programs in one room.</p>
          </div>
          <div class="pillar-card">
            <span class="num">03</span>
            <h4>Sector-Specific</h4>
            <p>Our solutions adapt to sectors: school calendars, developer escrow laws, and machine commissioning times.</p>
          </div>
          <div class="pillar-card">
            <span class="num">04</span>
            <h4>End-to-End Execution</h4>
            <p>We manage paperwork, address audit bottlenecks, and follow through to final sanction and disbursal.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ MID-PAGE CORPORATE BANNER ============ -->
    <div style="background-image: linear-gradient(rgba(11, 31, 58, 0.75), rgba(11, 31, 58, 0.75)), url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1200&auto=format&fit=crop'); background-attachment: fixed; background-position: center; background-repeat: no-repeat; background-size: cover; height: 260px; display: flex; align-items: center; justify-content: center; text-align: center; color: var(--white); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);">
      <div class="wrap" style="width: 100%;">
        <h3 style="color: var(--white); font-size: clamp(1.6rem, 3vw, 2.2rem); font-family: var(--font-serif); margin-bottom: 10px;">Premium Corporate Advisory Desk</h3>
        <p style="color: var(--gold-light); font-family: var(--font-mono); font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; margin: 0;">Unlocking capital channels with absolute alignment and transparent execution.</p>
      </div>
    </div>

    <!-- ============ SERVICES CATALOG ============ -->
    <section class="services-catalog" style="background-color: var(--white); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);">
      <div class="wrap">
        <div class="section-head center">
          <span class="eyebrow">COMPLETE CATALOGUE</span>
          <h2>Solutions built around your business.</h2>
          <p>Select a category to view the complete range of debt, equity and government incentive support.</p>
        </div>

        <div class="catalog-tabs">
          <div class="catalog-tab active">Loans</div>
          <div class="catalog-tab">Equity</div>
          <div class="catalog-tab">Incentives</div>
        </div>

        {catalog_grids_html}
      </div>
    </section>

    <!-- ============ INDUSTRY SECTIONS ============ -->
    <section class="section-dark">
      <div class="wrap">
        <div class="section-head center">
          <span class="eyebrow">MARKET SPECIALISATION</span>
          <h2>Capital expertise across industries.</h2>
          <p>We design specific underwriting briefs to speak the language of credit committees in each niche.</p>
        </div>

        <div class="industry-grid">
          <div class="industry-card">
            <div class="icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M2 20h20"/>
                <path d="M20 20V8l-6 4V8l-6 4V8L2 12v8h18z"/>
                <rect x="6" y="15" width="2" height="5"/>
                <rect x="11" y="15" width="2" height="5"/>
                <rect x="16" y="15" width="2" height="5"/>
              </svg>
            </div>
            <h4>Manufacturing</h4>
            <p>High-LTV SIDBI machine loans and technical subsidies (UP TUS).</p>
          </div>
          <div class="industry-card">
            <div class="icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="4" y="2" width="16" height="20" rx="2" ry="2"/>
                <line x1="9" y1="22" x2="9" y2="16"/>
                <line x1="15" y1="22" x2="15" y2="16"/>
                <line x1="9" y1="16" x2="15" y2="16"/>
                <path d="M8 6h2M14 6h2M8 10h2M14 10h2M8 14h2M14 14h2"/>
              </svg>
            </div>
            <h4>Real Estate</h4>
            <p>Milestone construction funding and RERA escrow structured accounts.</p>
          </div>
          <div class="industry-card">
            <div class="icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2v20M2 12h20"/>
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              </svg>
            </div>
            <h4>Healthcare</h4>
            <p>Hospital construction loans and medical diagnostics leasing.</p>
          </div>
          <div class="industry-card">
            <div class="icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"/>
              </svg>
            </div>
            <h4>Education</h4>
            <p>School/College expansions mapped to admissions and fee cash cycles.</p>
          </div>
          <div class="industry-card">
            <div class="icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M2 22h20M12 22V17h-2v5M4 22V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v16"/>
                <path d="M8 8h2M14 8h2M8 12h2M14 12h2"/>
              </svg>
            </div>
            <h4>Hospitality</h4>
            <p>Hotel capital and renovation funding flexed to occupancy seasonality.</p>
          </div>
          <div class="industry-card">
            <div class="icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 20c8-6 10-6 18 0"/>
                <path d="M3 12h18"/>
                <path d="M7 12v5M12 12v5M17 12v5M12 3v9"/>
              </svg>
            </div>
            <h4>Infrastructure</h4>
            <p>EPC contractor mobilization lines and bid-bond bank guarantees.</p>
          </div>
          <div class="industry-card">
            <div class="icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4.5 16.5c-1.5 1.5-2.5 3.5-2.5 5.5C4 22 6 21 7.5 19.5"/>
                <path d="M12 12l9-9-3 12-6 3-3-3z"/>
                <path d="M9 15l-3 3-2-2 3-3"/>
                <circle cx="15" cy="9" r="1"/>
              </svg>
            </div>
            <h4>Tech & Startups</h4>
            <p>Venture funding readiness, equity scaling, and investor placement.</p>
          </div>
          <div class="industry-card">
            <div class="icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
              </svg>
            </div>
            <h4>CFO Advisory</h4>
            <p>Statutory share valuations and statutory merchant banker reports.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ WHY CHOOSE US ============ -->
    <section>
      <div class="wrap">
        <div class="section-head center">
          <span class="eyebrow">CAPITAL ADVISORS</span>
          <h2>More than funding. A capital strategy.</h2>
          <p>Why corporate promoters and financial directors trust The Credit Lane as their advisor.</p>
        </div>

        <div class="why-grid">
          <div class="why-item">
            <div class="icon-box">01</div>
            <div>
              <h4>Right Capital Route</h4>
              <p>We benchmark loan options against equity dilution and incentive grants to choose the optimal route.</p>
            </div>
          </div>
          <div class="why-item">
            <div class="icon-box">02</div>
            <div>
              <h4>Structured Advisory</h4>
              <p>We examine historical and projected statements to structure the file for credit approval before submission.</p>
            </div>
          </div>
          <div class="why-item">
            <div class="icon-box">03</div>
            <div>
              <h4>Multiple Options</h4>
              <p>One advisory team manages unsecured CC, asset backing, IPO preparation, and government scheme subsidies.</p>
            </div>
          </div>
          <div class="why-item">
            <div class="icon-box">04</div>
            <div>
              <h4>Sector Understanding</h4>
              <p>We draft specific proposals outlining commissioning lags, RERA timelines, or collection seasonal flows.</p>
            </div>
          </div>
          <div class="why-item">
            <div class="icon-box">05</div>
            <div>
              <h4>Documentation Support</h4>
              <p>We handle auditor reviews, CMA formatting, bank queries, and statutory valuation certificates.</p>
            </div>
          </div>
          <div class="why-item">
            <div class="icon-box">06</div>
            <div>
              <h4>End-to-End Execution</h4>
              <p>Our work spans from initial planning diagnostics, to lender coordination, all the way to final bank disbursal.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ PROCESS TIMELINE ============ -->
    <section class="section-tight" style="background-color: var(--white); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);">
      <div class="wrap">
        <div class="section-head center">
          <span class="eyebrow">TRANSACTION LIFECYCLE</span>
          <h2>From requirement to capital.</h2>
          <p>A systematic methodology built to maximize speed and minimize sanction friction.</p>
        </div>

        <div class="process-row">
          <div class="process-step">
            <div class="idx">01</div>
            <h4>Understand</h4>
            <p>Diagnose target requirements, capital structure constraints, and target timeline.</p>
          </div>
          <div class="process-step">
            <div class="idx">02</div>
            <h4>Assess</h4>
            <p>Perform financial diagnostic checks, look up bank guidelines, and verify credit limits.</p>
          </div>
          <div class="process-step">
            <div class="idx">03</div>
            <h4>Structure</h4>
            <p>Choose optimal loan parameters, security mapping, or scheme subsidy pathways.</p>
          </div>
          <div class="process-step">
            <div class="idx">04</div>
            <h4>Prepare</h4>
            <p>Compile bank-ready dossiers, draft financial projections, and build files.</p>
          </div>
          <div class="process-step">
            <div class="idx">05</div>
            <h4>Connect</h4>
            <p>Introduce the structured file to senior credit officers, investors, or authorities.</p>
          </div>
          <div class="process-step">
            <div class="idx">06</div>
            <h4>Execute</h4>
            <p>Support through due diligence audits, legal vetting, and final sanction signature.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ SOCIAL PROOF ============ -->
    <section class="testimonials">
      <div class="wrap">
        <div class="section-head center">
          <span class="eyebrow">CLIENT FEEDBACK</span>
          <h2>Trusted through every stage of the funding journey.</h2>
        </div>

        <div class="rating-block">
          <div class="rating-score">4.7 / 5</div>
          <div>
            <div class="rating-stars">★★★★★</div>
            <div class="rating-meta">Based on 600+ verified business-owner ratings in Ghaziabad, Noida and Delhi NCR.</div>
          </div>
        </div>

        <div class="testi-grid">
          <div class="testi-card">
            <p class="quote">"Credit Lane structured our CNC machine loan through SIDBI's SPEED scheme. We saved roughly 2.5% in annual interest and they handled all the government subsidy files alongside the bank work."</p>
            <div class="who">
              <div class="avatar">RM</div>
              <div class="who-meta">
                <b>Rajeev Malhotra</b>
                <span>Manufacturing unit, Sahibabad</span>
              </div>
            </div>
          </div>
          <div class="testi-card">
            <p class="quote">"B2B invoice finance cleared our cash flow hurdles. We sell to top electronics manufacturers with a 90-day wait period. They set up the limit in 4 business days."</p>
            <div class="who">
              <div class="avatar">SS</div>
              <div class="who-meta">
                <b>Siddharth Sharma</b>
                <span>Technology exporter, Noida Sector 63</span>
              </div>
            </div>
          </div>
          <div class="testi-card">
            <p class="quote">"They compiled our FEMA-compliant share valuations and connected us with pre-IPO institutional funds. Clear communication, no false promises, and exceptional merchant banking coordinate."</p>
            <div class="who">
              <div class="avatar">AK</div>
              <div class="who-meta">
                <b>Alka Kathpalia</b>
                <span>Founder, Healthcare Chain</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta">
      <div class="wrap">
        <h2>Have a funding requirement?</h2>
        <p>Tell us what you are building. We'll help you explore the right capital route with no upfront advisory charge.</p>
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
          <a href="contact/index.html" class="btn btn-primary">Talk to The Credit Lane →</a>
          <a href="https://wa.me/918802905123" class="btn btn-outline" target="_blank">WhatsApp Us</a>
        </div>
      </div>
    </section>
    """
    
    html = get_layout(content, "Corporate Finance & Business Funding Advisory", "Access unsecured business loans, SIDBI machine finance, builder construction funding, share valuation and SME IPOs through a network of 100+ partner lenders.", "")
    
    with open("index.html", "w") as f:
        f.write(html)
    print("Homepage generated.")

# 8. ABOUT US COMPILER
def generate_aboutpage():
    content = """
    <section class="service-banner" style="padding-bottom: 40px;">
      <div class="wrap">
        <div>
          <span class="eyebrow" style="color:var(--gold-light);">OUR PROFILE</span>
          <h1 style="max-width: 100%;">Capital decisions deserve more than a generic answer.</h1>
          <p class="lead" style="max-width: 100%;">Meet the team of corporate finance specialists, CAs, Company Secretaries, and Legal Advocates committed to structuring optimal growth capitalization.</p>
        </div>
        <div class="service-banner-art">
          <div class="service-banner-art-img" style="background-image: url('https://images.unsplash.com/photo-1557804506-669a67965ba0?q=80&w=600&auto=format&fit=crop');"></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="about-story">
          <div>
            <span class="eyebrow">OUR MANDATE</span>
            <h2 style="font-size:32px; margin-top:12px; margin-bottom:20px;">Positioning businesses for capital readiness.</h2>
            <p style="color:var(--slate); margin-bottom:16px;">The Credit Lane was founded on a simple insight: Indian business promoters are frequently misdirected into standard retail loan products that burden cash flows, lock up critical collaterals, and miss out on eligible state subsidies.</p>
            <p style="color:var(--slate); margin-bottom:16px;">We operate as a capital desk that coordinates debt structuring, public market listings, statutory valuation files, and Uttar Pradesh government promotion schemes under a single relationship.</p>
            <p style="color:var(--slate); margin-bottom:24px;">Our mandate is to ensure our clients understand their balance sheet variables, compare options side-by-side, and submit clean, credit-ready applications that move through bank committees without friction.</p>
            <a href="../contact/index.html" class="btn btn-outline-dark">Consult with our Advisors →</a>
          </div>
          <div class="about-graphics" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
            <div style="background-image: url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=600&auto=format&fit=crop'); background-size: cover; background-position: center; height: 180px; width: 100%;"></div>
            <div style="padding: 32px 24px; text-align: center;">
              <div class="about-logo-wrapper" style="margin: 0 auto 16px; display: inline-block;">
                <svg viewBox="0 0 100 100" style="width: 72px; height: 72px; display: block;">
                  <rect width="100" height="100" rx="22" fill="#0B1F3A"/>
                  <rect x="6" y="6" width="88" height="88" rx="16" fill="#FFFFFF"/>
                  <circle cx="53" cy="50" r="24" stroke="#0B1F3A" stroke-width="12" fill="none" stroke-dasharray="113.1 37.7" stroke-dashoffset="-18.8"/>
                  <path d="M 44,39 L 44,54 Q 44,61 51,61 L 62,61 L 62,54 L 51,54 L 51,39 Z" fill="#0B1F3A"/>
                  <text x="86" y="15" font-family="'Public Sans', sans-serif" font-size="9" font-weight="900" fill="#FFFFFF">®</text>
                </svg>
              </div>
              <h3>Transparent. Methodical. Advisory-First.</h3>
              <p>We are channel partners to 100+ scheduled banks, industrial NBFCs, equity syndicates, and government portals, allowing us to find terms that serve the business interest.</p>
            </div>
          </div>
        </div>

        <div class="values-grid">
          <div class="value-card">
            <div class="icon-box">✓</div>
            <h4>Advisory-Led Matching</h4>
            <p>We diagnose credit ratings, debt service coverage, and asset commissions before picking a bank to prevent negative credit database markers.</p>
          </div>
          <div class="value-card">
            <div class="icon-box">✓</div>
            <h4>Lender Panel Competition</h4>
            <p>We map your requirements across public banks, private institutions, and industrial finance houses, ensuring you choose the best-suited term sheet.</p>
          </div>
          <div class="value-card">
            <div class="icon-box">✓</div>
            <h4>No Hidden Brokerages</h4>
            <p>We disclose processing charges, audit expectations, collateral criteria, and covenants upfront. No upfront fee, no hidden commissions.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section-tight" style="background-color: var(--white); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);">
      <div class="wrap">
        <div class="section-head center">
          <span class="eyebrow">CORE LEADERSHIP</span>
          <h2>A desk of financial & legal professionals.</h2>
          <p>Our team brings together professional credentials spanning Chartered Accountancy (CA), Company Secretarial (CS), and legal chambers.</p>
        </div>

        <div style="font-size: 15px; color: var(--slate); max-width: 800px; margin: 0 auto; text-align: center; line-height: 1.6;">
          This professional focus allows us to structure transactions correctly, whether navigating trust registration compliance for school infrastructure funding, title clearance for builder construction loans, or FEMA pricing guidelines for foreign equity investment.
        </div>
      </div>
    </section>

    <section class="final-cta">
      <div class="wrap">
        <h2>Want to evaluate your financing options?</h2>
        <p>Book a private consultation with our advisory team to review your credit potential and available subsidy schemes.</p>
        <a href="../contact/index.html" class="btn btn-primary">Schedule Advisory Call</a>
      </div>
    </section>
    """
    
    html = get_layout(content, "About Us | Capital Advisory Desk", "CA, CS and Advocate-led capital advisory team. Providing structured debt, equity capital, IPO advisory and state incentives for Indian enterprises.", "about", 1)
    
    os.makedirs("about", exist_ok=True)
    with open("about/index.html", "w") as f:
        f.write(html)
    print("About page generated.")

# 9. CONTACT US COMPILER
def generate_contactpage():
    content = """
    <section class="service-banner" style="padding-bottom: 40px;">
      <div class="wrap">
        <div>
          <span class="eyebrow" style="color:var(--gold-light);">GET IN TOUCH</span>
          <h1 style="max-width: 100%;">Let's talk about your requirement.</h1>
          <p class="lead" style="max-width: 100%;">Submit details of your project or capital needs. Our corporate advisory desk reviews submissions and responds within one working day.</p>
        </div>
        <div class="service-banner-art">
          <div class="service-banner-art-img" style="background-image: url('https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=600&auto=format&fit=crop');"></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="contact-grid">
          
          <div class="contact-info-col">
            <div class="contact-card" style="padding: 0; overflow: hidden;">
              <div style="background-image: url('https://images.unsplash.com/photo-1423666639041-f56000c27a9a?q=80&w=600&auto=format&fit=crop'); background-size: cover; background-position: center; height: 140px; width: 100%;"></div>
              <div style="padding: 32px 24px;">
                <h4>Advisory Desk Details</h4>
                <div class="contact-item">
                  <span class="label">Location</span>
                  <span>Ghaziabad, Delhi NCR, India</span>
                </div>
                <div class="contact-item">
                  <span class="label">Phone</span>
                  <span class="mono">+91-8802905123</span>
                </div>
                <div class="contact-item">
                  <span class="label">Email</span>
                  <span class="mono">advisory@thecreditlane.com</span>
                </div>
                <div class="contact-item">
                  <span class="label">WhatsApp</span>
                  <span class="mono">+91-8802905123</span>
                </div>
                <div class="contact-item">
                  <span class="label">Hours</span>
                  <span>Monday – Saturday, 10 AM – 6 PM</span>
                </div>
              </div>
            </div>

            <!-- Map container with Google Map and floating address badge -->
            <div class="map-container" style="position: relative; height: 240px; border: 1px solid var(--line); border-radius: var(--radius); overflow: hidden;">
              <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d112061.7613589945!2d77.3468962657398!3d28.63189916694833!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390cf1bb41c50fdf%3A0xe6dc4db006cfaf30!2sGhaziabad%2C%20Uttar%20Pradesh!5e0!3m2!1sen!2sin!4v1717012345678!5m2!1sen!2sin" 
                width="100%" 
                height="100%" 
                style="border:0; display:block;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
              </iframe>
              <div style="position: absolute; bottom: 12px; left: 12px; right: 12px; background: rgba(255, 255, 255, 0.95); padding: 12px 16px; border-radius: 6px; box-shadow: var(--shadow-premium); border-left: 3px solid var(--gold); pointer-events: none; backdrop-filter: blur(4px);">
                <b style="font-size: 13px; color: var(--navy-dark); display: block;">Ghaziabad Head Office</b>
                <p style="font-size: 11px; color: var(--slate); margin: 4px 0 0 0; line-height: 1.4;">Structured credit & public market advisory services across Uttar Pradesh, NCR, and nationwide.</p>
              </div>
            </div>
          </div>

          <!-- Split form -->
          <div class="lead-card">
            <h3 style="font-size: 24px; margin-bottom: 20px; border-bottom:1px solid var(--line); padding-bottom:10px;">Discuss Your Funding Need</h3>
            <form class="lead-form" onsubmit="return false;">
              <div class="form-grid">
                <div class="form-group">
                  <label>Full Name *</label>
                  <input type="text" placeholder="Enter your full name" required>
                </div>
                <div class="form-group">
                  <label>Company Name *</label>
                  <input type="text" placeholder="Enter company name" required>
                </div>
              </div>
              <div class="form-grid">
                <div class="form-group">
                  <label>Phone Number *</label>
                  <input type="tel" placeholder="+91" required>
                </div>
                <div class="form-group">
                  <label>Email Address *</label>
                  <input type="email" placeholder="you@company.com" required>
                </div>
              </div>
              <div class="form-grid">
                <div class="form-group">
                  <label>City *</label>
                  <input type="text" placeholder="Ghaziabad" required>
                </div>
                <div class="form-group">
                  <label>Business Type *</label>
                  <select required>
                    <option value="">Select your business type</option>
                    <option value="manufacturing">Manufacturing / Industrial</option>
                    <option value="real-estate">Real Estate Developer</option>
                    <option value="healthcare">Healthcare / Hospital</option>
                    <option value="education">Education / Trust</option>
                    <option value="hospitality">Hospitality / Hotel</option>
                    <option value="infrastructure">Infrastructure / EPC Contractor</option>
                    <option value="services">Services / B2B Trading</option>
                    <option value="startup">Startup / Tech</option>
                  </select>
                </div>
              </div>
              <div class="form-grid">
                <div class="form-group">
                  <label>Funding Requirement *</label>
                  <select required>
                    <option value="">Select primary need</option>
                    <option value="loans">Business Loan / OD Limit</option>
                    <option value="machinery">Machine Finance (SIDBI/Bank)</option>
                    <option value="project">Real Estate / Construction Finance</option>
                    <option value="invoice">Invoice Discounting / Trade Finance</option>
                    <option value="npa">Refinancing / NPA Settlement (OTS)</option>
                    <option value="valuation">Business Valuation Certification</option>
                    <option value="ipo">SME IPO / Mainboard Listing</option>
                    <option value="subsidy">UP Government Incentive Scheme</option>
                  </select>
                </div>
                <div class="form-group">
                  <label>Required Funding Amount *</label>
                  <select required>
                    <option value="">Select indicative size</option>
                    <option value="1">Under ₹10 Lakh</option>
                    <option value="2">₹10 Lakh – ₹50 Lakh</option>
                    <option value="3">₹50 Lakh – ₹1 Crore</option>
                    <option value="4">₹1 Crore – ₹5 Crore</option>
                    <option value="5">Above ₹5 Crore</option>
                  </select>
                </div>
              </div>
              <div class="form-group full-width">
                <label>Message / Detail of Project</label>
                <textarea rows="4" placeholder="Briefly describe what you are building or the nature of your cash flow requirement..."></textarea>
              </div>
              <label class="form-consent">
                <input type="checkbox" required>
                I authorise The Credit Lane and its empanelled institutional lending partners to contact me via phone, SMS, email, or WhatsApp regarding this advisory request.
              </label>
              <button class="btn btn-primary form-submit-btn" type="submit">Submit Inquiry & Request Callback →</button>
            </form>
          </div>

        </div>
      </div>
    </section>
    """
    
    html = get_layout(content, "Contact Our Advisory Desk", "Discuss your business funding needs. Speak with our corporate finance advisors regarding loan sanctions, share valuation, IPO structuring, or Uttar Pradesh incentive applications.", "contact", 1)
    
    os.makedirs("contact", exist_ok=True)
    with open("contact/index.html", "w") as f:
        f.write(html)
    print("Contact page generated.")

# 10. CATEGORY PAGES COMPILER (LOANS, EQUITY, INCENTIVES OVERVIEWS)
def generate_category_pages():
    # A. LOANS CATEGORY OVERVIEW
    loans_items = [p for p in PRODUCTS if p["category"] == "Loans"]
    
    # Group items logically
    groups = {
        "BUSINESS & WORKING CAPITAL": [],
        "ASSET & EQUIPMENT FINANCE": [],
        "SECTOR-SPECIFIC FUNDING": [],
        "SPECIAL SITUATION & GROWTH CAPITAL": []
    }
    
    for p in loans_items:
        sc = p["subcategory"]
        if sc == "Business & Working Capital":
            groups["BUSINESS & WORKING CAPITAL"].append(p)
        elif sc == "Asset & Equipment Finance":
            groups["ASSET & EQUIPMENT FINANCE"].append(p)
        elif sc == "Sector-Specific Funding":
            groups["SECTOR-SPECIFIC FUNDING"].append(p)
        elif sc == "Special Situation & Growth Capital":
            groups["SPECIAL SITUATION & GROWTH CAPITAL"].append(p)

    loans_content = """
    <section class="service-banner" style="padding-bottom: 40px;">
      <div class="wrap">
        <div>
          <span class="eyebrow" style="color:var(--gold-light);">LOANS CATALOGUE</span>
          <h1 style="max-width: 100%;">Business Funding, Structured Around Your Requirement.</h1>
          <p class="lead" style="max-width: 100%;">Access working capital, commercial mortgage property purchase, specialized SIDBI machine schemes, construction milestone financing, stressed asset resolution and growth debt.</p>
        </div>
        <div class="service-banner-art">
          <div class="service-banner-art-img" style="background-image: url('https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?q=80&w=600&auto=format&fit=crop');"></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
    """
    
    for g_title, items in groups.items():
        if len(items) == 0:
            continue
        loans_content += f"""
        <div class="category-group">
          <h2 class="category-group-title">{g_title} <span class="count">{len(items)} options</span></h2>
          <div class="category-grid-catalog">
        """
        for p in items:
            loans_content += f"""
            <div class="service-card">
              <div class="icon">{"MC" if "Machinery" in p["eyebrow"] else "PR" if "Property" in p["eyebrow"] else "TF" if "Trade" in p["eyebrow"] else "OD"}</div>
              <h4>{p["name"]}</h4>
              <p>{p["sub"]}</p>
              <a href="{p["id"]}/index.html" class="link">Explore solution →</a>
            </div>
            """
        loans_content += """
          </div>
        </div>
        """
        
    loans_content += """
      </div>
    </section>
    
    <section class="final-cta">
      <div class="wrap">
        <h2>Unsure which funding route fits your cash cycle?</h2>
        <p>Speak with our CAs and advocates. We analyze eligibility criteria across public, private, and SIDBI lenders to structure the file.</p>
        <a href="../contact/index.html" class="btn btn-primary">Request Portfolio Structure Check</a>
      </div>
    </section>
    """
    
    loans_html = get_layout(loans_content, "Business Loans & Structured Credit Advisory", "Compare unsecured business limits, drop-line overdrafts, asset-backed commercial term loans, machinery SPEED finance from SIDBI, real estate developer construction limits, stressed debt NPA solutions and venture debt.", "loans", 1)
    
    os.makedirs("loans", exist_ok=True)
    with open("loans/index.html", "w") as f:
        f.write(loans_html)
    print("Loans category page generated.")

    # B. EQUITY CATEGORY OVERVIEW
    equity_items = [p for p in PRODUCTS if p["category"] == "Equity"]
    
    equity_content = """
    <section class="service-banner" style="padding-bottom: 40px;">
      <div class="wrap">
        <div>
          <span class="eyebrow" style="color:var(--gold-light);">EQUITY SERVICES</span>
          <h1 style="max-width: 100%;">Build Value. Access Growth Capital. Prepare for Listing.</h1>
          <p class="lead" style="max-width: 100%;">Navigate company valuations, early-growth private placements, pre-IPO financing and NSE / BSE listings. Advisory-led coordinate through every statutory step.</p>
        </div>
        <div class="service-banner-art">
          <div class="service-banner-art-img" style="background-image: url('https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?q=80&w=600&auto=format&fit=crop');"></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="category-group">
          <h2 class="category-group-title">EQUITY & PUBLIC MARKET SERVICES <span class="count">4 solutions</span></h2>
          <div class="category-grid-catalog">
    """
    for p in equity_items:
        equity_content += f"""
        <div class="service-card">
          <div class="icon">EQ</div>
          <h4>{p["name"]}</h4>
          <p>{p["sub"]}</p>
          <a href="{p["id"]}/index.html" class="link">Explore solution →</a>
        </div>
        """
    equity_content += """
          </div>
        </div>

        <!-- Visual market readiness timeline -->
        <div style="margin-top: 80px; padding: 48px 32px; background-color: var(--white); border:1.5px solid var(--line); border-radius:var(--radius); box-shadow:var(--shadow-premium);">
          <h3 style="font-size:24px; text-align:center; margin-bottom:12px;">The Equity and Market Capitalisation Journey</h3>
          <p style="text-align:center; color:var(--slate); max-width:600px; margin: 0 auto 36px; font-size:14px;">How we support promoters in building investor trust and transitioning to public exchanges.</p>
          
          <div style="display:grid; grid-template-columns: repeat(5, 1fr); gap: 16px; text-align:center;">
            <div>
              <div class="mono" style="font-size:11px; color:var(--gold); font-weight:700; margin-bottom:6px;">STEP 01</div>
              <h4 style="font-size:15px; margin-bottom:4px;">Valuation</h4>
              <p style="font-size:11.5px; color:var(--muted); line-height:1.4;">Defensible asset & share reports matching tax and FEMA norms.</p>
            </div>
            <div>
              <div class="mono" style="font-size:11px; color:var(--gold); font-weight:700; margin-bottom:6px;">STEP 02</div>
              <h4 style="font-size:15px; margin-bottom:4px;">Structuring</h4>
              <p style="font-size:11.5px; color:var(--muted); line-height:1.4;">Dilution bounds, instrument choice (CCDs), and cap table design.</p>
            </div>
            <div>
              <div class="mono" style="font-size:11px; color:var(--gold); font-weight:700; margin-bottom:6px;">STEP 03</div>
              <h4 style="font-size:15px; margin-bottom:4px;">Pre-IPO Placement</h4>
              <p style="font-size:11.5px; color:var(--muted); line-height:1.4;">Secure mezzanine growth capital from family offices & HNIs.</p>
            </div>
            <div>
              <div class="mono" style="font-size:11px; color:var(--gold); font-weight:700; margin-bottom:6px;">STEP 04</div>
              <h4 style="font-size:15px; margin-bottom:4px;">Prospectus (DRHP)</h4>
              <p style="font-size:11.5px; color:var(--muted); line-height:1.4;">Draft exchange-ready prospectuses matching SEBI formats.</p>
            </div>
            <div>
              <div class="mono" style="font-size:11px; color:var(--gold); font-weight:700; margin-bottom:6px;">STEP 05</div>
              <h4 style="font-size:15px; margin-bottom:4px;">Public Market Bell</h4>
              <p style="font-size:11.5px; color:var(--muted); line-height:1.4;">Listing roadshows, subscription coordination, and allotment.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="final-cta">
      <div class="wrap">
        <h2>Preparing for listing or institutional raise?</h2>
        <p>Book a strategic session under NDA to review your financials against BSE SME, NSE Emerge or SEBI Mainboard criteria.</p>
        <a href="../contact/index.html" class="btn btn-primary">Schedule IPO Readiness Check</a>
      </div>
    </section>
    """
    
    equity_html = get_layout(equity_content, "Equity Advisory, Share Valuation & IPO Listings", "Statutory Registered Valuer and Merchant Banker valuations. Capital prep, mezzanine dilution plans, BSE SME / NSE Emerge listings and SEBI mainboard IPO coordinate.", "equity", 1)
    
    os.makedirs("equity", exist_ok=True)
    with open("equity/index.html", "w") as f:
        f.write(equity_html)
    print("Equity category page generated.")

    # C. INCENTIVES CATEGORY OVERVIEW
    incentives_items = [p for p in PRODUCTS if p["category"] == "Incentives"]
    
    incentives_content = """
    <section class="service-banner" style="padding-bottom: 40px;">
      <div class="wrap">
        <div>
          <span class="eyebrow" style="color:var(--gold-light);">STATE POLICY SUBSIDIES</span>
          <h1 style="max-width: 100%;">Don't Leave Eligible Business Incentives on the Table.</h1>
          <p class="lead" style="max-width: 100%;">Uttar Pradesh offers capital grants, stamp duty refunds and interest subsidies for new setups, manufacturing modernizations, and youth-led enterprises. We track and file your claim.</p>
        </div>
        <div class="service-banner-art">
          <div class="service-banner-art-img" style="background-image: url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=600&auto=format&fit=crop');"></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="category-group">
          <h2 class="category-group-title">UP GOVERNMENT INCENTIVE POLICIES <span class="count">3 schemes</span></h2>
          <div class="category-grid-catalog">
    """
    for p in incentives_items:
        incentives_content += f"""
        <div class="service-card">
          <div class="icon">IN</div>
          <h4>{p["name"]}</h4>
          <p>{p["sub"]}</p>
          <a href="{p["id"]}/index.html" class="link">Explore solution →</a>
        </div>
        """
    incentives_content += """
          </div>
        </div>

        <!-- Government Incentives Visual System -->
        <div style="margin-top: 80px; padding: 48px 32px; background-color: var(--white); border: 1.5px solid var(--line); border-radius:var(--radius); box-shadow:var(--shadow-premium);">
          <h3 style="font-size:24px; text-align:center; margin-bottom:12px;">Uttar Pradesh MSME Subsidy Framework</h3>
          <p style="text-align:center; color:var(--slate); max-width:600px; margin: 0 auto 36px; font-size:14px;">Understanding benefits, regional divisions and first-come-first-serve portal queues.</p>
          
          <div class="about-story" style="grid-template-columns: 1.2fr 0.8fr; gap:36px;">
            <div>
              <h4 style="font-size:17px; margin-bottom:12px; font-family:var(--font-sans); font-weight:700;">Regional Subsidies splits:</h4>
              <ul class="qualify-bullets">
                <li><b>Bundelkhand & Purvanchal (Eastern UP):</b> Eligible for the highest capital grants (15% - 25%) and 100% stamp duty exemption on industrial land.</li>
                <li><b>Madhyanchal (Central UP) & Paschimanchal (Western UP):</b> Eligible for up to 10% - 20% capital subsidies and 75% stamp duty exemptions.</li>
                <li><b>Gautam Buddh Nagar (Noida) & Ghaziabad:</b> Eligible for up to 10% - 15% capital subsidies and 50% stamp duty exemptions.</li>
                <li><b>Women-led Projects:</b> Eligible for 100% stamp duty exemption statewide, regardless of regional borders.</li>
              </ul>
            </div>
            <div style="background-color: var(--off-white); border-radius: var(--radius); padding: 24px; border:1px dashed var(--gold);">
              <h4 style="font-size:15px; margin-bottom:8px;">DIEPC District Committee Vetting</h4>
              <p style="font-size:12.5px; color:var(--slate); line-height:1.45; margin-bottom:12px;">Applications must map to Nivesh Mitra single-window timelines. Our team reviews unit age, prior policy benefits, and project bills before submission to prevent rejections.</p>
              <a href="../contact/index.html" class="btn btn-outline-dark" style="padding: 8px 16px; font-size:12px;">Check Policy Fit</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="final-cta">
      <div class="wrap">
        <h2>Are you building or buying machinery in UP?</h2>
        <p>Do not miss out on eligible technical or setup subsidies. Our advocates handle Single Window filings and district clearances.</p>
        <a href="../contact/index.html" class="btn btn-primary">Check Subsidy Eligibility</a>
      </div>
    </section>
    """
    
    incentives_html = get_layout(incentives_content, "UP Government Incentives, subsidies & Policies Desk", "Uttar Pradesh MSME Policy 2022 benefits, Technical Upgradation TUS grants, stamp duty exemption, interest relief, and MYSY youth collateral-free startup lines.", "incentives", 1)
    
    os.makedirs("incentives", exist_ok=True)
    with open("incentives/index.html", "w") as f:
        f.write(incentives_html)
    print("Incentives category page generated.")


# 11. INDIVIDUAL SERVICE PAGES COMPILER
def generate_service_pages():
    for p in PRODUCTS:
        cat_slug = p["category"].lower()
        slug = p["id"]
        
        # Determine category title
        cat_title = p["category"]
        
        # Build breadcrumb
        breadcrumb = f'<a href="../../index.html">Home</a> / <a href="../index.html">{cat_title}</a> / {p["name"]}'
        
        # Process vertical timeline
        timeline_html = ""
        for idx, step in enumerate(p["process"]):
            timeline_html += f"""
            <div class="route-timeline-step">
              <div class="dot">{str(idx+1).zfill(2)}</div>
              <div>
                <h3>{step[0]}</h3>
                <p>{step[1]}</p>
              </div>
            </div>\n"""
            
        # Key Features & Benefits
        features_html = ""
        for f in p["features"]:
            features_html += f"""
            <div class="feature-block">
              <span class="num">{f[0]}</span>
              <div>
                <h3>{f[1]}</h3>
                <p>{f[2]}</p>
              </div>
            </div>\n"""

        # FAQs
        faqs_html = ""
        for idx, faq in enumerate(p["faqs"]):
            open_class = "open" if idx == 0 else ""
            indicator_char = "−" if idx == 0 else "+"
            faqs_html += f"""
            <div class="faq-item {open_class}">
              <div class="faq-q">{faq[0]} <span>{indicator_char}</span></div>
              <div class="faq-a">
                <p>{faq[1]}</p>
              </div>
            </div>\n"""

        # Reviews
        reviews_html = ""
        for rev in p["reviews"]["items"]:
            # Get initials
            initials = "".join([w[0] for w in rev[0].split(" ")[:2]])
            reviews_html += f"""
            <div class="testi-card">
              <div class="quote">"{rev[2]}"</div>
              <div class="who">
                <div class="avatar">{initials}</div>
                <div class="who-meta">
                  <b>{rev[0]}</b>
                  <span>{rev[1]}</span>
                </div>
              </div>
            </div>\n"""

        # Determine Calculator Title
        calc_titles = {
            "dilution": "Dilution & Valuation Estimator",
            "settlement": "OTS Settlement Savings Estimator",
            "invoice": "Invoice Discounting Cash Advance Estimator",
            "ipo": "Fresh Issue Share Dilution Estimator",
            "valuation": "EBITDA Comparable Multiple Valuation Range",
            "subsidy": "UP Policy Scheme Subsidy Estimator"
        }
        calc_title = calc_titles.get(p["calcType"], "Indicative Repayment (EMI) Calculator")

        # Combine content layout
        service_content = f"""
        <!-- ============ SERVICE BANNER ============ -->
        <section class="service-banner">
          <div class="wrap">
            <div>
              <div class="breadcrumbs">{breadcrumb}</div>
              <span class="eyebrow" style="color:var(--gold-light);">{cat_title.upper()}</span>
              <h1>{p["name"]}</h1>
              <p class="lead">{p["sub"]}</p>
              <div class="hero-cta-row">
                <a href="#apply" class="btn btn-primary">Check Eligibility</a>
                <a href="#calculator" class="btn btn-outline">Estimate Numbers</a>
              </div>
            </div>
            <div class="service-banner-art">
              <div class="service-banner-art-img" style="background-image: url('{get_service_image(p)}');"></div>
            </div>
          </div>
          
          <div class="stat-strip">
            <div class="wrap">
              {"".join([f'<div class="stat-strip-item"><div class="v">{s[0]}</div><div class="k">{s[1]}</div></div>' for s in p["stats"]])}
            </div>
          </div>
        </section>

        <!-- ============ SERVICE DETAILS GRID ============ -->
        <section style="background-color: var(--white); border-bottom:1px solid var(--line);">
          <div class="wrap">
            <div class="service-content-grid">
              
              <!-- Main Column (Left) -->
              <div class="service-main-col">
                
                <!-- 1. ABOUT -->
                <div class="service-section" id="overview">
                  <span class="eyebrow">DIAGNOSTICS</span>
                  <h2 style="margin-top:8px;">About this funding solution</h2>
                  {"".join([f"<p>{par}</p>" for par in p["brief"]])}
                  <p style="font-size:12px; color:var(--muted); font-style:italic; margin-top:20px;">{p["statNote"]}</p>
                </div>

                <!-- 2. WHO SHOULD APPLY -->
                <div class="service-section" id="eligibility">
                  <span class="eyebrow">SUITABILITY CHECK</span>
                  <h2 style="margin-top:8px;">Who is this solution for?</h2>
                  <p>{p["whoIntro"]}</p>
                  
                  <div class="who-summary-box">
                    {"".join([f"<div>{s.replace('Best for:', '<b>Best for:</b>').replace('Think twice if:', '<b>Think twice if:</b>').replace('Note:', '<b>Note:</b>').replace('Not eligible if:', '<b>Not eligible if:</b>')}</div>" for s in p["whoSummary"]])}
                  </div>

                  <ul class="qualify-bullets">
                    {"".join([f"<li>{q}</li>" for q in p["qualify"]])}
                  </ul>
                </div>

                <!-- 3. KEY FEATURES & BENEFITS -->
                <div class="service-section" id="features">
                  <span class="eyebrow">ADVANTAGES</span>
                  <h2 style="margin-top:8px;">Why consider this funding route?</h2>
                  <div class="features-grid">
                    {features_html}
                  </div>
                </div>

                <!-- 4. OUR PROCESS -->
                <div class="service-section" id="process">
                  <span class="eyebrow">TRANSACTION STAGES</span>
                  <h2 style="margin-top:8px;">How it works</h2>
                  <div class="route-timeline">
                    {timeline_html}
                  </div>
                </div>

                <!-- 5. EMI CALCULATOR / ESTIMATOR -->
                <div class="service-section" id="calculator">
                  <span class="eyebrow">INDICATIVE ESTIMATES</span>
                  <h2 style="margin-top:8px; margin-bottom:12px;">{calc_title}</h2>
                  <p style="font-size:14.5px; color:var(--slate); margin-bottom:24px;">Use the sliders below to get an indicative estimate. Final terms are subject to formal underwriting and lender / investor committee assessment.</p>
                  
                  <div class="calc-container">
                    <div class="calc-grid">
                      <!-- Left Inputs -->
                      <div class="calc-inputs">
                        {render_calculator_html(p)}
                      </div>
                      
                      <!-- Right Outputs -->
                      <div class="calc-outputs">
                        {render_calculator_outputs_html(p)}
                      </div>
                    </div>
                    <div class="calc-disclaimer">
                      <b>* Notice:</b> Calculated figures are for simulation purposes only. Sizing, interest rate margins, security discount factors, and subsidy tranches depend on credit metrics and final sanction letters.
                    </div>
                  </div>
                </div>

                <!-- 6. SOCIAL PROOF (REVIEWS) -->
                <div class="service-section" id="reviews">
                  <span class="eyebrow">CLIENT FEEDBACK</span>
                  <h2 style="margin-top:8px; margin-bottom:20px;">Client experience</h2>
                  <div class="rating-block" style="justify-content: flex-start; border-bottom:none; margin-bottom:24px; padding-bottom:0;">
                    <div class="rating-score">{p["reviews"]["rating"]}</div>
                    <div>
                      <div class="rating-stars">★★★★★</div>
                      <div class="rating-meta">Based on {p["reviews"]["count"]} verified corporate accounts.</div>
                    </div>
                  </div>
                  
                  <div style="display:flex; flex-direction:column; gap:16px;">
                    {reviews_html}
                  </div>
                </div>

                <!-- 7. FAQ -->
                <div class="service-section" id="faq">
                  <span class="eyebrow">COMMON OBJECTS</span>
                  <h2 style="margin-top:8px; margin-bottom:20px;">FAQs</h2>
                  <div class="faq-accordion">
                    {faqs_html}
                  </div>
                </div>

              </div>

              <!-- Sticky Form Column (Right) -->
              <div>
                <div class="lead-card" id="apply" style="position: sticky; top: 100px;">
                  <h3 style="font-size: 22px; margin-bottom: 12px;">Check Eligibility</h3>
                  <p style="font-size: 13.5px; color: var(--slate); margin-bottom: 24px; line-height:1.4;">Submit details for <b>{p["name"]}</b>. Our desk reviews profile variables and calls you back the same working day.</p>
                  
                  <form class="lead-form" onsubmit="return false;">
                    <div class="form-group">
                      <label>Full Name *</label>
                      <input type="text" placeholder="Your full name" required>
                    </div>
                    <div class="form-group">
                      <label>Company Name *</label>
                      <input type="text" placeholder="Company name" required>
                    </div>
                    <div class="form-group">
                      <label>Phone Number *</label>
                      <input type="tel" placeholder="+91" required>
                    </div>
                    <div class="form-group">
                      <label>Email *</label>
                      <input type="email" placeholder="you@company.com" required>
                    </div>
                    <div class="form-group">
                      <label>City *</label>
                      <input type="text" placeholder="e.g. Ghaziabad" required>
                    </div>
                    <div class="form-group">
                      <label>Business Type *</label>
                      <select required>
                        <option value="">Select your type</option>
                        <option value="manufacturing">Manufacturing / Industrial</option>
                        <option value="real-estate">Real Estate Developer</option>
                        <option value="healthcare">Healthcare / Hospital</option>
                        <option value="education">Education / Trust</option>
                        <option value="hospitality">Hospitality / Hotel</option>
                        <option value="infrastructure">Infrastructure Contractor</option>
                        <option value="other">B2B Trade & Services</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label>Funding Size Required *</label>
                      <select required>
                        <option value="">Select size</option>
                        <option value="1">Under ₹10 Lakh</option>
                        <option value="2">₹10 Lakh – ₹50 Lakh</option>
                        <option value="3">₹50 Lakh – ₹1 Crore</option>
                        <option value="4">₹1 Crore – ₹5 Crore</option>
                        <option value="5">Above ₹5 Crore</option>
                      </select>
                    </div>
                    
                    <label class="form-consent">
                      <input type="checkbox" required>
                      I agree to the disclosure terms and authorise The Credit Lane to contact me regarding this enquiry.
                    </label>
                    <button class="btn btn-primary form-submit-btn" type="submit">Submit Request →</button>
                  </form>
                </div>
              </div>

            </div>
          </div>
        </section>
        """
        
        # Compile
        html = get_layout(service_content, f'{p["name"]} | Capital Advisory', p["sub"], f'{cat_slug}/{slug}', 2)
        
        # Save
        dir_path = f'{cat_slug}/{slug}'
        os.makedirs(dir_path, exist_ok=True)
        with open(f'{dir_path}/index.html', "w") as f:
            f.write(html)
        print(f"Generated service page: {dir_path}/index.html")

# 12. RUN ALL GENERATIONS
if __name__ == "__main__":
    # Create required asset folders
    os.makedirs("css", exist_ok=True)
    os.makedirs("js", exist_ok=True)
    
    # Generate pages
    generate_homepage()
    generate_aboutpage()
    generate_contactpage()
    generate_category_pages()
    generate_service_pages()
    print("Static website generation completed successfully.")
