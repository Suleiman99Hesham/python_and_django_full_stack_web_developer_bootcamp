var fName = prompt("welcome, what is your first name:")
var lName = prompt("what is your last name:")
var age = Number(prompt("what is your age:"))
var height =Number(prompt("what is your height:"))
var petName = prompt("what is your pet name:")

if ( (fName[0] === lName[0]) && (age > 20 && age < 30) && (height >= 170) &&
  (petName.substr(-1) === 'y') ) {
        console.log("Welcome, You have passed the Spy test!");
} else {
  console.log("Sorry, Nothing to show!");
}
