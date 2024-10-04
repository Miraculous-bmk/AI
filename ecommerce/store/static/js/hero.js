// Initialize slide indexes
let slideIndex = [1, 1]; // Assuming two slide containers
let slideContainerClass = ["slides-item", "mySlides"];
let dotsClass = ["", "dot"];

// Show the initial slides
showSlides(1, 0);
showSlides(slideIndex[1], 1);

// Function to move slides
function plusSlides(n, no) {
    showSlides(slideIndex[no] += n, no);
}

// Function to set current slide
function currentSlide(n, no) {
    showSlides(slideIndex[no] = n, no);
}

// Function to display slides
function showSlides(n, no) {
    let i;
    let slides = document.getElementsByClassName(slideContainerClass[no]);
    let dots = document.getElementsByClassName(dotsClass[no]);
    if (n > slides.length) { slideIndex[no] = 1 }
    if (n < 1) { slideIndex[no] = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex[no] - 1].style.display = "block";
    if (dots.length > 0) {
        dots[slideIndex[no] - 1].className += " active";
    }
}

// Auto-slide function
setInterval(() => {
    plusSlides(1, 1); // Adjust as needed
}, 5000);

// Example: Bind prev/next buttons for the first slideshow
document.querySelector(".prev").addEventListener("click", () => plusSlides(-1, 0));
document.querySelector(".next").addEventListener("click", () => plusSlides(1, 0));
