// Scroll down styling
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

// Open URL in new tab
function openUrl(url) {
    window.open(url);
}

// Open modal with gallery on click
$('.example-card-modal').on('click', function(ev) {
    let id = $(this).attr('id')


    $('#exampleModal').modal('show');
});

$('#exampleModal').on('hidden.bs.modal', function () {
   // $('#modalBody').empty();
});