
function sizes() {
    var  c = document.getElementById("category").value;
    var  shoes =  document.getElementById("shoes");
    var  clothes =  document.getElementById("clothes")
    var  accesories =  document.getElementById("accesories")
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