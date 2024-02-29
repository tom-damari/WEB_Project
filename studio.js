//// MOBILE PLATFORM ////
// Get the mobile bar icon, mobile side exit icon and the side navbar
const bar = document.getElementById('mobileBar');
const close = document.getElementById('mobileSideExit');
const nav = document.getElementById('navbar2');
// open the sidebar when clicking the bar icon
if (bar) {
    bar.addEventListener('click', () => {
        nav.classList.add('active');
    })
}
// close the sidebar when clicking the close icon
if (close) {
    close.addEventListener('click', () => {
        nav.classList.remove('active');
    })
}


// VALIDATION FUNCTIONS
function validateName(name) {
    const namePatternEng = /^[A-Za-z]{2,}$/; // Regular expression for validating names (letters only, at least 2 characters)
    const namePatternHeb = /^[\u0590-\u05FF\s']+$/; // Regular expression for validating Hebrew names (includes spaces and apostrophes)
    return namePatternEng.test(name) || namePatternHeb.test(name);
}
function validateEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Regular expression for validating email addresses
    return emailPattern.test(email);
}
function validatePhoneNumber(phoneNumber) {
    const phonePattern1 = /^(?:\+?972|0)(?:-|\s)?(?:\(0?\d\)|0\d)(?:-|\s)?\d{7}$/; // Regular expression for validating Israeli phone numbers
    const phonePattern2 = /^(0\d|0\d\d|\d{3})-?\d{7}$/; // pattern that matches phone numbers with starting like 054-*******
    return phonePattern1.test(phoneNumber) || phonePattern2.test(phoneNumber);
}
function validateBirthDate(birthDate) {
    // Regular expression for validating date format YYYY-MM-DD
    const datePattern = /^\d{4}-\d{2}-\d{2}$/;
    if (!datePattern.test(birthDate)) {
        return false; // Date format is invalid
    }
    // Convert the input string to a Date object
    const inputDate = new Date(birthDate);
    // Calculate the date 10 years ago
    let twelveYearsAgo = new Date(); // Get the current date
    twelveYearsAgo.setFullYear(twelveYearsAgo.getFullYear() - 12);
    // Check if the input date is before 10 years ago
    return inputDate <= twelveYearsAgo; // Date is valid if the input date is on or before 12 years ago
}
