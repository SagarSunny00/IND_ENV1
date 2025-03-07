// Simulated user data for login
const validUsername = "admin";  // Set username to "admin"
const validPassword = "admin";  // Set password to "admin"

// Handle login form submission
document.getElementById("loginForm")?.addEventListener("submit", function(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === validUsername && password === validPassword) {
        localStorage.setItem("loggedIn", "true");
        window.location.href = "home.html"; // Redirect to home page
    } else {
        document.getElementById("error").innerText = "Invalid username or password.";
    }
});

// Check if user is logged in on home page
if (document.getElementById("logout")) {
    if (!localStorage.getItem("loggedIn")) {
        window.location.href = "index.html"; // Redirect to login if not logged in
    }

    document.getElementById("logout").addEventListener("click", function() {
        localStorage.removeItem("loggedIn");
        window.location.href = "index.html"; // Redirect to login on logout
    });
}

// // Handle profile form submission
// document.getElementById("profileForm")?.addEventListener("submit", function(event) {
//     event.preventDefault();
//     const name = document.getElementById("name").value;
//     const email = document.getElementById("email").value;

//     // Here you can add code to save the profile data
//     alert("Profile updated: " + name + ", " + email);
// });


document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Here you can add your form validation and processing logic

    // If everything is valid, redirect to the home page
    window.location.href = 'home.html';
});