<?php
/**
 * Loan Cards Grid ACF Block Template
 *
 * @package CreditLane
 */

$title    = get_field('section_title') ?: 'Our Core Debt & Funding Solutions';
$subtitle = get_field('section_subtitle') ?: 'Tailored corporate finance products designed for working capital, expansion, and balance sheet optimization.';

$default_loans = array(
    array('title' => 'Unsecured Business Loan & DOD Limit', 'desc' => 'Working Capital without pledging collateral.', 'badge' => 'Up to ₹10 Cr', 'link' => home_url('/loans/unsecured-business-loan-dod/')),
    array('title' => 'Commercial or Industrial Purchase Loan', 'desc' => 'Own the commercial premises you currently rent.', 'badge' => 'Up to 90% LTV', 'link' => home_url('/loans/commercial-industrial-purchase-loan/')),
    array('title' => 'Machine Loan from SIDBI', 'desc' => 'Machinery finance on SIDBI’s SME-first terms.', 'badge' => 'Subsidised Interest', 'link' => home_url('/loans/machine-loan-sidbi/')),
    array('title' => 'Sale / Purchase Invoice Finance', 'desc' => 'Unlock cash tied up in unpaid B2B invoices.', 'badge' => '72-Hour Disbursal', 'link' => home_url('/loans/invoice-finance/')),
    array('title' => 'School & College Funding', 'desc' => 'Infrastructure finance for educational institutions.', 'badge' => 'Long Tenure', 'link' => home_url('/loans/school-college-funding/')),
    array('title' => 'Builder & Real Estate Funding', 'desc' => 'Construction finance structured around project timelines.', 'badge' => 'Custom Drawdown', 'link' => home_url('/loans/builder-real-estate-funding/')),
);

$loans = get_field('loan_items');
if ( ! $loans || empty($loans) ) {
    $loans = $default_loans;
}
?>

<section class="loans-grid-section" style="padding: 60px 0; background: var(--navy-medium);">
  <div class="wrap">
    <div style="text-align: center; margin-bottom: 40px;">
      <h2 style="color: var(--gold-light); font-size: 32px; font-family: var(--font-serif);"><?php echo esc_html( $title ); ?></h2>
      <p style="color: var(--slate-light); font-size: 16px; max-width: 640px; margin: 12px auto 0;"><?php echo esc_html( $subtitle ); ?></p>
    </div>

    <div class="catalog-grid active" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
      <?php foreach ( $loans as $item ) : ?>
        <div class="card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <?php if ( ! empty($item['badge']) ) : ?>
              <span class="badge" style="background: rgba(212, 175, 55, 0.15); color: var(--gold-light); padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: 600; display: inline-block; margin-bottom: 12px;"><?php echo esc_html( $item['badge'] ); ?></span>
            <?php endif; ?>
            <h3 style="color: #ffffff; font-size: 20px; margin-bottom: 8px; font-family: var(--font-serif);"><?php echo esc_html( $item['title'] ); ?></h3>
            <p style="color: var(--slate-light); font-size: 14px; line-height: 1.5; margin-bottom: 20px;"><?php echo esc_html( $item['desc'] ); ?></p>
          </div>
          <a href="<?php echo esc_url( isset($item['link']) ? $item['link'] : '#' ); ?>" class="btn btn-outline" style="font-size: 13px; padding: 8px 16px; width: 100%; text-align: center;">View Loan Details &rarr;</a>
        </div>
      <?php endforeach; ?>
    </div>
  </div>
</section>
