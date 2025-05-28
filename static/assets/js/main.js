(function($) {
  'use strict';

  /*-------------------------------------------------------------------------------
  Preloader
  -------------------------------------------------------------------------------*/
  $(window).on('load', function() {
    $('.sigma_preloader').addClass('hidden');
  });

  /*-------------------------------------------------------------------------------
  Team Socials Trigger
  -------------------------------------------------------------------------------*/
  $("a.trigger-team-socials").on('click', function(e) {
    e.preventDefault();
    $(this).closest('.sigma_sm').toggleClass('visible');
  });

  /*-------------------------------------------------------------------------------
  Cart Trigger
  -------------------------------------------------------------------------------*/
  $(".sigma_cart-trigger").on('click', function(e) {
    e.preventDefault();
    $("body").toggleClass('cart-open');
  });

  /*-------------------------------------------------------------------------------
  Search Trigger
  -------------------------------------------------------------------------------*/
  $(".search-trigger").on('click', function(e) {
    $(".search-form-wrapper").toggleClass('open');
  });

  /*-------------------------------------------------------------------------------
  Aside Menu
  -------------------------------------------------------------------------------*/
  $(".aside-trigger").on('click', function() {
    $("body").toggleClass('aside-open');
  });

  $(".aside-trigger-right").on('click', function() {
    $("body").toggleClass('aside-right-open');
  });

  $(".sigma_aside .menu-item-has-children > a").on('click', function(e) {
    var submenu = $(this).next(".sub-menu");
    e.preventDefault();

    submenu.slideToggle(200);
  });

  /*-------------------------------------------------------------------------------
  Sticky Header
    -------------------------------------------------------------------------------*/
  var header = $(".can-sticky");
  var headerHeight = header.innerHeight();

  function doSticky() {

    if (window.pageYOffset > headerHeight) {
      header.addClass("sticky");
    } else {
      header.removeClass("sticky");
    }

  }
  doSticky();

  /*-------------------------------------------------------------------------------
  Tooltips
  -------------------------------------------------------------------------------*/
  $('[data-toggle="tooltip"]').tooltip();

  /*-------------------------------------------------------------------------------
  Magnific Popup
  -------------------------------------------------------------------------------*/
  $('.popup-youtube').magnificPopup({type: 'iframe'});
  $('.popup-vimeo').magnificPopup({type: 'iframe'});
  $('.popup-video').magnificPopup({type: 'iframe'});
  $('.gallery-thumb').magnificPopup({
    type: 'image',
    gallery: {
      enabled: true
    }
  });

  /*-------------------------------------------------------------------------------
  ion Range Sliders (Price filter)
  -------------------------------------------------------------------------------*/
  $(".js-range-slider").ionRangeSlider();

  /*-------------------------------------------------------------------------------
  Countdown
  -------------------------------------------------------------------------------*/
  $(".sigma_countdown-timer").each(function() {
    var $this = $(this);
    $this.countdown($this.data('countdown'), function(event) {
      $(this).text(event.strftime('%D days %H:%M:%S'));
    });
  });

  /*-------------------------------------------------------------------------------
  Counter
  -------------------------------------------------------------------------------*/
  $(".counter").each(function() {
    var $this = $(this);
    $this.one('inview', function(event, isInView) {
      if (isInView) {
        $this.countTo({speed: 2000});
      }
    });
  });

  /*-------------------------------------------------------------------------------
  Before / After Slider
  -------------------------------------------------------------------------------*/
  if($(".twentytwenty-container").length > 0){
    $(".twentytwenty-container").twentytwenty({
      move_slider_on_hover: false,
      move_with_handle_only: false,
      click_to_move: true
    });
  }

  /*-------------------------------------------------------------------------------
  Checkout Notices
  -------------------------------------------------------------------------------*/
  $(".sigma_notice a").on('click', function(e) {
    e.preventDefault();

    $(this).closest('.sigma_notice').next().slideToggle();
  });

  /*-------------------------------------------------------------------------------
  Progress bar on view
  -------------------------------------------------------------------------------*/
  $(".sigma_progress").each(function() {
    var progressBar = $(this).find(".progress-bar");
    var progressCount = $(this).find(".sigma_progress-count");
    $(progressBar).on('inview', function(event, isInView) {
      if (isInView) {
        $(progressBar).animate({
          width:$(progressBar).attr("aria-valuenow") + "%"
        });
        $(progressCount).animate({
          left:$(progressBar).attr("aria-valuenow") + "%"
        });
      }
    });
   });

  $(".sigma_progress-round").each(function() {
    var animateTo = $(this).data('to'),
      $this = $(this);
    $this.one('inview', function(event, isInView) {
      if (isInView) {
        $this.css({'stroke-dashoffset': animateTo});
      }
    });
  });

  /*-------------------------------------------------------------------------------
  Product details slider
  -------------------------------------------------------------------------------*/
  $('.sigma_product-single-thumb .slider').slick({slidesToShow: 1, slidesToScroll: 1, arrows: false, fade: true, asNavFor: '.sigma_product-single-thumb .slider-nav'});

  $('.sigma_product-single-thumb .slider-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.sigma_product-single-thumb .slider',
    dots: false,
    centerMode: false,
    arrows: false,
    focusOnSelect: false
  });

  /*-------------------------------------------------------------------------------
  Banner slider (Home v1)
  -------------------------------------------------------------------------------*/
  $(".banner-3 .sigma_banner-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    dots: false,
    autoplay: true,
    prevArrow: $('.banner-3 .slider-prev'),
    nextArrow: $('.banner-3 .slider-next'),
    responsive: [{
        breakpoint: 991,
        settings: {
          dots: false,
        }
      }
    ]
  });

  /*-------------------------------------------------------------------------------
  Portfolio Slider
  -------------------------------------------------------------------------------*/
  $(".sigma_portfolio-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    dots: false,
    autoplay: true,
    autoplaySpeed: 12000,
    prevArrow: $('.sigma_portfolio-section .slider-prev'),
    nextArrow: $('.sigma_portfolio-section .slider-next'),
    responsive: [
    {
      breakpoint: 991,
      settings: {
        arrow: false
      }
    }
  ]
  });

  $(".sigma_portfolio-slider-2").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: false,
    dots: true,
    infinite: false,
    autoplay: true,
    autoplaySpeed: 12000,
    responsive: [
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 2,
      }
    },
    {
      breakpoint: 575,
      settings: {
        slidesToShow: 1,
      }
    }
  ]
  });

  /*-------------------------------------------------------------------------------
  Testimonials slider
  -------------------------------------------------------------------------------*/
  $(".sigma_testimonial-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    dots: true,
    autoplay: true,
    customPaging : function(slider, i) {
        return '<div class="sigma_round-dot dot-dark">'+
          '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 197 197" enable-background="new 0 0 197 197" xml:space="preserve">'+
            '<circle class="sigma_round-dot-stroke" stroke-linecap="round" cx="98.5" cy="98.6" r="97.5"></circle>'+
            '<circle class="sigma_round-dot-circle" stroke-linecap="round" cx="98.5" cy="98.6" r="97.5"></circle>'+
          '</svg>'+
        '</div>';
    },
  });

  /*-------------------------------------------------------------------------------
  Gallery Slider
  -------------------------------------------------------------------------------*/
  $(".gallery-slider").slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    arrows: true,
    autoplay: true,
    centerMode: true,
    centerPadding: '0px',
    responsive: [{
        breakpoint: 1200,
        settings: {
          slidesToShow: 4,
        }
      },
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 3,
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
          arrows: false,
          dots: true
        }
      },
       {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
          arrows: false,
          dots: true
        }
      },
    ]
  });


  /*-------------------------------------------------------------------------------
  Masonry
  -------------------------------------------------------------------------------*/
  $('.masonry').imagesLoaded(function() {
    var isotopeContainer = $('.masonry');
    isotopeContainer.isotope({itemSelector: '.masonry-item'});
  });

  /*------------------------------------------------------------------------------
  Isotope
  ------------------------------------------------------------------------------*/

  function doIsotope() {
    var $portfolioGrid = '';

    $('.masonry').imagesLoaded(function() {
      $portfolioGrid = $('.portfolio-filter').isotope({
        itemSelector: '.col-lg-4',
        percentPosition: true,
        masonry: {
          columnWidth: '.col-lg-4'
        }
      });
    });

    $('.filter-items').on('click', '.portfolio-trigger', function() {
      var filterValue = $(this).attr('data-filter');
      $portfolioGrid.isotope({filter: filterValue});
    });

    $('.portfolio-trigger').on('click', function(e) {
      $(this).closest('.filter-items').find('.active').removeClass('active');
      $(this).addClass('active');
      event.preventDefault();
    });

  }
  doIsotope();

  /*-------------------------------------------------------------------------------
  Add / Subtract Quantity
  -------------------------------------------------------------------------------*/
  $(".qty span").on('click', function() {
    var qty = $(this).closest('.qty').find('input');
    var qtyVal = parseInt(qty.val());
    if ($(this).hasClass('qty-add')) {
      qty.val(qtyVal + 1);
    } else {
      return qtyVal > 1
        ? qty.val(qtyVal - 1)
        : 0;
    }
  })

  /*-----------------------------------
    Back to Top
    -----------------------------------*/
  $('.sigma_back-to-top').on('click', function() {
    $("html, body").animate({
      scrollTop: 0
    }, 600);
    return false;
  });

  // init wow js
  new WOW().init();

  //On scroll events
  $(window).on('scroll', function() {

    doSticky();

  });

  //On resize events
  $(window).on('resize', function() {});

})(jQuery);
