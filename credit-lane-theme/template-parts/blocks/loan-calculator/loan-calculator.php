<?php
/**
 * Loan Calculator ACF Block Template
 *
 * @package CreditLane
 */

$title    = get_field('calc_title') ?: 'Financial & EMI Calculators';
$subtitle = get_field('calc_subtitle') ?: 'Calculate monthly EMIs, invoice factoring costs, and government subsidy eligibility instantaneously.';
?>

<section class="calculator-section" style="padding: 60px 0; background: var(--navy-dark);">
  <div class="wrap">
    <div style="text-align: center; margin-bottom: 36px;">
      <h2 style="color: var(--gold-light); font-size: 32px; font-family: var(--font-serif);"><?php echo esc_html( $title ); ?></h2>
      <p style="color: var(--slate-light); font-size: 16px; max-width: 600px; margin: 10px auto 0;"><?php echo esc_html( $subtitle ); ?></p>
    </div>

    <!-- Calculator Card -->
    <div class="calc-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 32px; max-width: 800px; margin: 0 auto;">
      <div class="calc-inputs">
        <div class="field" style="margin-bottom: 24px;">
          <label style="display: flex; justify-content: space-between; color: #ffffff; font-size: 14px; margin-bottom: 8px;">
            <span>Loan Amount (Principal)</span>
            <strong id="emi-p-val" style="color: var(--gold-light);">₹50,00,000</strong>
          </label>
          <input type="range" id="emi-p" min="500000" max="100000000" step="500000" value="5000000" oninput="updateEmiCalc()" style="width: 100%; accent-color: var(--gold-light);">
        </div>

        <div class="field" style="margin-bottom: 24px;">
          <label style="display: flex; justify-content: space-between; color: #ffffff; font-size: 14px; margin-bottom: 8px;">
            <span>Annual Interest Rate (%)</span>
            <strong id="emi-r-val" style="color: var(--gold-light);">9.5%</strong>
          </label>
          <input type="range" id="emi-r" min="6" max="24" step="0.25" value="9.5" oninput="updateEmiCalc()" style="width: 100%; accent-color: var(--gold-light);">
        </div>

        <div class="field" style="margin-bottom: 24px;">
          <label style="display: flex; justify-content: space-between; color: #ffffff; font-size: 14px; margin-bottom: 8px;">
            <span>Loan Tenure (Years)</span>
            <strong id="emi-y-val" style="color: var(--gold-light);">5 yrs</strong>
          </label>
          <input type="range" id="emi-y" min="1" max="15" step="1" value="5" oninput="updateEmiCalc()" style="width: 100%; accent-color: var(--gold-light);">
        </div>
      </div>

      <!-- Results Display -->
      <div class="calc-results" style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 24px; margin-top: 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; text-align: center;">
        <div>
          <span style="font-size: 12px; color: var(--slate-light); text-transform: uppercase;">Monthly EMI</span>
          <strong id="res-emi" style="display: block; font-size: 24px; color: var(--gold-light); font-family: var(--font-serif); margin-top: 4px;">₹1,04,991</strong>
        </div>
        <div>
          <span style="font-size: 12px; color: var(--slate-light); text-transform: uppercase;">Total Interest Payable</span>
          <strong id="res-interest" style="display: block; font-size: 24px; color: #ffffff; font-family: var(--font-serif); margin-top: 4px;">₹12,99,483</strong>
        </div>
        <div>
          <span style="font-size: 12px; color: var(--slate-light); text-transform: uppercase;">Total Outflow</span>
          <strong id="res-total" style="display: block; font-size: 24px; color: #ffffff; font-family: var(--font-serif); margin-top: 4px;">₹62,99,483</strong>
        </div>
      </div>

      <div style="text-align: center; margin-top: 24px;">
        <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="btn btn-primary">Apply for Sanction at these Terms →</a>
      </div>
    </div>
  </div>
</section>
