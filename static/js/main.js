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
$('.example-card-img').on('click', function (ev) {
    let id = $(this).parent().attr('id')
    $.ajax({
        type: "GET",
        url: "/examples/get/" + id,
        success: function (response) {
            let imagesContainer = $('#modalImages');
            let modalButtons = $('#modalButtons');

            let i = 0;
            for (key in response) {
                if (i === 0) {
                    imagesContainer.append("<div class=\"carousel-item active\">\n" +
                        "<img src=\"/media/" + key + "\" class=\"d-block w-100\" alt=\"...\">\n" +
                        "<div>")
                } else {
                     imagesContainer.append("<div class=\"carousel-item\">\n" +
                        "<img src=\"/media/" + key + "\" class=\"d-block w-100\" alt=\"...\">\n" +
                        "<div>")
                }
                i++;
            }

            for (let k = 0; k < i; k++) {
                if (k === 0) {
                    modalButtons.append("<button type=\"button\" data-bs-target=\"#carouselExampleIndicators\" data-bs-slide-to=\""+k+"\"\n" +
                    "class=\"active\" aria-current=\"true\" aria-label=\"Slide "+k+1+"\"></button>");
                } else {
                     modalButtons.append("<button type=\"button\" data-bs-target=\"#carouselExampleIndicators\" data-bs-slide-to=\""+k+"\"\n" +
                    "aria-current=\"true\" aria-label=\"Slide "+k+1+"\"></button>");
                }
            }
        }
    });


    $('#exampleModal').modal('show');
});

$('#exampleModal').on('hidden.bs.modal', function () {
    $('#modalImages').empty();
    $('#modalButtons').empty();
});