/**
 * Created by Эрлан on 25.04.2017.
 */

$.fn.hasAttr = function (value) {
    return this.attr(value) !== undefined;
};
$(document).ready(function () {
    var burger = $('#burger');
    var mobileMenu = $('.mobile-menu').first();
    $(burger).on('click', function (event) {
        if(!$(burger).hasAttr('data-toggle')) $(burger).attr('data-toggle', 'false');
        if($(burger).attr('data-toggle') == 'false') {
            openMobileMenu();
        } else if($(burger).attr('data-toggle') == 'true') {
            closeMobileMenu();
        }
    });

    $('#mobile-menu-ad-link').on('click', function (event) {
        closeMobileMenu();
    });

    $('.mobile-menu .menu-bar li a.auth-trigger').each(function (i, obj) {
        $(obj).on('click', function (event) {
            closeMobileMenu();
        });
    });

    function closeMobileMenu() {
        $(mobileMenu).fadeOut('fast');
        $(burger).attr('data-toggle', 'false');
        $('body').removeClass('no-scroll');
    }

    function openMobileMenu() {
        $(mobileMenu).fadeIn('fast');
        $(burger).attr('data-toggle', 'true');
        $('body').addClass('no-scroll');
    }

});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


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
    if(callback != null || callback != undefined) {
        script.onreadystatechange = callback;
        script.onload = callback;
    }

    body.appendChild(script);
}

function Modal(options) {
    var modal = options.element;
    var carcass = options.carcass;
    var trigger = options.triggers;

    function init() {
        modal = $(modal);
        carcass = $(modal).find(carcass);
        if(trigger != null) {
            trigger = $(trigger);

            $(trigger).each(function (i, obj) {
                $(obj).on('click', function (event) {
                    event.preventDefault();
                    openModal();
                });
            });
        }

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
        if(map != null && map != undefined) {
            google.maps.event.trigger(map, "resize");
            map.setCenter(haightAshbury);
        }
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
        init: init,
        openModal: openModal,
        closeModal: closeModal
    }
}

// ad add Modal
$(document).ready(function() {
    $('#id_images').on('change', function () {
        var reader = new FileReader();
        console.log($(this).val());
    });
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

function setPhoneMask(event) {
    $('input[data-type="phone-number"]').each(function (i, obj) {
        $(obj).mask('+7 - (999) - 999 - 99 - 99');
    });
}


$(document).ready(function () {
    if(pathToLibs == null || pathToLibs == '' || pathToLibs == undefined) {
        pathToLibs = 'public/js';
    }
    loadScript(pathToLibs + '/jquery.masked.min.js', setPhoneMask);

    var slider = $('#slider');
    if($(slider) != undefined) {
        loadScript(pathToSlick + '/slick.min.js', function () {
            var slickPagination = $('#slider-pagination');
            $(slider).slick({
                asNavFor: '#slider-pagination'
            });
            $(slickPagination).slick({
                asNavFor: '#slider',
                slidesToShow: 5,
                slidesToScroll: 1,
                focusOnSelect: true
            });
        }, pathToSlick + '/slick-theme.css,' + pathToSlick + '/slick.css');
    }
});


// Authenticate

$(document).ready(function () {
    var authTrigger = $('.auth-trigger').length;
    if(authTrigger > 0) {
        var loginModal = new Modal({
            element: '#auth-modal',
            carcass: '.login-carcass',
            triggers: '.auth-trigger'
        });
        loginModal.init();

        loadScript(pathToLibs + '/app/user.auth.js', function () {
            var login = new UserAuthentication({
                form: $('#login_form'),
                errorContainer: $('#login-errors')
            });
            login.init();

            var register = new UserAuthentication({
                form: $('#register-form'),
                errorContainer: $('#register-errors')
            });
            register.init();
        });

        $(document).on('emailSent', function (event) {
            var sentModal = new Modal({
                element: '#email-sent-modal',
                carcass: '.login-carcass',
                triggers: null
            });
            sentModal.init();
            loginModal.closeModal();
            sentModal.openModal();
        });
    }
});

$(document).ready(function () {
    var cityChoice = $('.city-choice');
    $(cityChoice).each(function (i, obj) {
        $(obj).on('change', function (event) {
            getMetroByCity(this);
        });
        getMetroByCity(obj);
    });

    function getMetroByCity(cityInput) {
        var value = $(cityInput).val();
        var form = null;
        if($(cityInput).attr('id') == 'search_city') {
            form = $(cityInput).parent().parent().parent().parent();
        } else {
            form = $(cityInput).parent().parent().parent();
        }
        var url = $(cityInput).attr('data-url');
        var cleanedData = {'csrfmiddlewaretoken': getCookie('csrftoken'), 'city': value};
        if(value != '') {
            $.ajax({
                method: 'POST',
                dataType: 'HTML',
                url: url,
                data: cleanedData,
                success: function (response) {
                    $(form).find('select[id="id_metro"]').html(response);
                },
                error: function () {
                    console.error('Can\'t send request for getting metro by city');
                }
            });
        } else {
            $(form).find('select[id="id_metro"]').html('<option value>Метро</option><option value>Выберите сначала город</option>');
        }
    }
});


// Pagination

// $(document).ready(function () {
//     var pagination = $('#pagination');
//     if($(pagination).length > 0) {
//         var pages = [];
//         var current = null;
//         $(pagination).find('li').each(function (i, obj) {
//             if($(obj).find('a') != $('#prev-page') && $(obj).find('a') != $('#next-page')) {
//                 pages.push(parseInt($(obj).find('a').text()));
//             }
//             if($(obj).hasClass('active')) {
//                 current = parseInt($(obj).find('a').text());
//             }
//         });
//         var newPages = [];
//         var currentPages = [];
//         var hasPrev = false;
//         if(current - 2 >= 5) {
//             var leftSide = current - 2;
//             //noinspection JSDuplicatedDeclaration
//             for(var i=leftSide; i < current; ++i) {
//                 currentPages.push('<li><a href="?page=' + i + '">' + i + '</a></li>');
//             }
//             hasPrev = true;
//         }
//         if(!hasPrev && current > 5) {
//             var side = 5 - (current - 2);
//             //noinspection JSDuplicatedDeclaration
//             for(var i = 5; i < 5 + side; ++i) {
//                 currentPages.push('<li><a href="?page=' + i + '">' + i + '</a></li>');
//             }
//             console.log(side);
//         }
//         if((current + 2) <= pages[pages.length - 1] - 2) {
//             var rightSide = current + 2;
//             //noinspection JSDuplicatedDeclaration
//             for(var i=current; i <= rightSide; ++i) {
//                 if(i==current) {
//                     currentPages.push('<li class="active"><a href="?page=' + i + '">' + i + '</a></li>');
//                 } else {
//                     currentPages.push('<li><a href="?page=' + i + '">' + i + '</a></li>');
//                 }
//             }
//         } else {
//             //noinspection JSDuplicatedDeclaration
//             for(var i = current; i <= pages[pages.length - 1]; ++i) {
//                 if(i==current) {
//                     currentPages.push('<li class="active"><a href="?page=' + i + '">' + i + '</a></li>');
//                 } else {
//                     currentPages.push('<li><a href="?page=' + i + '">' + i + '</a></li>');
//                 }
//             }
//         }
//         if(current >= 2) {
//             newPages.push('<li><a href="?page=' + (current - 1) + '" id="prev-page"><<</a></li>');
//         }
//         if(current >= 5) {
//             newPages.push('<li><a href="?page=1">1</a></li>');
//             newPages.push('<li><a href="#">...</a></li>');
//         } else {
//             //noinspection JSDuplicatedDeclaration
//             for(var i=1; i < current; i++) {
//                 newPages.push('<li><a href="?page=' + pages[i] + '">' + pages[i] + '</a></li>');
//             }
//         }
//         //noinspection JSDuplicatedDeclaration
//         for(var i=0; i < currentPages.length; ++i) {
//             newPages.push(currentPages[i]);
//         }
//         if(current < pages[pages.length-1] - 2) {
//             newPages.push('<li><a href="#">...</a></li>');
//             newPages.push('<li><a href="?page=' + pages[pages.length - 2] + '">' + pages[pages.length - 2] + '</a></li>');
//         }
//         if(current < pages[pages.length - 1]) {
//             newPages.push('<li><a href="?page=' + (current + 1) + '" id="next-page">>></a></li>');
//         }
//         $(pagination).html('');
//         //noinspection JSDuplicatedDeclaration
//         for(var i=0; i < newPages.length; ++i) {
//             $(pagination).append(newPages[i]);
//         }
//         console.log(pages);
//         console.log(newPages);
//     }
// });