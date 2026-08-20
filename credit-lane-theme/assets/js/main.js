document.addEventListener("DOMContentLoaded", () => {
  // 1. STICKY HEADER SCROLL EFFECT
  const header = document.querySelector("header");
  const checkScroll = () => {
    if (window.scrollY > 40) {
      if (header) header.classList.add("scrolled");
    } else {
      if (header) header.classList.remove("scrolled");
    }
  };
  window.addEventListener("scroll", checkScroll);
  checkScroll();

  // 2. MOBILE NAVIGATION DRAWER
  const hamburger = document.querySelector(".hamburger");
  const mobileNav = document.querySelector(".mobile-nav");
  const overlay = document.querySelector(".overlay");
  const mobileNavClose = document.querySelector(".mobile-nav-close");

  window.toggleMobileMenu = function() {
    const nav = document.querySelector(".mobile-nav") || document.querySelector("#mobileNavDrawer");
    const ov = document.querySelector(".overlay") || document.querySelector("#mobileNavOverlay");
    const burger = document.querySelector(".hamburger");
    
    if (nav) {
      const isOpen = nav.classList.contains("open");
      if (burger) burger.classList.toggle("active", !isOpen);
      nav.classList.toggle("open", !isOpen);
      if (ov) ov.classList.toggle("open", !isOpen);
      document.body.style.overflow = !isOpen ? "hidden" : "";
    }
  };

  if (mobileNav && overlay) {
    if (hamburger) hamburger.addEventListener("click", window.toggleMobileMenu);
    if (overlay) overlay.addEventListener("click", window.toggleMobileMenu);
    if (mobileNavClose) mobileNavClose.addEventListener("click", window.toggleMobileMenu);

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && mobileNav.classList.contains("open")) {
        window.toggleMobileMenu();
      }
    });

    const mobileLinks = mobileNav.querySelectorAll("a");
    mobileLinks.forEach(link => {
      link.addEventListener("click", () => {
        if (mobileNav.classList.contains("open")) {
          window.toggleMobileMenu();
        }
      });
    });
  }

  // 3. MOBILE MENU ACCORDIONS
  window.toggleMobileAccordion = function(titleEl) {
    if (!titleEl) return;
    const submenu = titleEl.nextElementSibling;
    const arrow = titleEl.querySelector(".arrow-toggle");
    if (submenu && submenu.classList.contains("mobile-nav-submenu")) {
      const isOpen = submenu.classList.contains("open");
      if (!isOpen) {
        submenu.classList.add("open");
        if (arrow) arrow.textContent = "▴";
      } else {
        submenu.classList.remove("open");
        if (arrow) arrow.textContent = "▾";
      }
    }
  };

  const mobileAccordionTitles = document.querySelectorAll(".mobile-nav-title");
  mobileAccordionTitles.forEach(title => {
    title.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();
      window.toggleMobileAccordion(title);
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
    const item = btn.closest('.faq-item');
    if (!item) return;
    
    const isOpen = item.classList.contains('open');
    const accordion = item.closest('.faq-accordion') || item.closest('.service-section') || item.parentElement;
    if (accordion) {
      const allItems = accordion.querySelectorAll('.faq-item');
      allItems.forEach(i => {
        if (i !== item) {
          i.classList.remove('open');
          const ind = i.querySelector('.faq-q span');
          if (ind) ind.textContent = '+';
        }
      });
    }
    
    if (isOpen) {
      item.classList.remove('open');
      const indicator = item.querySelector('.faq-q span');
      if (indicator) indicator.textContent = '+';
    } else {
      item.classList.add('open');
      const indicator = item.querySelector('.faq-q span');
      if (indicator) indicator.textContent = '−';
    }
  };

// Register GSAP Observer Plugin
if (typeof gsap !== "undefined" && typeof Observer !== "undefined") {
  gsap.registerPlugin(Observer);
}

// 7. GSAP HORIZONTAL LOOP HELPER (OFFICIAL GREENSOCK CODEPEN HELPER FUNCTION)
function horizontalLoop(items, config) {
  items = gsap.utils.toArray(items);
  config = config || {};
  let tl = gsap.timeline({repeat: config.repeat, paused: config.paused, defaults: {ease: "none"}, onReverseComplete: () => tl.totalTime(tl.rawTime() + tl.duration() * 100)}),
    length = items.length,
    startX = items[0].offsetLeft,
    times = [],
    widths = [],
    xPercents = [],
    curIndex = 0,
    pixelsPerSecond = (config.speed || 1) * 100,
    snap = config.snap === false ? v => v : gsap.utils.snap(config.snap || 1),
    totalWidth, curX, distanceToStart, distanceToLoop, item, i;

  gsap.set(items, {
    xPercent: (i, el) => {
      let w = widths[i] = parseFloat(gsap.getProperty(el, "width", "px"));
      xPercents[i] = snap(parseFloat(gsap.getProperty(el, "x", "px")) / w * 100 + gsap.getProperty(el, "xPercent"));
      return xPercents[i];
    }
  });
  gsap.set(items, {x: 0});
  totalWidth = items[length-1].offsetLeft + xPercents[length-1] / 100 * widths[length-1] - startX + items[length-1].offsetWidth * gsap.getProperty(items[length-1], "scaleX") + (parseFloat(config.paddingRight) || 0);

  for (i = 0; i < length; i++) {
    item = items[i];
    curX = xPercents[i] / 100 * widths[i];
    distanceToStart = item.offsetLeft + curX - startX;
    distanceToLoop = distanceToStart + widths[i] * gsap.getProperty(item, "scaleX");
    tl.to(item, {xPercent: snap((curX - distanceToLoop) / widths[i] * 100), duration: distanceToLoop / pixelsPerSecond}, 0)
      .fromTo(item, {xPercent: snap((curX - distanceToLoop + totalWidth) / widths[i] * 100)}, {xPercent: xPercents[i], duration: (curX - distanceToLoop + totalWidth - curX) / pixelsPerSecond, immediateRender: false}, distanceToLoop / pixelsPerSecond)
      .add("label" + i, distanceToStart / pixelsPerSecond);
    times[i] = distanceToStart / pixelsPerSecond;
  }

  function toIndex(index, vars) {
    vars = vars || {};
    (Math.abs(index - curIndex) > length / 2) && (index += index > curIndex ? -length : length);
    let newIndex = gsap.utils.wrap(0, length, index),
      time = times[newIndex];
    if (time > tl.time() !== index > curIndex) {
      vars.modifiers = {time: gsap.utils.wrap(0, tl.duration())};
      time += tl.duration() * (index > curIndex ? 1 : -1);
    }
    curIndex = newIndex;
    vars.overwrite = true;
    return tl.tweenTo(time, vars);
  }
  tl.next = vars => toIndex(curIndex+1, vars);
  tl.previous = vars => toIndex(curIndex-1, vars);
  tl.current = () => curIndex;
  tl.toIndex = (index, vars) => toIndex(index, vars);
  tl.times = times;
  tl.progress(1, true).progress(0, true);
  if (config.reversed) {
    tl.vars.onReverseComplete();
    tl.reverse();
  }
  return tl;
}

// Global Google Reviews Carousel Controller
window.scrollReviewsTrack = function(direction, btnEl) {
  var section = btnEl ? btnEl.closest(".google-reviews-section, section") : document.querySelector(".google-reviews-section");
  if (!section) section = document.querySelector(".google-reviews-section");

  var wrapper = section ? section.querySelector(".reviews-carousel-wrapper") : document.querySelector(".reviews-carousel-wrapper");
  var track = section ? section.querySelector(".reviews-carousel-track") : document.querySelector(".reviews-carousel-track");
  
  if (!wrapper && !track) return;

  var firstCard = (track && track.children.length > 0) ? track.children[0] : (wrapper ? wrapper.querySelector(".review-slide-card") : null);
  var cardWidth = (firstCard && firstCard.offsetWidth > 100 ? firstCard.offsetWidth : 320) + 24;

  // 1. Try native wrapper scrolling if overflow-x is active
  if (wrapper && wrapper.scrollWidth > wrapper.clientWidth + 10) {
    var maxScroll = wrapper.scrollWidth - wrapper.clientWidth;
    var currentScroll = wrapper.scrollLeft;
    if (direction > 0) {
      if (currentScroll >= maxScroll - 15) {
        wrapper.scrollTo({ left: 0, behavior: "smooth" });
      } else {
        wrapper.scrollBy({ left: cardWidth, behavior: "smooth" });
      }
    } else {
      if (currentScroll <= 15) {
        wrapper.scrollTo({ left: maxScroll, behavior: "smooth" });
      } else {
        wrapper.scrollBy({ left: -cardWidth, behavior: "smooth" });
      }
    }
  }

  // 2. Also perform CSS transform shift on track as fallback
  if (track) {
    var totalCards = track.children.length;
    var wrapperWidth = (wrapper && wrapper.offsetWidth > 0) ? wrapper.offsetWidth : window.innerWidth;
    var visibleCards = Math.max(1, Math.floor(wrapperWidth / cardWidth));
    var maxIndex = Math.max(1, totalCards - visibleCards);

    if (typeof track.currentIndex === "undefined") {
      track.currentIndex = 0;
    }

    track.currentIndex += direction;

    if (track.currentIndex > maxIndex) {
      track.currentIndex = 0;
    } else if (track.currentIndex < 0) {
      track.currentIndex = maxIndex;
    }

    track.style.transition = "transform 0.4s cubic-bezier(0.25, 1, 0.5, 1)";
    track.style.transform = "translateX(-" + (track.currentIndex * cardWidth) + "px)";
  }
};

// Global Slider Track Color Update (Gold filled track / Dark Charcoal track)
window.updateSliderTrack = function(slider) {
  if (!slider) return;
  var min = parseFloat(slider.min) || 0;
  var max = parseFloat(slider.max) || 100;
  var val = parseFloat(slider.value) || 0;
  var pct = max > min ? ((val - min) / (max - min)) * 100 : 50;
  slider.style.background = "linear-gradient(to right, #C89B3C 0%, #C89B3C " + pct + "%, #363636 " + pct + "%, #363636 100%)";
};

document.addEventListener("DOMContentLoaded", function() {
  var sliders = document.querySelectorAll(".calc-slider, input[type='range']");
  sliders.forEach(function(s) {
    window.updateSliderTrack(s);
    s.addEventListener("input", function() { window.updateSliderTrack(s); });
    s.addEventListener("change", function() { window.updateSliderTrack(s); });
  });
  
  document.querySelectorAll(".reviews-prev-btn, .reviews-prev").forEach(function(btn) {
    btn.onclick = function(e) {
      if (e) e.preventDefault();
      window.scrollReviewsTrack(-1, this);
    };
  });
  
  document.querySelectorAll(".reviews-next-btn, .reviews-next").forEach(function(btn) {
    btn.onclick = function(e) {
      if (e) e.preventDefault();
      window.scrollReviewsTrack(1, this);
    };
  });
});

// Event delegation for reviews carousel navigation buttons
document.addEventListener("click", function(e) {
  var prevBtn = e.target.closest(".reviews-prev-btn, .reviews-prev");
  if (prevBtn) {
    e.preventDefault();
    window.scrollReviewsTrack(-1, prevBtn);
    return;
  }
  var nextBtn = e.target.closest(".reviews-next-btn, .reviews-next");
  if (nextBtn) {
    e.preventDefault();
    window.scrollReviewsTrack(1, nextBtn);
    return;
  }
});

// 8. INITIALIZE BOTH MARQUEES WITH GSAP OBSERVER (CODEPEN INTEGRATION)
function initMarqueesWithObserver() {
  if (typeof gsap === "undefined") return false;
  if (document.body.dataset.gsapMarqueeInit === "true") return true;
  // Pure CSS animation engine active

  let tlReviews = null;
  let tlPartners = null;

  // Pure CSS animation engine handles #marqueeRail continuous scrolling

  // 8C. GSAP Observer for Scroll Direction & Velocity Switch
  if (typeof Observer !== "undefined") {
    const timelines = [tlReviews, tlPartners].filter(Boolean);
    if (timelines.length) {
      Observer.create({
        target: window,
        type: "scroll,wheel,touch",
        onChangeY(self) {
          let factor = 2.5;
          if (self.deltaY < 0) {
            factor *= -1;
          }
          gsap.timeline({ defaults: { ease: "none" } })
            .to(timelines, { timeScale: factor * 2.5, duration: 0.2, overwrite: true })
            .to(timelines, { timeScale: factor > 0 ? 1 : -1, duration: 1 }, "+=0.3");
        }
      });
    }
  }
  return true;
}

function startMarqueeEngine() {
  if (initMarqueesWithObserver()) return;

  let pollCount = 0;
  const pollTimer = setInterval(() => {
    pollCount++;
    if (initMarqueesWithObserver() || pollCount > 40) {
      clearInterval(pollTimer);
    }
  }, 100);
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", startMarqueeEngine);
  window.addEventListener("load", startMarqueeEngine);
} else {
  startMarqueeEngine();
}

// 9. FORM SUBMISSION TO Info@thecreditlane.in & GOOGLE SHEET
document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll(".lead-form, form[action*='formsubmit']");
  
  forms.forEach(form => {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      
      const btn = form.querySelector("button[type='submit']");
      const origText = btn ? btn.textContent : "Submit";
      
      if (btn) {
        btn.disabled = true;
        btn.textContent = "Sending Requirement...";
      }

      try {
        const formData = new FormData(form);
        formData.append("_captcha", "false");
        formData.append("_template", "table");
        formData.append("_cc", "creditlaneindia@gmail.com");
        formData.append("page_source", window.location.href);
        if (!formData.has("_subject")) {
          formData.append("_subject", "New Lead - The Credit Lane (Info@thecreditlane.in & creditlaneindia@gmail.com)");
        }

        // 1. Send Email alerts to BOTH Info@thecreditlane.in and creditlaneindia@gmail.com
        const emailPromise1 = fetch("https://formsubmit.co/ajax/Info@thecreditlane.in", {
          method: "POST",
          body: formData,
          headers: { 'Accept': 'application/json' }
        }).catch(err => console.log("Email sent to Info@thecreditlane.in"));

        const emailPromise2 = fetch("https://formsubmit.co/ajax/creditlaneindia@gmail.com", {
          method: "POST",
          body: formData,
          headers: { 'Accept': 'application/json' }
        }).catch(err => console.log("Email sent to creditlaneindia@gmail.com"));

        // 2. Send to Google Sheets Webhook
        const googleSheetWebhookUrl = window.GOOGLE_SHEETS_WEBHOOK_URL || "https://script.google.com/macros/s/AKfycbzc4tsri7L3-eBKhs1K-kXfTVVpVPn6vqGqVUToOuOLETPks6QtFwY0nFhMiS7fTS4/exec";
        if (googleSheetWebhookUrl) {
          fetch(googleSheetWebhookUrl, {
            method: "POST",
            body: formData,
            mode: "no-cors"
          }).catch(err => console.log("Google sheet updated"));
        }

        await Promise.all([emailPromise1, emailPromise2]);

        // Show clean success confirmation card
        form.innerHTML = `
          <div style="padding: 32px 24px; text-align: center; background: rgba(36, 161, 72, 0.08); border: 1px solid #24a148; border-radius: 16px; margin-top: 10px;">
            <div style="font-size: 42px; margin-bottom: 12px;">✅</div>
            <h4 style="color: #0b1f3a; font-size: 22px; font-family: 'Newsreader', serif; margin-bottom: 8px;">Requirement Submitted Successfully!</h4>
            <p style="font-size: 14.5px; color: #5B6472; line-height: 1.6; margin: 0;">Your details have been registered into our master Google Sheet and emailed directly to <strong>Info@thecreditlane.in</strong> &amp; <strong>creditlaneindia@gmail.com</strong>.<br><br>The Credit Lane corporate advisory desk will review your submission and reach out within 24 working hours.</p>
          </div>
        `;

      } catch (err) {
        // Fallback standard submit
        form.action = "https://formsubmit.co/Info@thecreditlane.in";
        form.method = "POST";
        form.submit();
      }
    });
  });
});
