

// Rotate element by 90 degrees clockwise
const sizes = document.getElementById('size')
const sizebtn = document.getElementById('sizebtn')
const conditions = document.getElementById('condition')
const conditionbtn = document.getElementById('conditionbtn')
const countries = document.getElementById('country')
const countrybtn = document.getElementById('countrybtn')
document.addEventListener('click', function (e) {

    if (sizebtn.contains(e.target) == false && sizes.contains(e.target) == false &&
        conditionbtn.contains(e.target) == false && conditions.contains(e.target) == false &&
        countrybtn.contains(e.target) == false && countries.contains(e.target) == false) {
        document.getElementById('sizecheck').checked = false;
        document.getElementById('conditioncheck').checked = false;

        document.getElementById('countrycheck').checked = false;
        const size = document.getElementById('size');
        const condition = document.getElementById('condition');

        const country = document.getElementById('country');
        const rotatedsize = document.getElementById('Size_arrow');
        const rotatedcondition = document.getElementById('condition_arrow');

        const rotatedcountry = document.getElementById('country_arrow');




        size.style.display = "none";
        condition.style.display = "none";

        country.style.display = "none";
        rotatedsize.style.transform = 'rotate(0deg)';
        rotatedcondition.style.transform = 'rotate(0deg)';

        rotatedcountry.style.transform = 'rotate(0deg)';
    }
})







function Size() {

    document.getElementById('sizecheck').checked = true;
    document.getElementById('conditioncheck').checked = false;

    document.getElementById('countrycheck').checked = false;

    const size = document.getElementById('size');
    const condition = document.getElementById('condition');

    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');
    const rotatedcondition = document.getElementById('condition_arrow');

    const rotatedcountry = document.getElementById('country_arrow');

    if (size.style.display == "block") {

        size.style.display = "none";
        rotatedsize.style.transform = 'rotate(0deg)';
        document.getElementById('sizecheck').checked = false;
        document.getElementById('conditioncheck').checked = false;

        document.getElementById('countrycheck').checked = false;

    }
    else {

        size.style.display = "block";
        condition.style.display = "none";

        country.style.display = "none";
        rotatedsize.style.transform = 'rotate(180deg)';
        rotatedcondition.style.transform = 'rotate(0deg)';

        rotatedcountry.style.transform = 'rotate(0deg)';
    }
}
function Condition() {
    document.getElementById('sizecheck').checked = false;
    document.getElementById('conditioncheck').checked = true;

    document.getElementById('countrycheck').checked = false;

    const size = document.getElementById('size');
    const condition = document.getElementById('condition');

    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');
    const rotatedcondition = document.getElementById('condition_arrow');

    const rotatedcountry = document.getElementById('country_arrow');


    if (condition.style.display == "block") {

        condition.style.display = "none";
        rotatedcondition.style.transform = 'rotate(0deg)';
        document.getElementById('sizecheck').checked = false;
        document.getElementById('conditioncheck').checked = false;

        document.getElementById('countrycheck').checked = false;

    }
    else {

        condition.style.display = "block";

        country.style.display = "none";
        size.style.display = "none";
        rotatedcondition.style.transform = 'rotate(180deg)';

        rotatedcountry.style.transform = 'rotate(0deg)';
        rotatedsize.style.transform = 'rotate(0deg)';
    }
}

function Country() {
    document.getElementById('sizecheck').checked = false;
    document.getElementById('conditioncheck').checked = false;

    document.getElementById('countrycheck').checked = true;

    const size = document.getElementById('size');
    const condition = document.getElementById('condition');

    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');
    const rotatedcondition = document.getElementById('condition_arrow');

    const rotatedcountry = document.getElementById('country_arrow');


    if (country.style.display == "block") {

        country.style.display = "none";
        rotatedcountry.style.transform = 'rotate(0deg)';
        document.getElementById('sizecheck').checked = false;
        document.getElementById('conditioncheck').checked = false;

        document.getElementById('countrycheck').checked = false;

    }
    else {

        country.style.display = "block";
        size.style.display = "none";
        condition.style.display = "none";

        rotatedcountry.style.transform = 'rotate(180deg)';
        rotatedsize.style.transform = 'rotate(0deg)';
        rotatedcondition.style.transform = 'rotate(0deg)';

    }
}