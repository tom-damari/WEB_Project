document.addEventListener('DOMContentLoaded', function() {

    const mainImg = document.getElementById('main-img');
    const smallImages = document.querySelectorAll('.small-img');
    if (smallImages.length > 0) {
        // Loop through each small image and add onclick event
        smallImages.forEach((smallImg) => {
            smallImg.addEventListener('click', (e) => {
                mainImg.src = smallImg.src; // Update main image src with clicked small image src
                window.alert('לא מימשנו במסגרת הפרויקט');
            });
        });
    } else {
        window.alert('לא מימשנו במסגרת הפרויקט');
    }

    const addToCartButton = document.getElementById('addToCart');
    addToCartButton.addEventListener('click', (e) => {
         e.preventDefault();
         // Retrieve product details
         const productName = document.querySelector('.section-p1 h3').textContent;
         const productStatus = document.querySelector('.productStatus').textContent;
         if (productStatus === 'זמין') {
             // convert the background to green when item is added
             addToCartButton.classList.add('successful');
             setTimeout(() => {
                 addToCartButton.classList.remove('successful'); // Clear the message design
                }, 3000); // remove success massage after 3 sec
                // Show a confirmation message to the user
             window.alert(' נוסף לעגלה ' + productName);
            // Redirect to add to cart route
            window.location.href = `/product/{{category}}/{{productName}}/addToCart`;
         } else {
             // Show product sold out
             window.alert(' אזל מהמלאי ' + productName);
         }
     });
});


// const mainImg = document.getElementById('main-img');
// const smallImages = document.querySelectorAll('.small-img');
//
// // Loop through each small image and add onclick event
// smallImages.forEach((smallImg) => {
//     smallImg.addEventListener('click', (e) => {
//         e.preventDefault();
//         mainImg.src = smallImg.src;
//     });
// });

// // get the images from the product pages
// let mainImg = document.getElementById('main-img')
// let smallImg = document.getElementsByClassName('small-img')
//
// // replace image source with main image
// smallImg[0].onclick = function () {
//     mainImg.src = smallImg[0].src;
// }
// smallImg[1].onclick = function () {
//     mainImg.src = smallImg[1].src;
// }
// smallImg[2].onclick = function () {
//     mainImg.src = smallImg[2].src;
// }
// smallImg[3].onclick = function () {
//     mainImg.src = smallImg[3].src;
// }