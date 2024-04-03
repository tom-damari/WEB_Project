document.addEventListener('DOMContentLoaded', function () {
    const quantityInputs = document.querySelectorAll('.quantity-input');
    quantityInputs.forEach(function (input) {
        const decrementBtn = input.previousElementSibling;
        const incrementBtn = input.nextElementSibling;

        decrementBtn.addEventListener('click', function (e) {
            const currentValue = parseInt(input.value);
            if (currentValue > 0) {
                input.value = currentValue - 1;
                updateQuantity(input);
            }
        });

        incrementBtn.addEventListener('click', function () {
            const currentValue = parseInt(input.value);
            input.value = currentValue + 1;
            updateQuantity(input);
        });
    });
});

function updateQuantity(input) {
    const cartID = document.getElementById('cartID').getAttribute('data-parameter');
    const productName = input.closest('tr').querySelector('.product-name').getAttribute('data-parameter');
    const quantity = input.value;
    window.location.href = `/cart/updateQuantity/${encodeURIComponent(cartID)}/${encodeURIComponent(productName)}/${encodeURIComponent(quantity)}`;
}
