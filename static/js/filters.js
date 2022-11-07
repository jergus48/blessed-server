

// Rotate element by 90 degrees clockwise

function Size()  {
    
    
    const size = document.getElementById('size');
    const condition = document.getElementById('condition');
    const categories = document.getElementById('categories');
    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');
    const rotatedcondition = document.getElementById('condition_arrow');
    const rotatedcategory = document.getElementById('categories_arrow');
    const rotatedcountry = document.getElementById('country_arrow');
    
    if (size.style.display == "block"){
        
        size.style.display = "none";
        rotatedsize.style.transform = 'rotate(0deg)';

    }
    else{
      
        size.style.display = "block";
        condition.style.display = "none";
        categories.style.display = "none";
        country.style.display = "none";
        rotatedsize.style.transform = 'rotate(180deg)';
        rotatedcondition.style.transform = 'rotate(0deg)';
        rotatedcategory.style.transform = 'rotate(0deg)';
        rotatedcountry.style.transform = 'rotate(0deg)';
    }
}
function Condition()  {
   
    
    const size = document.getElementById('size');
    const condition = document.getElementById('condition');
    const categories = document.getElementById('categories');
    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');
    const rotatedcondition = document.getElementById('condition_arrow');
    const rotatedcategory = document.getElementById('categories_arrow');
    const rotatedcountry = document.getElementById('country_arrow');
    
    
    if (condition.style.display == "block"){
        
        condition.style.display = "none";
        rotatedcondition.style.transform = 'rotate(0deg)';

    }
    else{
      
        condition.style.display = "block";
        categories.style.display = "none";
        country.style.display = "none";
        size.style.display = "none";
        rotatedcondition.style.transform = 'rotate(180deg)';
        rotatedcategory.style.transform = 'rotate(0deg)';
        rotatedcountry.style.transform = 'rotate(0deg)';
        rotatedsize.style.transform = 'rotate(0deg)';
    }
}
function Categories()  {
   
    
    const size = document.getElementById('size');
    const condition = document.getElementById('condition');
    const categories = document.getElementById('categories');
    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');
    const rotatedcondition = document.getElementById('condition_arrow');
    const rotatedcategory = document.getElementById('categories_arrow');
    const rotatedcountry = document.getElementById('country_arrow');
    
    
    if (categories.style.display == "block"){
       
        categories.style.display = "none";
        rotatedcategory.style.transform = 'rotate(0deg)';

    }
    else{
      
        categories.style.display = "block";
        country.style.display = "none";
        size.style.display = "none";
        condition.style.display = "none";
        rotatedcategory.style.transform = 'rotate(180deg)';
        rotatedcountry.style.transform = 'rotate(0deg)';
        rotatedsize.style.transform = 'rotate(0deg)';
        rotatedcondition.style.transform = 'rotate(0deg)';
    }
}
function Country()  {
    
    
    const size = document.getElementById('size');
    const condition = document.getElementById('condition');
    const categories = document.getElementById('categories');
    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');
    const rotatedcondition = document.getElementById('condition_arrow');
    const rotatedcategory = document.getElementById('categories_arrow');
    const rotatedcountry = document.getElementById('country_arrow');
    
    
    if (country.style.display == "block"){
        
        country.style.display = "none";
        rotatedcountry.style.transform = 'rotate(0deg)';

    }
    else{
      
        country.style.display = "block";
        size.style.display = "none";
        condition.style.display = "none";
        categories.style.display = "none";
        rotatedcountry.style.transform = 'rotate(180deg)';
        rotatedsize.style.transform = 'rotate(0deg)';
        rotatedcondition.style.transform = 'rotate(0deg)';
        rotatedcategory.style.transform = 'rotate(0deg)';
    }
}