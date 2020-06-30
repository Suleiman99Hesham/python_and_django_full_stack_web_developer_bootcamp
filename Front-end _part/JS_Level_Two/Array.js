// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

function addNew() {
  var studentName =prompt("What name would you like to add?")
  roster.push(studentName)
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function remove() {
  var studentName =prompt("What name would you like to remove?")
  var index = roster.indexOf(studentName);
  if(index > -1){
    roster.splice(index,1);
  }
}
// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
  roster.forEach(function(entry) {
    console.log(entry);
  });
}

// Start by asking if they want to use the web app
var start = prompt("do you want to start the App? (Y/N)");
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
var operation = "";
if (start.toLowerCase() === "y") {
  while (operation !== "quit") {
    operation=prompt("Please select an action add, remove, display, quit.");
    if (operation === "add") {
      addNew();
    }else if (operation === "remove") {
      remove();
    }else if (operation === "display") {
      display();
    }
  }
}
