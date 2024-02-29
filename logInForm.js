//// LOG IN FORM VALIDATION ////
const logInForm = document.querySelector('#form-login');
const LogInEmailInput = document.querySelector('#form-login input[name="email"]');
const LogInPasswordInput = document.querySelector('#form-login input[name="password"]');
const LogInMsg = document.querySelector('#form-login .msg');
// Define the on log in submit listener function
const onLogInSubmit = (e) => {
    e.preventDefault(); // prevent default behaviour

    // Trim whitespace from input
    let enteredEmail = LogInEmailInput.value.trim();
    let enteredPassword = LogInPasswordInput.value.trim();

    let errorMessage = ''; // Initialize an empty error message variable
    if (enteredEmail === '' || enteredPassword === '') {
        errorMessage = 'נא להזין את כל השדות';
    } else if (!validateEmail(enteredEmail)) {
        errorMessage = 'נא להזין כתובת מייל תקינה';
    }

    if (errorMessage) { // if there is a wrong input then show error message
        LogInMsg.innerHTML = errorMessage;
        LogInMsg.classList.add('error');
        setTimeout(() => {
            LogInMsg.innerHTML = '';
            LogInMsg.classList.remove('error'); // Clear the message design
        }, 2000); // remove error massage after 2 sec
    } else { // after successful log in direct to purchase history page
        window.location.href = 'purchaseHistory.html';
    }
};
logInForm.addEventListener('submit', onLogInSubmit);