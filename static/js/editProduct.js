
const priceinput = document.getElementById('priceinput');
const priceoutput = document.getElementById('priceoutput');
const priceoutputmob = document.getElementById('priceoutputmob');

const inputPrice = function (e) {
    console.log(e.target.value + " €")
    priceoutput.innerHTML = e.target.value + ",0 €";
    priceoutputmob.innerHTML = "Price:" + e.target.value + ",0 €";
}

priceinput.addEventListener('input', inputPrice);
priceinput.addEventListener('propertychange', inputPrice);


const changeColor = function () {

    const color1input = document.getElementById('colorinput1');
    const color2input = document.getElementById('colorinput2');
    const gradient = document.getElementById('gradient');
    const gradient2 = document.getElementById('conditionoutput');
    const gradient3 = document.getElementById('gradient3');
    const conoutmob = document.getElementById('conditionoutputmob');
    const priceoutputmob = document.getElementById('priceoutputmob');
    gradient.style.background =
        "linear-gradient( "
        + color1input.value
        + ", "
        + color2input.value
        + ")";
    gradient2.style.background =
        "linear-gradient( "
        + color1input.value
        + ", "
        + color2input.value
        + ")";
    gradient3.style.background =
        "linear-gradient( "
        + color1input.value
        + ", "
        + color2input.value
        + ")";
    conoutmob.style.background =
        "linear-gradient( "
        + color1input.value
        + ", "
        + color2input.value
        + ")";
    priceoutputmob.style.background =
        "linear-gradient( "
        + color1input.value
        + ", "
        + color2input.value
        + ")";

}

function prosim() {

    const con = document.getElementById('conditioninput').value;
    const conout = document.getElementById('conditionoutput');
    const conoutmob = document.getElementById('conditionoutputmob');
    conout.innerHTML = "Condition: " + con
    conoutmob.innerHTML = "Condition: " + con



}
function inputShoes() {

    const shoes = document.getElementById("shoesinput").value;
    const sizeoutput = document.getElementById("sizeoutput");
    const sizeoutputmob = document.getElementById("sizeoutputmob");
    sizeoutput.innerHTML = shoes
    sizeoutputmob.innerHTML = shoes

}
function inputClothes() {
    const clothes = document.getElementById("clothesinput").value;
    const sizeoutput = document.getElementById("sizeoutput");
    const sizeoutputmob = document.getElementById("sizeoutputmob");
    sizeoutput.innerHTML = clothes
    sizeoutputmob.innerHTML = clothes
}
const accesoriesin = document.getElementById('accesoriesinput');
const sizeout = document.getElementById('sizeoutput');
const sizeoutputmob = document.getElementById("sizeoutputmob");
const inputAccesory = function (e) {
    sizeout.innerHTML = e.target.value;
    sizeoutputmob.innerHTML = e.target.value;
}
accesoriesin.addEventListener('input', inputAccesory);
accesoriesin.addEventListener('propertychange', inputAccesory);