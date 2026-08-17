<?php
/**
 * Page Template for All Website Pages
 *
 * @package CreditLane
 */

get_header();

global $post;
$slug = isset( $post->post_name ) ? $post->post_name : '';
$template_file = get_template_directory() . '/pages/' . $slug . '.php';

if ( file_exists( $template_file ) ) {
    include $template_file;
} else {
    // Default page renderer
    if ( have_posts() ) :
        while ( have_posts() ) : the_post();
            echo '<section style="padding: 60px 0; background: var(--navy-dark); color: #ffffff;">';
            echo '<div class="wrap">';
            echo '<h1 style="color: var(--gold-light); margin-bottom: 24px; font-family: var(--font-serif);">' . esc_html( get_the_title() ) . '</h1>';
            echo '<div class="page-content" style="line-height: 1.8; font-size: 16px;">';
            the_content();
            echo '</div>';
            echo '</div>';
            echo '</section>';
        endwhile;
    endif;
}

get_footer();
