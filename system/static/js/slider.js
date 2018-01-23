/**
 * Created by work-a-lot on 1/18/2018.
 */
if (navigator.msMaxTouchPoints) {
    $('#slider').addClass('ms-touch');

    $('#slider').on('scroll', function () {
        $('.slide-image').css('transform', 'translate3d(-' + (100 - $(this).scrollLeft() / 6) + 'px,0,0)');
    })
} else {
    var slider = {
        el: {
            slider: $("#slider"),
            holder: $(".holder"),
            imgSlide: $(".slide-image"),
        },
        slideWidth: $('#slider').width(),
        touchstartx: undefined,
        touchmovex: undefined,
        movex: undefined,
        index: 0,
        longTouch: undefined,

        init: function () {
            this.bindUIEvents();
        },
        bindUIEvents: function () {

            this.el.holder.on("touchstart", function (event) {
                slider.start(event);
            });

            this.el.holder.on("touchmove", function (event) {
                slider.move(event);
            });

            this.el.holder.on("touchend", function (event) {
                slider.end(event);
            });
            this.longTouch = false;
            setTimeout(function () {
                window.slider.longTouch = true;
            },250);
            this.touchstartx = event.originalEvent.touches[0].pageX;
            $('.animate').removeClass('animate')
        }
    }

}