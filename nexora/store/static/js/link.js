document.addEventListener('DOMContentLoaded', function() {
    const allCheckbox = document.getElementById('all');
    const individualCheckboxes = document.querySelectorAll('.channel-options input[type="checkbox"]:not(#all)');

    // Handle "Subscribe to All" checkbox logic
    allCheckbox.addEventListener('change', function() {
        individualCheckboxes.forEach(checkbox => {
            checkbox.checked = this.checked;
        });
    });

    // Uncheck "Subscribe to All" if any individual checkbox is unchecked
    individualCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            if (!this.checked) {
                allCheckbox.checked = false;
            }
        });
    });
});
