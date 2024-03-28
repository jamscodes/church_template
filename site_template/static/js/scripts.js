$(function() {
    $(".featured-playlist-slider").slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        prevArrow: $(".nav-previous"),
        nextArrow: $(".nav-next")
    })
})