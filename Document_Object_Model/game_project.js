const cells = document.querySelectorAll("td");
const restartButton = document.querySelector("#restart");

const states = {
    "X" : "O",
    "O" : "",
    "" : "X"
}

function changeState(){
    this.textContent = states[this.textContent];
}
cells.forEach((cell) => cell.addEventListener('click',changeState));

restartButton.addEventListener('click',function() {
    cells.forEach((cell) => cell.textContent = "");
})