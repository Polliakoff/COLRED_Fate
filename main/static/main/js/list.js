//===============================================FORM_1
function add_id_form_1(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "form_1")
        .appendTo("#form_1");
    return true;
}

$('#name_field').change(function(){
    add_id_form_1();
    $('#form_1').submit();
});

$('#desc_field').change(function(){
    add_id_form_1();
    $('#form_1').submit();
});

//===============================================main_aspects
function add_id_main_aspects(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "main_aspects")
        .appendTo("#main_aspects");
    return true;
}

$('#high_concept_field').change(function(){
    add_id_main_aspects();
    $('#main_aspects').submit();
});

$('#trouble_field').change(function(){
    add_id_main_aspects();
    $('#main_aspects').submit();
});

//===============================================secondary_aspects
function add_id_delete_aspect(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "delete_aspect_form")
        .appendTo("#delete_aspect_form");
    return true;
}

$('.secondary_aspect_delete_button').click(function(){
    sentenced_id = $(this).attr("aspect_in_question");
    $("#to_delete_ident_input").val(sentenced_id);
    add_id_delete_aspect();
    $("#delete_aspect_form").submit();
});

function add_id_update_aspect(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "update_aspect_form")
        .appendTo("#update_aspect_form");
    return true;
}

$('.secondary_aspect_input').change(function(){
    new_text = $(this).val();
    update_id = $(this).attr("aspect_in_question");
    $("#to_update_ident_input").val(update_id);
    $("#to_update_text_input").val(new_text);
    add_id_update_aspect();
    $('#update_aspect_form').submit();
});

//===============================================fate_points
function add_id_fate_points(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "fate_points")
        .appendTo("#fate_points");
    return true;
}

$('#fate_point_number_field').change(function(){
    add_id_fate_points();
    $('#fate_points').submit();
});

$('#fate_point_refresh_field').change(function(){
    add_id_fate_points();
    $('#fate_points').submit();
});

$('#refresh_button').click(function(){
    current_number = $('#fate_point_number_field').val()
    refresh_number = $('#fate_point_refresh_field').val()
    if(current_number<refresh_number){
        $('#fate_point_number_field').val(refresh_number);
        add_id_fate_points();
        $('#fate_points').submit();
    }
});

//===============================================CHOSEN_GUY
$( document ).ready(function() {
    current_guy = $(".inform_box").attr("current_guy");

    $( ".profiles .listing" ).each(function() {
        id = $( this ).attr("guys_id")
        if(current_guy == id) {
            $( this ).css("background-color","#dfc35f");
            $( this ).css("border-radius","20px");
        } 
    });
})

//================================================reload_scroll_magic
document.addEventListener("DOMContentLoaded", function(event) { 
    var scrollpos = localStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo(0, scrollpos);
});

window.onbeforeunload = function(e) {
    localStorage.setItem('scrollpos', window.scrollY);
};



// function welp(t){
//     switch (t) {
//         case "1":
//             return "-5";
//             break;
//         case "2":
//         case "3":
//             return "-4";
//             break;
//         case "4":
//         case "5":
//             return "-3";
//             break;
//         case "6":
//         case "7":
//             return "-2";
//             break;
//         case "8":
//         case "9":
//             return "-1";
//             break;
//         case "10":
//         case "11":
//             return "+0";
//             break;
//         case "12":
//         case "13":
//             return "+1";
//             break;
//         case "14":
//         case "15":
//             return "+2";
//             break;
//         case "16":
//         case "17":
//             return "+3";
//             break;
//         case "18":
//         case "19":
//             return "+4";
//             break;
//         case "20":
//         case "21":
//             return "+5";
//             break;
//         case "22":
//         case "23":
//             return "+6";
//             break;
//         case "24":
//         case "25":
//             return "+7";
//             break;
//     }
// }


// $(document).ready(function () {
//     t = $("#DX").val()
//     $(".DX").text(welp(t))

//     t = $("#STR").val()
//     $(".STR").text(welp(t))

//     t = $("#CON").val()
//     $(".CON").text(welp(t))

//     t = $("#IN").val()
//     $(".IN").text(welp(t))

//     t = $("#WIS").val()
//     $(".WIS").text(welp(t))

//     t = $("#CHR").val()
//     $(".CHR").text(welp(t))

//     t = Math.floor($("#id_xp").val()/1000)
//     $("#class_lvl").text(t)
// });

// $("input").change(function () {
//     t = $("#DX").val()
//     $(".DX").text(welp(t))

//     t = $("#STR").val()
//     $(".STR").text(welp(t))

//     t = $("#CON").val()
//     $(".CON").text(welp(t))

//     t = $("#IN").val()
//     $(".IN").text(welp(t))

//     t = $("#WIS").val()
//     $(".WIS").text(welp(t))

//     t = $("#CHR").val()
//     $(".CHR").text(welp(t))
    
//     t = Math.floor($("#id_xp").val()/1000)
//     $("#class_lvl").text(t)
// });



