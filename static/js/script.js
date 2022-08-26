$(document).ready(function() {
    $('.main-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.nav-slider'
    });
    $('.nav-slider').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: '.main-slider',
        dots: false,
        centerMode: true,
        focusOnSelect: true,
        speed: 500,
        easing: 'linear',
        infinite: true,
        initialSlide: 0,
        autoplay: true,
        variableWidth: true,
    });

});