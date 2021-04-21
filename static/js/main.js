$(document).ready(function () {
    $(window).scroll(function () {
        var position = $(this).scrollTop();
        if (position >= 100) {
            $('#mainNav').addClass('navbar-shrink');
        } else {
            $('#mainNav').removeClass('navbar-shrink');
        }
    });
});


function openUrl(url) {
    window.open(url);
}