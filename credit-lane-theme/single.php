<?php
/**
 * Single Post Template
 *
 * @package CreditLane
 */

get_header();
?>
<section style="padding: 60px 0; background: var(--navy-dark); color: #ffffff;">
  <div class="wrap">
    <?php
    if ( have_posts() ) :
        while ( have_posts() ) : the_post();
            echo '<h1 style="color: var(--gold-light); margin-bottom: 24px;">' . esc_html( get_the_title() ) . '</h1>';
            echo '<div class="post-content" style="line-height: 1.8; font-size: 16px;">';
            the_content();
            echo '</div>';
        endwhile;
    endif;
    ?>
  </div>
</section>
<?php
get_footer();
