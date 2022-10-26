var loadFile = function(event) {
    var output = document.getElementById('imgoutput');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.src) // free memory
    }
  };
  
const nameinput = document.getElementById('nameinput');
const nameoutput = document.getElementById('nameoutput');

const inputName = function(e) {
    nameoutput.innerHTML = e.target.value;
}

nameinput.addEventListener('input', inputName);
nameinput.addEventListener('propertychange', inputName);

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


function shoes(){
    const  shoes =  document.getElementById("shoes").value;
    const  sizeoutput =  document.getElementById("sizeoutput");
    sizeoutput.innerHTML = shoes
}
function clothes(){
    const  clothes =  document.getElementById("clothes").value;
    const  sizeoutput =  document.getElementById("sizeoutput");
    sizeoutput.innerHTML = clothes
}
function sizes() {
    const  c = document.getElementById("category").value;
    const  shoes =  document.getElementById("shoes");
    const  clothes =  document.getElementById("clothes");
    const  accesories =  document.getElementById("accesories");
    
    if (c == "Shoes"){
        console.log("Shoes")
        shoes.style.display = "inline-block"
        clothes.style.display = "none"
        accesories.style.display = "none"
        
        
    }
    else if (c == "Clothes"){
        console.log("clothes")
        clothes.style.display = "inline-block"
        shoes.style.display = "none"
        accesories.style.display = "none"
        
    }
    else if (c == "Accesories"){
        console.log("accesories")
        accesories.style.display = "inline-block"
        shoes.style.display = "none"
        clothes.style.display = "none"
        
    }
    
}

