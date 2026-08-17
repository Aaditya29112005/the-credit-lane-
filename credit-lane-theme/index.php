<?php
/**
 * Main Template File
 *
 * @package CreditLane
 */

global $wp_query;

if ( is_front_page() || is_home() || ! have_posts() ) {
    if ( isset($wp_query->is_404) ) {
        $wp_query->is_404 = false;
        status_header( 200 );
    }
    include get_template_directory() . '/front-page.php';
    exit;
}

get_header();

while ( have_posts() ) : the_post();
    the_content();
endwhile;

get_footer();
