

// Rotate element by 90 degrees clockwise

function Size()  {
    
    
    const size = document.getElementById('size');
    const rotated = document.getElementById('Size_arrow');
    
    
    if (size.style.display == "block"){
        
        size.style.display = "none";
        rotated.style.transform = 'rotate(0deg)';

    }
    else{
      
        size.style.display = "block";
        rotated.style.transform = 'rotate(180deg)';
    }
}
function Condition()  {
   
    
    const condition = document.getElementById('condition');
    const rotated = document.getElementById('condition_arrow');
    
    
    if (condition.style.display == "block"){
        
        condition.style.display = "none";
        rotated.style.transform = 'rotate(0deg)';

    }
    else{
      
        condition.style.display = "block";
        rotated.style.transform = 'rotate(180deg)';
    }
}
function Categories()  {
   
    
    const categories = document.getElementById('categories');
    const rotated = document.getElementById('categories_arrow');
    
    
    if (categories.style.display == "block"){
       
        categories.style.display = "none";
        rotated.style.transform = 'rotate(0deg)';

    }
    else{
      
        categories.style.display = "block";
        rotated.style.transform = 'rotate(180deg)';
    }
}
function Country()  {
    
    
    const country = document.getElementById('country');
    const rotated = document.getElementById('country_arrow');
    
    
    if (country.style.display == "block"){
        
        country.style.display = "none";
        rotated.style.transform = 'rotate(0deg)';

    }
    else{
      
        country.style.display = "block";
        rotated.style.transform = 'rotate(180deg)';
    }
}