function convert() {
  // Get the input values
  var temp = document.getElementById("temp").value;
  var from_unit = document.getElementById("from_unit").value;
  var to_unit = document.getElementById("to_unit").value;

  // Send a POST request to the Flask route
  fetch("/", {
    method: "POST",
    body: JSON.stringify({temp: temp, from_unit: from_unit, to_unit: to_unit}),
    headers: {"Content-Type": "application/json"}
  })
  .then(response => response.json())
  .then(data => {
    // Update the result field with the converted temperature
    document.getElementById("result").innerHTML = "Result: " + data.result;
  });
}
