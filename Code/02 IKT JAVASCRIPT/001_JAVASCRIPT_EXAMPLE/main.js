console.log("Hello, World!");

function boksClick(id) {
    let el = document.getElementById(id);
    let cd = 2000;
    let active = true
    let oldText = el.innerHTML

    if (active == true) {
        active = false;
        el.innerHTML = 'Innholdet endret seg!'
        setTimeout(()=>{
            active = true;
            el.innerHTML = oldText;
        }, cd)
    } else if (active == false) {return}
}


function createPyramid(rows) {
    for (let i = 1; i <= rows; i++) {
      let pattern = '';
      for (let space = 1; space <= rows - i; space++) {
        pattern += ' ';
      }
      for (let star = 1; star <= 2 * i - 1; star++) {
        pattern += '*';
      }
      console.log(pattern);
    }
}
createPyramid(5);


var dogs = 2;
var cats = 3;
var isRaining = false;

if (isRaining == true && (cats + dogs) >= 1) {
    console.log("It's raining " + (cats + dogs) + " cats and dogs!!");
    console.log("Look out I see 2 more dogs falling in the distance!")
    dogs += 2;
    console.log("It's now raining " + (cats + dogs) + " cats and dogs!!");
} else {
    console.log("Animals: " + (dogs + cats));
    console.log("Aww! 2 more dogs came over!")
    dogs += 2;
    console.log("We now have: " + (dogs + cats));
}


var pris = 20;
var antall = 3;
var avslag = 5;

var totalPris = pris * antall
console.log("Total pris: " + totalPris)

var avslagsPris = (pris - avslag) * antall
console.log("Avslagspris: " + avslagsPris)


