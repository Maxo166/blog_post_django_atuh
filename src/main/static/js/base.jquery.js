$(function(){
    $(".navbar-burger").click(function(){
        $("#navbarBasicExample").slideToggle('fast');
    })
    $('.navbar-item.has-dropdown a.navbar-link').on('click', function(){
        $('.navbar-dropdown').slideToggle('fast')
    });
    $('.comment-dropdown-trigger button').on('click', function(){
        $(this).parent()
            .next('.comment-dropdown-menu')
            .slideToggle('fast')
    });
    
})