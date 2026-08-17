<?php
/**
 * 404 Error Fallback Template
 *
 * @package CreditLane
 */

$req_uri = isset($_SERVER['REQUEST_URI']) ? trim(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/') : '';
if ( $req_uri === '' || $req_uri === 'index.php' || is_front_page() || is_home() ) {
    global $wp_query;
    if ( isset($wp_query->is_404) ) {
        $wp_query->is_404 = false;
        status_header( 200 );
    }
    include get_template_directory() . '/front-page.php';
    exit;
}

get_header();
?>

<section class="error-404 not-found" style="padding: 120px 0 80px; text-align: center;">
  <div class="wrap">
    <div style="max-width: 600px; margin: 0 auto; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 24px; padding: 48px 24px;">
      <h1 style="font-size: 72px; color: var(--gold); margin-bottom: 12px; font-weight: 900;">404</h1>
      <h2 style="font-size: 24px; color: #fff; margin-bottom: 16px;">Page Not Found</h2>
      <p style="color: #94A3B8; margin-bottom: 32px; font-size: 15px;">The page you are looking for may have been moved, renamed, or is currently unavailable.</p>
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="btn btn-primary" style="padding: 14px 32px; font-size: 15px;">Return To Homepage &rarr;</a>
    </div>
  </div>
</section>

<?php
get_footer();
