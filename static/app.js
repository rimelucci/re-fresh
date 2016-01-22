var main = function () {
    var onOrOff = false;
    console.log("hello");
    $('#item-view').hide();
    $('#setting-view').hide();
    $('.view-cover').hide();

    $('.info').click(function(){
      $('.view-cover').fadeIn();
      $('#item-view').fadeIn();
    });

    $('.change-button').click(function(){
      $('.view-cover').fadeIn();
      $('#setting-view').fadeIn();
    });

    $('#close').click(function(){
      $('#item-view').fadeOut();
      $("#setting-view").fadeOut();
      $('.view-cover').fadeOut();
    });

    $("#shopping-cart").click(function(){
      onOrOff = !onOrOff;
      $("#cart").animate({width: 'toggle'});
      if (onOrOff) {
        $("#big-container").animate({left: '-25%'});
      }
      else {
        $("#big-container").animate({left: '0'});
      }
    });

}

$(document).ready(main);
