var evenTurn = true;
var player = {
    playerOneName: prompt("Player One: Enter your name, you will be Blue"),
    playerTwoName: prompt("Player Two: Enter your name, you will be Red"),
    colorOne: "blue",
    colorTwo: "red",
}
$(document).ready(function () {

    // jQuery methods go here...
    var cells = $('span');

    checkGame();

    cells.each(function (index, value) {
        $(value).on('click', fill);
    });
});

function fill() {
    
    var draw =true;

    if($(this).parent().find(".filled").length == 0){
        var targetCell = $(this).parent().find(".seven");
    }
    else if ($(this).parent().find(".filled").length > 0 && $(this).parent().find(".filled").length <7) { 
        var targetCell = $(this).parent().find(".filled").first().prev();
    }
    else{
        draw = false;
    }
    if(draw){
        if(evenTurn === true){
            var color = 'blue';
        }
        else{
            var color = 'red';
        }
        targetCell.css('background-color', color)
        targetCell.addClass('filled')
        evenTurn = !evenTurn;
        checkGame();
    }
}

function checkGame() {
    if (evenTurn) {
        var currentPlayer = player["playerOneName"];
        var currentColor = player["colorOne"];
    }
    else {
        var currentPlayer = player["playerTwoName"];
        var currentColor = player["colorTwo"];
    }
    $('h3').text(currentPlayer + ": it's your turn, please pick a column to drop your " + currentColor + " chip.");
}

