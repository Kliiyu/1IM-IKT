function pageRedirect(page) {
    let intro = document.querySelector('.intro');
    intro.style.transition = '0.7s'
    intro.style.top = '0vh'
    setTimeout(function() {
        window.location.href = page;
    }, 800); 
}

window.addEventListener("DOMContentLoaded", ()=>{
    let intro = document.querySelector('.intro');
    let logo = document.querySelector('.logo-header');
    let logoSpan = document.querySelectorAll('.i-logo');
    intro.style.transition = '1s'

    setTimeout(()=>{
        logoSpan.forEach((span, idx) => {
            setTimeout(() => {
                span.classList.add('active');
            }, (idx + 1) * 200)
        })
    })

    setTimeout(()=>{
        logoSpan.forEach((span, idx) => {
            setTimeout(() => {
                span.classList.remove('active');
                span.classList.add('fade');
            }, (idx + 1) * 50)
        })
    }, 1000)

    setTimeout(()=>{
        intro.style.top = '-100vh'
    }, 1300)
})

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting && entry.target.classList.contains('slider')) {
            loadShow();
        }
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));