$(".little_form>input").on("click",
    function(){
        $(".little_button").css("display","block");
    }
);

$('.popup_close').on('click',
    function(){
        $('.little_button').css('display','none');
    }
);