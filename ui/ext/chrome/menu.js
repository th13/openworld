$.get(chrome.extension.getURL('/menu.html'), function(data) {
    $(data).appendTo('body');
});

$(function() {

    $('.ui-votes').each(function(i) {
        $score = $(this).find('.ui-score');
        console.log($score);
        let score = parseInt($score.text());
        if (score > 0) {
            $score.addClass('prominent-upvoted');
        }
        else if (score < 0) {
            $score.text(score * -1);
            $score.addClass('prominent-downvoted');
        }
    });

    let active = false;
    let commentData = $('#ui-main').detach();


    $('#ui-menu-button').click(function() {
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

            // Disable body scrolling when mouse in comment feed.
            $('.ui-comment-section').hover(function() {
                $('body').addClass('noscroll');
            }, function() {
                $('body').removeClass('noscroll');
            });

            
        }
    });

});