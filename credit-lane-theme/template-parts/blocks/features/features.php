<?php
/**
 * Features & Advisory Process ACF Block Template
 *
 * @package CreditLane
 */

$title    = get_field('features_title') ?: 'Why Indian Mid-Market Corporates Trust The Credit Lane';
$subtitle = get_field('features_subtitle') ?: 'Led by Chartered Accountants and Corporate Advocates with over a decade of financial structuring experience.';
?>

<section class="features-section" style="padding: 60px 0; background: var(--navy-medium);">
  <div class="wrap">
    <div style="text-align: center; margin-bottom: 40px;">
      <h2 style="color: var(--gold-light); font-size: 32px; font-family: var(--font-serif);"><?php echo esc_html( $title ); ?></h2>
      <p style="color: var(--slate-light); font-size: 16px; max-width: 640px; margin: 10px auto 0;"><?php echo esc_html( $subtitle ); ?></p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
        <span style="font-size: 32px; display: block; margin-bottom: 12px;">📊</span>
        <h3 style="color: #ffffff; font-size: 20px; font-family: var(--font-serif); margin-bottom: 8px;">CA & Advocate Led Desk</h3>
        <p style="color: var(--slate-light); font-size: 14px; line-height: 1.6;">Direct advisory from financial professionals who understand credit underwriting, tax laws, and MCA compliances.</p>
      </div>

      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
        <span style="font-size: 32px; display: block; margin-bottom: 12px;">🏛️</span>
        <h3 style="color: #ffffff; font-size: 20px; font-family: var(--font-serif); margin-bottom: 8px;">100+ Partner Network</h3>
        <p style="color: var(--slate-light); font-size: 14px; line-height: 1.6;">Direct access to PSU banks, private banks, NBFCs, AIFs, and SIDBI key decision makers.</p>
      </div>

      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
        <span style="font-size: 32px; display: block; margin-bottom: 12px;">📜</span>
        <h3 style="color: #ffffff; font-size: 20px; font-family: var(--font-serif); margin-bottom: 8px;">Government Subsidies</h3>
        <p style="color: var(--slate-light); font-size: 14px; line-height: 1.6;">Maximize capital, interest, and stamp duty subsidies through State & Central government schemes.</p>
      </div>
    </div>
  </div>
</section>
