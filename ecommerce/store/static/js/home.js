document.addEventListener('DOMContentLoaded', function () {
    // Language Dropdown functionality
    document.querySelectorAll('.language-content a').forEach(function (element) {
        element.addEventListener('click', function () {
            document.getElementById('language-code').textContent = this.getAttribute('data-lang');
        });
    });

    // Option bar width adjustment functionality
    const selectElement = document.querySelector('.option-bar');

    function adjustWidth() {
        const selectedOption = selectElement.options[selectElement.selectedIndex];
        const tempSpan = document.createElement('span');
        tempSpan.style.visibility = 'hidden';
        tempSpan.style.position = 'absolute';
        tempSpan.style.whiteSpace = 'nowrap';
        tempSpan.innerText = selectedOption.text;

        document.body.appendChild(tempSpan);

        const tempWidth = tempSpan.clientWidth;
        selectElement.style.width = `${tempWidth + 20}px`; // Add some padding

        document.body.removeChild(tempSpan);
    }

    adjustWidth();

    selectElement.addEventListener('change', adjustWidth);
});
