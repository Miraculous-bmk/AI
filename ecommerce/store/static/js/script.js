document.addEventListener('DOMContentLoaded', function () {
    // Toggle dropdown visibility
    function toggleDropdown(button, content) {
        button.addEventListener('click', () => {
            const isOpen = content.style.display === 'block';
            closeAllDropdowns();
            if (!isOpen) {
                content.style.display = 'block';
            }
        });
    }

    function closeAllDropdowns() {
        document.querySelectorAll('.dropdown-content').forEach(content => {
            content.style.display = 'none';
        });
    }

    const languageButton = document.querySelector('.language-button');
    const languageContent = document.querySelector('.language-content');
    const registerButton = document.querySelector('.register-button');
    const registerContent = document.querySelector('.register-content');
    const settingsButton = document.querySelector('.settings-button');
    const settingsContent = document.querySelector('.settings-content');

    toggleDropdown(languageButton, languageContent);
    toggleDropdown(registerButton, registerContent);
    toggleDropdown(settingsButton, settingsContent);

    // Close dropdowns if clicked outside
    window.addEventListener('click', function(event) {
        if (!event.target.matches('.language-button') &&
            !event.target.matches('.register-button') &&
            !event.target.matches('.settings-button')) {
            closeAllDropdowns();
        }
    });
});
