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
const registerForm = document.getElementById('signupForm');
const loader = document.getElementById('loader');

// signupForm.addEventListener('submit', (e) => {
//     e.preventDefault();
//     loader.style.display = 'block';
    
//     // Simulate server request
//     setTimeout(() => {
//         loader.style.display = 'none';
//         alert('Account Created successfully!');
//     }, 200);
// });
