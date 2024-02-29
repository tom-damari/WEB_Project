//// SIGN IN FORM VALIDATION ////
const signInForm = document.querySelector('#form-signIn')
const firstNameInput = document.querySelector('#form-signIn input[name="Fname"]')
const lastNameInput = document.querySelector('#form-signIn input[name="Lname"]')
const emailInput = document.querySelector('#form-signIn input[name="mail"]')
const birthDateInput = document.querySelector('#form-signIn input[name="bday"]')
const phoneInput = document.querySelector('#form-signIn input[name="pnum"]')
const msg = document.querySelector('#form-signIn .msg')
// Define the on sign in submit listener function
const onSignInSubmit = (e) => {
    e.preventDefault(); // prevent default behaviour

    let errorMessage = ''; // Initialize an empty error message variable
    if (!validateName(firstNameInput.value) || !validateName(lastNameInput.value)) {
        errorMessage = 'נא להזין שם תקין';
    } else if (!validateEmail(emailInput.value)) {
        errorMessage = 'נא להזין כתובת מייל תקינה';
    } else if (!validatePhoneNumber(phoneInput.value)) {
        errorMessage = 'נא להזין מספר טלפון תקין';
    } else if (!validateBirthDate(birthDateInput.value)) {
        errorMessage = 'נא להזין תאריך לידה תקין';
    }

    if (errorMessage) { // if there is a wrong input then show error message
        msg.innerHTML = errorMessage;
        msg.classList.add('error');
        setTimeout(() => {
            msg.innerHTML = '';
            msg.classList.remove('error'); // Clear the message design
        }, 2000); // remove error massage after 2 sec
    } else {
        // success massage
        msg.innerHTML = '!הרישום הושלם בהצלחה';
        msg.classList.add('successful');
        setTimeout(() => {
            msg.innerHTML = '';
            msg.classList.remove('successful'); // Clear the message design
        }, 5000); // remove success massage after 5 sec
    }
        // clear fields
        firstNameInput.innerHTML = '';
        lastNameInput.innerHTML = '';
        emailInput.innerHTML = '';
        birthDateInput.innerHTML = '';
        phoneInput.innerHTML = '';
};
signInForm.addEventListener('submit', onSignInSubmit);
