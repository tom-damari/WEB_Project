//// FORGOT PASSWORD FORM VALIDATION ////
const forgotPasswordForm = document.querySelector('#form-forgotPassword');
const forgotPasswordEmailInput = document.querySelector('#form-forgotPassword input[name="email"]');
const forgotPasswordMsg = document.querySelector('#form-forgotPassword .msg');
// Define the on log in submit listener function
const onResetPasswordSubmit = (e) => {
    e.preventDefault(); // prevent default behaviour

    // Trim whitespace from email input
    let enteredEmailInput = forgotPasswordEmailInput.value.trim();
    let errorEmailMessage = ''; // Initialize an empty error message variable
    if (!validateEmail(enteredEmailInput)) {
        errorEmailMessage = 'נא להזין כתובת מייל תקינה';
    }

    if (errorEmailMessage) { // if there is a wrong email input then show error message
        forgotPasswordMsg.innerHTML = errorEmailMessage;
        forgotPasswordMsg.classList.add('error');
        setTimeout(() => {
            forgotPasswordMsg.innerHTML = '';
            forgotPasswordMsg.classList.remove('error'); // Clear the message design
        }, 2000); // remove error massage after 2 sec
    } else { // after successful password reset direct back to log in page
        // success massage
        forgotPasswordMsg.innerHTML = 'הבקשה לאיפוס הסיסמה נשלחה. אנא השלם את התהליך בקישור שנשלח לכתובת המייל שלך';
        forgotPasswordMsg.classList.add('successful');
        setTimeout(() => {
            forgotPasswordMsg.innerHTML = '';
            forgotPasswordMsg.classList.remove('successful'); // Clear the message design
        }, 5000); // remove success massage after 5 sec

        // clear fild
        forgotPasswordEmailInput.innerHTML = '';
    }
};
forgotPasswordForm.addEventListener('submit', onResetPasswordSubmit);
