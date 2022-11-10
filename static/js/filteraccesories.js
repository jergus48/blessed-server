


function Condition()  {
   
    document.getElementById('conditioncheck').checked = true;
  
    document.getElementById('countrycheck').checked = false;

    
    const condition = document.getElementById('condition');
   
    const country = document.getElementById('country');
   
    const rotatedcondition = document.getElementById('condition_arrow');
  
    const rotatedcountry = document.getElementById('country_arrow');
    
    
    if (condition.style.display == "block"){
        
        condition.style.display = "none";
        rotatedcondition.style.transform = 'rotate(0deg)';
      
        document.getElementById('conditioncheck').checked = false;
       
        document.getElementById('countrycheck').checked = false;

    }
    else{
      
        condition.style.display = "block";
       
        country.style.display = "none";
       
        rotatedcondition.style.transform = 'rotate(180deg)';
       
        rotatedcountry.style.transform = 'rotate(0deg)';
        
    }
}

function Country()  {
   
    document.getElementById('conditioncheck').checked = false;
  
    document.getElementById('countrycheck').checked = true;
    
   
    const condition = document.getElementById('condition');
  
    const country = document.getElementById('country');
  
    const rotatedcondition = document.getElementById('condition_arrow');
   
    const rotatedcountry = document.getElementById('country_arrow');
    
    
    if (country.style.display == "block"){
        
        country.style.display = "none";
        rotatedcountry.style.transform = 'rotate(0deg)';
       
        document.getElementById('conditioncheck').checked = false;
      
        document.getElementById('countrycheck').checked = false;

    }
    else{
      
        country.style.display = "block";
      
        condition.style.display = "none";
      
        rotatedcountry.style.transform = 'rotate(180deg)';
       
        rotatedcondition.style.transform = 'rotate(0deg)';
      
    }
}