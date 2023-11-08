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
    if (clickCount == 1) {
        scoreBoxNum.innerHTML = abbreviateNumber(clickCount);
    } else {
        scoreBoxNum.innerHTML = abbreviateNumber(clickCount);
    }
    comboBoxNum.innerHTML = "x" + comboCount;
}

let lastClickTime = null

let clickCount = 0;
let comboCount = 0;

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
            comboCount = 0;
            console.log("Combo Reset! " + secondsPassed + "s");
            updateText();
        } else if (secondsPassed == 5) {
            updateFace('bad')
            console.log("Haven't clicked in a while! " + secondsPassed + "s");
        }
    }
}
setInterval(updateSeconds, 1000); 

function manClick() {
    let baseMultiplier = 1;
    let upgradeMultiplier = 1;
    let comboMultiplier = comboCount;

    let secondsPassed = checkSecondsPassed();
    if (secondsPassed < 1) {
        lastClickTime = null;
        comboCount += 1;
        if (comboCount >= 25) {
            updateFace('good');
        } else {
            updateFace('normal');
        }
    }

    clickCount += 1 * (comboMultiplier + upgradeMultiplier + baseMultiplier);
    clickCount = Math.floor(clickCount);
    updateText();
}