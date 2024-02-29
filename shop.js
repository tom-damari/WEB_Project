//// SHOPPING PAGES - SORT & FILTER ////

// make sure the page is loaded before starting
document.addEventListener('DOMContentLoaded', function () {

    // Selecting sort header and sorting bar elements
    const sortHeader = document.querySelector('#sort-header');
    const sortingBar = document.querySelector('#sorting-bar');
    // Adding click event listener to the sorting header and bar
    sortHeader.addEventListener('click', () => {
        // Toggle the 'active' class of the sort header
        sortHeader.classList.toggle('active');
        // Toggle the 'active' class of the sorting bar
        sortingBar.classList.toggle('active');
    });

    // Selecting filter header and filtering bar elements
    const filterHeader = document.querySelector('#filter-header');
    const filteringBar = document.querySelector('#filtering-bar');
    // Adding click event listener to the filtering header and bar
    filterHeader.addEventListener('click', () => {
        // Toggle the 'active' class of the filter header
        filterHeader.classList.toggle('active');
        // Toggle the 'active' class of the filtering bar
        filteringBar.classList.toggle('active');
    });
});
