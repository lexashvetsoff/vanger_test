// $(document).ready(function() {
//     $('.main-slider').slick({
//         slidesToShow: 1,
//         slidesToScroll: 1,
//         arrows: false,
//         fade: true,
//         asNavFor: '.nav-slider'
//     });
//     $('.nav-slider').slick({
//         slidesToShow: 4,
//         slidesToScroll: 1,
//         asNavFor: '.main-slider',
//         dots: false,
//         centerMode: true,
//         focusOnSelect: true,
//         speed: 500,
//         easing: 'linear',
//         infinite: true,
//         initialSlide: 0,
//         autoplay: true,
//         variableWidth: true,
//     });
// });

$(document).ready(function(){
    let slides_all = document.querySelectorAll('.main-slider');
    let main_id_all = [];
    slides_all.forEach(element => {
        main_id_all.push(element.getAttribute('id'));
    });

    let nav_slides_all = document.querySelectorAll('.nav-slider');
    let nav_id_all = [];
    nav_slides_all.forEach(element => {
        nav_id_all.push(element.getAttribute('id'));
    });

    for (let i = 0; i <= main_id_all.length; i++) {
        main_id = '#' + main_id_all[i];
        nav_id = '#' + nav_id_all[i];

        $(main_id).slick({
            dots: false,
            infinite: true,
            speed: 500,
            fade: true,
            cssEase: 'linear'
        });
    }
});