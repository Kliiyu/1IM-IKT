function pageRedirect(page) {
    let intro = document.querySelector('.intro');
    intro.style.transition = '0.7s'
    intro.style.top = '0vh'
    setTimeout(function() {
        window.location.href = page;
    }, 800); 
}