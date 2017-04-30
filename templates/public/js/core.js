/**
 * Created by Эрлан on 25.04.2017.
 */


function loadScript(url, callback, css) {
    var body = document.getElementsByTagName('body')[0];
    var script = document.createElement('script');

    if(css != null) {
        if(css.includes(',')) {
            var styles = css.split(',');
            for(var s in styles) {
                var style = document.createElement('link');
                style.rel = 'stylesheet';
                style.type = 'text/css';
                style.href = styles[s];
                $('head').prepend(style);
            }
        } else {
            var _style = document.createElement('link');
            _style.rel = 'stylesheet';
            _style.type = 'text/css';
            _style.href = css;
            document.getElementsByTagName('head')[0].appendChild(_style);
        }
    }

    script.src = url;
    script.onreadystatechange = callback;
    script.onload = callback;

    body.appendChild(script);
}

function Modal(options) {
    var modal = options.element;
    var carcass = options.carcass;
    var trigger = options.triggers;

    function init() {
        modal = $(modal);
        carcass = $(modal).find(carcass);
        trigger = $(trigger);

        $(trigger).each(function (i, obj) {
            $(obj).on('click', function (event) {
                event.preventDefault();
                openModal();
            });
        });

        $(carcass).find('.md-close').on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            closeModal();
        });
    }

    function openModal() {
        $('body').addClass('no-scroll');
        $(modal).fadeIn('slow');
        $(carcass).on('click', function (event) {
            event.stopPropagation();
        });
        $(modal).on('click', function (event) {
            closeModal();
        });
    }

    function closeModal() {
        $(carcass).animate({'margin-top': -1000}, 500, function () {
            $(modal).fadeOut('slow', function () {
                $(carcass).removeAttr('style');
                $('body').removeClass('no-scroll');
            });
        });
    }

    return {
        init: init
    }
}

// ad add Modal
$(document).ready(function() {

    var adModal = new Modal({
        element: '#ad-modal',
        carcass: '.modal-carcass',
        triggers: '.add-ad-link'
    });
    adModal.init();
});


//Fix header

$(document).ready(function () {
    if($(window).scrollTop() >= 100) {
        $('header').addClass('fixed');
    }
    $(window).on('scroll', function (event) {
        var current_scroll_position = $(window).scrollTop();
        var header = $('header');
        if(current_scroll_position >= 100) {
            $(header).addClass('fixed');
        } else {
            $(header).removeClass('fixed');
        }
    });
});

$(document).ready(function () {
    if(pathToLibs == null || pathToLibs == '' || pathToLibs == undefined) {
        pathToLibs = 'public/js';
    }
    loadScript(pathToLibs + '/jquery.masked.min.js', function (event) {
        $('#phone').mask('+7 - (999) - 999 - 99 - 99');
    });

    var slider = $('#slider');
    if($(slider) != undefined) {
        loadScript(pathToSlick + '/slick.min.js', function () {
            var slickPagination = $('#slider-pagination');
            $(slider).slick({
                asNavFor: slickPagination
            });
            $(slickPagination).slick({
                asNavFor: slider,
                slidesToShow: 5,
                slidesToScroll: 1
            });
        }, pathToSlick + '/slick-theme.css,' + pathToSlick + '/slick.css');
    }
});


// Authenticate

$(document).ready(function () {
    var loginModal = new Modal({
        element: '#auth-modal',
        carcass: '.login-carcass',
        triggers: '.auth-trigger'
    });
    loginModal.init();
});