$(".navbar-burger").click(function(){
    $("#navbarBasicExample").slideToggle(100);
})
$('.navbar-item.has-dropdown a.navbar-link').on('click', function(){
    $('.navbar-dropdown').slideToggle()
});