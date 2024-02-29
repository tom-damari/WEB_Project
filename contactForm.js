//// CONTACT US FORM VALIDATION ////
const contactUsForm = document.querySelector('#form-contactUs');
const ContactFullNameInput = document.querySelector('#form-contactUs input[name="Flname"]');
const ContactEmailInput = document.querySelector('#form-contactUs input[name="mail"]');
const ContactPhoneInput = document.querySelector('#form-contactUs input[name="pnum"]');
const ContactMessageInput = document.querySelector('#form-contactUs textarea[name="massage"]');
const ContactMsg = document.querySelector('#form-contactUs .msg');
// Define the on contact us submit listener function
const onContactUsSubmit = (e) => {
    e.preventDefault(); // prevent default behaviour

    let errorMessage = ''; // Initialize an empty error message variable
    if (!validateName(ContactFullNameInput.value)) {
        errorMessage = 'נא להזין שם תקין';
    } else if (!validateEmail(ContactEmailInput.value)) {
        errorMessage = 'נא להזין כתובת מייל תקינה';
    } else if (ContactMessageInput.value === '') {
        errorMessage = 'נא להזין את תוכן ההודעה';
    } else if (!validatePhoneNumber(ContactPhoneInput.value)) {
        errorMessage = 'נא להזין מספר טלפון תקין';
    }

    if (errorMessage) { // if there is a wrong input then show error message
        ContactMsg.innerHTML = errorMessage;
        ContactMsg.classList.add('error');
        setTimeout(() => {
            ContactMsg.innerHTML = '';
            ContactMsg.classList.remove('error'); // Clear the message design
        }, 2000); // remove error massage after 2 sec
    } else {
        // success massage
        ContactMsg.innerHTML = '!ההודעה שלך נשלחה בהצלחה';
        ContactMsg.classList.add('successful');
        setTimeout(() => {
            ContactMsg.innerHTML = '';
            ContactMsg.classList.remove('successful'); // Clear the message design
        }, 3000); // remove success massage after 3 sec

        // Clear Fields
        ContactFullNameInput.value = '';
        ContactEmailInput.value = '';
        ContactPhoneInput.value = '';
        ContactMessageInput.value = '';
    }
};
contactUsForm.addEventListener('submit', onContactUsSubmit);

