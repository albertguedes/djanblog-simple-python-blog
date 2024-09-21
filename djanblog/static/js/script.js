// Checks if the footer needs to be fixed at the bottom of the page
// based on the height of the page and the wrapper.
$(function() {
    fixarFooter('#wrapper','#footer');
    $(window).resize(fixarFooter);
});

// Keeps the footer at the bottom of the page.
// If the height of the wrapper is less than the height of the
// page, the footer will be fixed at the bottom of the page.
function fixarFooter(wrapper, footer) {

    var wrapperHeight = $(wrapper).height();
    var screenHeight = $(window).height();

    // If the height of the wrapper is less than the height of the
    // page, the footer will be fixed at the bottom of the page.
    if (wrapperHeight < screenHeight) {
        $(footer).addClass('fixed-bottom');
    } else {
        $(footer).removeClass('fixed-bottom');
    }
}

