$(document).ready(function(){

    $(window).scroll(function () { 
      console.log($(window).scrollTop())
    if ($(window).scrollTop() > 100) {
      $('#nav_bar').addClass('navbar-fixed');
    }
    if ($(window).scrollTop() < 101) {
      $('#nav_bar').removeClass('navbar-fixed');
    }
    });

    $('.carousel').carousel();

    $(".dropdown-button").dropdown();

    $('.modal-trigger').leanModal();

    $("#portrait").fadeIn(1000);

    $('.datepicker').pickadate({
    selectMonths: true, 
    selectYears: 8 
    });
});
