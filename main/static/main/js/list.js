function welp(t){
    switch (t) {
        case "1":
            return "-5";
            break;
        case "2":
        case "3":
            return "-4";
            break;
        case "4":
        case "5":
            return "-3";
            break;
        case "6":
        case "7":
            return "-2";
            break;
        case "8":
        case "9":
            return "-1";
            break;
        case "10":
        case "11":
            return "+0";
            break;
        case "12":
        case "13":
            return "+1";
            break;
        case "14":
        case "15":
            return "+2";
            break;
        case "16":
        case "17":
            return "+3";
            break;
        case "18":
        case "19":
            return "+4";
            break;
        case "20":
        case "21":
            return "+5";
            break;
        case "22":
        case "23":
            return "+6";
            break;
        case "24":
        case "25":
            return "+7";
            break;
    }
}


$(document).ready(function () {
    t = $("#DX").val()
    $(".DX").text(welp(t))

    t = $("#STR").val()
    $(".STR").text(welp(t))

    t = $("#CON").val()
    $(".CON").text(welp(t))

    t = $("#IN").val()
    $(".IN").text(welp(t))

    t = $("#WIS").val()
    $(".WIS").text(welp(t))

    t = $("#CHR").val()
    $(".CHR").text(welp(t))

    t = Math.floor($("#id_xp").val()/1000)
    $("#class_lvl").text(t)
});

$("input").change(function () {
    t = $("#DX").val()
    $(".DX").text(welp(t))

    t = $("#STR").val()
    $(".STR").text(welp(t))

    t = $("#CON").val()
    $(".CON").text(welp(t))

    t = $("#IN").val()
    $(".IN").text(welp(t))

    t = $("#WIS").val()
    $(".WIS").text(welp(t))

    t = $("#CHR").val()
    $(".CHR").text(welp(t))
    
    t = Math.floor($("#id_xp").val()/1000)
    $("#class_lvl").text(t)
});



