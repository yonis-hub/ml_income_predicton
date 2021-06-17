console.log("app.js connected");


function buttonClick() {
  d3.text('/magic').then (function(d){
    // console.log(d)
    document.getElementById("prediction").textContent = 'The Modle Predicts' + d
  });
}

function clearButton() {
  var pTag = (document.getElementById('prediction').innerHTML = '');
}


