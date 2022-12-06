

// Rotate element by 90 degrees clockwise
const sizes = document.getElementById('size')
const sizebtn = document.getElementById('sizebtn')

const countries = document.getElementById('country')
const countrybtn = document.getElementById('countrybtn')
const category = document.getElementById('categories')
const categorybtn = document.getElementById('categorybtn')
document.addEventListener('click', function (e) {

    if (sizebtn.contains(e.target) == false && sizes.contains(e.target) == false &&
        countrybtn.contains(e.target) == false && countries.contains(e.target) == false &&
        categorybtn.contains(e.target) == false && category.contains(e.target) == false) {
        document.getElementById('sizecheck').checked = false;

        document.getElementById('categoriescheck').checked = false;
        document.getElementById('countrycheck').checked = false;
        const size = document.getElementById('size');

        const country = document.getElementById('country');
        const categories = document.getElementById('categories');
        const rotatedsize = document.getElementById('Size_arrow');

        const rotatedcategory = document.getElementById('categories_arrow');
        const rotatedcountry = document.getElementById('country_arrow');




        size.style.display = "none";

        categories.style.display = "none";
        country.style.display = "none";
        rotatedsize.style.transform = 'rotate(0deg)';

        rotatedcategory.style.transform = 'rotate(0deg)';
        rotatedcountry.style.transform = 'rotate(0deg)';
    }
})
function Size() {

    document.getElementById('sizecheck').checked = true;

    document.getElementById('categoriescheck').checked = false;
    document.getElementById('countrycheck').checked = false;

    const size = document.getElementById('size');

    const categories = document.getElementById('categories');
    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');

    const rotatedcategory = document.getElementById('categories_arrow');
    const rotatedcountry = document.getElementById('country_arrow');

    if (size.style.display == "block") {

        size.style.display = "none";
        rotatedsize.style.transform = 'rotate(0deg)';
        document.getElementById('sizecheck').checked = false;

        document.getElementById('categoriescheck').checked = false;
        document.getElementById('countrycheck').checked = false;

    }
    else {

        size.style.display = "block";

        categories.style.display = "none";
        country.style.display = "none";
        rotatedsize.style.transform = 'rotate(180deg)';

        rotatedcategory.style.transform = 'rotate(0deg)';
        rotatedcountry.style.transform = 'rotate(0deg)';
    }
}

function Categories() {

    document.getElementById('sizecheck').checked = false;

    document.getElementById('categoriescheck').checked = true;
    document.getElementById('countrycheck').checked = false;

    const size = document.getElementById('size');

    const categories = document.getElementById('categories');
    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');

    const rotatedcategory = document.getElementById('categories_arrow');
    const rotatedcountry = document.getElementById('country_arrow');


    if (categories.style.display == "block") {

        categories.style.display = "none";
        rotatedcategory.style.transform = 'rotate(0deg)';
        document.getElementById('sizecheck').checked = false;

        document.getElementById('categoriescheck').checked = false;
        document.getElementById('countrycheck').checked = false;

    }
    else {

        categories.style.display = "block";
        country.style.display = "none";
        size.style.display = "none";

        rotatedcategory.style.transform = 'rotate(180deg)';
        rotatedcountry.style.transform = 'rotate(0deg)';
        rotatedsize.style.transform = 'rotate(0deg)';

    }
}
function Country() {
    document.getElementById('sizecheck').checked = false;

    document.getElementById('categoriescheck').checked = false;
    document.getElementById('countrycheck').checked = true;

    const size = document.getElementById('size');

    const categories = document.getElementById('categories');
    const country = document.getElementById('country');
    const rotatedsize = document.getElementById('Size_arrow');

    const rotatedcategory = document.getElementById('categories_arrow');
    const rotatedcountry = document.getElementById('country_arrow');


    if (country.style.display == "block") {

        country.style.display = "none";
        rotatedcountry.style.transform = 'rotate(0deg)';
        document.getElementById('sizecheck').checked = false;

        document.getElementById('categoriescheck').checked = false;
        document.getElementById('countrycheck').checked = false;

    }
    else {

        country.style.display = "block";
        size.style.display = "none";

        categories.style.display = "none";
        rotatedcountry.style.transform = 'rotate(180deg)';
        rotatedsize.style.transform = 'rotate(0deg)';

        rotatedcategory.style.transform = 'rotate(0deg)';
    }
}