import React, { useState, useEffect } from "react"; // Import necessary modules
import Cookies from "universal-cookie"; // Import Cookies module for managing cookies

const cookies = new Cookies(); // Instantiate Cookies class to create cookies object

const App = () => { // Define functional component App
  const [username, setUsername] = useState(""); // State variable for username
  const [password, setPassword] = useState(""); // State variable for password
  const [error, setError] = useState(""); // State variable for error message
  const [isAuthenticated, setIsAuthenticated] = useState(false); // State variable for authentication status

  useEffect(() => { // Effect hook to run once on component mount
    getSession(); // Fetch session on component mount
  }, []);

  // Function to fetch session status from the server
  const getSession = () => {
    fetch("/api/session/", { // Make a GET request to fetch session status
      credentials: "same-origin", // Use same-origin credentials
    })
    .then((res) => res.json()) // Parse response as JSON
    .then((data) => {
      setIsAuthenticated(data.isAuthenticated); // Update authentication status based on response
    })
    .catch((err) => {
      console.log(err); // Log any errors that occur during fetch
    });
  };

  // Function to fetch the current user's information
  const whoami = () => {
    fetch("/api/whoami/", { // Make a GET request to fetch user information
      headers: {
        "Content-Type": "application/json", // Set request header content type
      },
      credentials: "same-origin", // Use same-origin credentials
    })
    .then((res) => res.json()) // Parse response as JSON
    .then((data) => {
      console.log("You are logged in as: " + data.username); // Log username to console
    })
    .catch((err) => {
      console.log(err); // Log any errors that occur during fetch
    });
  };

  // Event handler for password change
  const handlePasswordChange = (event) => {
    setPassword(event.target.value); // Update password state with new value
  };

  // Event handler for username change
  const handleUserNameChange = (event) => {
    setUsername(event.target.value); // Update username state with new value
  };

  // Function to check if the response status is OK
  const isResponseOk = (response) => {
    if (response.status >= 200 && response.status <= 299) {
      return response.json(); // Parse response as JSON if status is within OK range
    } else {
      throw Error(response.statusText); // Throw error with status text if status is not within OK range
    }
  };

  // Function to handle the login process
  const login = (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    fetch("/api/login/", { // Make a POST request to login endpoint
      method: "POST", // Use POST method
      headers: {
        "Content-Type": "application/json", // Set request header content type
        "X-CSRFToken": cookies.get("csrftoken"), // Set CSRF token header
      },
      credentials: "same-origin", // Use same-origin credentials
      body: JSON.stringify({ username: username, password: password }), // Convert form data to JSON string
    })
    .then(isResponseOk) // Check if response status is OK
    .then((data) => {
      console.log(data);
      setIsAuthenticated(true); // Update authentication status to true
      setUsername(""); // Clear username input
      setPassword(""); // Clear password input
      setError(""); // Clear error message
    })
    .catch((err) => {
      setError("Wrong username or password."); // Display error message
      console.log(err); // Log any errors that occur during fetch
    });
  };

  // Function to handle the logout process
  const logout = () => {
    fetch("/api/logout", { // Make a GET request to logout endpoint
      credentials: "same-origin", // Use same-origin credentials
    })
    .then(isResponseOk) // Check if response status is OK
    .then((data) => {
      console.log(data)
      setIsAuthenticated(false); // Update authentication status to false
    })
    .catch((err) => {
      console.log(err); // Log any errors that occur during fetch
    });
  };

  // Render login form if not authenticated, otherwise render logged-in state
  if (!isAuthenticated) {
    return (
      <div className="container mt-3"> {/* Container for login form */}
        <h1>React Cookie Auth</h1> {/* Title */}
        <br />
        <h2>Login</h2> {/* Subtitle */}
        <form onSubmit={login}> {/* Login form */}
          <div className="form-group"> {/* Username input field */}
            <label htmlFor="username">Username</label> {/* Label for username input */}
            <input type="text" className="form-control" id="username" name="username" value={username} onChange={handleUserNameChange} /> {/* Username input */}
          </div>
          <div className="form-group"> {/* Password input field */}
            <label htmlFor="username">Password</label> {/* Label for password input */}
            <input type="password" className="form-control" id="password" name="password" value={password} onChange={handlePasswordChange} /> {/* Password input */}
            <div> {/* Error message container */}
              {error && <small className="text-danger">{error}</small>} {/* Display error message if exists */}
            </div>
          </div>
          <button type="submit" className="btn btn-primary">Login</button> {/* Login button */}
        </form>
      </div>
    );
  }

  // Render logged-in state
  return (
    <div className="container mt-3"> {/* Container for logged-in state */}
      <h1>React Cookie Auth</h1> {/* Title */}
      <p>You are logged in!</p> {/* Logged-in message */}
      <button className="btn btn-primary mr-2" onClick={whoami}>WhoAmI</button> {/* WhoAmI button */}
      <button className="btn btn-danger" onClick={logout}>Log out</button> {/* Logout button */}
    </div>
  );
};

export default App; // Export App component
