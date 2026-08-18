<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo( 'charset' ); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <script>
    function fmtINR(n) {
      if (isNaN(n) || !isFinite(n)) return "₹0";
      return "₹" + Math.round(n).toLocaleString("en-IN");
    }

    function updateEmiCalc() {
      var pInput = document.getElementById("emi-p");
      var rInput = document.getElementById("emi-r");
      var yInput = document.getElementById("emi-y");
      if (!pInput || !rInput || !yInput) return;
      var P = parseFloat(pInput.value) || 0;
      var annR = parseFloat(rInput.value) || 0;
      var yrs = parseFloat(yInput.value) || 0;
      var pOut = document.getElementById("emi-p-val");
      var rOut = document.getElementById("emi-r-val");
      var yOut = document.getElementById("emi-y-val");
      if (pOut) pOut.textContent = fmtINR(P);
      if (rOut) rOut.textContent = annR + "%";
      if (yOut) yOut.textContent = yrs + " yrs";
      var r = annR / 1200;
      var n = yrs * 12;
      var emi = 0;
      if (r > 0 && n > 0) {
        emi = P * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
      } else if (n > 0) {
        emi = P / n;
      }
      var total = emi * n;
      var interest = Math.max(0, total - P);
      var emiOut = document.getElementById("res-emi");
      var interestOut = document.getElementById("res-interest");
      var totalOut = document.getElementById("res-total");
      var pBar = document.getElementById("bar-p");
      var iBar = document.getElementById("bar-i");
      if (emiOut) emiOut.textContent = fmtINR(emi);
      if (interestOut) interestOut.textContent = fmtINR(interest);
      if (totalOut) totalOut.textContent = fmtINR(total);
      if (pBar && iBar && total > 0) {
        var pPct = Math.min(100, Math.max(0, (P / total) * 100));
        pBar.style.width = pPct + "%";
        iBar.style.width = (100 - pPct) + "%";
      }
    }

    function updateInvoiceCalc() {
      var valInput = document.getElementById("inv-val");
      var advInput = document.getElementById("inv-adv");
      var daysInput = document.getElementById("inv-days");
      if (!valInput || !advInput || !daysInput) return;
      var mRate = parseFloat(document.getElementById("inv-mrate") ? document.getElementById("inv-mrate").value : "2");
      var val = parseFloat(valInput.value) || 0;
      var advPct = parseFloat(advInput.value) || 0;
      var days = parseFloat(daysInput.value) || 0;
      var valOut = document.getElementById("inv-val-val");
      var advOut = document.getElementById("inv-adv-val");
      var daysOut = document.getElementById("inv-days-val");
      if (valOut) valOut.textContent = fmtINR(val);
      if (advOut) advOut.textContent = advPct + "%";
      if (daysOut) daysOut.textContent = days + " days";
      var advanceAmt = val * advPct / 100;
      var cost = advanceAmt * (mRate / 100) * (days / 30);
      var net = Math.max(0, val - cost);
      var resAdv = document.getElementById("res-inv-adv");
      var resCost = document.getElementById("res-inv-cost");
      var resNet = document.getElementById("res-inv-net");
      if (resAdv) resAdv.textContent = fmtINR(advanceAmt);
      if (resCost) resCost.textContent = fmtINR(cost);
      if (resNet) resNet.textContent = fmtINR(net);
    }

    function updateSettlementCalc() {
      var duesInput = document.getElementById("set-dues");
      var setPctInput = document.getElementById("set-pct");
      var tokPctInput = document.getElementById("set-tok");
      if (!duesInput || !setPctInput || !tokPctInput) return;
      var dues = parseFloat(duesInput.value) || 0;
      var setPct = parseFloat(setPctInput.value) || 0;
      var tokPct = parseFloat(tokPctInput.value) || 0;
      var duesOut = document.getElementById("set-dues-val");
      var setPctOut = document.getElementById("set-pct-val");
      var tokPctOut = document.getElementById("set-tok-val");
      if (duesOut) duesOut.textContent = fmtINR(dues);
      if (setPctOut) setPctOut.textContent = setPct + "% of dues";
      if (tokPctOut) tokPctOut.textContent = tokPct + "% of settlement";
      var settlementAmt = dues * setPct / 100;
      var savings = Math.max(0, dues - settlementAmt);
      var tokenAmt = settlementAmt * tokPct / 100;
      var resSettle = document.getElementById("res-set-amt");
      var resSave = document.getElementById("res-set-save");
      var resToken = document.getElementById("res-set-tok");
      if (resSettle) resSettle.textContent = fmtINR(settlementAmt);
      if (resSave) resSave.textContent = fmtINR(savings);
      if (resToken) resToken.textContent = fmtINR(tokenAmt);
    }

    function updateDilutionCalc() {
      var raiseInput = document.getElementById("dil-raise");
      var preInput = document.getElementById("dil-pre");
      if (!raiseInput || !preInput) return;
      var raise = parseFloat(raiseInput.value) || 0;
      var pre = parseFloat(preInput.value) || 0;
      var raiseOut = document.getElementById("dil-raise-val");
      var preOut = document.getElementById("dil-pre-val");
      if (raiseOut) raiseOut.textContent = fmtINR(raise);
      if (preOut) preOut.textContent = fmtINR(pre);
      var post = pre + raise;
      var dilution = post > 0 ? (raise / post) * 100 : 0;
      var retain = Math.max(0, 100 - dilution);
      var resPost = document.getElementById("res-dil-post");
      var resDil = document.getElementById("res-dil-dil");
      var resRet = document.getElementById("res-dil-ret");
      if (resPost) resPost.textContent = fmtINR(post);
      if (resDil) resDil.textContent = dilution.toFixed(1) + "%";
      if (resRet) resRet.textContent = retain.toFixed(1) + "%";
    }

    function updateIpoCalc() {
      var issueInput = document.getElementById("ipo-issue");
      var preInput = document.getElementById("ipo-pre");
      if (!issueInput || !preInput) return;
      var fresh = parseFloat(issueInput.value) || 0;
      var pre = parseFloat(preInput.value) || 0;
      var issueOut = document.getElementById("ipo-issue-val");
      var preOut = document.getElementById("ipo-pre-val");
      if (issueOut) issueOut.textContent = fmtINR(fresh);
      if (preOut) preOut.textContent = fmtINR(pre);
      var post = pre + fresh;
      var pubPct = post > 0 ? (fresh / post) * 100 : 0;
      var promPct = Math.max(0, 100 - pubPct);
      var resPost = document.getElementById("res-ipo-post");
      var resPublic = document.getElementById("res-ipo-pub");
      var resProm = document.getElementById("res-ipo-prom");
      if (resPost) resPost.textContent = fmtINR(post);
      if (resPublic) resPublic.textContent = pubPct.toFixed(1) + "%";
      if (resProm) resProm.textContent = promPct.toFixed(1) + "%";
    }

    function updateValuationCalc() {
      var ebitdaInput = document.getElementById("val-ebitda");
      var multLoInput = document.getElementById("val-mlo");
      var multHiInput = document.getElementById("val-mhi");
      if (!ebitdaInput || !multLoInput || !multHiInput) return;
      var ebitda = parseFloat(ebitdaInput.value) || 0;
      var lo = parseFloat(multLoInput.value) || 0;
      var hi = parseFloat(multHiInput.value) || 0;
      if (hi < lo) {
        hi = lo;
        multHiInput.value = hi;
      }
      var ebitdaOut = document.getElementById("val-ebitda-val");
      var multLoOut = document.getElementById("val-mlo-val");
      var multHiOut = document.getElementById("val-mhi-val");
      if (ebitdaOut) ebitdaOut.textContent = fmtINR(ebitda);
      if (multLoOut) multLoOut.textContent = lo + "x";
      if (multHiOut) multHiOut.textContent = hi + "x";
      var resLo = document.getElementById("res-val-lo");
      var resHi = document.getElementById("res-val-hi");
      if (resLo) resLo.textContent = fmtINR(ebitda * lo);
      if (resHi) resHi.textContent = fmtINR(ebitda * hi);
    }

    // TUS Subsidy / Grant Calculator: 50% Rate, Capped at max 15 Lacs
    function updateSubsidyCalc() {
      var costInput = document.getElementById("sub-cost");
      var rateInput = document.getElementById("sub-rate");
      if (!costInput) return;
      var capVal = 1500000; // Max 15 Lac Grant
      var cost = parseFloat(costInput.value) || 0;
      var rate = rateInput ? parseFloat(rateInput.value) || 50 : 50; // 50% Grant rate
      var costOut = document.getElementById("sub-cost-val");
      var rateOut = document.getElementById("sub-rate-val");
      if (costOut) costOut.textContent = fmtINR(cost);
      if (rateOut) rateOut.textContent = rate + "%";
      var subsidy = Math.min(cost * (rate / 100), capVal);
      var net = Math.max(0, cost - subsidy);
      var resSub = document.getElementById("res-sub-amt");
      var resNet = document.getElementById("res-sub-net");
      if (resSub) resSub.textContent = fmtINR(subsidy);
      if (resNet) resNet.textContent = fmtINR(net);
    }

    function initAllCalculators() {
      updateEmiCalc();
      updateInvoiceCalc();
      updateSettlementCalc();
      updateDilutionCalc();
      updateIpoCalc();
      updateValuationCalc();
      updateSubsidyCalc();
    }

    function switchStackTab(index) {
      var card = document.getElementById("selector");
      if (!card) card = document;
      var tabs = card.querySelectorAll(".stack-tab");
      var lists = card.querySelectorAll(".stack-list");
      for (var i = 0; i < tabs.length; i++) tabs[i].classList.remove("active");
      for (var j = 0; j < lists.length; j++) lists[j].classList.remove("active");
      if (tabs[index]) tabs[index].classList.add("active");
      if (lists[index]) lists[index].classList.add("active");
    }

    function switchCatalogTab(index) {
      var tabs = document.querySelectorAll(".catalog-tab");
      var grids = document.querySelectorAll(".catalog-grid");
      for (var i = 0; i < tabs.length; i++) tabs[i].classList.remove("active");
      for (var j = 0; j < grids.length; j++) grids[j].classList.remove("active");
      if (tabs[index]) tabs[index].classList.add("active");
      if (grids[index]) grids[index].classList.add("active");
    }

    window.toggleFaq = function(btn) {
      if (!btn) return;
      var item = btn.closest('.faq-item');
      if (!item) return;

      var isOpen = item.classList.contains('open');
      var accordion = item.closest('.faq-accordion') || item.closest('.service-section') || item.parentElement;
      if (accordion) {
        var allItems = accordion.querySelectorAll('.faq-item');
        for (var i = 0; i < allItems.length; i++) {
          if (allItems[i] !== item) {
            allItems[i].classList.remove('open');
            var ind = allItems[i].querySelector('.faq-q span');
            if (ind) ind.textContent = '+';
          }
        }
      }
      if (isOpen) {
        item.classList.remove('open');
        var indicator = item.querySelector('.faq-q span');
        if (indicator) indicator.textContent = '+';
      } else {
        item.classList.add('open');
        var indicator = item.querySelector('.faq-q span');
        if (indicator) indicator.textContent = '−';
      }
    };

    function toggleMobileMenu() {
      var mobileNav = document.querySelector(".mobile-nav");
      var overlay = document.querySelector(".overlay");
      var hamburger = document.querySelector(".hamburger");
      if (!mobileNav) return;
      var isOpen = mobileNav.classList.contains("open");
      if (hamburger) hamburger.classList.toggle("active", !isOpen);
      if (isOpen) {
        mobileNav.classList.remove("open");
        if (overlay) overlay.classList.remove("open");
        document.body.style.overflow = "";
      } else {
        mobileNav.classList.add("open");
        if (overlay) overlay.classList.add("open");
        document.body.style.overflow = "hidden";
      }
    }

    function toggleMobileAccordion(title) {
      if (!title) return;
      var submenu = title.nextElementSibling;
      var arrow = title.querySelector(".arrow-toggle");
      if (submenu && submenu.classList.contains("mobile-nav-submenu")) {
        var isOpen = submenu.classList.contains("open");
        if (isOpen) {
          submenu.classList.remove("open");
          if (arrow) arrow.textContent = "▾";
        } else {
          submenu.classList.add("open");
          if (arrow) arrow.textContent = "▴";
        }
      }
    }

    document.addEventListener("DOMContentLoaded", initAllCalculators);
    window.addEventListener("load", initAllCalculators);
    setTimeout(initAllCalculators, 50);
    setTimeout(initAllCalculators, 300);
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

  <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

  <!-- ============ HEADER / NAV ============ -->
  <header style="position: sticky; top: 0; z-index: 10000; background: var(--white); box-shadow: 0 2px 20px rgba(11,31,58,0.08);">
    <div class="wrap">
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="logo" style="text-decoration: none !important; display: inline-flex !important; align-items: center !important; gap: 10px !important; font-family: 'Plus Jakarta Sans', sans-serif !important;">
        <img src="<?php echo esc_url( get_template_directory_uri() . '/assets/images/logo.png' ); ?>" alt="The Credit Lane Logo" class="logo-img" style="width: 38px; height: 38px; object-fit: contain; flex-shrink: 0; display: block;">
        <span class="logo-text" style="font-family: 'Plus Jakarta Sans', sans-serif !important; display: inline-flex !important; align-items: baseline !important; gap: 5px !important; font-size: 25px !important; letter-spacing: -0.03em !important; line-height: 1 !important;">
          <span class="logo-the" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 300 !important; color: #0B1F3A !important; font-size: 25px !important;">The</span>
          <span class="logo-bold" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 900 !important; color: #0B1F3A !important; font-size: 25px !important;">Credit Lane</span>
        </span>
      </a>

      <nav class="mainnav">
        <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="<?php echo is_front_page() ? 'active' : ''; ?>">Home</a>
        
        <div class="nav-item">
          <a href="<?php echo esc_url( home_url( '/loans/' ) ); ?>" class="nav-title <?php echo ( is_page('loans') || (is_page() && $post->post_parent == get_page_by_path('loans')->ID) ) ? 'active' : ''; ?>">Loans ▾</a>
          <div class="mega-menu loans-menu">
            <h4>Debt Solutions & Funding</h4>
            <div class="mega-grid">
              <a href="<?php echo esc_url( home_url( '/loans/unsecured-business-loan-dod/' ) ); ?>" class="mega-item"><span class="title">Unsecured Business Loan & DOD Limit</span><span class="desc">Working Capital, Without Pledging Collateral</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/commercial-industrial-purchase-loan/' ) ); ?>" class="mega-item"><span class="title">Commercial or Industrial Purchase Loan</span><span class="desc">Own the Premises You Currently Rent</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/machine-loan-sidbi/' ) ); ?>" class="mega-item"><span class="title">Machine Loan from SIDBI</span><span class="desc">Machinery Finance on SIDBI's SME-First Terms</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/machine-loan-bank/' ) ); ?>" class="mega-item"><span class="title">Machine Loan from Bank</span><span class="desc">Bank-Funded Machinery Loans</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/invoice-finance/' ) ); ?>" class="mega-item"><span class="title">Sale Invoice Finance / Purchase Invoice Finance</span><span class="desc">Unlock Cash Tied Up in Unpaid Invoices</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/school-college-funding/' ) ); ?>" class="mega-item"><span class="title">School & College Funding</span><span class="desc">Infrastructure Finance for Educational Institutions</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/builder-real-estate-funding/' ) ); ?>" class="mega-item"><span class="title">Builder and Real Estate Developers Funding</span><span class="desc">Construction Finance</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/hospital-funding/' ) ); ?>" class="mega-item"><span class="title">Hospital Funding</span><span class="desc">Capital for Beds, Equipment and Expansion</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/hotel-resort-funding/' ) ); ?>" class="mega-item"><span class="title">Hotel & Resort Funding</span><span class="desc">Finance Built for Hospitality's Seasonal Cash Cycle</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/npa-funding/' ) ); ?>" class="mega-item"><span class="title">NPA Funding</span><span class="desc">Resolve a Stressed Account Before It Escalates</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/infrastructure-funding/' ) ); ?>" class="mega-item"><span class="title">Infrastructure Companies Funding</span><span class="desc">Project and Working Capital Finance</span></a>
              <a href="<?php echo esc_url( home_url( '/loans/venture-funding/' ) ); ?>" class="mega-item"><span class="title">Venture Funding</span><span class="desc">Growth Capital for Businesses Ready to Scale</span></a>
            </div>
          </div>
        </div>

        <div class="nav-item">
          <a href="<?php echo esc_url( home_url( '/equity/' ) ); ?>" class="nav-title <?php echo ( is_page('equity') || (is_page() && $post->post_parent == get_page_by_path('equity')->ID) ) ? 'active' : ''; ?>">Equity ▾</a>
          <div class="mega-menu">
            <h4>Advisory & Public Listings</h4>
            <div class="mega-grid">
              <a href="<?php echo esc_url( home_url( '/equity/valuation-services/' ) ); ?>" class="mega-item"><span class="title">Valuation Services</span><span class="desc">Defensible Valuations for Statutory Purpose</span></a>
              <a href="<?php echo esc_url( home_url( '/equity/pre-ipo-funding/' ) ); ?>" class="mega-item"><span class="title">Pre-IPO Funding</span><span class="desc">Bridge Capital Before Listing</span></a>
              <a href="<?php echo esc_url( home_url( '/equity/sme-ipo/' ) ); ?>" class="mega-item"><span class="title">SME IPO</span><span class="desc">List on BSE SME or NSE Emerge</span></a>
              <a href="<?php echo esc_url( home_url( '/equity/main-board-ipo/' ) ); ?>" class="mega-item"><span class="title">Main Board IPO</span><span class="desc">Take Your Company to NSE and BSE Mainboard</span></a>
            </div>
          </div>
        </div>

        <div class="nav-item">
          <a href="<?php echo esc_url( home_url( '/incentives/' ) ); ?>" class="nav-title <?php echo ( is_page('incentives') || (is_page() && $post->post_parent == get_page_by_path('incentives')->ID) ) ? 'active' : ''; ?>">Grants & Subsidies ▾</a>
          <div class="mega-menu">
            <h4>Government Schemes & Grants</h4>
            <div class="mega-grid">
              <a href="<?php echo esc_url( home_url( '/incentives/up-tus-scheme/' ) ); ?>" class="mega-item"><span class="title">UP Govt Technical Upgradation Support (TUS) Grant</span><span class="desc">50% Grant on Machinery Upgrades (Max ₹15 Lac)</span></a>
              <a href="<?php echo esc_url( home_url( '/incentives/up-msme-scheme/' ) ); ?>" class="mega-item"><span class="title">UP Govt MSME Promotion Policy Grant</span><span class="desc">Capital Subsidy & Stamp Duty Relief</span></a>
              <a href="<?php echo esc_url( home_url( '/incentives/up-msmy-scheme/' ) ); ?>" class="mega-item"><span class="title">UP Govt MSMY Scheme Grant</span><span class="desc">Collateral-Free Startup Capital</span></a>
            </div>
          </div>
        </div>

        <a href="<?php echo esc_url( home_url( '/about/' ) ); ?>" class="<?php echo is_page('about') ? 'active' : ''; ?>">About Us</a>
        <a href="<?php echo esc_url( home_url( '/partner-with-us/' ) ); ?>" class="<?php echo is_page('partner-with-us') ? 'active' : ''; ?>">Partner With Us</a>
        <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="<?php echo is_page('contact') ? 'active' : ''; ?>">Contact Us</a>
        <a href="<?php echo esc_url( get_template_directory_uri() . '/assets/docs/The-Credit-Lane-Company-Brochure.pdf?v=1.2.4' ); ?>" download="The-Credit-Lane-Company-Brochure.pdf" target="_blank" class="brochure-link" style="color: var(--gold); font-weight: 700; white-space: nowrap;">Brochure 📄</a>
      </nav>
      
      <div class="header-cta" style="display: flex; align-items: center; gap: 14px; flex-shrink: 0;">
        <a href="tel:9217924499" class="phone" style="font-weight: 700; font-size: 13.5px; white-space: nowrap; color: var(--navy-dark); text-decoration: none;">📞 9217924499</a>
        <a href="<?php echo esc_url( home_url( '/' ) ); ?>#calculator" class="btn btn-primary" style="white-space: nowrap; padding: 10px 18px; font-size: 13.5px;">Check my EMI calculator</a>
      </div>

      <!-- Hamburger mobile icon -->
      <button class="hamburger" onclick="toggleMobileMenu()" aria-label="Toggle Navigation">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>

  <!-- Mobile nav drawer -->
  <div class="mobile-nav">
    <div class="mobile-nav-header" style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 14px; border-bottom: 1px solid var(--line); margin-bottom: 16px;">
      <span style="font-family: var(--font-serif); font-weight: 700; font-size: 18px; color: var(--navy-dark);">Navigation</span>
      <button class="mobile-nav-close" onclick="toggleMobileMenu()" aria-label="Close Menu" style="background: none; border: none; font-size: 22px; color: var(--navy-dark); cursor: pointer; padding: 4px 8px; line-height: 1;">✕</button>
    </div>
    <div class="mobile-nav-links">
      <div class="mobile-nav-item">
        <a href="<?php echo esc_url( home_url( '/' ) ); ?>" style="font-weight: 700; font-size: 16px;">Home</a>
      </div>
      <div class="mobile-nav-item">
        <div class="mobile-nav-title" onclick="toggleMobileAccordion(this)">Loans <span class="arrow-toggle">▾</span></div>
        <div class="mobile-nav-submenu">
          <a href="<?php echo esc_url( home_url( '/loans/' ) ); ?>" style="font-weight:700; color: var(--gold);">→ All Loans Catalog</a>
          <a href="<?php echo esc_url( home_url( '/loans/unsecured-business-loan-dod/' ) ); ?>">Unsecured Business Loan & DOD Limit</a>
          <a href="<?php echo esc_url( home_url( '/loans/commercial-industrial-purchase-loan/' ) ); ?>">Commercial or Industrial Purchase Loan</a>
          <a href="<?php echo esc_url( home_url( '/loans/machine-loan-sidbi/' ) ); ?>">Machine Loan from SIDBI</a>
          <a href="<?php echo esc_url( home_url( '/loans/machine-loan-bank/' ) ); ?>">Machine Loan from Bank</a>
          <a href="<?php echo esc_url( home_url( '/loans/invoice-finance/' ) ); ?>">Sale Invoice Finance / Purchase Invoice Finance</a>
          <a href="<?php echo esc_url( home_url( '/loans/school-college-funding/' ) ); ?>">School & College Funding</a>
          <a href="<?php echo esc_url( home_url( '/loans/builder-real-estate-funding/' ) ); ?>">Builder and Real Estate Developers Funding</a>
          <a href="<?php echo esc_url( home_url( '/loans/hospital-funding/' ) ); ?>">Hospital Funding</a>
          <a href="<?php echo esc_url( home_url( '/loans/hotel-resort-funding/' ) ); ?>">Hotel & Resort Funding</a>
          <a href="<?php echo esc_url( home_url( '/loans/npa-funding/' ) ); ?>">NPA Funding</a>
          <a href="<?php echo esc_url( home_url( '/loans/infrastructure-funding/' ) ); ?>">Infrastructure Companies Funding</a>
          <a href="<?php echo esc_url( home_url( '/loans/venture-funding/' ) ); ?>">Venture Funding</a>
        </div>
      </div>
      <div class="mobile-nav-item">
        <div class="mobile-nav-title" onclick="toggleMobileAccordion(this)">Equity <span class="arrow-toggle">▾</span></div>
        <div class="mobile-nav-submenu">
          <a href="<?php echo esc_url( home_url( '/equity/' ) ); ?>" style="font-weight:700; color: var(--gold);">→ All Equity Catalog</a>
          <a href="<?php echo esc_url( home_url( '/equity/valuation-services/' ) ); ?>">Valuation Services</a>
          <a href="<?php echo esc_url( home_url( '/equity/pre-ipo-funding/' ) ); ?>">Pre-IPO Funding</a>
          <a href="<?php echo esc_url( home_url( '/equity/sme-ipo/' ) ); ?>">SME IPO</a>
          <a href="<?php echo esc_url( home_url( '/equity/main-board-ipo/' ) ); ?>">Main Board IPO</a>
        </div>
      </div>
      <div class="mobile-nav-item">
        <div class="mobile-nav-title" onclick="toggleMobileAccordion(this)">Grants & Subsidies <span class="arrow-toggle">▾</span></div>
        <div class="mobile-nav-submenu">
          <a href="<?php echo esc_url( home_url( '/incentives/' ) ); ?>" style="font-weight:700; color: var(--gold);">→ All Government Grants Catalog</a>
          <a href="<?php echo esc_url( home_url( '/incentives/up-tus-scheme/' ) ); ?>">UP Govt Technical Upgradation Support (TUS) Grant</a>
          <a href="<?php echo esc_url( home_url( '/incentives/up-msme-scheme/' ) ); ?>">UP Govt MSME Promotion Policy Grant</a>
          <a href="<?php echo esc_url( home_url( '/incentives/up-msmy-scheme/' ) ); ?>">UP Govt MSMY Scheme Grant</a>
        </div>
      </div>
      <div class="mobile-nav-item">
        <a href="<?php echo esc_url( home_url( '/about/' ) ); ?>" style="font-weight: 700; font-size: 16px;">About Us</a>
      </div>
      <div class="mobile-nav-item">
        <a href="<?php echo esc_url( home_url( '/partner-with-us/' ) ); ?>" style="font-weight: 700; font-size: 16px;">Partner With Us</a>
      </div>
      <div class="mobile-nav-item">
        <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" style="font-weight: 700; font-size: 16px;">Contact Us</a>
      </div>
      <div class="mobile-nav-item">
        <a href="<?php echo esc_url( get_template_directory_uri() . '/assets/docs/The-Credit-Lane-Company-Brochure.pdf?v=1.2.4' ); ?>" download="The-Credit-Lane-Company-Brochure.pdf" target="_blank" style="font-weight: 700; font-size: 16px; color: var(--gold);">Company Brochure 📄</a>
      </div>
    </div>
    
    <div class="mobile-nav-cta">
      <div style="display: flex; flex-direction: column; gap: 6px; text-align: center;">
        <a href="tel:9217924499" class="phone" style="font-size: 15px;">📞 9217924499</a>
        <a href="tel:9818709747" class="phone" style="font-size: 15px;">📞 9818709747</a>
      </div>
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>#calculator" class="btn btn-primary">Check my EMI calculator</a>
    </div>
  </div>

  <div class="overlay" onclick="toggleMobileMenu()"></div>

  <!-- Main Content Area -->
  <main>
