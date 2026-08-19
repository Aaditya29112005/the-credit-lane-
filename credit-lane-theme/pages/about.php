<?php
/**
 * Template for about.php - Complete Team, Founders, Events & Photo Gallery
 */
$gallery_base = get_template_directory_uri() . '/assets/images/gallery/';
?>

    <!-- ============ HERO BANNER ============ -->
    <section class="service-banner" style="padding: 80px 0 60px; background: linear-gradient(135deg, #0B1F3A 0%, #071529 100%);">
      <div class="wrap">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 48px; align-items: center;">
          <div style="text-align: left;">
            <span class="eyebrow" style="color: var(--gold-light); display: inline-block; margin-bottom: 12px; font-weight: 700; letter-spacing: 0.1em;">OUR PROFILE</span>
            <h1 style="font-size: clamp(32px, 4vw, 48px); line-height: 1.2; color: #FFFFFF; font-family: var(--font-serif); margin-bottom: 20px;">Capital decisions deserve more than a generic answer.</h1>
            <p class="lead" style="font-size: 16.5px; color: rgba(255,255,255,0.85); line-height: 1.65; margin-bottom: 28px;">
              Meet our advisory team of Chartered Accountants, Company Secretaries, and Legal Advocates driving transparent corporate capitalization, debt syndication, equity advisory, and government subsidy filings across India.
            </p>
            
            <div style="display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 32px;">
              <a href="#promoters" class="btn btn-primary" style="padding: 14px 28px; font-size: 15px; font-weight: 700; box-shadow: 0 6px 20px rgba(184,134,11,0.3);">Meet Our Leadership &rarr;</a>
              <a href="#mandate" class="btn btn-outline" style="padding: 14px 28px; font-size: 15px; font-weight: 600;">Our Advisory Mandate</a>
            </div>

            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); border-radius: 16px; padding: 18px; text-align: center;">
              <div>
                <div style="color: var(--gold-light); font-size: 22px; font-weight: 800; font-family: var(--font-serif);">₹500+ Cr</div>
                <div style="color: rgba(255,255,255,0.7); font-size: 11.5px; margin-top: 2px;">Capital Structured</div>
              </div>
              <div style="border-left: 1px solid rgba(255,255,255,0.1); border-right: 1px solid rgba(255,255,255,0.1);">
                <div style="color: var(--gold-light); font-size: 22px; font-weight: 800; font-family: var(--font-serif);">CA / CS / Law</div>
                <div style="color: rgba(255,255,255,0.7); font-size: 11.5px; margin-top: 2px;">Direct Oversight</div>
              </div>
              <div>
                <div style="color: var(--gold-light); font-size: 22px; font-weight: 800; font-family: var(--font-serif);">100+</div>
                <div style="color: rgba(255,255,255,0.7); font-size: 11.5px; margin-top: 2px;">Lender Empanelments</div>
              </div>
            </div>
          </div>

          <div style="position: relative;">
            <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 20px; padding: 12px; box-shadow: 0 20px 50px rgba(0,0,0,0.4); overflow: hidden; cursor: pointer;" onclick="openGalleryModal('<?php echo $gallery_base; ?>image copy 8.png')">
              <img src="<?php echo $gallery_base; ?>image copy 8.png" alt="The Credit Lane Executive Team &amp; Office" style="width: 100%; height: 380px; object-fit: cover; border-radius: 12px; display: block;">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ MANDATE STORY ============ -->
    <section id="mandate" style="padding: 70px 0; background: var(--offwhite);">
      <div class="wrap">
        <div class="about-story" style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 48px; align-items: center;">
          <div>
            <span class="eyebrow" style="color: var(--gold); font-weight: 700;">OUR MANDATE</span>
            <h2 style="font-size: 34px; margin-top: 8px; margin-bottom: 20px; color: var(--navy-dark); font-family: var(--font-serif);">Positioning Indian MSMEs &amp; Enterprises for Capital Readiness.</h2>
            <p style="color: var(--slate); font-size: 15px; line-height: 1.7; margin-bottom: 16px;">The Credit Lane was founded on a core commitment: Indian business promoters deserve direct advisory from CAs, CSs, and Advocates who understand balance sheets, bank credit committees, and government grant schemes.</p>
            <p style="color: var(--slate); font-size: 15px; line-height: 1.7; margin-bottom: 16px;">We operate as a single relationship desk coordinating debt structuring, SIDBI machine loans, public market listings (SME &amp; Mainboard IPO), statutory valuation files, and Uttar Pradesh government promotion schemes (TUS, MSME Policy, MSMY).</p>
            <p style="color: var(--slate); font-size: 15px; line-height: 1.7; margin-bottom: 28px;">Headquartered in Ghaziabad (Delhi NCR), we ensure our clients submit clean, audit-backed applications that move through lender committees without friction.</p>
            
            <div style="display: flex; gap: 16px; flex-wrap: wrap; align-items: center;">
              <a href="<?php echo esc_url(home_url('/contact/')); ?>" class="btn btn-primary" style="padding: 14px 28px; font-size: 15px; font-weight: 700; box-shadow: 0 6px 20px rgba(184,134,11,0.25);">Talk to Our Team &rarr;</a>
              <a href="#brochure" class="btn btn-outline-dark" style="padding: 14px 28px; font-size: 15px; font-weight: 600; border-color: var(--navy-dark); color: var(--navy-dark);">Download Corporate Brochure 📄</a>
            </div>
          </div>

          <div class="about-graphics" style="padding: 32px 28px; overflow: hidden; display: flex; flex-direction: column; border-radius: 20px; border: 1px solid #E2DDD5; border-top: 4px solid #C89B3C; background: var(--white); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <div class="about-logo-wrapper" style="margin: 0 auto 16px; display: inline-block;">
              <img src="<?php echo get_template_directory_uri(); ?>/assets/images/logo.png" alt="The Credit Lane Logo" style="width: 70px; height: 70px; object-fit: contain; border-radius: 14px; padding: 8px; background: #fff; box-shadow: 0 4px 14px rgba(0,0,0,0.08); border: 1px solid #E2DDD5;">
            </div>
            <h3 style="font-family: var(--font-serif); font-size: 22px; color: var(--navy-dark); text-align: center; margin-bottom: 12px;">Transparent. Methodical. Advisory-First.</h3>
            <p style="color: var(--slate); font-size: 14px; line-height: 1.65; text-align: center; margin: 0 0 20px;">Empaneled advisory channel to 100+ scheduled banks, industrial NBFCs, equity syndicates, and government grant portals across Delhi NCR and India.</p>
            <div style="background: #FAF8F5; border-radius: 12px; padding: 16px; border: 1px solid #E2DDD5; text-align: center;">
              <span style="font-size: 12px; font-weight: 700; color: #C89B3C; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 4px;">EXECUTIVE ADVISORY DESK</span>
              <span style="font-size: 13px; color: #0B1F3A; font-weight: 600;">HQ: B 31 First Floor, Raj Nagar, Ghaziabad 201001</span>
            </div>
          </div>
        </div>

        <!-- Core Value Pillars -->
        <div class="values-grid" style="margin-top: 50px; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
          <div class="value-card" style="background: var(--white); border: 1px solid var(--line); border-radius: 16px; padding: 28px; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
            <div class="icon-box" style="width: 44px; height: 44px; border-radius: 50%; background: rgba(184,134,11,0.12); color: var(--gold); font-size: 20px; font-weight: 800; display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">✓</div>
            <h4 style="font-size: 18px; color: var(--navy-dark); margin-bottom: 8px;">CA, CS &amp; Advocate Led</h4>
            <p style="color: var(--slate); font-size: 13.5px; line-height: 1.6; margin: 0;">Direct professional oversight by Chartered Accountants, Company Secretaries, and Legal Advocates for 100% statutory &amp; credit compliance.</p>
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

    <!-- ============ PROFILE OF PROMOTERS & LEADERSHIP ============ -->
    <section class="section-tight" id="promoters" style="background-color: var(--white); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 80px 0;">
      <div class="wrap">
        <div class="section-head center" style="margin-bottom: 40px; text-align: center;">
          <span class="eyebrow" style="color: var(--gold); font-weight: 700;">EXECUTIVE LEADERSHIP</span>
          <h2 style="font-size: 36px; color: var(--navy-dark); font-family: var(--font-serif); margin-top: 8px; margin-bottom: 12px;">Profile of Promoters &amp; Advisory Desk</h2>
          <p style="font-size: 16px; color: var(--slate); max-width: 760px; margin: 0 auto; line-height: 1.6;">Guided by senior Chartered Accountants, Business Strategists, Company Secretaries, and Legal Advocates dedicated to structured corporate capital, taxation, and growth advisory.</p>
        </div>

        <!-- 40+ Years Combined Experience Highlight Bar -->
        <div style="background: linear-gradient(135deg, #0B1F3A 0%, #1A365D 100%); border: 1px solid #C89B3C; border-radius: 16px; padding: 20px 24px; text-align: center; max-width: 900px; margin: 0 auto 48px; box-shadow: 0 8px 24px rgba(11, 31, 58, 0.15);">
          <div style="color: #C89B3C; font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">COMBINED ADVISORY EXCELLENCE</div>
          <div style="color: #FFFFFF; font-size: 17px; font-weight: 700; font-family: var(--font-serif);">
            Together, the Leadership Team brings 40+ years of combined experience across Taxation, Finance, Subsidies, Business Strategy, and Growth.
          </div>
        </div>

        <div class="founders-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; align-items: stretch;">
          
          <!-- Promoter 1: Rajat Garg -->
          <div class="promoter-card" style="background: #FAF8F5; border: 1px solid #E2DDD5; border-top: 4px solid #C89B3C; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(11, 31, 58, 0.05); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="height: 280px; overflow: hidden; position: relative; background: #e5dfd5;">
                <img src="<?php echo $gallery_base; ?>image copy 15.png" alt="CA Rajat Garg - Head Finance & Subsidy Division" style="width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block;">
              </div>
              <div style="padding: 24px 24px 0;">
                <span style="font-size: 11px; font-weight: 700; color: #C89B3C; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 4px;">CHARTERED ACCOUNTANT</span>
                <h3 style="font-size: 22px; color: #0B1F3A; font-family: var(--font-serif); margin: 0; font-weight: 700;">Rajat Garg</h3>
                <span style="font-size: 13.5px; font-weight: 600; color: #5B6472; display: block; margin-top: 2px; margin-bottom: 12px;">Head – Finance &amp; Subsidy Division</span>
                
                <div style="display: inline-block; background: rgba(200, 155, 60, 0.12); color: #B8860B; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 16px;">
                  10+ Years Finance &amp; Subsidy Experience
                </div>

                <p style="font-size: 14px; color: #3E5372; line-height: 1.65; margin-bottom: 14px;">
                  CA Rajat Garg is a Chartered Accountant by profession with over 10 years of experience in the fields of Finance and Taxation. He has extensive experience in financial advisory, business funding, structured finance, and government subsidy solutions.
                </p>
                <p style="font-size: 14px; color: #3E5372; line-height: 1.65; margin-bottom: 0;">
                  At <b>THE CREDIT LANE</b>, he heads the Finance &amp; Subsidy Division, helping businesses identify the right funding opportunities and maximize available financial and government incentives.
                </p>
              </div>
            </div>

            <div style="border-top: 1px solid #E2DDD5; padding: 16px 24px; margin-top: 24px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #0B1F3A;">Finance &amp; Subsidies</span>
              <a href="<?php echo esc_url(home_url('/contact/')); ?>" style="font-size: 12px; color: #C89B3C; font-weight: 700; text-decoration: none;">📞 Contact Division &rarr;</a>
            </div>
          </div>

          <!-- Promoter 2: Tarang Mittal -->
          <div class="promoter-card" style="background: #FAF8F5; border: 1px solid #E2DDD5; border-top: 4px solid #0B1F3A; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(11, 31, 58, 0.05); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="height: 280px; overflow: hidden; position: relative; background: #e5dfd5;">
                <img src="<?php echo $gallery_base; ?>image copy 2.png" alt="Tarang Mittal - Head Growth Division" style="width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block;">
              </div>
              <div style="padding: 24px 24px 0;">
                <span style="font-size: 11px; font-weight: 700; color: #C89B3C; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 4px;">STRATEGIST &amp; BUSINESS ANALYST</span>
                <h3 style="font-size: 22px; color: #0B1F3A; font-family: var(--font-serif); margin: 0; font-weight: 700;">Tarang Mittal</h3>
                <span style="font-size: 13.5px; font-weight: 600; color: #5B6472; display: block; margin-top: 2px; margin-bottom: 12px;">Head – Growth Division</span>

                <div style="display: inline-block; background: rgba(11, 31, 58, 0.08); color: #0B1F3A; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 16px;">
                  15+ Years Strategy &amp; Growth Experience
                </div>

                <p style="font-size: 14px; color: #3E5372; line-height: 1.65; margin-bottom: 14px;">
                  Tarang Mittal is a Strategist and Business Analyst with over 15 years of experience in Business Consultancy, Strategy, and Management. He brings strong expertise in business growth, strategic planning, process improvement, and management consulting.
                </p>
                <p style="font-size: 14px; color: #3E5372; line-height: 1.65; margin-bottom: 0;">
                  At <b>THE CREDIT LANE</b>, he heads the Growth Division, driving strategic initiatives, business development, and sustainable growth for the organization.
                </p>
              </div>
            </div>

            <div style="border-top: 1px solid #E2DDD5; padding: 16px 24px; margin-top: 24px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #0B1F3A;">Strategy &amp; Growth</span>
              <span style="font-size: 12px; color: #C89B3C; font-weight: 700;">Growth Division</span>
            </div>
          </div>

          <!-- Promoter 3: Bhagchand Bangani -->
          <div class="promoter-card" style="background: #FAF8F5; border: 1px solid #E2DDD5; border-top: 4px solid #C89B3C; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(11, 31, 58, 0.05); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="height: 280px; overflow: hidden; position: relative; background: #e5dfd5;">
                <img src="<?php echo $gallery_base; ?>image copy 3.png" alt="CA Bhagchand Bangani - Head Taxation Division" style="width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block;">
              </div>
              <div style="padding: 24px 24px 0;">
                <span style="font-size: 11px; font-weight: 700; color: #C89B3C; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 4px;">CHARTERED ACCOUNTANT</span>
                <h3 style="font-size: 22px; color: #0B1F3A; font-family: var(--font-serif); margin: 0; font-weight: 700;">Bhagchand Bangani</h3>
                <span style="font-size: 13.5px; font-weight: 600; color: #5B6472; display: block; margin-top: 2px; margin-bottom: 12px;">Head – Taxation Division</span>
                
                <div style="display: inline-block; background: rgba(200, 155, 60, 0.12); color: #B8860B; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 16px;">
                  15+ Years Taxation Advisory Experience
                </div>

                <p style="font-size: 14px; color: #3E5372; line-height: 1.65; margin-bottom: 14px;">
                  CA Bhagchand Bangani is a Chartered Accountant by profession with over 15 years of extensive experience in the fields of Direct Taxation and Indirect Taxation. He brings deep expertise in tax advisory, compliance, planning, and strategic tax management.
                </p>
                <p style="font-size: 14px; color: #3E5372; line-height: 1.65; margin-bottom: 0;">
                  At <b>THE CREDIT LANE</b>, he heads the Taxation Division, guiding clients with practical and strategic taxation solutions.
                </p>
              </div>
            </div>
            
            <div style="border-top: 1px solid #E2DDD5; padding: 16px 24px; margin-top: 24px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #0B1F3A;">Direct &amp; Indirect Taxation</span>
              <span style="font-size: 12px; color: #C89B3C; font-weight: 700;">Taxation Division</span>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ============ BUILD BHARAT EXPO PARTICIPATION CERTIFICATE ============ -->
    <section style="padding: 80px 0; background: var(--offwhite);">
      <div class="wrap">
        <div class="section-head center" style="margin-bottom: 40px; text-align: center;">
          <span class="eyebrow" style="color: var(--gold); font-weight: 700;">NATIONAL EXPOS &amp; RECOGNITION</span>
          <h2 style="font-size: 34px; color: var(--navy-dark); font-family: var(--font-serif); margin-top: 8px;">Build Bharat Expo 2025 Participation</h2>
          <p style="font-size: 16px; color: var(--slate); max-width: 700px; margin: 8px auto 0;">The Credit Lane is officially certified by the Indian Industries Association (IIA) for participating at Bharat Mandapam, New Delhi.</p>
        </div>

        <div style="max-width: 680px; margin: 0 auto;">
          <!-- Official Certificate Card -->
          <div style="background: #fff; padding: 32px; border-radius: 20px; border: 1px solid var(--line); border-top: 4px solid var(--gold); box-shadow: 0 10px 35px rgba(0,0,0,0.06); text-align: center;">
            <span style="font-size: 12px; font-weight: 700; color: var(--gold); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">OFFICIAL PARTICIPATION CERTIFICATE</span>
            <h3 style="font-size: 22px; color: var(--navy-dark); margin-bottom: 20px; font-family: var(--font-serif);">Build Bharat Expo 2025 - Hall 6 Stall D19</h3>
            <div style="overflow: hidden; border-radius: 14px; border: 1px solid var(--line); margin-bottom: 16px; cursor: pointer; box-shadow: 0 4px 16px rgba(0,0,0,0.05);" onclick="openGalleryModal('<?php echo $gallery_base; ?>BRT CorporateBBE Participation Certificate_page-0001.jpg')">
              <img src="<?php echo $gallery_base; ?>BRT CorporateBBE Participation Certificate_page-0001.jpg" alt="Build Bharat Expo 2025 Participation Certificate" style="width: 100%; height: auto; display: block; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
            </div>
            <p style="font-size: 14px; color: var(--slate); margin: 0; line-height: 1.6;">Certified by Indian Industries Association (IIA) for exhibiting corporate credit &amp; government incentive advisory at Hall 6 Stall D19, Bharat Mandapam, New Delhi.</p>
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

        <div class="overview-4grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 40px;">
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
                <li><strong>Credentials:</strong> IIA Member &amp; Expo Certified</li>
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

          <!-- Card 3: Executive Leadership Team -->
          <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); border-radius: 18px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span style="color: var(--gold-light); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">EXECUTIVE LEADERSHIP</span>
              <h3 style="color: #fff; font-size: 20px; font-family: var(--font-serif); margin-bottom: 12px;">Promoter &amp; Leadership Desk</h3>
              <div style="width: 100%; height: 140px; border-radius: 12px; overflow: hidden; margin-bottom: 14px; border: 1px solid rgba(255,255,255,0.15); cursor: pointer;" onclick="openGalleryModal('<?php echo $gallery_base; ?>WhatsApp Image 2026-08-11 at 10.10.23.jpeg')">
                <img src="<?php echo $gallery_base; ?>WhatsApp Image 2026-08-11 at 10.10.23.jpeg" alt="The Credit Lane Executive Leadership Team" style="width: 100%; height: 100%; object-fit: cover;">
              </div>
              <p style="color: #CBD5E1; font-size: 13.5px; line-height: 1.6; margin: 0;">Led by Chartered Accountants, Business Strategists, and Legal Advocates heading Credit Committee Structuring, Finance, Taxation, and Growth Divisions.</p>
            </div>
            <span style="color: var(--gold-light); font-weight: 700; font-size: 13.5px; cursor: pointer; margin-top: 14px;" onclick="openGalleryModal('<?php echo $gallery_base; ?>WhatsApp Image 2026-08-11 at 10.10.23.jpeg')">🔍 View Leadership Photo &rarr;</span>
          </div>

          <!-- Card 4: Certificates & National Recognition Showcase -->
          <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); border-radius: 18px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span style="color: var(--gold-light); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">EXPO RECOGNITION</span>
              <h3 style="color: #fff; font-size: 20px; font-family: var(--font-serif); margin-bottom: 12px;">Official Certification</h3>
              <div style="height: 130px; border-radius: 10px; overflow: hidden; border: 1px solid rgba(255,255,255,0.2); margin-bottom: 14px; cursor: pointer;" onclick="openGalleryModal('<?php echo $gallery_base; ?>BRT CorporateBBE Participation Certificate_page-0001.jpg')">
                <img src="<?php echo $gallery_base; ?>BRT CorporateBBE Participation Certificate_page-0001.jpg" alt="IIA Build Bharat Expo 2025 Certificate" style="width: 100%; height: 100%; object-fit: cover; object-position: top;" title="IIA Build Bharat Expo 2025 Certificate">
              </div>
              <p style="color: #CBD5E1; font-size: 13px; line-height: 1.5; margin: 0;">Certified by Indian Industries Association (IIA) for participating at Build Bharat Expo 2025, Hall 6 Stall D19, Bharat Mandapam, New Delhi.</p>
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
