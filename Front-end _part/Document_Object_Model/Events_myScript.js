var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headThree = document.querySelector("#three");

headOne.addEventListener('mouseover',function(){
  headOne.textContent = "Mouse Currently Over";
  headOne.style.color = 'red';
})

headOne.addEventListener('mouseout',function(){
  headOne.textContent = "Hover Over Me!";
  headOne.style.color = 'black';
})

headTwo.addEventListener('click',function(){
  headTwo.textContent = "Clicked On";
  headTwo.style.color = 'blue';
})

headTwo.addEventListener('mouseout',function(){
  headTwo.textContent = "Click Me!";
  headTwo.style.color = 'black';
})

headThree.addEventListener('dblclick',function(){
  headThree.textContent = "I was Double Clicked";
  headThree.style.color = 'green';
})

headThree.addEventListener('mouseout',function(){
  headThree.textContent = "Double Click Me!";
  headThree.style.color = 'black';
})
