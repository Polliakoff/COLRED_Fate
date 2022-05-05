
$( "#main_search" ).change(function() {
    value = $("#main_search").val().toLowerCase();
    if(value==""){
        $(".profiles").css("display","none");
    } 
    else {
        $(".profiles").css("display","unset");

        $( ".profiles>a" ).each(function() {
            t = $( this ).attr("filter").toLowerCase()
            if(t.indexOf(value)!=-1) {
                $( this ).css("display","unset");
            } else {
                $( this ).css("display","none");
            }
        });
    }
});



