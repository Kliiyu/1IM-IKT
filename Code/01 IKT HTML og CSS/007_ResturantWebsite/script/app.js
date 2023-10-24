window.addEventListener("DOMContentLoaded", ()=>{
    let intro = document.querySelector('.intro');
    let logo = document.querySelector('.logo-header');
    let logoSpan = document.querySelectorAll('.i-logo');

    setTimeout(()=>{
        logoSpan.forEach((span, idx) => {
            setTimeout(() => {
                span.classList.add('active');
            }, (idx + 1) * 400)
        })
    })

    setTimeout(()=>{
        logoSpan.forEach((span, idx) => {
            setTimeout(() => {
                span.classList.remove('active');
                span.classList.add('fade');
            }, (idx + 1) * 50)
        })
    }, 2000)

    setTimeout(()=>{
        intro.style.top = '-100vh'
    }, 2300)
})

window.addEventListener("scroll", function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
})

let items = document.querySelectorAll('.slider .review');
let next = document.getElementById('next');
let prev = document.getElementById('prev');

let active = 3;
function loadShow(){
    let stt = 0;
    items[active].style.transform = `none`;
    items[active].style.zIndex = 1;
    items[active].style.filter = 'none';
    items[active].style.opacity = 1;
    for(var i = active + 1; i < items.length; i++){
        stt++;
        items[i].style.transform = `translateX(${120*stt}px) scale(${1 - 0.2*stt}) perspective(16px) rotateY(-1deg)`;
        items[i].style.zIndex = -stt;
        items[i].style.filter = 'blur(5px)';
        items[i].style.opacity = stt > 2 ? 0 : 0.6;
    }
    stt = 0;
    for(var i = active - 1; i >= 0; i--){
        stt++;
        items[i].style.transform = `translateX(${-120*stt}px) scale(${1 - 0.2*stt}) perspective(16px) rotateY(1deg)`;
        items[i].style.zIndex = -stt;
        items[i].style.filter = 'blur(5px)';
        items[i].style.opacity = stt > 2 ? 0 : 0.6;
    }
}
loadShow();
next.onclick = function(){
    active = active + 1 < items.length ? active + 1 : active;
    loadShow();
}
prev.onclick = function(){
    active = active - 1 >= 0 ? active - 1 : active;
    loadShow();
}

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));