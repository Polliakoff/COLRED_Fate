// $( window ).resize(function() {
//     $(".floating_search").css("display","none")
// });

$( "#main_search" ).change(function() {
    value = $("#main_search").val().toLowerCase();
    if(value==""){
        $(".floating_search").css("display","none")
    } else {
        $(".floating_search").css("left", $(".search").offset().left);
        $(".floating_search").css("display","unset")

        $( ".search_field>a" ).each(function() {
            t = $( this ).attr("filter").toLowerCase()
            // if($( this ).attr("filter")=="")
            if(t.indexOf(value)!=-1) {
                $( this ).css("display","unset");
            } else {
                $( this ).css("display","none");
            }
        });

        $( ".new_one" ).css("display","unset");
    }
    document.activeElement.blur();
});



