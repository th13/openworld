$(function() {

    let mainIsActive = false;

    // $('#ui-menu-button').click(function() {
    //     if (mainIsActive) {
    //         $('#ui-main').fadeOut(500);
    //     }
    //     else {
    //         $('#ui-main').fadeIn(500);
    //     }
    //     mainIsActive = !mainIsActive;
    // });

    $('#ui-menu-button').click(function() {
        $('#ui-main').fadeToggle(500);
    });

});