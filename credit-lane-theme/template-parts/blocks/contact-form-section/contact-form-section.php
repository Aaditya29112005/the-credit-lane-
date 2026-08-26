<?php
/**
 * Contact Form Section ACF Block Template
 *
 * @package CreditLane
 */

$title       = get_field('contact_title') ?: 'Discuss Your Funding Requirement';
$subtitle    = get_field('contact_subtitle') ?: 'Speak directly with The Credit Lane CA, CS, Advocate led advisory desk.';
$form_code   = get_field('contact_form_shortcode') ?: '';
?>

<section class="contact-section" style="padding: 60px 0; background: var(--navy-medium);">
  <div class="wrap" style="max-width: 900px;">
    <div style="text-align: center; margin-bottom: 36px;">
      <h2 style="color: var(--gold-light); font-size: 32px; font-family: var(--font-serif);"><?php echo esc_html( $title ); ?></h2>
      <p style="color: var(--slate-light); font-size: 16px; max-width: 600px; margin: 10px auto 0;"><?php echo esc_html( $subtitle ); ?></p>
    </div>

    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 32px;">
      <?php if ( ! empty( $form_code ) ) : ?>
        <?php echo do_shortcode( $form_code ); ?>
      <?php else : ?>
        <form action="https://script.google.com/macros/s/AKfycbzaSs_XJESePwtNQJZDAGWiyHISLA66LCuXEhPCeLhVWp58g472FDNjuJPH75gxPTNw/exec" method="POST" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
          <input type="hidden" name="_cc" value="creditlaneindia@gmail.com">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_subject" value="New Contact Inquiry - The Credit Lane">
          
          <div>
            <label style="color: #ffffff; font-size: 13.5px; font-weight: 600; display: block; margin-bottom: 6px;">Full Name *</label>
            <input type="text" name="full_name" placeholder="Full Name" required style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: rgba(0,0,0,0.3); color: #fff;">
          </div>
          <div>
            <label style="color: #ffffff; font-size: 13.5px; font-weight: 600; display: block; margin-bottom: 6px;">Phone Number *</label>
            <input type="tel" name="phone" placeholder="10-digit Mobile Number" required style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: rgba(0,0,0,0.3); color: #fff;">
          </div>
          <div>
            <label style="color: #ffffff; font-size: 13.5px; font-weight: 600; display: block; margin-bottom: 6px;">Business Type *</label>
            <select name="business_type" required style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: rgba(8,21,39,0.9); color: #fff;">
              <option value="">Select Business Type</option>
              <option value="Manufacturing">Manufacturing</option>
              <option value="Trading / Wholesale">Trading / Wholesale</option>
              <option value="Services / IT">Services / IT</option>
              <option value="Real Estate / Construction">Real Estate / Construction</option>
              <option value="Healthcare / Hospital">Healthcare / Hospital</option>
              <option value="Education / School">Education / School</option>
              <option value="Hospitality / Hotel">Hospitality / Hotel</option>
              <option value="Infrastructure">Infrastructure</option>
              <option value="Other">Other</option>
            </select>
          </div>
          <div>
            <label style="color: #ffffff; font-size: 13.5px; font-weight: 600; display: block; margin-bottom: 6px;">Funding Requirement *</label>
            <select name="funding_requirement" required style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: rgba(8,21,39,0.9); color: #fff;">
              <option value="">Select Requirement</option>
              <option value="Unsecured Business Loan / DOD">Unsecured Business Loan / DOD</option>
              <option value="Commercial / Industrial Purchase Loan">Commercial / Industrial Purchase Loan</option>
              <option value="Machine Loan (SIDBI / Bank)">Machine Loan (SIDBI / Bank)</option>
              <option value="Sale / Purchase Invoice Finance">Sale / Purchase Invoice Finance</option>
              <option value="Real Estate / Builder Funding">Real Estate / Builder Funding</option>
              <option value="Hospital / School Funding">Hospital / School Funding</option>
              <option value="NPA Funding / Debt Resolution">NPA Funding / Debt Resolution</option>
              <option value="Pre-IPO / SME IPO / Equity Advisory">Pre-IPO / SME IPO / Equity Advisory</option>
              <option value="Government Grant / Subsidy (TUS / MSME)">Government Grant / Subsidy (TUS / MSME)</option>
              <option value="Other">Other</option>
            </select>
          </div>
          <div style="grid-column: 1 / -1;">
            <label style="color: #ffffff; font-size: 13.5px; font-weight: 600; display: block; margin-bottom: 6px;">Required Funding Amount *</label>
            <select name="funding_amount" required style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: rgba(8,21,39,0.9); color: #fff;">
              <option value="">Select Funding Range</option>
              <option value="5lac to 25lac">₹5 Lac to ₹25 Lac</option>
              <option value="above 25lac">Above ₹25 Lac</option>
              <option value="₹25 Lac - ₹1 Crore">₹25 Lac - ₹1 Crore</option>
              <option value="₹1 Crore - ₹5 Crore">₹1 Crore - ₹5 Crore</option>
              <option value="Above ₹5 Crore">Above ₹5 Crore</option>
            </select>
          </div>
          <div style="grid-column: 1 / -1;">
            <label style="color: #ffffff; font-size: 13.5px; font-weight: 600; display: block; margin-bottom: 6px;">Brief Requirement / Message</label>
            <textarea name="requirement" rows="3" placeholder="Describe your funding needs or turnover..." style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: rgba(0,0,0,0.3); color: #fff;"></textarea>
          </div>
          <div style="grid-column: 1 / -1; text-align: center; margin-top: 10px;">
            <button type="submit" class="btn btn-primary" style="padding: 14px 36px; font-size: 16px; width: 100%;">Submit Request for Advisory Callback →</button>
          </div>
        </form>
      <?php endif; ?>
    </div>
  </div>
</section>
