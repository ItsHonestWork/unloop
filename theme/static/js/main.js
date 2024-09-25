// Show or hide the scroll to top button
$(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
        $('#scrollToTop').fadeIn();
    } else {
        $('#scrollToTop').fadeOut();
    }
});

// Smooth scroll to top
$('#scrollToTop').click(function() {
    $('html, body').animate({ scrollTop: 0 }, 600);
    return false;
});

// Smooth scrolling for anchor links
$('a[href^="#"]').click(function(event) {
    var target = $(this.getAttribute('href'));
    if (target.length) {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: target.offset().top
        }, 600);
    }
});
