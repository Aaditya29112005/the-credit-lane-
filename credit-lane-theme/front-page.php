<?php
get_header();
?>

    <!-- ============ HERO ============ -->
    <section class="hero" style="padding-bottom: 0;">
      <video autoplay muted loop playsinline style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: fill; z-index: 1; opacity: 0.65; pointer-events: none;">
        <source src="<?php echo esc_url(get_template_directory_uri() . '/assets/video/hero-bg.mov'); ?>" type="video/quicktime">
        <source src="<?php echo esc_url(get_template_directory_uri() . '/assets/video/hero-bg.mov'); ?>" type="video/mp4">
      </video>
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to right, rgba(8, 21, 39, 0.96) 0%, rgba(8, 21, 39, 0.65) 45%, rgba(8, 21, 39, 0.15) 100%); z-index: 1; pointer-events: none;"></div>
      <div class="wrap" style="padding-top: 40px; padding-bottom: 40px;">
        <div>
          <span class="eyebrow">CA · CS · ADVOCATE-LED CAPITAL ADVISORY — 10+ YEARS · ₹2,500 CR+ RAISED</span>
          <h1>Capital for Your Next Stage of Growth.</h1>
          <p class="lead">Strategic funding, equity advisory, and government grant solutions for ambitious Indian businesses. Access 100+ institutional lenders with the transparency of a CA, CS, and Advocate led advisory desk.</p>
          
          <div class="hero-trust">Loans • Equity • Government Grants &amp; Subsidies</div>
          
          <div class="hero-cta-row">
            <a href="<?php echo esc_url(home_url('/contact/')); ?>" class="btn btn-primary">Discuss Your Funding Need</a>
            <a href="#selector" class="btn btn-outline">Explore Our Services</a>
          </div>
          
          <div class="hero-stats">
            <div class="stat"><b>₹2,500 Cr+</b><span>Debt &amp; Equity Structured</span></div>
            <div class="stat"><b>100+</b><span>Lending Partners</span></div>
            <div class="stat"><b>1,000+</b><span>SMEs Funded</span></div>
            <div class="stat"><b>10 Years</b><span>On-Ground Execution</span></div>
          </div>
        </div>

        <!-- Interactive Capital Selector -->
        <div class="stack-card" id="selector">
          <div class="stack-tabs">
            <button type="button" class="stack-tab active" onclick="switchStackTab(0)">LOANS</button>
            <button type="button" class="stack-tab" onclick="switchStackTab(1)">EQUITY</button>
            <button type="button" class="stack-tab" onclick="switchStackTab(2)">GRANTS</button>
          </div>
          <div class="stack-list active">
            <a href="<?php echo esc_url(home_url('/loans/unsecured-business-loan-dod/')); ?>">Unsecured Business Loan &amp; DOD Limit <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/commercial-industrial-purchase-loan/')); ?>">Commercial or Industrial Purchase Loan <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/machine-loan-sidbi/')); ?>">Machine Loan from SIDBI <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/machine-loan-bank/')); ?>">Machine Loan from Bank <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/invoice-finance/')); ?>">Sale Invoice Finance / Purchase Invoice Finance <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/school-college-funding/')); ?>">School &amp; College Funding <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/builder-real-estate-funding/')); ?>">Builder and Real Estate Developers Funding <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/hospital-funding/')); ?>">Hospital Funding <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/hotel-resort-funding/')); ?>">Hotel &amp; Resort Funding <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/npa-funding/')); ?>">NPA Funding <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/infrastructure-funding/')); ?>">Infrastructure Companies Funding <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/loans/venture-funding/')); ?>">Venture Funding <span class="arrow">→</span></a>
          </div>
          <div class="stack-list ">
            <a href="<?php echo esc_url(home_url('/equity/valuation-services/')); ?>">Valuation Services <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/equity/pre-ipo-funding/')); ?>">Pre-IPO Funding <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/equity/sme-ipo/')); ?>">SME IPO <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/equity/main-board-ipo/')); ?>">Main Board IPO <span class="arrow">→</span></a>
          </div>
          <div class="stack-list ">
            <a href="<?php echo esc_url(home_url('/incentives/up-tus-scheme/')); ?>">UP Govt Technical Upgradation Support (TUS) Grant <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/incentives/up-msme-scheme/')); ?>">UP Govt MSME Promotion Policy Grant <span class="arrow">→</span></a>
            <a href="<?php echo esc_url(home_url('/incentives/up-msmy-scheme/')); ?>">UP Govt MSMY Scheme Grant <span class="arrow">→</span></a>
          </div>

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
            <p>Access debt limits, private capital pre-IPO financing, and state grant programs in one room.</p>
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

    <!-- ============ WHY CHOOSE US SECTION ============ -->
    <section class="why-choose-us">
      <div class="wrap">
        <div class="wcu-inner">
          <div class="wcu-left">
            <span class="eyebrow">WHY CHOOSE US</span>
            <h2>Tailored financial solutions for every stage of growth.</h2>
            <p class="lead">At <strong>The Credit Lane</strong>, Rajat Garg and our team of CA, CS, and Advocate advisors specialize in providing tailored financial solutions for MSMEs, mid-corporates, and promoters. Whether you need funding for business expansion, working capital, SIDBI machinery purchase, loan against property, or equity fundraising, we help you secure financing from leading Banks, NBFCs, and investors with ease.</p>
            <p style="font-size: 14px; color: var(--slate); line-height: 1.7; margin-top: 16px;">Our expertise lies in empowering MSMEs, ensuring they get the financial backing and state grants needed to scale, innovate, and succeed. Let's connect to find the right loan or grant solution for your business goals.</p>
            <a href="<?php echo esc_url(home_url('/contact/')); ?>" class="btn btn-primary" style="margin-top: 28px; display: inline-flex;">Connect With Us &rarr;</a>
          </div>
          <div class="wcu-right">
            <div class="wcu-grid">
              <div class="wcu-item">
                <span class="wcu-check">&#10003;</span>
                <div>
                  <strong>Comprehensive Loan Solutions</strong>
                  <p>Business Loans, Working Capital, Machinery Loans, CGTMSE, Home Loans, and Loan Against Property.</p>
                </div>
              </div>
              <div class="wcu-item">
                <span class="wcu-check">&#10003;</span>
                <div>
                  <strong>Equity Fundraising &amp; SME IPOs</strong>
                  <p>Helping businesses raise capital through structured funding and public offerings.</p>
                </div>
              </div>
              <div class="wcu-item">
                <span class="wcu-check">&#10003;</span>
                <div>
                  <strong>Unsecured Business Loans &amp; DOD</strong>
                  <p>Flexible drop-line overdraft options without collateral for growing businesses.</p>
                </div>
              </div>
              <div class="wcu-item">
                <span class="wcu-check">&#10003;</span>
                <div>
                  <strong>Hassle-Free Process</strong>
                  <p>We manage the entire paperwork and application process end-to-end.</p>
                </div>
              </div>
              <div class="wcu-item">
                <span class="wcu-check">&#10003;</span>
                <div>
                  <strong>Faster Approvals</strong>
                  <p>Leverage our banking partnerships for quick loan disbursals.</p>
                </div>
              </div>
              <div class="wcu-item">
                <span class="wcu-check">&#10003;</span>
                <div>
                  <strong>Competitive Interest Rates</strong>
                  <p>Secure funding at optimal rates to maximize growth.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ MID-PAGE CORPORATE BANNER ============ -->
    <div style="background-image: linear-gradient(rgba(11, 31, 58, 0.75), rgba(11, 31, 58, 0.75)), url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1200&auto=format&fit=crop'); background-attachment: fixed; background-position: center; background-repeat: no-repeat; background-size: cover; height: 260px; display: flex; align-items: center; justify-content: center; text-align: center; color: var(--white); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);">
      <div class="wrap" style="width: 100%;">
        <h3 style="color: var(--white); font-size: clamp(1.6rem, 3vw, 2.2rem); font-family: var(--font-serif); margin-bottom: 10px;">CA, CS and Advocate-Led Corporate Finance Desk</h3>
        <p style="color: var(--gold-light); font-family: var(--font-mono); font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; margin: 0;">Unlocking capital channels with absolute alignment and transparent execution.</p>
      </div>
    </div>

    <!-- ============ CALCULATOR SECTION ============ -->
    <section id="calculator" style="padding: 70px 0; background: var(--offwhite); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);">
      <div class="wrap">
        <div class="section-head center" style="margin-bottom: 36px;">
          <span class="eyebrow">REAL-TIME EMI &amp; GRANT CALCULATOR</span>
          <h2>Check Your Business Loan EMI &amp; Grant Eligibility</h2>
          <p>Use our real-time calculators below to estimate monthly EMI payouts, drop-line overdrafts, or UP TUS 50% Grant approvals.</p>
        </div>

        <div style="background: var(--white); border: 1px solid var(--line); border-radius: 20px; padding: 36px; box-shadow: 0 8px 30px rgba(0,0,0,0.04); max-width: 900px; margin: 0 auto;">
          <div class="calculator-card-grid">
            <div style="display: flex; flex-direction: column; gap: 20px;">
              <div>
                <label style="font-size: 13.5px; font-weight: 700; color: var(--navy-dark); display: flex; justify-content: space-between;">
                  <span>Loan Amount (P)</span>
                  <span id="emi-p-val" style="color: var(--gold); font-weight: 800;">₹50,00,000</span>
                </label>
                <input type="range" id="emi-p" min="500000" max="50000000" step="500000" value="5000000" oninput="updateEmiCalc()" style="width: 100%; margin-top: 8px; accent-color: var(--gold);">
              </div>
              <div>
                <label style="font-size: 13.5px; font-weight: 700; color: var(--navy-dark); display: flex; justify-content: space-between;">
                  <span>Interest Rate (% p.a.)</span>
                  <span id="emi-r-val" style="color: var(--gold); font-weight: 800;">10.5%</span>
                </label>
                <input type="range" id="emi-r" min="7" max="18" step="0.25" value="10.5" oninput="updateEmiCalc()" style="width: 100%; margin-top: 8px; accent-color: var(--gold);">
              </div>
              <div>
                <label style="font-size: 13.5px; font-weight: 700; color: var(--navy-dark); display: flex; justify-content: space-between;">
                  <span>Loan Tenure (Years)</span>
                  <span id="emi-y-val" style="color: var(--gold); font-weight: 800;">5 yrs</span>
                </label>
                <input type="range" id="emi-y" min="1" max="15" step="1" value="5" oninput="updateEmiCalc()" style="width: 100%; margin-top: 8px; accent-color: var(--gold);">
              </div>
            </div>

            <div style="background: var(--navy-dark); color: #fff; padding: 28px; border-radius: 16px; display: flex; flex-direction: column; gap: 16px;">
              <div>
                <span style="font-size: 12px; color: var(--gold-light); font-weight: 700; text-transform: uppercase;">MONTHLY EMI PAIRED</span>
                <div id="res-emi" style="font-size: 32px; font-weight: 800; font-family: var(--font-serif); color: #fff; margin-top: 4px;">₹1,07,469</div>
              </div>
              <div class="calculator-output-stats">
                <div>
                  <span style="font-size: 11.5px; color: var(--slate-light);">Total Interest</span>
                  <div id="res-interest" style="font-size: 16px; font-weight: 700; color: #fff;">₹14,48,165</div>
                </div>
                <div>
                  <span style="font-size: 11.5px; color: var(--slate-light);">Total Payable</span>
                  <div id="res-total" style="font-size: 16px; font-weight: 700; color: #fff;">₹64,48,165</div>
                </div>
              </div>
              <a href="<?php echo esc_url(home_url('/contact/')); ?>" class="btn btn-primary" style="width: 100%; text-align: center; justify-content: center; margin-top: 8px;">Apply for In-Principle Sanction &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ FINAL CTA ============ -->
    <section class="final-cta">
      <div class="wrap">
        <h2>Have a funding or grant requirement?</h2>
        <p>Tell us what you are building. The Credit Lane team will help you explore the right capital route with no upfront advisory charge.</p>
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
          <a href="<?php echo esc_url(home_url('/contact/')); ?>" class="btn btn-primary">Talk to The Credit Lane &rarr;</a>
          <a href="https://wa.me/919217924499" class="btn btn-outline" target="_blank">WhatsApp Us (9217924499)</a>
        </div>
      </div>
    </section>

<?php
get_footer();
