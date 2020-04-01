
var countElement = document.getElementById('count');
var count = 0;

setInterval(() => {
  countElement.innerHTML = ++count;
}, 1000);