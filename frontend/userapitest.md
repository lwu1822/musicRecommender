---
layout: custom
---

<html>
<head>
  <title>User Creation</title>
</head>
<body>
  <h1>User Creation</h1>
  <form id="userForm">
    <label for="name">Name:</label>
    <input type="text" id="name" required>
    <br>
    <label for="uid">User ID:</label>
    <input type="text" id="uid" required>
    <br>
    <label for="password">Password:</label>
    <input type="password" id="password">
    <br>
    <label for="dob">Date of Birth:</label>
    <input type="date" id="dob">
    <br>
    <button type="submit">Create User</button>
  </form>
  <div id="result"></div>

  <script>
    document.getElementById("userForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent the form from submitting

  // Get user input values
  var name = document.getElementById("name").value;
  var uid = document.getElementById("uid").value;
  var password = document.getElementById("password").value;
  var dob = document.getElementById("dob").value;

  // Create request body object
  var requestBody = {
    name: name,
    uid: uid,
    password: password,
    dob: dob
  };

  // Send POST request to the API
  fetch("http://localhost:8086/api/users", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(requestBody)
  })
  .then(function(response) {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error: " + response.status);
    }
  })
  .then(function(data) {
    // Display the API response
    document.getElementById("result").innerText = JSON.stringify(data);
  })
  .catch(function(error) {
    // Handle any errors
    console.log(error);
    document.getElementById("result").innerText = "An error occurred.";
  });
});

  </script>
</body>
</html>
