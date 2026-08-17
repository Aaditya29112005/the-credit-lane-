<?php
/**
 * Home Template File
 *
 * @package CreditLane
 */

global $wp_query;
if ( isset($wp_query->is_404) && $wp_query->is_404 ) {
    $wp_query->is_404 = false;
    status_header( 200 );
}

include get_template_directory() . '/front-page.php';
