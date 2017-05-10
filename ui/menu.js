$(function() {

    $('#openworld-menu-button').draggable({
        cursor: 'pointer',
        scroll: true
    });

    /**
    * We want the menu to open when we click the button, but not if we drag it.
    * So, we should open the menu on mouse click up, but only if its position 
    * has stayed the same.
    */

});