//// SHOPPING CART PAGE - REMOVE ITEMS FROM CART ////

// make sure the page is loaded before starting
document.addEventListener('DOMContentLoaded', function () {

    // Get all remove icons and number inputs
    const removeIcons = document.querySelectorAll('.fa-times-circle');
    const numberInputs = document.querySelectorAll('input[type="number"]');

    // Add event listeners to remove icons
    removeIcons.forEach(function (icon) {
        icon.addEventListener('click', function () {
            const row = icon.closest('tr'); // Find the closest parent row (tr)
            row.remove(); // Remove the row from the DOM
        });
    });

    // Add event listeners to number inputs
    numberInputs.forEach(function (input) {
        input.addEventListener('input', function () {
            if (parseInt(input.value) === 0) {
                const row = input.closest('tr'); // Find the closest parent row (tr)
                row.remove(); // Remove the row from the DOM
            }
        });
    });
});
