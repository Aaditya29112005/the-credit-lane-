<?php
/**
 * Testimonials ACF Block Template
 *
 * @package CreditLane
 */

$title    = get_field('testi_title') ?: 'Client Success Stories';
$subtitle = get_field('testi_subtitle') ?: 'See what business leaders say about working with The Credit Lane.';

$default_reviews = array(
    array(
        'quote'  => '"The Credit Lane structured our SIDBI machine loan at 8.2% p.a. within 12 business days. Highly professional CA team with zero upfront charges."',
        'author' => 'Rajesh Goel',
        'role'   => 'Managing Director, Precision Auto Components',
        'avatar' => 'RG'
    ),
    array(
        'quote'  => '"B2B invoice finance cleared our cash flow hurdles. We sell to top electronics manufacturers with a 90-day wait period. They set up the limit in 4 business days."',
        'author' => 'Siddharth Sharma',
        'role'   => 'Technology exporter, Noida Sector 63',
        'avatar' => 'SS'
    ),
    array(
        'quote'  => '"They compiled our FEMA-compliant share valuations and connected us with pre-IPO institutional funds. Exceptional merchant banking coordinate."',
        'author' => 'Alka Kathpalia',
        'role'   => 'Founder, Healthcare Chain',
        'avatar' => 'AK'
    )
);

$reviews = get_field('testimonials_items') ?: $default_reviews;
?>

<section class="testimonials-section" style="padding: 60px 0; background: var(--navy-dark);">
  <div class="wrap">
    <div style="text-align: center; margin-bottom: 40px;">
      <h2 style="color: var(--gold-light); font-size: 32px; font-family: var(--font-serif);"><?php echo esc_html( $title ); ?></h2>
      <p style="color: var(--slate-light); font-size: 16px; max-width: 600px; margin: 10px auto 0;"><?php echo esc_html( $subtitle ); ?></p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
      <?php foreach ( $reviews as $item ) : ?>
        <div class="testi-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <p class="quote" style="color: #ffffff; font-size: 15px; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            <?php echo esc_html( $item['quote'] ); ?>
          </p>
          <div style="display: flex; align-items: center; gap: 12px;">
            <div style="width: 40px; height: 40px; border-radius: 50%; background: var(--gold-light); color: var(--navy-dark); font-weight: 700; display: flex; align-items: center; justify-content: center; font-size: 14px;">
              <?php echo esc_html( isset($item['avatar']) ? $item['avatar'] : 'CL' ); ?>
            </div>
            <div>
              <b style="color: #ffffff; font-size: 15px; display: block;"><?php echo esc_html( $item['author'] ); ?></b>
              <span style="color: var(--slate-light); font-size: 13px;"><?php echo esc_html( $item['role'] ); ?></span>
            </div>
          </div>
        </div>
      <?php endforeach; ?>
    </div>
  </div>
</section>
