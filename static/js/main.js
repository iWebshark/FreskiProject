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

function openUrlSameTab(url) {
    window.open(url, '_self')
}

// Open modal with gallery on click
$('.example-card-img').on('click', function(ev) {
    let id = $(this).attr('id')


    $('#exampleModal').modal('show');
});

$('#exampleModal').on('hidden.bs.modal', function () {
   // $('#modalBody').empty();
});