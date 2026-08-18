<?php
/**
 * The Credit Lane Theme Functions & Definitions
 *
 * @package CreditLane
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Theme Setup
 */
function credit_lane_setup() {
    add_theme_support( 'automatic-feed-links' );
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    add_theme_support( 'align-wide' );
    add_theme_support( 'responsive-embeds' );

    add_theme_support( 'custom-logo', array(
        'height'      => 80,
        'width'       => 80,
        'flex-height' => true,
        'flex-width'  => true,
    ) );

    register_nav_menus( array(
        'primary-menu' => __( 'Primary Header Menu', 'credit-lane' ),
        'footer-menu'  => __( 'Footer Menu', 'credit-lane' ),
    ) );
}
add_action( 'after_setup_theme', 'credit_lane_setup' );

/**
 * Enqueue Scripts and Styles
 */
function credit_lane_scripts() {
    // Google Fonts
    wp_enqueue_style( 'credit-lane-font-jakarta', 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap', array(), null );

    // Theme CSS
    wp_enqueue_style( 'credit-lane-style', get_stylesheet_uri(), array(), '1.3.0' );
    wp_enqueue_style( 'credit-lane-main', get_template_directory_uri() . '/assets/css/main.css', array('credit-lane-font-jakarta'), '1.3.0' );

    // GSAP Libraries for Motion Animations
    wp_enqueue_script( 'gsap', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js', array(), '3.12.5', true );
    wp_enqueue_script( 'gsap-scroll-trigger', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js', array('gsap'), '3.12.5', true );
    wp_enqueue_script( 'gsap-observer', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/Observer.min.js', array('gsap'), '3.12.5', true );

    // Theme Core JS
    wp_enqueue_script( 'credit-lane-main-js', get_template_directory_uri() . '/assets/js/main.js', array('gsap', 'gsap-scroll-trigger', 'gsap-observer'), '1.3.0', true );
}
add_action( 'wp_enqueue_scripts', 'credit_lane_scripts' );

/**
 * Auto-set Permalinks to /%postname%/ and Static Home Page
 */
function credit_lane_setup_permalinks() {
    global $wp_rewrite;
    if ( strpos( get_option( 'permalink_structure' ), '%postname%' ) === false ) {
        update_option( 'permalink_structure', '/%postname%/' );
        $wp_rewrite->set_permalink_structure( '/%postname%/' );
    }
    // Set static front page if not already set
    $home_page = get_page_by_path( 'home' ) ?: get_page_by_title( 'Home' );
    if ( $home_page && get_option( 'show_on_front' ) !== 'page' ) {
        update_option( 'show_on_front', 'page' );
        update_option( 'page_on_front', $home_page->ID );
    }
    flush_rewrite_rules();
}
add_action( 'after_switch_theme', 'credit_lane_setup_permalinks' );
add_action( 'admin_init', 'credit_lane_setup_permalinks' );

/**
 * Auto-create Website Pages with Hierarchy
 */
function credit_lane_auto_create_pages() {
    // 1. Parent Pages
    $parents = array(
        'About Us' => 'about',
        'Partner With Us' => 'partner-with-us',
        'Contact Us' => 'contact',
        'Loans' => 'loans',
        'Equity' => 'equity',
        'Incentives' => 'incentives',
    );

    $parent_ids = array();
    foreach ( $parents as $title => $slug ) {
        $existing = get_page_by_path( $slug );
        if ( $existing ) {
            $parent_ids[$slug] = $existing->ID;
        } else {
            $id = wp_insert_post( array(
                'post_title'   => $title,
                'post_name'    => $slug,
                'post_status'  => 'publish',
                'post_type'    => 'page',
            ) );
            $parent_ids[$slug] = $id;
        }
    }

    // 2. Loans Child Pages
    $loan_children = array(
        'Unsecured Business Loan & DOD Limit' => 'unsecured-business-loan-dod',
        'Commercial or Industrial Purchase Loan' => 'commercial-industrial-purchase-loan',
        'Machine Loan from SIDBI' => 'machine-loan-sidbi',
        'Machine Loan from Bank' => 'machine-loan-bank',
        'Sale / Purchase Invoice Finance' => 'invoice-finance',
        'School & College Funding' => 'school-college-funding',
        'Builder & Real Estate Developers Funding' => 'builder-real-estate-funding',
        'Hospital Funding' => 'hospital-funding',
        'Hotel & Resort Funding' => 'hotel-resort-funding',
        'NPA Funding' => 'npa-funding',
        'Infrastructure Companies Funding' => 'infrastructure-funding',
        'Venture Funding' => 'venture-funding',
    );
    foreach ( $loan_children as $title => $slug ) {
        $existing = get_page_by_path( 'loans/' . $slug ) ?: get_page_by_path( $slug );
        if ( ! $existing ) {
            wp_insert_post( array(
                'post_title'   => $title,
                'post_name'    => $slug,
                'post_parent'  => isset($parent_ids['loans']) ? $parent_ids['loans'] : 0,
                'post_status'  => 'publish',
                'post_type'    => 'page',
            ) );
        } elseif ( empty($existing->post_parent) && isset($parent_ids['loans']) ) {
            wp_update_post( array(
                'ID'          => $existing->ID,
                'post_parent' => $parent_ids['loans'],
            ) );
        }
    }

    // 3. Equity Child Pages
    $equity_children = array(
        'Valuation Services' => 'valuation-services',
        'Pre-IPO Funding' => 'pre-ipo-funding',
        'SME IPO' => 'sme-ipo',
        'Main Board IPO' => 'main-board-ipo',
    );
    foreach ( $equity_children as $title => $slug ) {
        $existing = get_page_by_path( 'equity/' . $slug ) ?: get_page_by_path( $slug );
        if ( ! $existing ) {
            wp_insert_post( array(
                'post_title'   => $title,
                'post_name'    => $slug,
                'post_parent'  => isset($parent_ids['equity']) ? $parent_ids['equity'] : 0,
                'post_status'  => 'publish',
                'post_type'    => 'page',
            ) );
        } elseif ( empty($existing->post_parent) && isset($parent_ids['equity']) ) {
            wp_update_post( array(
                'ID'          => $existing->ID,
                'post_parent' => $parent_ids['equity'],
            ) );
        }
    }

    // 4. Incentives Child Pages
    $incentives_children = array(
        'UP Govt Technical Upgradation Support (TUS) Scheme' => 'up-tus-scheme',
        'UP Govt MSME Promotion Policy Scheme' => 'up-msme-scheme',
        'UP Govt MSMY Scheme' => 'up-msmy-scheme',
    );
    foreach ( $incentives_children as $title => $slug ) {
        $existing = get_page_by_path( 'incentives/' . $slug ) ?: get_page_by_path( $slug );
        if ( ! $existing ) {
            wp_insert_post( array(
                'post_title'   => $title,
                'post_name'    => $slug,
                'post_parent'  => isset($parent_ids['incentives']) ? $parent_ids['incentives'] : 0,
                'post_status'  => 'publish',
                'post_type'    => 'page',
            ) );
        } elseif ( empty($existing->post_parent) && isset($parent_ids['incentives']) ) {
            wp_update_post( array(
                'ID'          => $existing->ID,
                'post_parent' => $parent_ids['incentives'],
            ) );
        }
    }

    // Automatically set static front page to 'Home' page
    $home_page = get_page_by_path( 'home' ) ?: get_page_by_title( 'Home' );
    if ( $home_page ) {
        if ( get_option( 'show_on_front' ) !== 'page' || (int) get_option( 'page_on_front' ) !== $home_page->ID ) {
            update_option( 'show_on_front', 'page' );
            update_option( 'page_on_front', $home_page->ID );
            flush_rewrite_rules();
        }
    }
}
add_action( 'after_switch_theme', 'credit_lane_auto_create_pages' );
add_action( 'init', 'credit_lane_auto_create_pages' );

/**
 * Force Front Page Template & Prevent 404 on Homepage
 */
add_filter( 'template_include', function( $template ) {
    $req_uri = isset($_SERVER['REQUEST_URI']) ? trim(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/') : '';
    if ( is_front_page() || is_home() || $req_uri === '' || $req_uri === 'index.php' ) {
        global $wp_query;
        if ( isset($wp_query->is_404) && $wp_query->is_404 ) {
            $wp_query->is_404 = false;
            status_header( 200 );
        }
        $front_page = get_template_directory() . '/front-page.php';
        if ( file_exists( $front_page ) ) {
            return $front_page;
        }
    }
    return $template;
}, 99 );

/**
 * Register Custom ACF Gutenberg Blocks
 */
function credit_lane_register_acf_blocks() {
    if ( function_exists( 'acf_register_block_type' ) ) {
        acf_register_block_type( array(
            'name'            => 'hero',
            'title'           => __( 'Hero Banner', 'credit-lane' ),
            'description'     => __( 'Editable Hero Section with Title, Subtitle, and CTAs', 'credit-lane' ),
            'render_template' => 'template-parts/blocks/hero/hero.php',
            'category'        => 'layout',
            'icon'            => 'cover-image',
            'keywords'        => array( 'hero', 'banner', 'heading' ),
        ) );
    }
}
add_action( 'acf/init', 'credit_lane_register_acf_blocks' );

/**
 * Local JSON Sync for ACF Fields
 */
add_filter( 'acf/settings/save_json', function( $path ) {
    return get_stylesheet_directory() . '/acf-json';
} );
add_filter( 'acf/settings/load_json', function( $paths ) {
    unset( $paths[0] );
    $paths[] = get_stylesheet_directory() . '/acf-json';
    return $paths;
} );
