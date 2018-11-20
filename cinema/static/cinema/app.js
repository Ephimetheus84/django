$(function(){
    $("#hall").chained("#cinema");
    $("#seance").chained("#hall, #film");
    $("#seats").chained('#seance');
})