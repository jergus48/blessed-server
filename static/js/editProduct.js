
const priceinput = document.getElementById('priceinput');
const priceoutput = document.getElementById('priceoutput');

const inputPrice = function(e) {
    priceoutput.innerHTML = e.target.value + " €";
}

priceinput.addEventListener('input', inputPrice);
priceinput.addEventListener('propertychange', inputPrice);


const ChangeColor = function() {
    const color1input = document.getElementById('color1input');
    const color2input = document.getElementById('color2input');
    const gradient = document.getElementById('gradient');
    const gradient2 = document.getElementById('gradient2');
    const gradient3 = document.getElementById('gradient3');
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
    
    
}
