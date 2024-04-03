//// LOG IN FORM VALIDATION ////
const logInForm = document.querySelector('#form-login');
const LogInEmailInput = document.querySelector('#form-login input[name="email"]');
const LogInPasswordInput = document.querySelector('#form-login input[name="password"]');
const LogInMsg = document.querySelector('#form-login .msg');

// Define the on log in submit listener function
const onLogInSubmit = (e) => {
    e.preventDefault(); // prevent default behaviour

    // validation check
    let errorMessage = ''; // Initialize an empty error message variable
    if (LogInEmailInput.value === '' || LogInPasswordInput.value === '') {
        errorMessage = 'נא להזין את כל השדות';
    } else if (!validateEmail(LogInEmailInput.value)) {
        errorMessage = 'נא להזין כתובת מייל תקינה';
    }

    if (errorMessage) { // if there is a wrong input then show error message
        LogInMsg.innerHTML = errorMessage;
        LogInMsg.classList.add('error');
        setTimeout(() => {
            LogInMsg.innerHTML = '';
            LogInMsg.classList.remove('error'); // Clear the message design
        }, 2000); // remove error massage after 2 sec
    } else {
        // success massage
        LogInMsg.innerHTML = '!בדיקת ולידציה הושלמה בהצלחה';
        LogInMsg.classList.add('successful');
        setTimeout(() => {
            LogInMsg.innerHTML = '';
            LogInMsg.classList.remove('successful'); // Clear the message design
        }, 5000); // remove success massage after 5 sec

        // now after passing the login validation check - submit the form
        logInForm.submit();
    }
};
logInForm.addEventListener('submit', onLogInSubmit);

// Get Update Account Details Button
const changePassword = document.querySelector('#forgot-psw');

// Add event listeners to remove icons
changePassword.addEventListener('click', (e) => {
    e.preventDefault();
    window.alert('לא מימשנו במסגרת הפרויקט');
});