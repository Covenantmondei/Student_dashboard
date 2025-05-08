// Get all the OTP input fields
const inputs = document.querySelectorAll('.otp-inputs input');

// Add an event listener for each input
inputs.forEach((input, index) => {
    input.addEventListener('input', (e) => {
        if (e.target.value) {
            // Move to the next input
            if (index < inputs.length - 1) {
                inputs[index + 1].focus();
            }
        }
    });

    input.addEventListener('keydown', (e) => {
        // Move to previous input when backspace is pressed
        if (e.key === 'Backspace' && index > 0 && !inputs[index].value) {
            inputs[index - 1].focus();
        }
    });
});
