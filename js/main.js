document.addEventListener("DOMContentLoaded", () => {
  // 1. STICKY HEADER SCROLL EFFECT
  const header = document.querySelector("header");
  const checkScroll = () => {
    if (window.scrollY > 40) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  };
  window.addEventListener("scroll", checkScroll);
  checkScroll();

  // 2. MOBILE NAVIGATION DRAWER
  const hamburger = document.querySelector(".hamburger");
  const mobileNav = document.querySelector(".mobile-nav");
  const overlay = document.querySelector(".overlay");
  const mobileNavClose = document.querySelector(".mobile-nav-close");

  if (mobileNav && overlay) {
    const toggleMobileMenu = () => {
      const isOpen = mobileNav.classList.contains("open");
      if (hamburger) hamburger.classList.toggle("active", !isOpen);
      mobileNav.classList.toggle("open", !isOpen);
      overlay.classList.toggle("open", !isOpen);
      document.body.style.overflow = !isOpen ? "hidden" : "";
    };

    if (hamburger) hamburger.addEventListener("click", toggleMobileMenu);
    if (overlay) overlay.addEventListener("click", toggleMobileMenu);
    if (mobileNavClose) mobileNavClose.addEventListener("click", toggleMobileMenu);

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && mobileNav.classList.contains("open")) {
        toggleMobileMenu();
      }
    });

    // Close mobile nav when clicking on a link
    const mobileLinks = mobileNav.querySelectorAll("a");
    mobileLinks.forEach(link => {
      link.addEventListener("click", () => {
        if (mobileNav.classList.contains("open")) {
          toggleMobileMenu();
        }
      });
    });
  }

  // 3. MOBILE MENU ACCORDIONS
  const mobileAccordionTitles = document.querySelectorAll(".mobile-nav-title");
  mobileAccordionTitles.forEach(title => {
    title.addEventListener("click", () => {
      const submenu = title.nextElementSibling;
      const arrow = title.querySelector(".arrow-toggle");
      if (submenu && submenu.classList.contains("mobile-nav-submenu")) {
        const isOpen = submenu.classList.contains("open");
        
        // Close other submenus first
        document.querySelectorAll(".mobile-nav-submenu").forEach(sub => sub.classList.remove("open"));
        document.querySelectorAll(".arrow-toggle").forEach(a => a.textContent = "▾");

        if (!isOpen) {
          submenu.classList.add("open");
          if (arrow) arrow.textContent = "▴";
        }
      }
    });
  });

  // 4. HOMEPAGE CAPITAL SELECTOR TABS
  window.switchStackTab = function(index) {
    const selectorTabs = document.querySelectorAll(".stack-tab");
    const selectorLists = document.querySelectorAll(".stack-list");
    if (selectorTabs.length > 0 && selectorLists.length > 0) {
      selectorTabs.forEach(t => t.classList.remove("active"));
      selectorLists.forEach(l => l.classList.remove("active"));
      if (selectorTabs[index]) selectorTabs[index].classList.add("active");
      if (selectorLists[index]) selectorLists[index].classList.add("active");
    }
  };

  const selectorTabs = document.querySelectorAll(".stack-tab");
  if (selectorTabs.length > 0) {
    selectorTabs.forEach((tab, index) => {
      tab.addEventListener("click", (e) => {
        e.preventDefault();
        window.switchStackTab(index);
      });
    });
  }

  // 5. HOMEPAGE SERVICES CATALOG TABS
  window.switchCatalogTab = function(index) {
    const catalogTabs = document.querySelectorAll(".catalog-tab");
    const catalogGrids = document.querySelectorAll(".catalog-grid");
    if (catalogTabs.length > 0 && catalogGrids.length > 0) {
      catalogTabs.forEach(t => t.classList.remove("active"));
      catalogGrids.forEach(g => g.classList.remove("active"));
      if (catalogTabs[index]) catalogTabs[index].classList.add("active");
      if (catalogGrids[index]) catalogGrids[index].classList.add("active");
    }
  };

  const catalogTabs = document.querySelectorAll(".catalog-tab");
  if (catalogTabs.length > 0) {
    catalogTabs.forEach((tab, index) => {
      tab.addEventListener("click", (e) => {
        e.preventDefault();
        window.switchCatalogTab(index);
      });
    });
  }

  // 6. FAQ ACCORDION
  window.toggleFaq = function(btn) {
    if (!btn) return;
    const item = btn.closest('.faq-item') || btn.parentElement;
    if (!item) return;
    const isOpen = item.classList.contains('open');
    
    const accordion = item.closest('.faq-accordion') || item.closest('.service-section') || document;
    const allItems = accordion.querySelectorAll('.faq-item');
    allItems.forEach(i => {
      i.classList.remove('open');
      const ind = i.querySelector('.faq-q span');
      if (ind) ind.textContent = '+';
    });
    
    if (!isOpen) {
      item.classList.add('open');
      const indicator = item.querySelector('.faq-q span');
      if (indicator) indicator.textContent = '−';
    }
  };

  const faqQuestions = document.querySelectorAll(".faq-q");
  faqQuestions.forEach(q => {
    q.addEventListener("click", (e) => {
      e.preventDefault();
      window.toggleFaq(q);
    });
  });

  // 7. INTERACTIVE CALCULATORS
  const fmtINR = n => {
    if (isNaN(n) || !isFinite(n)) return "₹0";
    return "₹" + Math.round(n).toLocaleString("en-IN");
  };

  const wireEMI = () => {
    const pInput = document.getElementById("emi-p");
    const rInput = document.getElementById("emi-r");
    const yInput = document.getElementById("emi-y");

    if (!pInput || !rInput || !yInput) return;

    const pOut = document.getElementById("emi-p-val");
    const rOut = document.getElementById("emi-r-val");
    const yOut = document.getElementById("emi-y-val");

    const emiOut = document.getElementById("res-emi");
    const interestOut = document.getElementById("res-interest");
    const totalOut = document.getElementById("res-total");
    const pBar = document.getElementById("bar-p");
    const iBar = document.getElementById("bar-i");

    const calculate = () => {
      const P = +pInput.value;
      const annR = +rInput.value;
      const yrs = +yInput.value;

      if (pOut) pOut.textContent = fmtINR(P);
      if (rOut) rOut.textContent = annR + "%";
      if (yOut) yOut.textContent = yrs + " yrs";

      const r = annR / 1200;
      const n = yrs * 12;

      let emi = 0;
      if (r > 0 && n > 0) {
        emi = P * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
      } else if (n > 0) {
        emi = P / n;
      }
      
      const total = emi * n;
      const interest = Math.max(0, total - P);

      if (emiOut) emiOut.textContent = fmtINR(emi);
      if (interestOut) interestOut.textContent = fmtINR(interest);
      if (totalOut) totalOut.textContent = fmtINR(total);

      if (pBar && iBar && total > 0) {
        const pPct = Math.min(100, Math.max(0, (P / total) * 100));
        pBar.style.width = pPct + "%";
        iBar.style.width = (100 - pPct) + "%";
      }
    };

    [pInput, rInput, yInput].forEach(inp => {
      inp.addEventListener("input", calculate);
      inp.addEventListener("change", calculate);
    });
    calculate();
  };

  const wireInvoice = () => {
    const valInput = document.getElementById("inv-val");
    const advInput = document.getElementById("inv-adv");
    const daysInput = document.getElementById("inv-days");
    const mRate = parseFloat(document.getElementById("inv-mrate")?.value || "2");

    if (!valInput || !advInput || !daysInput) return;

    const valOut = document.getElementById("inv-val-val");
    const advOut = document.getElementById("inv-adv-val");
    const daysOut = document.getElementById("inv-days-val");

    const resAdv = document.getElementById("res-inv-adv");
    const resCost = document.getElementById("res-inv-cost");
    const resNet = document.getElementById("res-inv-net");

    const calculate = () => {
      const val = +valInput.value;
      const advPct = +advInput.value;
      const days = +daysInput.value;

      if (valOut) valOut.textContent = fmtINR(val);
      if (advOut) advOut.textContent = advPct + "%";
      if (daysOut) daysOut.textContent = days + " days";

      const advanceAmt = val * advPct / 100;
      const cost = advanceAmt * (mRate / 100) * (days / 30);
      const net = Math.max(0, val - cost);

      if (resAdv) resAdv.textContent = fmtINR(advanceAmt);
      if (resCost) resCost.textContent = fmtINR(cost);
      if (resNet) resNet.textContent = fmtINR(net);
    };

    [valInput, advInput, daysInput].forEach(inp => {
      inp.addEventListener("input", calculate);
      inp.addEventListener("change", calculate);
    });
    calculate();
  };

  const wireSettlement = () => {
    const duesInput = document.getElementById("set-dues");
    const setPctInput = document.getElementById("set-pct");
    const tokPctInput = document.getElementById("set-tok");

    if (!duesInput || !setPctInput || !tokPctInput) return;

    const duesOut = document.getElementById("set-dues-val");
    const setPctOut = document.getElementById("set-pct-val");
    const tokPctOut = document.getElementById("set-tok-val");

    const resSettle = document.getElementById("res-set-amt");
    const resSave = document.getElementById("res-set-save");
    const resToken = document.getElementById("res-set-tok");

    const calculate = () => {
      const dues = +duesInput.value;
      const setPct = +setPctInput.value;
      const tokPct = +tokPctInput.value;

      if (duesOut) duesOut.textContent = fmtINR(dues);
      if (setPctOut) setPctOut.textContent = setPct + "% of dues";
      if (tokPctOut) tokPctOut.textContent = tokPct + "% of settlement";

      const settlementAmt = dues * setPct / 100;
      const savings = Math.max(0, dues - settlementAmt);
      const tokenAmt = settlementAmt * tokPct / 100;

      if (resSettle) resSettle.textContent = fmtINR(settlementAmt);
      if (resSave) resSave.textContent = fmtINR(savings);
      if (resToken) resToken.textContent = fmtINR(tokenAmt);
    };

    [duesInput, setPctInput, tokPctInput].forEach(inp => {
      inp.addEventListener("input", calculate);
      inp.addEventListener("change", calculate);
    });
    calculate();
  };

  const wireDilution = () => {
    const raiseInput = document.getElementById("dil-raise");
    const preInput = document.getElementById("dil-pre");

    if (!raiseInput || !preInput) return;

    const raiseOut = document.getElementById("dil-raise-val");
    const preOut = document.getElementById("dil-pre-val");

    const resPost = document.getElementById("res-dil-post");
    const resDil = document.getElementById("res-dil-dil");
    const resRet = document.getElementById("res-dil-ret");

    const calculate = () => {
      const raise = +raiseInput.value;
      const pre = +preInput.value;

      if (raiseOut) raiseOut.textContent = fmtINR(raise);
      if (preOut) preOut.textContent = fmtINR(pre);

      const post = pre + raise;
      const dilution = post > 0 ? (raise / post) * 100 : 0;
      const retain = Math.max(0, 100 - dilution);

      if (resPost) resPost.textContent = fmtINR(post);
      if (resDil) resDil.textContent = dilution.toFixed(1) + "%";
      if (resRet) resRet.textContent = retain.toFixed(1) + "%";
    };

    [raiseInput, preInput].forEach(inp => {
      inp.addEventListener("input", calculate);
      inp.addEventListener("change", calculate);
    });
    calculate();
  };

  const wireIPO = () => {
    const issueInput = document.getElementById("ipo-issue");
    const preInput = document.getElementById("ipo-pre");

    if (!issueInput || !preInput) return;

    const issueOut = document.getElementById("ipo-issue-val");
    const preOut = document.getElementById("ipo-pre-val");

    const resPost = document.getElementById("res-ipo-post");
    const resPublic = document.getElementById("res-ipo-pub");
    const resProm = document.getElementById("res-ipo-prom");

    const calculate = () => {
      const fresh = +issueInput.value;
      const pre = +preInput.value;

      if (issueOut) issueOut.textContent = fmtINR(fresh);
      if (preOut) preOut.textContent = fmtINR(pre);

      const post = pre + fresh;
      const pubPct = post > 0 ? (fresh / post) * 100 : 0;
      const promPct = Math.max(0, 100 - pubPct);

      if (resPost) resPost.textContent = fmtINR(post);
      if (resPublic) resPublic.textContent = pubPct.toFixed(1) + "%";
      if (resProm) resProm.textContent = promPct.toFixed(1) + "%";
    };

    [issueInput, preInput].forEach(inp => {
      inp.addEventListener("input", calculate);
      inp.addEventListener("change", calculate);
    });
    calculate();
  };

  const wireValuation = () => {
    const ebitdaInput = document.getElementById("val-ebitda");
    const multLoInput = document.getElementById("val-mlo");
    const multHiInput = document.getElementById("val-mhi");

    if (!ebitdaInput || !multLoInput || !multHiInput) return;

    const ebitdaOut = document.getElementById("val-ebitda-val");
    const multLoOut = document.getElementById("val-mlo-val");
    const multHiOut = document.getElementById("val-mhi-val");

    const resLo = document.getElementById("res-val-lo");
    const resHi = document.getElementById("res-val-hi");

    const calculate = () => {
      const ebitda = +ebitdaInput.value;
      let lo = +multLoInput.value;
      let hi = +multHiInput.value;

      if (hi < lo) {
        hi = lo;
        multHiInput.value = hi;
      }

      if (ebitdaOut) ebitdaOut.textContent = fmtINR(ebitda);
      if (multLoOut) multLoOut.textContent = lo + "x";
      if (multHiOut) multHiOut.textContent = hi + "x";

      if (resLo) resLo.textContent = fmtINR(ebitda * lo);
      if (resHi) resHi.textContent = fmtINR(ebitda * hi);
    };

    [ebitdaInput, multLoInput, multHiInput].forEach(inp => {
      inp.addEventListener("input", calculate);
      inp.addEventListener("change", calculate);
    });
    calculate();
  };

  const wireSubsidy = () => {
    const costInput = document.getElementById("sub-cost");
    const rateInput = document.getElementById("sub-rate");
    const capVal = parseFloat(document.getElementById("sub-cap")?.value || "1500000");

    if (!costInput || !rateInput) return;

    const costOut = document.getElementById("sub-cost-val");
    const rateOut = document.getElementById("sub-rate-val");

    const resSub = document.getElementById("res-sub-amt");
    const resNet = document.getElementById("res-sub-net");

    const calculate = () => {
      const cost = +costInput.value;
      const rate = +rateInput.value;

      if (costOut) costOut.textContent = fmtINR(cost);
      if (rateOut) rateOut.textContent = rate + "%";

      const subsidy = Math.min(cost * rate / 100, capVal);
      const net = Math.max(0, cost - subsidy);

      if (resSub) resSub.textContent = fmtINR(subsidy);
      if (resNet) resNet.textContent = fmtINR(net);
    };

    [costInput, rateInput].forEach(inp => {
      inp.addEventListener("input", calculate);
      inp.addEventListener("change", calculate);
    });
    calculate();
  };

  // Wire up all calculators
  wireEMI();
  wireInvoice();
  wireSettlement();
  wireDilution();
  wireValuation();
  wireIPO();
  wireSubsidy();

  // 8. LEAD GENERATION FORM VALIDATION
  const leadForms = document.querySelectorAll(".lead-form, form[onsubmit='return false;']");
  leadForms.forEach(form => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();

      const name = form.querySelector("input[placeholder='Your full name'], input[type='text']:nth-of-type(1)");
      const phone = form.querySelector("input[placeholder='+91'], input[type='tel']");
      const email = form.querySelector("input[type='email']");
      const consent = form.querySelector("input[type='checkbox']");

      let hasError = false;

      // Reset styles
      form.querySelectorAll("input, select, textarea").forEach(el => {
        el.style.borderColor = "";
      });

      if (name && !name.value.trim()) {
        name.style.borderColor = "red";
        hasError = true;
      }

      if (phone && (!phone.value.trim() || phone.value.length < 10)) {
        phone.style.borderColor = "red";
        hasError = true;
      }

      if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) {
        email.style.borderColor = "red";
        hasError = true;
      }

      if (consent && !consent.checked) {
        consent.parentElement.style.color = "red";
        hasError = true;
      }

      if (hasError) {
        alert("Please fill in all required fields and accept the communication consent checkbox.");
        return;
      }

      // Successful validation
      alert("Thank you. Your funding advisory inquiry has been received. Our advisory team will review your financial profile and call you back shortly.");
      form.reset();
    });
  });

  // 9. GSAP SCROLL & LOAD ANIMATIONS
  if (typeof gsap !== "undefined") {
    // Initial page load animations for Hero elements
    const heroTl = gsap.timeline();
    if (document.querySelector(".hero")) {
      heroTl.from(".hero .eyebrow", { opacity: 0, y: -20, duration: 0.8, ease: "power2.out" })
            .from(".hero h1", { opacity: 0, y: 30, duration: 1, ease: "power3.out" }, "-=0.6")
            .from(".hero .lead", { opacity: 0, y: 20, duration: 1, ease: "power2.out" }, "-=0.6")
            .from(".hero-cta-row, .hero-trust", { opacity: 0, y: 20, duration: 0.8, stagger: 0.1, ease: "power2.out" }, "-=0.6")
            .from(".hero-stats .stat", { opacity: 0, scale: 0.9, y: 20, duration: 0.8, stagger: 0.15, ease: "power2.out" }, "-=0.6")
            .from(".hero .stack-card", { opacity: 0, x: 50, duration: 1, ease: "power3.out" }, "-=0.8");
    } else if (document.querySelector(".service-banner")) {
      heroTl.from(".service-banner .eyebrow", { opacity: 0, y: -20, duration: 0.8, ease: "power2.out" })
            .from(".service-banner h1", { opacity: 0, y: 30, duration: 1, ease: "power3.out" }, "-=0.6")
            .from(".service-banner p.lead", { opacity: 0, y: 20, duration: 1, ease: "power2.out" }, "-=0.6")
            .from(".service-banner .hero-cta-row", { opacity: 0, y: 20, duration: 0.8, ease: "power2.out" }, "-=0.6")
            .from(".service-banner-art", { opacity: 0, scale: 0.96, y: 15, duration: 1, ease: "power2.out" }, "-=0.8");
    }

    // Intersection Observer for scroll triggers
    const observerOptions = {
      root: null,
      rootMargin: "0px 0px -100px 0px",
      threshold: 0.15
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = entry.target;
          observer.unobserve(target); // Only trigger once

          // Run GSAP reveal based on target class
          if (target.classList.contains("section-head")) {
            gsap.from(target, { opacity: 0, y: 30, duration: 0.8, ease: "power2.out" });
          } else if (target.classList.contains("pillars")) {
            const cards = target.querySelectorAll(".pillar-card");
            gsap.from(cards, {
              opacity: 0,
              y: 40,
              scale: 0.95,
              duration: 0.8,
              stagger: 0.15,
              ease: "power2.out",
              onStart: () => { gsap.set(cards, { transition: "none" }); },
              onComplete: () => { gsap.set(cards, { clearProps: "transition,opacity,transform" }); }
            });
          } else if (target.classList.contains("why-grid")) {
            const items = target.querySelectorAll(".why-item");
            gsap.from(items, {
              opacity: 0,
              y: 30,
              duration: 0.8,
              stagger: 0.1,
              ease: "power2.out",
              onStart: () => { gsap.set(items, { transition: "none" }); },
              onComplete: () => { gsap.set(items, { clearProps: "transition,opacity,transform" }); }
            });
          } else if (target.classList.contains("catalog-grid")) {
            const cards = target.querySelectorAll(".service-card");
            gsap.from(cards, {
              opacity: 0,
              y: 40,
              duration: 0.8,
              stagger: 0.1,
              ease: "power2.out",
              onStart: () => { gsap.set(cards, { transition: "none" }); },
              onComplete: () => { gsap.set(cards, { clearProps: "transition,opacity,transform" }); }
            });
          } else if (target.classList.contains("industry-grid")) {
            const cards = target.querySelectorAll(".industry-card");
            gsap.from(cards, {
              opacity: 0,
              y: 30,
              duration: 0.8,
              stagger: 0.1,
              ease: "power2.out",
              onStart: () => { gsap.set(cards, { transition: "none" }); },
              onComplete: () => { gsap.set(cards, { clearProps: "transition,opacity,transform" }); }
            });
          } else if (target.classList.contains("process-row")) {
            const steps = target.querySelectorAll(".process-step");
            gsap.from(steps, {
              opacity: 0,
              scale: 0.95,
              y: 30,
              duration: 0.8,
              stagger: 0.15,
              ease: "power2.out",
              onStart: () => { gsap.set(steps, { transition: "none" }); },
              onComplete: () => { gsap.set(steps, { clearProps: "transition,opacity,transform" }); }
            });
          } else if (target.classList.contains("route-timeline")) {
            const steps = target.querySelectorAll(".route-timeline-step");
            gsap.from(steps, {
              opacity: 0,
              x: -30,
              duration: 0.8,
              stagger: 0.15,
              ease: "power2.out",
              onStart: () => { gsap.set(steps, { transition: "none" }); },
              onComplete: () => { gsap.set(steps, { clearProps: "transition,opacity,transform" }); }
            });
          } else if (target.classList.contains("about-graphics") || target.classList.contains("contact-card")) {
            gsap.from(target, {
              opacity: 0,
              scale: 0.96,
              y: 30,
              duration: 1,
              ease: "power2.out"
            });
          }
        }
      });
    }, observerOptions);

    // Observe elements
    document.querySelectorAll(".section-head, .pillars, .why-grid, .catalog-grid.active, .industry-grid, .process-row, .route-timeline, .about-graphics, .contact-card").forEach(el => {
      revealObserver.observe(el);
    });

    // Also handle tab switches for catalog grids
    const catalogTabs = document.querySelectorAll(".catalog-tab");
    const catalogGrids = document.querySelectorAll(".catalog-grid");
    if (catalogTabs.length > 0 && catalogGrids.length > 0) {
      catalogTabs.forEach((tab, index) => {
        tab.addEventListener("click", () => {
          // Whenever switching tabs, make sure the cards are visible
          // In case the tab grid has not been animated yet
          const activeGrid = catalogGrids[index];
          if (activeGrid) {
            // Remove any GSAP inline styles that might hide them
            gsap.set(activeGrid.querySelectorAll(".service-card"), { clearProps: "all" });
            // Observe again
            revealObserver.observe(activeGrid);
          }
        });
      });
    }
  }
});

/* ==========================================================================
   GSAP HORIZONTAL LOOP MARQUEE WITH OBSERVER DIRECTION CHANGE
   ========================================================================== */
function horizontalLoop(items, config) {
  items = gsap.utils.toArray(items);
  config = config || {};
  let tl = gsap.timeline({
      repeat: config.repeat,
      paused: config.paused,
      defaults: { ease: "none" },
      onReverseComplete() {
        this.totalTime(this.rawTime() + this.duration() * 100);
      }
    }),
    length = items.length,
    startX = items[0].offsetLeft,
    times = [],
    widths = [],
    xPercents = [],
    curIndex = 0,
    pixelsPerSecond = (config.speed || 1) * 100,
    snap = config.snap === false ? v => v : gsap.utils.snap(config.snap || 1),
    totalWidth,
    curX,
    distanceToStart,
    distanceToLoop,
    item,
    i;

  gsap.set(items, {
    xPercent: (i, el) => {
      let w = (widths[i] = parseFloat(gsap.getProperty(el, "width", "px")));
      xPercents[i] = snap(
        (parseFloat(gsap.getProperty(el, "x", "px")) / w) * 100 +
          gsap.getProperty(el, "xPercent")
      );
      return xPercents[i];
    }
  });
  gsap.set(items, { x: 0 });
  totalWidth =
    items[length - 1].offsetLeft +
    (xPercents[length - 1] / 100) * widths[length - 1] -
    startX +
    items[length - 1].offsetWidth *
      gsap.getProperty(items[length - 1], "scaleX") +
    (config.paddingRight || 0);

  for (i = 0; i < length; i++) {
    item = items[i];
    curX = (xPercents[i] / 100) * widths[i];
    distanceToStart = item.offsetLeft + curX - startX;
    distanceToLoop =
      distanceToStart + widths[i] * gsap.getProperty(item, "scaleX");
    tl.to(
      item,
      {
        xPercent: snap(((curX - distanceToLoop) / widths[i]) * 100),
        duration: distanceToLoop / pixelsPerSecond
      },
      0
    )
      .fromTo(
        item,
        {
          xPercent: snap(
            ((curX - distanceToLoop + totalWidth) / widths[i]) * 100
          )
        },
        {
          xPercent: xPercents[i],
          duration:
            (curX - distanceToLoop + totalWidth - curX) / pixelsPerSecond,
          immediateRender: false
        },
        distanceToLoop / pixelsPerSecond
      )
      .add("label" + i, distanceToStart / pixelsPerSecond);
    times[i] = distanceToStart / pixelsPerSecond;
  }
  return tl;
}

// Init marquee on homepage only
(function () {
  const rail = document.getElementById("marqueeRail");
  if (!rail || typeof gsap === "undefined" || typeof Observer === "undefined") return;

  gsap.registerPlugin(Observer);

  const items = gsap.utils.toArray("#marqueeRail > span");
  const tl = horizontalLoop(items, {
    repeat: -1,
    speed: 0.6,
    paddingRight: 0
  });

  Observer.create({
    onChangeY(self) {
      let factor = 2.5;
      if (self.deltaY < 0) factor *= -1;
      gsap.timeline({ defaults: { ease: "none" } })
        .to(tl, { timeScale: factor * 2.5, duration: 0.2, overwrite: true })
        .to(tl, { timeScale: factor > 0 ? 1 : -1, duration: 1 }, "+=0.3");
  });
})();

// 8. FORM SUBMISSION TO Info@thecreditlane.in
document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll(".lead-form");
  forms.forEach(form => {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      
      const btn = form.querySelector("button[type='submit']");
      const origText = btn ? btn.textContent : "Submit";
      
      if (btn) {
        btn.disabled = true;
        btn.textContent = "Sending Inquiry...";
      }

      try {
        const formData = new FormData(form);
        formData.append("_captcha", "false");
        formData.append("_template", "table");
        if (!formData.has("_subject")) {
          formData.append("_subject", "New Advisory Request - The Credit Lane");
        }

        const response = await fetch("https://formsubmit.co/ajax/Info@thecreditlane.in", {
          method: "POST",
          body: formData,
          headers: {
            'Accept': 'application/json'
          }
        });

        if (response.ok || response.status === 200) {
          form.innerHTML = `
            <div style="padding: 32px 20px; text-align: center; background: rgba(36, 161, 72, 0.08); border: 1px solid #24a148; border-radius: var(--radius); margin-top: 10px;">
              <div style="font-size: 40px; margin-bottom: 12px;">✅</div>
              <h4 style="color: var(--navy-dark); font-size: 20px; font-family: var(--font-serif); margin-bottom: 8px;">Inquiry Submitted Successfully!</h4>
              <p style="font-size: 14px; color: var(--slate); line-height: 1.6; margin: 0;">Your details have been sent directly to <strong>Info@thecreditlane.in</strong>.<br>Our corporate advisory desk will review your requirements and reach out within 24 working hours.</p>
            </div>
          `;
        } else {
          throw new Error("Form submission error");
        }
      } catch (err) {
        // Direct browser form submission fallback
        form.action = "https://formsubmit.co/Info@thecreditlane.in";
        form.method = "POST";
        form.submit();
      }
    });
  });
});
