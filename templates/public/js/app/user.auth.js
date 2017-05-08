/**
 * Created by erlan on 5/6/17.
 */

function UserAuthentication(options) {
    var form = options.form;
    var errors = options.errorContainer;

    function init() {
        $(errors).fadeOut('fast');
        $(form).on('submit', function (event) {
            event.preventDefault();
            var that = this;
            var button = $(form).find('button[type="submit"]');
            var loginText = $(button).html();
            var loadingText = 'Загрузка...';

            $(button).html(loadingText);
            $.ajax({
                url: $(that).attr('action'),
                method: 'POST',
                dataType: 'JSON',
                data: $(that).serialize(),
                success: function (response) {
                    $(button).html(loginText);
                    if(response.success) {
                        if(response.message == 'login') {
                            document.location.reload();
                        } else if(response.message == 'register') {
                            $(document).trigger('emailSent');
                        }
                    } else {
                        $(errors).find('span').html(response.message);
                        $(errors).fadeIn('slow');
                    }
                },
                error: function () {
                    console.error('Can\'t send login request!');
                }
            });
        });
    }

    return {
        init: init
    }
}
