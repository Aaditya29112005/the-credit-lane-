<?php
/**
 * Hero Banner Block Template
 *
 * @package CreditLane
 */

$eyebrow    = get_field('hero_eyebrow') ?: 'CA · CS · ADVOCATE-LED CAPITAL ADVISORY — 10+ YEARS · ₹2,500 CR+ RAISED';
$title      = get_field('hero_title') ?: 'Capital for Your Next Stage of Growth.';
$description = get_field('hero_description') ?: 'We help Indian mid-market corporates, SMEs, and growth-stage companies secure structural debt, institutional equity, and government scheme subsidies through a network of 100+ partner banks & NBFCs.';
$btn1_text  = get_field('hero_primary_btn_text') ?: 'Explore All Funding Products →';
$btn1_url   = get_field('hero_primary_btn_url') ?: home_url('/loans/');
$btn2_text  = get_field('hero_secondary_btn_text') ?: 'Book Advisory Call';
$btn2_url   = get_field('hero_secondary_btn_url') ?: home_url('/contact/');
?>

<section class="hero" style="padding-bottom: 0;">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to right, rgba(8, 21, 39, 0.96) 0%, rgba(8, 21, 39, 0.65) 45%, rgba(8, 21, 39, 0.15) 100%); z-index: 1; pointer-events: none;"></div>
  <div class="wrap" style="padding-top: 40px; padding-bottom: 40px;">
    <div>
      <span class="eyebrow"><?php echo esc_html( $eyebrow ); ?></span>
      <h1><?php echo esc_html( $title ); ?></h1>
      <p style="margin-top: 16px; font-size: 16px; color: var(--slate-light); max-width: 680px; line-height: 1.6;">
        <?php echo esc_html( $description ); ?>
      </p>
      
      <div style="display: flex; gap: 16px; margin-top: 28px; flex-wrap: wrap;">
        <a href="<?php echo esc_url( $btn1_url ); ?>" class="btn btn-primary"><?php echo esc_html( $btn1_text ); ?></a>
        <a href="<?php echo esc_url( $btn2_url ); ?>" class="btn btn-outline"><?php echo esc_html( $btn2_text ); ?></a>
      </div>

      <div class="hero-stats" style="margin-top: 40px; display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 20px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 24px;">
        <div>
          <strong style="font-size: 26px; color: var(--gold-light); font-family: var(--font-serif); display: block;">₹2,500 Cr+</strong>
          <span style="font-size: 13px; color: var(--slate-light);">Sanctioned & Disbursed</span>
        </div>
        <div>
          <strong style="font-size: 26px; color: var(--gold-light); font-family: var(--font-serif); display: block;">100+</strong>
          <span style="font-size: 13px; color: var(--slate-light);">Lending Partners</span>
        </div>
        <div>
          <strong style="font-size: 26px; color: var(--gold-light); font-family: var(--font-serif); display: block;">10+ Yrs</strong>
          <span style="font-size: 13px; color: var(--slate-light);">Corporate Finance Desk</span>
        </div>
        <div>
          <strong style="font-size: 26px; color: var(--gold-light); font-family: var(--font-serif); display: block;">100%</strong>
          <span style="font-size: 13px; color: var(--slate-light);">Transparent Structure</span>
        </div>
      </div>
    </div>
  </div>
</section>
