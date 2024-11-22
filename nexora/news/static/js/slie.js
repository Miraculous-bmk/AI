document.addEventListener('DOMContentLoaded', function() {
    const brandSlideshow = document.querySelector('.brand-news-slideshow .news-container');
    const cryptoSlideshow = document.querySelector('.crypto-news-slideshow .news-container');

    // Function to animate slideshow
    function animateSlideshow(container, direction) {
        let slides = container.children;
        let totalSlides = slides.length;
        let currentIndex = 0;

        setInterval(() => {
            currentIndex = (currentIndex + 1) % totalSlides;
            container.style.transform = `translateX(-${currentIndex * 100}%)`;
        }, 5000); // Change slide every 5 seconds
    }

    if (brandSlideshow) {
        animateSlideshow(brandSlideshow, 'right');
    }

    if (cryptoSlideshow) {
        animateSlideshow(cryptoSlideshow, 'left');
    }
});
