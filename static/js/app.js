console.log("app.js connected");


function buttonClick() {
  d3.text('/magic').then (function(d){
    // console.log(d)
    document.getElementById("prediction").textContent = (d)
  });
}

function clearButton() {
  var pTag = (document.getElementById('prediction').innerHTML = '');
}
