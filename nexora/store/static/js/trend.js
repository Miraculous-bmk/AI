document.addEventListener("DOMContentLoaded", function() {
    const categories = document.querySelectorAll('input[name="category"]');
    const productLists = document.querySelectorAll('.product-list');

    // Function to show the selected category's products
    function showCategoryProducts() {
        const selectedCategory = document.querySelector('input[name="category"]:checked').value;
        
        productLists.forEach((list) => {
            if (list.getAttribute('data-category') === selectedCategory) {
                list.style.display = 'grid'; // Show selected category
            } else {
                list.style.display = 'none'; // Hide others
            }
        });
    }

    // Add event listeners to each radio button
    categories.forEach((category) => {
        category.addEventListener('change', showCategoryProducts);
    });

    // Show products for the initially checked category on page load
    showCategoryProducts();
});
