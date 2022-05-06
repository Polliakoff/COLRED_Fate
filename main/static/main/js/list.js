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

//===============================================STUNTS
$('.stunt_drop_down_choice').change(function(){
    drop = $(this).is(":checked")
    need_id = $(this).attr("stunt_in_question")
    if(drop){
        $('.stunt_to_hide').each(function(){
            check_id = $(this).attr("stunt_in_question")
            if(check_id == need_id){
                $(this).css('display','flex')
            }
        })
    }
    else{
        $('.stunt_to_hide').each(function(){
            check_id = $(this).attr("stunt_in_question")
            if(check_id == need_id){
                $(this).css('display','none')
            }
        })
    }
})

function add_id_delete_stunt(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "delete_stunt_form")
        .appendTo("#delete_stunt_form");
    return true;
}

$('.stunt_delete_button').click(function(){
    sentenced_id = $(this).attr("stunt_in_question");
    $("#stunt_to_delete_ident_input").val(sentenced_id);
    add_id_delete_stunt();
    $("#delete_stunt_form").submit();
});

function add_id_update_stunt(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "update_stunt_form")
        .appendTo("#update_stunt_form");
    return true;
}

$('.stunt_div').change(function(){
    update_id = $(this).attr("stunt_in_question");
    $("#stunt_to_update_ident_input").val(update_id);
    
    $( ".stunt_name_input" ).each(function() {
        check_id = $(this).attr("stunt_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#stunt_to_update_text_input").val(new_text);
        }
    })
    
    $( ".stunt_desc_input" ).each(function() {
        check_id = $(this).attr("stunt_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#stunt_to_update_desc_text_input").val(new_text);
        }
    })

    add_id_update_stunt();
    $('#update_stunt_form').submit();
})
//===============================================stress
function add_id_delete_stress(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "delete_stress_form")
        .appendTo("#delete_stress_form");
    return true;
}

$('.stress_delete_button').click(function(){
    sentenced_id = $(this).attr("stress_in_question");
    $("#stress_to_delete_ident_input").val(sentenced_id);
    add_id_delete_stress();
    $("#delete_stress_form").submit();
});

function add_id_update_stress(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "update_stress_form")
        .appendTo("#update_stress_form");
    return true;
}

$('.stress_line').change(function(){
    update_id = $(this).attr("stress_in_question");
    $("#stress_to_update_ident_input").val(update_id);
    
    $( ".stress_type_input" ).each(function() {
        check_id = $(this).attr("stress_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#stress_to_update_text_input").val(new_text);
        }
    })
    
    $( ".stress_level_input" ).each(function() {
        check_id = $(this).attr("stress_in_question");
        if(check_id == update_id){
            new_number = $(this).val();
            $("#stress_to_update_level_number_input").val(new_number);
        }
    })

    $( ".stress_avaliable_input" ).each(function() {
        check_id = $(this).attr("stress_in_question");
        if(check_id == update_id){
            new_number = $(this).val();
            $("#stress_to_update_avaliable_number_input").val(new_number);
        }
    })

    $( ".stress_spent_input" ).each(function() {
        check_id = $(this).attr("stress_in_question");
        if(check_id == update_id){
            new_number = $(this).val();
            $("#stress_to_update_spent_number_input").val(new_number);
        }
    })

    add_id_update_stress();
    $('#update_stress_form').submit();
})

//===============================================skill
function add_id_delete_skill(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "delete_skill_form")
        .appendTo("#delete_skill_form");
    return true;
}

$('.skill_delete_button').click(function(){
    sentenced_id = $(this).attr("skill_in_question");
    $("#skill_to_delete_ident_input").val(sentenced_id);
    add_id_delete_skill();
    $("#delete_skill_form").submit();
});

function add_id_update_skill(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "update_skill_form")
        .appendTo("#update_skill_form");
    return true;
}

$('.skill_line').change(function(){
    update_id = $(this).attr("skill_in_question");
    $("#skill_to_update_ident_input").val(update_id);
    
    $( ".skill_name_input" ).each(function() {
        check_id = $(this).attr("skill_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#skill_to_update_text_input").val(new_text);
        }
    })
    
    $( ".skill_level_input" ).each(function() {
        check_id = $(this).attr("skill_in_question");
        if(check_id == update_id){
            new_number = $(this).val();
            $("#skill_to_update_level_number_input").val(new_number);
        }
    })

    add_id_update_skill();
    $('#update_skill_form').submit();
})


//===============================================consequences
$('.consequence_drop_down_choice').change(function(){
    drop = $(this).is(":checked")
    need_id = $(this).attr("consequence_in_question")
    if(drop){
        $('.consequence_to_hide').each(function(){
            check_id = $(this).attr("consequence_in_question")
            if(check_id == need_id){
                $(this).css('display','flex')
            }
        })
    }
    else{
        $('.consequence_to_hide').each(function(){
            check_id = $(this).attr("consequence_in_question")
            if(check_id == need_id){
                $(this).css('display','none')
            }
        })
    }
})

function add_id_delete_consequence(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "delete_consequence_form")
        .appendTo("#delete_consequence_form");
    return true;
}

$('.consequence_delete_button').click(function(){
    sentenced_id = $(this).attr("consequence_in_question");
    $("#consequence_to_delete_ident_input").val(sentenced_id);
    add_id_delete_consequence();
    $("#delete_consequence_form").submit();
});

function add_id_update_consequence(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "update_consequence_form")
        .appendTo("#update_consequence_form");
    return true;
}

$('.consequence_div').change(function(){
    update_id = $(this).attr("consequence_in_question");
    $("#consequence_to_update_ident_input").val(update_id);
    
    $( ".consequence_severity_input" ).each(function() {
        check_id = $(this).attr("consequence_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#consequence_to_update_text_input").val(new_text);
        }
    })
    
    $( ".consequence_desc_input" ).each(function() {
        check_id = $(this).attr("consequence_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#consequence_to_update_desc_text_input").val(new_text);
        }
    })

    add_id_update_consequence();
    $('#update_consequence_form').submit();
})

//===============================================EXTRAS
$('.extra_drop_down_choice').change(function(){
    drop = $(this).is(":checked")
    need_id = $(this).attr("extra_in_question")
    if(drop){
        $('.extra_to_hide').each(function(){
            check_id = $(this).attr("extra_in_question")
            if(check_id == need_id){
                $(this).css('display','flex')
            }
        })
    }
    else{
        $('.extra_to_hide').each(function(){
            check_id = $(this).attr("extra_in_question")
            if(check_id == need_id){
                $(this).css('display','none')
            }
        })
    }
})

function add_id_delete_extra(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "delete_extra_form")
        .appendTo("#delete_extra_form");
    return true;
}

$('.extra_delete_button').click(function(){
    sentenced_id = $(this).attr("extra_in_question");
    $("#extra_to_delete_ident_input").val(sentenced_id);
    add_id_delete_extra();
    $("#delete_extra_form").submit();
});

function add_id_update_extra(eventObj) {
    $("<input />").attr("type", "hidden")
        .attr("name", "update_extra_form")
        .appendTo("#update_extra_form");
    return true;
}

$('.extra_div').change(function(){
    update_id = $(this).attr("extra_in_question");
    $("#extra_to_update_ident_input").val(update_id);
    
    $( ".extra_name_input" ).each(function() {
        check_id = $(this).attr("extra_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#extra_to_update_text_input").val(new_text);
        }
    })
    
    $( ".extra_cost_input" ).each(function() {
        check_id = $(this).attr("extra_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#extra_to_update_cost_text_input").val(new_text);
        }
    })

    $( ".extra_attached_aspects_input" ).each(function() {
        check_id = $(this).attr("extra_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#extra_to_update_attached_aspects_text_input").val(new_text);
        }
    })

    $( ".extra_attached_stunts_input" ).each(function() {
        check_id = $(this).attr("extra_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#extra_to_update_attached_stunts_text_input").val(new_text);
        }
    })

    $( ".extra_attached_skills_input" ).each(function() {
        check_id = $(this).attr("extra_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#extra_to_update_attached_skills_text_input").val(new_text);
        }
    })

    $( ".extra_details_input" ).each(function() {
        check_id = $(this).attr("extra_in_question");
        if(check_id == update_id){
            new_text = $(this).val();
            $("#extra_to_update_details_text_input").val(new_text);
        }
    })

    add_id_update_extra();
    $('#update_extra_form').submit();
})


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