document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const errorMessage = document.getElementById('error-message');

    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            // Prevent the default form submission
            event.preventDefault();

            // Get trimmed values from the input fields
            const username = usernameInput.value.trim();
            const password = passwordInput.value.trim();

            // Check if username or password is empty
            if (username === '' || password === '') {
                errorMessage.textContent = 'Username and password cannot be empty.';
                errorMessage.style.display = 'block'; // Show the error message
            } else {
                // If validation is successful
                errorMessage.style.display = 'none'; // Hide the error message
                alert('Login successful!');
                // In a real application, you would proceed with form submission here,
                // e.g., using fetch() to send data to a server.
            }
        });
    }
});