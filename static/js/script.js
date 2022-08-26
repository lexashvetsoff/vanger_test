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

// $(document).ready(function(){
//     let slides = $('.main-slider');
//     let nav_slides = $('.nav-slider');

//     for (let i =0; i <= slides.length; i++) {
//         main_id = '#{0}'.f(slides[i].attr('id'));
//         nav_id = '#{0}'.f(nav_slides[i].attr('id'));
//         $(main_id).slick({
//             slidesToShow: 1,
//             slidesToScroll: 1,
//             arrows: false,
//             fade: true,
//             asNavFor: '.nav-slider'
//         });
//         $(nav_id).slick({
//             slidesToShow: 4,
//             slidesToScroll: 1,
//             asNavFor: '.main-slider',
//             dots: false,
//             centerMode: true,
//             focusOnSelect: true,
//             speed: 500,
//             easing: 'linear',
//             infinite: true,
//             initialSlide: 0,
//             autoplay: true,
//             variableWidth: true,
//         });
//     }
// });