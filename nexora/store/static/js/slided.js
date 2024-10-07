document.querySelectorAll('.slide-bland').forEach(slideshow => {
    slideshow.addEventListener('mouseover', () => {
        slideshow.style.animationPlayState = 'paused';
    });
    slideshow.addEventListener('mouseout', () => {
        slideshow.style.animationPlayState = 'running';
    });
});

