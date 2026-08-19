import os
import re

PRODUCTS = [
    ("unsecured-business-loan-dod", "loans/unsecured-business-loan-dod/index.html"),
    ("commercial-industrial-purchase-loan", "loans/commercial-industrial-purchase-loan/index.html"),
    ("machine-loan-sidbi", "loans/machine-loan-sidbi/index.html"),
    ("machine-loan-bank", "loans/machine-loan-bank/index.html"),
    ("invoice-finance", "loans/invoice-finance/index.html"),
    ("school-college-funding", "loans/school-college-funding/index.html"),
    ("builder-real-estate-funding", "loans/builder-real-estate-funding/index.html"),
    ("hospital-funding", "loans/hospital-funding/index.html"),
    ("hotel-resort-funding", "loans/hotel-resort-funding/index.html"),
    ("npa-funding", "loans/npa-funding/index.html"),
    ("infrastructure-funding", "loans/infrastructure-funding/index.html"),
    ("venture-funding", "loans/venture-funding/index.html"),
    ("valuation-services", "equity/valuation-services/index.html"),
    ("pre-ipo-funding", "equity/pre-ipo-funding/index.html"),
    ("sme-ipo", "equity/sme-ipo/index.html"),
    ("main-board-ipo", "equity/main-board-ipo/index.html"),
    ("up-tus-scheme", "incentives/up-tus-scheme/index.html"),
    ("up-msme-scheme", "incentives/up-msme-scheme/index.html"),
    ("up-msmy-scheme", "incentives/up-msmy-scheme/index.html"),
]

for pid, html_path in PRODUCTS:
    php_path = f"credit-lane-theme/pages/{pid}.php"
    if not os.path.exists(html_path) or not os.path.exists(php_path):
        continue

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    start_token = '<div class="service-section" id="calculator">'
    if start_token not in html_content:
        continue

    start_idx = html_content.find(start_token)
    next_sec_idx = html_content.find('<div class="service-section"', start_idx + len(start_token))
    if next_sec_idx == -1:
        next_sec_idx = html_content.find('</section>', start_idx)

    calc_html = html_content[start_idx:next_sec_idx].strip()

    with open(php_path, "r", encoding="utf-8") as f:
        php_content = f.read()

    if start_token in php_content:
        php_start_idx = php_content.find(start_token)
        php_next_sec_idx = php_content.find('<div class="service-section"', php_start_idx + len(start_token))
        if php_next_sec_idx == -1:
            php_next_sec_idx = php_content.find('</section>', php_start_idx)

        updated_php = php_content[:php_start_idx] + calc_html + "\n\n                " + php_content[php_next_sec_idx:]
        with open(php_path, "w", encoding="utf-8") as f:
            f.write(updated_php)
        print(f"Successfully synced calculator for {pid}.php")

print("Theme calculators sync complete.")
