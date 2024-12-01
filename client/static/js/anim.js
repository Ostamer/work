function scrollSlider(direction) {
    const slider = document.querySelector('.slider');
    const scrollAmount = 200;
    slider.scrollBy({
        left: scrollAmount * direction,
        behavior: 'smooth'
    });
}
