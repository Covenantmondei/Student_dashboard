// Toggle password visibility
const togglePassword = document.getElementById('togglePassword');
const password = document.getElementById('password');

togglePassword.addEventListener('click', () => {
    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }
});

// Show loader on submit
const loginForm = document.getElementById('loginForm');
const loader = document.getElementById('loader');

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    loader.style.display = 'block';
    
    // Simulate server request
    setTimeout(() => {
        loader.style.display = 'none';
        alert('Logged in successfully!');
    }, 2000);
});
