// document.addEventListener('DOMContentLoaded', function () {
//     // Function to toggle visibility of a content section
//     function toggleContent(button, content) {
//         button.addEventListener('click', () => {
//             const isVisible = content.style.display === 'block';
//             content.style.display = isVisible ? 'none' : 'block';
//             closeAllDropdowns(content); // Close other dropdowns
//         });
//     }

//     const languageButton = document.querySelector('.language-button');
//     const languageContent = document.querySelector('.language-content');
//     const registerButton = document.querySelector('.register-button');
//     const settingsButton = document.querySelector('.settings-button');
//     const userButton = document.querySelector('.user-button');
//     const settingsContent = document.querySelector('.settings-content');

//     // Setup toggles for buttons
//     toggleContent(settingsButton, settingsContent);
//     setupRedirect(registerButton, '/signup'); // Change to your signup page URL
//     setupRedirect(userButton, '/profile'); // Change to your user profile page URL

//     // Toggle dropdown for language selection
//     toggleDropdown(languageButton, languageContent);

//     // Close dropdowns if clicked outside
//     window.addEventListener('click', function (event) {
//         if (!event.target.matches('.language-button') &&
//             !event.target.matches('.settings-button')) {
//             closeAllDropdowns();
//         }
//     });
// });
