document.addEventListener('DOMContentLoaded', function () {
    const allCheckbox = document.querySelector('input[value="all"]'); // Update this selector as needed
    const channelCheckboxes = document.querySelectorAll('input[type="checkbox"]');

    // Listener for the "All" checkbox
    allCheckbox.addEventListener('change', function () {
        if (this.checked) {
            channelCheckboxes.forEach(checkbox => {
                if (checkbox !== allCheckbox) {
                    checkbox.checked = true;  // Check all other channels
                }
            });
        } else {
            // If "All" is unchecked, ensure all other checkboxes remain as they are
            channelCheckboxes.forEach(checkbox => {
                if (checkbox !== allCheckbox) {
                    checkbox.checked = false; // Uncheck all other channels if desired
                }
            });
        }
    });                                

    // Listener for other checkboxes
    channelCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                allCheckbox.checked = false; // Uncheck "All" if any other checkbox is selected
            } else {
                // If you want to implement logic where unchecking a channel might trigger checking "All" if all channels are unchecked, you can add that logic here.
                const allChecked = Array.from(channelCheckboxes).every(cb => cb.checked);
                if (!allChecked) {
                    allCheckbox.checked = false; // Ensure "All" remains unchecked if not all are checked
                }
            }
        });
    });
});