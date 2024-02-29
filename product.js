// get the images from the product pages
let mainImg = document.getElementById('main-img')
let smallImg = document.getElementsByClassName('small-img')

// replace image source with main image
smallImg[0].onclick = function () {
    mainImg.src = smallImg[0].src;
}
smallImg[1].onclick = function () {
    mainImg.src = smallImg[1].src;
}
smallImg[2].onclick = function () {
    mainImg.src = smallImg[2].src;
}
smallImg[3].onclick = function () {
    mainImg.src = smallImg[3].src;
}