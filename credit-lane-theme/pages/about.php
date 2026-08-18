<?php
/**
 * Template for about.php - Complete Team, Founders, Events & Photo Gallery
 */
$gallery_base = get_template_directory_uri() . '/assets/images/gallery/';
?>

    <!-- ============ HERO BANNER ============ -->
    <section class="service-banner" style="padding-bottom: 50px;">
      <div class="wrap">
        <div>
          <span class="eyebrow" style="color:var(--gold-light);">OUR PROFILE</span>
          <h1 style="max-width: 100%; font-size: clamp(32px, 4vw, 48px); line-height: 1.2;">Capital decisions deserve more than a generic answer.</h1>
          <p class="lead" style="max-width: 100%; font-size: 17px; color: rgba(255,255,255,0.85); margin-top: 14px;">Meet Rajat Garg and our advisory team of Chartered Accountants, Company Secretaries, and Legal Advocates driving transparent corporate capitalization across India.</p>
        </div>
        <div class="service-banner-art" style="display: flex; align-items: center; justify-content: center; width: 100%;">
          <div style="width: 100%; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 20px; padding: 10px; box-shadow: 0 15px 40px rgba(0,0,0,0.35);">
            <img src="<?php echo $gallery_base; ?>WhatsApp Image 2026-08-11 at 10.10.23.jpeg" alt="The Credit Lane Founders & Leadership Team" style="width: 100%; height: auto; max-height: 440px; object-fit: contain; border-radius: 14px; display: block;">
            <div style="text-align: center; padding: 8px 0 4px; color: var(--gold-light); font-size: 12.5px; font-weight: 600; letter-spacing: 0.03em;">
              ⭐ Rajat Garg & Executive Leadership at Build Bharat Expo 2025
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ MANDATE STORY ============ -->
    <section style="padding: 70px 0; background: var(--offwhite);">
      <div class="wrap">
        <div class="about-story" style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 48px; align-items: center;">
          <div>
            <span class="eyebrow">OUR MANDATE</span>
            <h2 style="font-size: 34px; margin-top: 12px; margin-bottom: 20px; color: var(--navy-dark); font-family: var(--font-serif);">Positioning Indian MSMEs & Enterprises for Capital Readiness.</h2>
            <p style="color: var(--slate); font-size: 15px; line-height: 1.7; margin-bottom: 16px;">The Credit Lane was founded by Rajat Garg on a core commitment: Indian business promoters deserve direct advisory from CAs, CSs, and Advocates who understand balance sheets, bank credit committees, and government grant schemes.</p>
            <p style="color: var(--slate); font-size: 15px; line-height: 1.7; margin-bottom: 16px;">We operate as a single relationship desk coordinating debt structuring, SIDBI machine loans, public market listings (SME & Mainboard IPO), statutory valuation files, and Uttar Pradesh government promotion schemes (TUS, MSME Policy, MSMY).</p>
            <p style="color: var(--slate); font-size: 15px; line-height: 1.7; margin-bottom: 28px;">Headquartered in Ghaziabad (Delhi NCR), we ensure our clients submit clean, audit-backed applications that move through lender committees without friction.</p>
            
            <div style="display: flex; gap: 16px; flex-wrap: wrap; align-items: center;">
              <a href="<?php echo esc_url(home_url('/contact/')); ?>" class="btn btn-primary" style="padding: 14px 28px; font-size: 15px; font-weight: 700; box-shadow: 0 6px 20px rgba(184,134,11,0.25);">Talk to Our Founders &rarr;</a>
              <a href="#brochure" class="btn btn-outline-dark" style="padding: 14px 28px; font-size: 15px; font-weight: 600; border-color: var(--navy-dark); color: var(--navy-dark);">Download Corporate Brochure 📄</a>
            </div>
          </div>

          <div class="about-graphics" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; border-radius: 20px; border: 1px solid var(--line); background: var(--white); box-shadow: 0 10px 30px rgba(0,0,0,0.06);">
            <div style="width: 100%; height: 260px; overflow: hidden; position: relative;">
              <img src="<?php echo $gallery_base; ?>image copy 16.png" alt="Build Bharat Expo Showcase" style="width: 100%; height: 100%; object-fit: cover; object-position: center; display: block;">
            </div>
            <div style="padding: 28px 24px; text-align: center;">
              <div class="about-logo-wrapper" style="margin: 0 auto 14px; display: inline-block;">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/images/logo.png" alt="The Credit Lane Logo" style="width: 60px; height: 60px; object-fit: contain; border-radius: 12px; padding: 6px; background: #fff; box-shadow: 0 4px 14px rgba(0,0,0,0.1); border: 1px solid var(--line);">
              </div>
              <h3 style="font-family: var(--font-serif); font-size: 22px; color: var(--navy-dark); margin-bottom: 8px;">Transparent. Methodical. Advisory-First.</h3>
              <p style="color: var(--slate); font-size: 14px; line-height: 1.6; margin: 0;">Channel partners to 100+ scheduled banks, industrial NBFCs, equity syndicates, and government grant portals across Delhi NCR and India.</p>
            </div>
          </div>
        </div>

        <!-- Core Value Pillars -->
        <div class="values-grid" style="margin-top: 50px; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
          <div class="value-card" style="background: var(--white); border: 1px solid var(--line); border-radius: 16px; padding: 28px; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
            <div class="icon-box" style="width: 44px; height: 44px; border-radius: 50%; background: rgba(184,134,11,0.12); color: var(--gold); font-size: 20px; font-weight: 800; display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">✓</div>
            <h4 style="font-size: 18px; color: var(--navy-dark); margin-bottom: 8px;">CA, CS &amp; Advocate Led</h4>
            <p style="color: var(--slate); font-size: 13.5px; line-height: 1.6; margin: 0;">Direct professional oversight by Chartered Accountants, Company Secretaries, and Legal Advocates for 100% statutory & credit compliance.</p>
          </div>
          <div class="value-card" style="background: var(--white); border: 1px solid var(--line); border-radius: 16px; padding: 28px; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
            <div class="icon-box" style="width: 44px; height: 44px; border-radius: 50%; background: rgba(184,134,11,0.12); color: var(--gold); font-size: 20px; font-weight: 800; display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">✓</div>
            <h4 style="font-size: 18px; color: var(--navy-dark); margin-bottom: 8px;">Advisory-Led Matching</h4>
            <p style="color: var(--slate); font-size: 13.5px; line-height: 1.6; margin: 0;">We diagnose credit ratings, DSCR ratios, and asset commissions before submitting files to prevent database dings and rejections.</p>
          </div>
          <div class="value-card" style="background: var(--white); border: 1px solid var(--line); border-radius: 16px; padding: 28px; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
            <div class="icon-box" style="width: 44px; height: 44px; border-radius: 50%; background: rgba(184,134,11,0.12); color: var(--gold); font-size: 20px; font-weight: 800; display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">✓</div>
            <h4 style="font-size: 18px; color: var(--navy-dark); margin-bottom: 8px;">No Hidden Brokerages</h4>
            <p style="color: var(--slate); font-size: 13.5px; line-height: 1.6; margin: 0;">We disclose processing charges, audit expectations, collateral criteria, and covenants upfront. Zero upfront advisory charge.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ FOUNDERS & CORE LEADERSHIP ============ -->
    <section class="section-tight" style="background-color: var(--white); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 80px 0;">
      <div class="wrap">
        <div class="section-head center" style="margin-bottom: 48px; text-align: center;">
          <span class="eyebrow">FOUNDERS &amp; LEADERSHIP</span>
          <h2 style="font-size: 34px; color: var(--navy-dark); font-family: var(--font-serif); margin-top: 6px;">Meet the Team Behind The Credit Lane</h2>
          <p style="font-size: 16px; color: var(--slate); max-width: 680px; margin: 8px auto 0;">Led by Rajat Garg and our co-founders across CA, CS, and Corporate Legal disciplines.</p>
        </div>

        <div class="founders-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px;">
          <!-- Founder 1: Rajat Garg -->
          <div class="founder-card" style="background: var(--offwhite); border: 1px solid var(--line); border-radius: 18px; overflow: hidden; box-shadow: 0 6px 24px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
            <div style="height: 340px; overflow: hidden; position: relative;">
              <img src="<?php echo $gallery_base; ?>image copy 15.png" alt="Rajat Garg - Founder & Managing Director" style="width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block;">
            </div>
            <div style="padding: 24px;">
              <span style="font-size: 11px; font-weight: 700; color: var(--gold); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 6px;">FOUNDER &amp; MANAGING DIRECTOR</span>
              <h3 style="font-size: 22px; color: var(--navy-dark); font-family: var(--font-serif); margin-bottom: 8px;">Rajat Garg</h3>
              <p style="font-size: 14px; color: var(--slate); line-height: 1.6; margin-bottom: 18px;">Leading corporate debt syndication, SIDBI machinery loans, equity advisory, and UP Government grants desk.</p>
              <a href="tel:9217924499" style="display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: var(--navy-dark); text-decoration: none;">📞 Contact Rajat Garg &rarr;</a>
            </div>
          </div>

          <!-- Founder 2: Co-Founder Financial Advisory -->
          <div class="founder-card" style="background: var(--offwhite); border: 1px solid var(--line); border-radius: 18px; overflow: hidden; box-shadow: 0 6px 24px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
            <div style="height: 340px; overflow: hidden; position: relative;">
              <img src="<?php echo $gallery_base; ?>image copy 2.png" alt="Co-Founder - Financial Advisory & Credit Underwriting" style="width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block;">
            </div>
            <div style="padding: 24px;">
              <span style="font-size: 11px; font-weight: 700; color: var(--gold); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 6px;">CO-FOUNDER &amp; DEBT HEAD</span>
              <h3 style="font-size: 22px; color: var(--navy-dark); font-family: var(--font-serif); margin-bottom: 8px;">Co-Founder (Financial Advisory)</h3>
              <p style="font-size: 14px; color: var(--slate); line-height: 1.6; margin-bottom: 18px;">Overseeing banking committee relations, credit underwriting, drop-line overdrafts &amp; project finance.</p>
              <span style="font-size: 14px; font-weight: 700; color: var(--navy-dark);">Credit Committee Advisory Desk</span>
            </div>
          </div>

          <!-- Founder 3: Co-Founder Legal & Compliance -->
          <div class="founder-card" style="background: var(--offwhite); border: 1px solid var(--line); border-radius: 18px; overflow: hidden; box-shadow: 0 6px 24px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
            <div style="height: 340px; overflow: hidden; position: relative;">
              <img src="<?php echo $gallery_base; ?>image copy 3.png" alt="Co-Founder - Legal & Compliance Chambers" style="width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block;">
            </div>
            <div style="padding: 24px;">
              <span style="font-size: 11px; font-weight: 700; color: var(--gold); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 6px;">CO-FOUNDER &amp; LEGAL HEAD</span>
              <h3 style="font-size: 22px; color: var(--navy-dark); font-family: var(--font-serif); margin-bottom: 8px;">Co-Founder (Legal &amp; Compliance)</h3>
              <p style="font-size: 14px; color: var(--slate); line-height: 1.6; margin-bottom: 18px;">Advocate &amp; CS leading statutory due diligence, title clearances, SME IPO filings &amp; grant compliance.</p>
              <span style="font-size: 14px; font-weight: 700; color: var(--navy-dark);">Legal Chambers &amp; CS Desk</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ BUILD BHARAT EXPO & EVENTS PARTICIPATION ============ -->
    <section style="padding: 80px 0; background: var(--offwhite);">
      <div class="wrap">
        <div class="section-head center" style="margin-bottom: 48px; text-align: center;">
          <span class="eyebrow">NATIONAL EXPOS &amp; EVENTS</span>
          <h2 style="font-size: 34px; color: var(--navy-dark); font-family: var(--font-serif);">Build Bharat Expo 2025 &amp; World Startup Convention</h2>
          <p style="font-size: 16px; color: var(--slate); max-width: 700px; margin: 8px auto 0;">The Credit Lane actively represents Indian MSMEs at national trade expos, investor summits, and government forums.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; align-items: stretch; margin-bottom: 48px;">
          <!-- Certificate Card -->
          <div style="background: #fff; padding: 24px; border-radius: 18px; border: 1px solid var(--line); box-shadow: 0 8px 30px rgba(0,0,0,0.06); text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span style="font-size: 12px; font-weight: 700; color: var(--gold); text-transform: uppercase; display: block; margin-bottom: 8px;">OFFICIAL PARTICIPATION CERTIFICATE</span>
              <h3 style="font-size: 20px; color: var(--navy-dark); margin-bottom: 16px; font-family: var(--font-serif);">Build Bharat Expo 2025 - Hall 6 Stall D19</h3>
              <div style="overflow: hidden; border-radius: 12px; border: 1px solid var(--line); margin-bottom: 12px; cursor: pointer;" onclick="openGalleryModal('<?php echo $gallery_base; ?>BRT CorporateBBE Participation Certificate_page-0001.jpg')">
                <img src="<?php echo $gallery_base; ?>BRT CorporateBBE Participation Certificate_page-0001.jpg" alt="Build Bharat Expo 2025 Participation Certificate" style="width: 100%; height: auto; display: block; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
              </div>
            </div>
            <p style="font-size: 13px; color: var(--slate); margin: 0;">Certified by Indian Industries Association (IIA) for exhibiting at Bharat Mandapam, New Delhi.</p>
          </div>

          <!-- Booth Showcase Card -->
          <div style="background: #fff; padding: 24px; border-radius: 18px; border: 1px solid var(--line); box-shadow: 0 8px 30px rgba(0,0,0,0.06); text-align: center; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span style="font-size: 12px; font-weight: 700; color: var(--gold); text-transform: uppercase; display: block; margin-bottom: 8px;">EXHIBITION STALL &amp; ADVISORY DESK</span>
              <h3 style="font-size: 20px; color: var(--navy-dark); margin-bottom: 16px; font-family: var(--font-serif);">On-Ground Client Consultations</h3>
              <div style="overflow: hidden; border-radius: 12px; border: 1px solid var(--line); margin-bottom: 12px; cursor: pointer;" onclick="openGalleryModal('<?php echo $gallery_base; ?>WhatsApp Image 2026-08-11 at 10.10.23.jpeg')">
                <img src="<?php echo $gallery_base; ?>WhatsApp Image 2026-08-11 at 10.10.23.jpeg" alt="The Credit Lane Exhibition Booth" style="width: 100%; height: auto; max-height: 320px; object-fit: cover; display: block; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
              </div>
            </div>
            <p style="font-size: 13px; color: var(--slate); margin: 0;">Rajat Garg &amp; team conducting live funding feasibility reviews for MSME business owners.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ COMPLETE PHOTO GALLERY ============ -->
    <section style="padding: 80px 0; background: var(--white); border-top: 1px solid var(--line);">
      <div class="wrap">
        <div class="section-head center" style="margin-bottom: 44px; text-align: center;">
          <span class="eyebrow">PHOTO GALLERY</span>
          <h2 style="font-size: 34px; color: var(--navy-dark); font-family: var(--font-serif);">Our Journey in Pictures</h2>
          <p style="font-size: 16px; color: var(--slate);">Exhibitions, team moments, founder presentations, and Build Bharat Expo highlights.</p>
        </div>

        <div class="gallery-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 20px;">
          <?php
          $gallery_images = [
            'WhatsApp Image 2026-08-11 at 10.10.23.jpeg' => 'Build Bharat Expo Stall D19',
            'WhatsApp Image 2026-08-11 at 10.10.24 (1).jpeg' => 'Team Advisory Session',
            'WhatsApp Image 2026-08-11 at 10.10.24 (2).jpeg' => 'Exhibition Booth Interaction',
            'WhatsApp Image 2026-08-11 at 10.10.24.jpeg' => 'Client Consultation Desk',
            'WhatsApp Image 2026-08-11 at 10.10.25 (1).jpeg' => 'MSME Advisory Session',
            'WhatsApp Image 2026-08-11 at 10.10.25 (2).jpeg' => 'The Credit Lane Booth Banner',
            'WhatsApp Image 2026-08-11 at 10.10.25.jpeg' => 'Build Bharat Expo Team',
            'WhatsApp Image 2026-08-11 at 10.10.26 (1).jpeg' => 'Client Funding Discussion',
            'WhatsApp Image 2026-08-11 at 10.10.26.jpeg' => 'Exhibition Client Presentation',
            'WhatsApp Image 2026-08-11 at 10.10.27 (1).jpeg' => 'Build Bharat Expo Highlights',
            'WhatsApp Image 2026-08-11 at 10.10.27 (2).jpeg' => 'Team Group Photo',
            'image copy 4.png' => 'World Startup Convention',
            'image copy 5.png' => 'Startup Summit Presentation',
            'image copy 6.png' => 'Founders Keynote',
            'image copy 7.png' => 'Industry Networking Session',
            'image copy 8.png' => 'Corporate Finance Panel',
            'image copy 9.png' => 'Investor Meetup',
            'image copy 10.png' => 'Banking Syndication Event',
            'image copy 11.png' => 'Exhibition Floor Session',
            'image copy 12.png' => 'Trade Expo Booth',
            'image copy 13.png' => 'Build Bharat Expo Overview',
            'image copy 16.png' => 'Build Bharat Expo 2025 Showcase',
            'image copy 17.png' => 'The Credit Lane Team Presentation'
          ];

          foreach ($gallery_images as $img_filename => $caption):
          ?>
            <div class="gallery-item" style="position: relative; overflow: hidden; border-radius: 14px; height: 210px; border: 1px solid var(--line); cursor: pointer; box-shadow: 0 4px 14px rgba(0,0,0,0.04);" onclick="openGalleryModal('<?php echo $gallery_base . $img_filename; ?>')">
              <img src="<?php echo $gallery_base . $img_filename; ?>" alt="<?php echo esc_attr($caption); ?>" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.35 ease;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform='scale(1)'">
              <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 12px 14px; background: linear-gradient(transparent, rgba(11,31,58,0.9)); color: #fff; font-size: 12px; font-weight: 600;">
                <?php echo esc_html($caption); ?>
              </div>
            </div>
          <?php endforeach; ?>
        </div>
      </div>
    </section>

    <!-- ============ COMPANY BROCHURE & PROFILE SHOWCASE ============ -->
    <section id="brochure" style="padding: 80px 0; background: var(--navy-dark); color: #fff;">
      <div class="wrap">
        <div style="text-align: center; max-width: 850px; margin: 0 auto 48px;">
          <span style="font-size: 12px; font-weight: 700; color: var(--gold-light); text-transform: uppercase; letter-spacing: 0.12em; display: block; margin-bottom: 8px;">OFFICIAL CORPORATE BROCHURE &amp; COMPLETE COMPANY DOSSIER</span>
          <h2 style="color: #fff; font-family: var(--font-serif); font-size: clamp(28px, 4vw, 42px); margin-bottom: 16px;">The Credit Lane Complete Brochure &amp; Achievements Showcase</h2>
          <p style="color: var(--slate-light); font-size: 16px; line-height: 1.6; margin-bottom: 24px;">BRT Corporate Advisory Pvt. Ltd. — CA, CS and Advocate-led Corporate Finance Desk. Complete company profile covering Debt Syndication, SIDBI Machinery Funding, Public Market IPOs, Government Subsidies, Exhibition Credentials &amp; Certifications.</p>
          <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
            <a href="<?php echo esc_url(get_template_directory_uri() . '/assets/docs/The-Credit-Lane-Company-Brochure.pdf?v=1.2.4'); ?>" download="The-Credit-Lane-Company-Brochure.pdf" target="_blank" class="btn btn-primary" style="padding: 16px 36px; font-size: 16px; font-weight: 700; box-shadow: 0 10px 30px rgba(184,134,11,0.3);">📥 Download Official Brochure PDF (Direct File)</a>
            <a href="tel:9217924499" class="btn btn-secondary" style="padding: 16px 28px; font-size: 15px; border-color: rgba(255,255,255,0.25); color: #fff;">📞 Speak With Founder Desk</a>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 28px; margin-top: 40px;">
          <!-- Card 1: Corporate Profile & Advisory Desk -->
          <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); border-radius: 18px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span style="color: var(--gold-light); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">COMPANY OVERVIEW</span>
              <h3 style="color: #fff; font-size: 20px; font-family: var(--font-serif); margin-bottom: 12px;">BRT Corporate Advisory Pvt. Ltd.</h3>
              <p style="color: #CBD5E1; font-size: 13.5px; line-height: 1.6; margin-bottom: 16px;">Premier CA, CS &amp; Advocate-led corporate finance desk assisting Indian enterprises in capital structuring, SIDBI machine loans, equity syndication, and government grant sanctions.</p>
              <ul style="color: #CBD5E1; font-size: 13px; line-height: 1.8; padding-left: 18px; margin-bottom: 16px;">
                <li><strong>HQ Address:</strong> B 31 First Floor, Raj Nagar, Ghaziabad 201001</li>
                <li><strong>Official Email:</strong> Info@thecreditlane.in</li>
                <li><strong>Helplines:</strong> +91 9217924499 / 9818709747</li>
                <li><strong>Credentials:</strong> ISO 9001:2015 Quality Certified</li>
              </ul>
            </div>
            <a href="tel:9217924499" style="color: var(--gold-light); font-weight: 700; font-size: 13.5px; text-decoration: none;">📞 Contact Desk Directly &rarr;</a>
          </div>

          <!-- Card 2: Complete Service Offerings Portfolio -->
          <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); border-radius: 18px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span style="color: var(--gold-light); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">SOLUTIONS SPECTRUM</span>
              <h3 style="color: #fff; font-size: 20px; font-family: var(--font-serif); margin-bottom: 12px;">Complete Financial Offerings</h3>
              <div style="color: #CBD5E1; font-size: 13px; line-height: 1.7;">
                <p style="margin-bottom: 8px;"><strong style="color:#fff;">• Debt Solutions:</strong> Unsecured Business Loans, SIDBI &amp; Bank Machinery Loans, Invoice Discounting, Builder &amp; Real Estate Funding, Hospital &amp; School Infrastructure, NPA Resolution.</p>
                <p style="margin-bottom: 8px;"><strong style="color:#fff;">• Government Incentives:</strong> UP MSME Policy 2022 (25% Subsidy + 50% Subvention), UP TUS Textile Scheme (50% Grant), UP MSMY Scheme.</p>
                <p style="margin: 0;"><strong style="color:#fff;">• Equity &amp; Capital Markets:</strong> Pre-IPO Funding, SME IPO &amp; Main Board IPO Listing, Venture Capital, Valuation Services.</p>
              </div>
            </div>
            <a href="<?php echo esc_url(home_url('/loans/')); ?>" style="color: var(--gold-light); font-weight: 700; font-size: 13.5px; text-decoration: none; margin-top: 16px;">Explore All Services &rarr;</a>
          </div>

          <!-- Card 3: 3 Co-Founders Leadership Team -->
          <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); border-radius: 18px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span style="color: var(--gold-light); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">EXECUTIVE LEADERSHIP</span>
              <h3 style="color: #fff; font-size: 20px; font-family: var(--font-serif); margin-bottom: 12px;">3 Co-Founders Desk</h3>
              <div style="width: 100%; height: 150px; border-radius: 12px; overflow: hidden; margin-bottom: 14px; border: 1px solid rgba(255,255,255,0.15); cursor: pointer;" onclick="openGalleryModal('<?php echo $gallery_base; ?>WhatsApp Image 2026-08-11 at 10.10.23.jpeg')">
                <img src="<?php echo $gallery_base; ?>WhatsApp Image 2026-08-11 at 10.10.23.jpeg" alt="The Credit Lane 3 Co-Founders" style="width: 100%; height: 100%; object-fit: cover;">
              </div>
              <p style="color: #CBD5E1; font-size: 13.5px; line-height: 1.6; margin: 0;">Led by <strong>Rajat Garg</strong> (Founder &amp; MD) together with Co-Founders heading Credit Committee Structuring &amp; Legal Compliance Chambers.</p>
            </div>
            <span style="color: var(--gold-light); font-weight: 700; font-size: 13.5px; cursor: pointer; margin-top: 14px;" onclick="openGalleryModal('<?php echo $gallery_base; ?>WhatsApp Image 2026-08-11 at 10.10.23.jpeg')">🔍 View Leadership Photo &rarr;</span>
          </div>

          <!-- Card 4: Certificates & National Recognition Showcase -->
          <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); border-radius: 18px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span style="color: var(--gold-light); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">ALL CERTIFICATES &amp; RECOGNITIONS</span>
              <h3 style="color: #fff; font-size: 20px; font-family: var(--font-serif); margin-bottom: 12px;">Certificates &amp; Awards</h3>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 14px;">
                <div style="height: 100px; border-radius: 8px; overflow: hidden; border: 1px solid rgba(255,255,255,0.2); cursor: pointer;" onclick="openGalleryModal('<?php echo $gallery_base; ?>BRT CorporateBBE Participation Certificate_page-0001.jpg')">
                  <img src="<?php echo $gallery_base; ?>BRT CorporateBBE Participation Certificate_page-0001.jpg" alt="IIA Build Bharat Expo 2025 Certificate" style="width: 100%; height: 100%; object-fit: cover; object-position: top;" title="IIA Build Bharat Expo 2025 Certificate">
                </div>
                <div style="height: 100px; border-radius: 8px; overflow: hidden; border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.08); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 8px; text-align: center;">
                  <span style="font-size: 22px;">🏅</span>
                  <span style="font-size: 11px; font-weight: 700; color: var(--gold-light);">ISO 9001:2015</span>
                  <span style="font-size: 10px; color: #CBD5E1;">Corporate Quality</span>
                </div>
              </div>
              <p style="color: #CBD5E1; font-size: 13px; line-height: 1.5; margin: 0;">Includes IIA Build Bharat Expo 2025 Participation Certificate (Bharat Mandapam, New Delhi) and ISO 9001:2015 Quality Standards.</p>
            </div>
            <span style="color: var(--gold-light); font-weight: 700; font-size: 13.5px; cursor: pointer; margin-top: 14px;" onclick="openGalleryModal('<?php echo $gallery_base; ?>BRT CorporateBBE Participation Certificate_page-0001.jpg')">📜 View IIA Certificate &rarr;</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ LIGHTBOX MODAL ============ -->
    <div id="galleryModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: rgba(0,0,0,0.92); z-index: 99999; align-items: center; justify-content: center; padding: 20px;" onclick="closeGalleryModal()">
      <span style="position: absolute; top: 20px; right: 30px; color: #fff; font-size: 36px; cursor: pointer; font-weight: 700;">✕</span>
      <img id="galleryModalImg" src="" alt="Enlarged Photo" style="max-width: 92%; max-height: 88vh; border-radius: 12px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 10px 40px rgba(0,0,0,0.6);">
    </div>

    <script>
      function openGalleryModal(src) {
        var modal = document.getElementById("galleryModal");
        var modalImg = document.getElementById("galleryModalImg");
        if (modal && modalImg) {
          modalImg.src = src;
          modal.style.display = "flex";
        }
      }
      function closeGalleryModal() {
        var modal = document.getElementById("galleryModal");
        if (modal) modal.style.display = "none";
      }
    </script>
