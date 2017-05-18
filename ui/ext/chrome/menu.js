$.get(chrome.extension.getURL('/menu.html'), function(data) {
    $(data).appendTo('body');
});

$(function() {

    let active = false;
    let commentData = $('#ui-main').detach();

    $('#ui-menu-button').click(function() {
        console.log('working');
        if (active) {
            $('#ui-main').fadeOut(500, function() {
                commentData = $(this).detach();
                active = false;
            });
        }
        else {
            if (commentData) {
                console.log(commentData);
                commentData.appendTo('body');
                commentData = null;
            }
            $('#ui-main').fadeIn(500, function() {
                active = true;
            });
        }
    });

});