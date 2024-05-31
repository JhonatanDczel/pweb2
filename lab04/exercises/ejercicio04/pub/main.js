function recitar(markupText) {
  const url = "http://localhost:3000/";
  const data = { text: markupText };
  
  // Log the data to be sent
  console.log('Data to be sent:', data);

  const request = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  // Make the HTTP request
  fetch(url, request)
    .then((response) => {
      // Check if the request was successful
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      // Log the received data
      console.log('Received data:', data);
      document.getElementById("output").innerHTML = data.text;
    })
    .catch((error) => {
      // Log any errors
      console.log('There was an error:', error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const text = document.querySelector('#markup')
}