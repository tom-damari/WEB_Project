// document.addEventListener('DOMContentLoaded', function () {
//     const sortSelect = document.getElementById('select-sort');
//     sortSelect.addEventListener('change', function () {
//         const selectedValue = sortSelect.value;
//         const category = "{{ category }}";
//         let url = '/catalog/' + category;
//         if (selectedValue === 'asc' || selectedValue === 'desc') {
//             url += '/' + selectedValue;
//         }
//         window.location.href = url;
//     });
// })
// ;
function updateSort(sort) {
    const category = "{{ category }}";
    let url = '/catalog/' + category;
    if (sort === 'asc' || sort === 'desc') {
        url += '/' + sort;
    }
    window.location.href = url;
}
