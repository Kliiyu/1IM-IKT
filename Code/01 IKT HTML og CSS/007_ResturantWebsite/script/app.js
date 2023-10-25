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

window.addEventListener("scroll", function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
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

function cardTilt() {

    let elem = document.getElementById('tilt')
    if (!elem) {return};

    let height = elem.clientHeight
    let width = elem.clientWidth

    const config = { attributes: true };
    ELEMobserver.observe(elem, config);

    function handleMove(e) {
        let xVal = e.layerX
        let yVal = e.layerY
            
        let yRotation = 20 * ((xVal - width / 2) / width)
        let xRotation = -20 * ((yVal - height / 2) / height)
            
        let string = 'perspective(500px) scale(1.1) rotateX(' + xRotation + 'deg) rotateY(' + yRotation + 'deg)'
        elem.style.transform = string
    }

    e.addEventListener('mousemove', handleMove)

    e.addEventListener('mouseout', function() {
        e.style.transform = 'perspective(500px) scale(1) rotateX(0) rotateY(0)'
    })
            
    e.addEventListener('mousedown', function() {
        e.style.transform = 'perspective(500px) scale(0.9) rotateX(0) rotateY(0)'
    })
            
    e.addEventListener('mouseup', function() {
        e.style.transform = 'perspective(500px) scale(1.1) rotateX(0) rotateY(0)'
    })
}
cardTilt();