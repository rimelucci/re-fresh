var main = function () {

    console.log("hello");
    $('#item-view').hide();
    $('.view-cover').hide();

    $('.info').click(function(){
      $('.view-cover').fadeIn();
      $('#item-view').fadeIn();
    });

    $('#close').click(function(){
      $('#item-view').fadeOut();
      $('.view-cover').fadeOut();
    });
    /*$(".friends-button").click(
        function(){

            $('.menu').animate({
                right: "0px"
            }, 300);


            $('body').animate({
                right: "250px"
            }, 300);
        }
    );

    $(".close").click(
        function(){

            $('.menu').animate({
                right: "-250px"
            }, 300);


            $('body').animate({
                right: "0px"
            }, 300);
        }
    );

    $(".startwriting").click(
        function(){

            $('.startwriting').hide(300);
            $('.fullform').show(300);
        }
    );

    $(".showcomments").click(
        function(){

            $('.comments').toggle(300);
        }
    );

    $(".startcomment").click(
        function(){

            $('.postcomment').show(300);
            $('.comments').show(300);
        }
    );*/

}

$(document).ready(main);
