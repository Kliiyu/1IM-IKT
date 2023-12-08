const button = document.getElementById('manFaceBTN');
const scoreBoxNum = document.getElementById('scoreBoxNum');
const comboBoxNum = document.getElementById('comboBoxNum');
const mFace = document.getElementById('mFace');

function abbreviateNumber(number) {
    const SI_SYMBOLS = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion', 'Decillion', 'Undecillion', 'Duodecillion', 'Tredecillion', 'Quattuordecillion', 'Quindecillion', 'Sexdecillion', 'Septendecillion', 'Octodecillion', 'Novemdecillion', 'Vigintillion', 'Unvigintillion'];
    const tier = Math.log10(Math.abs(number)) / 3 | 0;
    if (tier === 0) return number;
  
    const suffix = SI_SYMBOLS[tier];
    const scale = Math.pow(10, tier * 3);
    const scaled = number / scale;
    const formatted = scaled.toFixed(1);
  
    return formatted + " " + suffix;
}

function updateText() {
    if (score == 1) {
        scoreBoxNum.innerHTML = abbreviateNumber(score);
    } else {
        scoreBoxNum.innerHTML = abbreviateNumber(score);
    }
    comboBoxNum.innerHTML = "x" + comboMultiplier();
}

let lastClickTime = null

let score = 0;
let clickCount = 0;

button.addEventListener('click', () => { lastClickTime = new Date(); }); 

function checkSecondsPassed() {
    const currentTime = new Date(); 
    const secondsPassed = Math.floor((currentTime - lastClickTime) / 1000);
    return secondsPassed;
}

function updateFace(mood) {
    if (mood == 'normal') {
        mFace.src = "images/Manface.png";
    } else if (mood == 'good') {
        mFace.src = "images/Pal_Face.png";
    } else if (mood == 'bad') {
        mFace.src = "images/TiredMan.png";
    };
}

function updateSeconds() {
    if (lastClickTime !== null) { 
        let secondsPassed = checkSecondsPassed();
        if (secondsPassed == 1) {
            clickCount = 0;
            console.log("Combo Reset! " + secondsPassed + "s");
            updateText();
        } else if (secondsPassed == 5) {
            updateFace('bad')
            console.log("Haven't clicked in a while! " + secondsPassed + "s");
        }
    }
}
setInterval(updateSeconds, 1000); 

function playSound(path) {
    if (path == 'c1') {
        path = 'soundFX/combo/combo1.mp3'
    } else if (path == 'c2') {
        path = 'soundFX/combo/combo2.mp3'
    } else if (path == 'c3') {
        path = 'soundFX/combo/combo3.mp3'
    } else if (path == 'c4') {
        path = 'soundFX/combo/combo4.mp3'
    } else if (path == 'c5') {
        path = 'soundFX/combo/combo5.mp3'
    }

    var sound = new Audio(path);
    if (path != '') {sound.play();}
}

function comboMultiplier() {
    let multiplier = 1
    if (clickCount >= 20 && clickCount < 50) {
        multiplier = 2
        if (clickCount == 20) {playSound('c1'); updateFace('normal')}
    } else if (clickCount >= 50 && clickCount < 100) {
        multiplier = 3
        if (clickCount == 50) {playSound('c2'); updateFace('good')}
    } else if (clickCount >= 100 && clickCount < 500) {
        multiplier = 4
        if (clickCount ==100) {playSound('c3')}
    } else if (clickCount >= 500) {
        multiplier = 5
        if (clickCount == 500) {playSound('c4')}
    } else {multiplier = 1}
    return multiplier
}

watcher.addEventListener('myVariableChanged', myFunction);


function increaseScore() {
    let secondsPassed = checkSecondsPassed();
    if (secondsPassed < 1) {
        lastClickTime = null;
        clickCount += 1;
    }

    score += 1 * (comboMultiplier());
    score = Math.floor(score);
    updateText();
}