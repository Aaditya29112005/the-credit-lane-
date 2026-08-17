import os
import sys
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable, KeepTogether
)
from reportlab.pdfgen import canvas

# File paths
gallery_dir = "/Users/aadityamohansamadhiya/the credit lane/credit-lane-theme/assets/images/gallery"
out_pdf_theme = "/Users/aadityamohansamadhiya/the credit lane/credit-lane-theme/assets/docs/The-Credit-Lane-Brochure.pdf"
out_pdf_root = "/Users/aadityamohansamadhiya/the credit lane/The-Credit-Lane-Brochure.pdf"

# Ensure output directory exists
os.makedirs(os.path.dirname(out_pdf_theme), exist_ok=True)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Top banner background
        self.setFillColor(colors.HexColor("#0B1F3A"))
        self.rect(0, 810, 595.27, 32, fill=1, stroke=0)
        
        # Top text
        self.setFillColor(colors.HexColor("#FFD700"))
        self.setFont("Helvetica-Bold", 8)
        self.drawString(36, 822, "THE CREDIT LANE — BRT CORPORATE ADVISORY PVT. LTD.")
        self.setFillColor(colors.white)
        self.setFont("Helvetica", 8)
        self.drawRightString(595.27 - 36, 822, "CA, CS & Advocate Led Corporate Finance Desk")

        # Bottom footer bar
        self.setFillColor(colors.HexColor("#071426"))
        self.rect(0, 0, 595.27, 32, fill=1, stroke=0)
        self.setFillColor(colors.HexColor("#94A3B8"))
        self.setFont("Helvetica", 8)
        self.drawString(36, 12, "HQ: B 31 First Floor, Raj Nagar, Ghaziabad 201001 | Phone: 9217924499 / 9818709747 | Info@thecreditlane.in")
        self.drawRightString(595.27 - 36, 12, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        out_pdf_theme,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=48,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=30,
        textColor=colors.HexColor('#0B1F3A'),
        alignment=0,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'CoverSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#B8860B'),
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#0B1F3A'),
        spaceBefore=12,
        spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#B8860B'),
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#222222'),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#333333'),
        spaceAfter=3
    )

    story = []

    # ================= PAGE 1: COVER PAGE & EXECUTIVE SUMMARY =================
    story.append(Paragraph("THE CREDIT LANE", title_style))
    story.append(Paragraph("BRT CORPORATE ADVISORY PRIVATE LIMITED", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#B8860B'), spaceBefore=2, spaceAfter=12))

    summary_text = (
        "<b>Official Corporate Dossier & Financial Services Spectrum</b><br/>"
        "The Credit Lane is a premier <b>CA, CS and Advocate-led Corporate Finance Desk</b> headquartered in Ghaziabad (Delhi NCR). "
        "We specialize in structuring complex debt, SIDBI machinery term loans, government capital subsidies & grants, equity syndication, "
        "and public market listings (SME IPO / Main Board IPO) for Indian commercial enterprises, manufacturers, builders, hospitals, and educational institutions."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 8))

    # Badges Table
    badges_data = [
        [
            Paragraph("<b>ISO 9001:2015</b><br/><font size=7 color='#555'>Quality Standard Certified</font>", bullet_style),
            Paragraph("<b>CA / CS / Advocate Desk</b><br/><font size=7 color='#555'>Expert Legal & Audit Advisory</font>", bullet_style),
            Paragraph("<b>10+ Yrs Experience</b><br/><font size=7 color='#555'>₹500+ Cr Debt & Equity Mandates</font>", bullet_style),
            Paragraph("<b>4.9 ★★★★★</b><br/><font size=7 color='#555'>150+ Verified Google Reviews</font>", bullet_style),
        ]
    ]
    t_badges = Table(badges_data, colWidths=[125, 135, 130, 130])
    t_badges.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F4F6F9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER')
    ]))
    story.append(t_badges)
    story.append(Spacer(1, 14))

    # Cover Image (3 Co-Founders Leadership Photo)
    founder_img_path = os.path.join(gallery_dir, "WhatsApp Image 2026-08-11 at 10.10.23.jpeg")
    if os.path.exists(founder_img_path):
        img_cover = Image(founder_img_path, width=520, height=260)
        story.append(img_cover)
        story.append(Spacer(1, 6))
        story.append(Paragraph("<b>Figure 1:</b> 3 Co-Founders Desk & Executive Leadership (Rajat Garg, Founder & MD)", ParagraphStyle('Cap', fontName='Helvetica-Oblique', fontSize=8, textColor=colors.HexColor('#666'), alignment=1)))

    story.append(Spacer(1, 14))

    # Company Contact Info Box
    contact_data = [
        [
            Paragraph("<b>Corporate Headquarters:</b> B 31 First Floor, Raj Nagar, Ghaziabad 201001<br/>"
                      "<b>Direct Helplines:</b> +91 9217924499 / +91 9818709747 | <b>Official Email:</b> Info@thecreditlane.in<br/>"
                      "<b>Web Portal:</b> https://thecreditlane.in", body_style)
        ]
    ]
    t_contact = Table(contact_data, colWidths=[520])
    t_contact.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0B1F3A')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#B8860B')),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_contact)

    story.append(PageBreak())

    # ================= PAGE 2: EXECUTIVE LEADERSHIP & RECOGNITIONS =================
    story.append(Paragraph("EXECUTIVE LEADERSHIP & NATIONAL RECOGNITIONS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#B8860B'), spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>Professional Advisory Desk Structure</b>", h2_style))
    desk_info = (
        "The Credit Lane functions under <b>BRT Corporate Advisory Private Limited</b>. Unlike transactional brokerage agencies, "
        "our desk is personally led by Chartered Accountants, Company Secretaries, and Advocates. We structure every corporate mandate "
        "with rigorous DSCR (Debt Service Coverage Ratio) math, CMA data validation, legal due diligence, and credit rating enhancement."
    )
    story.append(Paragraph(desk_info, body_style))
    story.append(Spacer(1, 10))

    # Certificate Image (IIA Build Bharat Expo 2025)
    cert_img_path = os.path.join(gallery_dir, "BRT CorporateBBE Participation Certificate_page-0001.jpg")
    if os.path.exists(cert_img_path):
        story.append(Paragraph("<b>National Recognition: IIA Build Bharat Expo 2025 Certificate</b>", h2_style))
        img_cert = Image(cert_img_path, width=480, height=310)
        story.append(img_cert)
        story.append(Spacer(1, 4))
        story.append(Paragraph("<b>Figure 2:</b> Certificate of Participation presented to BRT Corporate Advisory by Indian Industries Association (IIA), Hall 6, Bharat Mandapam, New Delhi", ParagraphStyle('Cap2', fontName='Helvetica-Oblique', fontSize=8, textColor=colors.HexColor('#666'), alignment=1)))

    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Key Organizational Highlights:</b>", h2_style))
    highlights = [
        "<b>• Official Participation:</b> Exhibitor & Finance Desk Partner at IIA Build Bharat Expo 2025, Bharat Mandapam.",
        "<b>• ISO Accreditation:</b> Certified ISO 9001:2015 Quality Management System for Corporate Financial Structuring.",
        "<b>• Advisory Expertise:</b> Over ₹500 Crore total capital syndicated across 250+ satisfied industrial & corporate clients.",
        "<b>• Zero Upfront Fee Policy:</b> Complete transparency with fee structures aligned strictly to successful sanction & disbursement."
    ]
    for h in highlights:
        story.append(Paragraph(h, bullet_style))

    story.append(PageBreak())

    # ================= PAGE 3: DEBT SOLUTIONS & FUNDING SPECTRUM (11 SERVICES) =================
    story.append(Paragraph("DEBT SOLUTIONS & COMMERCIAL FUNDING (11 PRODUCTS)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#B8860B'), spaceBefore=2, spaceAfter=10))

    debt_services = [
        ("1. Unsecured Business Loan & DOD Limit", "Working capital & DOD limits up to ₹10 Crore without pledging property or collateral. Instant liquidity for business expansion."),
        ("2. Commercial & Industrial Purchase Loan", "Term loans for purchasing factory land, industrial plots, or commercial office premises with long repayment tenures up to 15 years."),
        ("3. Machine Loan from SIDBI", "Machinery financing on SIDBI's SME-first terms with low interest rates, reduced processing fees, and fast-track approval for MSMEs."),
        ("4. Machine Loan from Bank", "Bank-funded machinery term financing for new equipment acquisition, plant modernization, or capacity expansion."),
        ("5. Sale & Purchase Invoice Finance", "Unlock cash tied up in unpaid customer invoices with fast discounting rates and seamless invoice factoring facilities."),
        ("6. School & College Infrastructure Funding", "Capital term loans for educational institutions, school building construction, labs, and campus infrastructure expansion."),
        ("7. Builder & Real Estate Developers Funding", "Construction financing, project debt, and inventory funding for real estate developers and commercial builders."),
        ("8. Hospital & Medical Funding", "Specialized capital for hospitals, diagnostic centers, medical equipment purchase, and ICU expansion."),
        ("9. Infrastructure & EPC Funding", "Project financing for roads, highways, renewable energy, EPC contractors, and civic infrastructure projects."),
        ("10. Hotel & Resort Funding", "Term loans for hospitality projects, hotel renovation, resort development, and commercial leisure properties."),
        ("11. NPA & Stressed Asset Funding", "Debt restructuring, OTS (One-Time Settlement) funding, and NPA takeover solutions for stressed business accounts.")
    ]

    for title, desc in debt_services:
        story.append(Paragraph(f"<b>{title}</b>", ParagraphStyle('DTitle', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#0B1F3A'), spaceBefore=4, spaceAfter=2)))
        story.append(Paragraph(desc, ParagraphStyle('DDesc', fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor('#444'), spaceAfter=5)))

    story.append(PageBreak())

    # ================= PAGE 4: GOVERNMENT INCENTIVES, EQUITY & VALUATION =================
    story.append(Paragraph("GOVERNMENT SUBSIDIES, EQUITY & CAPITAL MARKETS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#B8860B'), spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>Government Subsidy & Incentive Schemes</b>", h2_style))
    subsidies = [
        ("• UP MSME Promotion Policy 2022:", "15% to 25% Capital Subsidy (up to ₹4 Crore) + 50% Annual Interest Subvention for UP manufacturing units."),
        ("• UP TUS Textile Scheme:", "50% Machinery Subsidy & capital grant for textile, apparel, weaving, and garmenting manufacturing units in Uttar Pradesh."),
        ("• UP MSMY Scheme:", "Micro & Small Enterprise financial assistance scheme with seed capital subsidies and interest rebates.")
    ]
    for s_title, s_desc in subsidies:
        story.append(Paragraph(f"<b>{s_title}</b> {s_desc}", bullet_style))

    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Equity, IPO & Corporate Valuation Services</b>", h2_style))
    equity_services = [
        ("• Pre-IPO Funding:", "Growth equity capital for mature private companies preparing for public listing within 12-24 months."),
        ("• SME IPO Listing:", "End-to-end advisory for listing on NSE Emerge & BSE SME platforms. Valuation, DRHP filing, and merchant banking coordination."),
        ("• Main Board IPO Listing:", "Comprehensive public market listing management for large enterprises on NSE Main Board & BSE Main Board."),
        ("• Venture Funding:", "Institutional VC syndication (Seed, Series A & Series B) for high-growth tech & tech-enabled startups."),
        ("• Business Valuation Services:", "Registered Valuer certified valuation reports for M&A transactions, FEMA compliance, income tax & investor pitch decks.")
    ]
    for e_title, e_desc in equity_services:
        story.append(Paragraph(f"<b>{e_title}</b> {e_desc}", bullet_style))

    story.append(Spacer(1, 14))

    # Gallery Photo Collage Table on Page 4
    story.append(Paragraph("<b>Exhibition Highlights Gallery Preview</b>", h2_style))
    p1 = os.path.join(gallery_dir, "WhatsApp Image 2026-08-11 at 10.10.24 (1).jpeg")
    p2 = os.path.join(gallery_dir, "WhatsApp Image 2026-08-11 at 10.10.25 (1).jpeg")
    p3 = os.path.join(gallery_dir, "WhatsApp Image 2026-08-11 at 10.10.26.jpeg")

    gallery_cells = []
    for path in [p1, p2, p3]:
        if os.path.exists(path):
            gallery_cells.append(Image(path, width=160, height=100))

    if len(gallery_cells) == 3:
        t_gal = Table([gallery_cells], colWidths=[170, 170, 170])
        t_gal.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
            ('PADDING', (0,0), (-1,-1), 4)
        ]))
        story.append(t_gal)

    story.append(PageBreak())

    # ================= PAGE 5: COMPLETE EXHIBITION PHOTO DOSSIER (23 PHOTOS GRID) =================
    story.append(Paragraph("OFFICIAL COMPANY PHOTO DOSSIER (EXHIBITIONS & SUMMITS)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#B8860B'), spaceBefore=2, spaceAfter=10))
    story.append(Paragraph("Exhibitions, Build Bharat Expo 2025 moments, team advisory sessions, client presentations & founder keynotes.", body_style))
    story.append(Spacer(1, 8))

    photo_files = [
        "WhatsApp Image 2026-08-11 at 10.10.23.jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.24 (1).jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.24 (2).jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.24.jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.25 (1).jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.25 (2).jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.25.jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.26 (1).jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.26.jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.27 (1).jpeg",
        "WhatsApp Image 2026-08-11 at 10.10.27 (2).jpeg",
        "image copy 4.png"
    ]

    rows = []
    current_row = []
    for fname in photo_files:
        fpath = os.path.join(gallery_dir, fname)
        if os.path.exists(fpath):
            img_obj = Image(fpath, width=120, height=80)
            current_row.append(img_obj)
            if len(current_row) == 4:
                rows.append(current_row)
                current_row = []
    if current_row:
        while len(current_row) < 4:
            current_row.append(Spacer(1, 1))
        rows.append(current_row)

    if rows:
        t_photos = Table(rows, colWidths=[128, 128, 128, 128])
        t_photos.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#F1F5F9')),
            ('PADDING', (0,0), (-1,-1), 4)
        ]))
        story.append(t_photos)

    story.append(Spacer(1, 14))
    story.append(Paragraph("<b>End of Official Corporate Brochure Dossier — The Credit Lane</b>", ParagraphStyle('EndDoc', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#0B1F3A'), alignment=1)))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated multi-page brochure PDF: {out_pdf_theme}")

    # Copy to root and about/ directory
    import shutil
    shutil.copy(out_pdf_theme, out_pdf_root)
    about_dir_pdf = "/Users/aadityamohansamadhiya/the credit lane/about/The-Credit-Lane-Brochure.pdf"
    if os.path.exists(os.path.dirname(about_dir_pdf)):
        shutil.copy(out_pdf_theme, about_dir_pdf)

if __name__ == "__main__":
    build_pdf()
