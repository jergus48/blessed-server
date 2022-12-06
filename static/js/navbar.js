const menu_btn = document.querySelector('.hamburger');
const mobile_menu = document.querySelector('.mobile-nav');
const menu = document.getElementById('mobilemenu')
const link1 = document.getElementById('link1');
const link2 = document.getElementById('link2');
const link3 = document.getElementById('link3');
const link4 = document.getElementById('link4');
const link5 = document.getElementById('link5');
menu_btn.addEventListener('click', function () {
    menu_btn.classList.toggle('is-active');
    mobile_menu.classList.toggle('is-active');
    if (menu.style.display == "none") {
        menu.style.display = "none"
        link1.style.display = "none"
        link2.style.display = "none"
        link3.style.display = "none"
        link4.style.display = "none"
        link5.style.display = "none"
        console.log("hah")

    }
    else {
        menu.style.display = "block"
        link1.style.display = "block"
        link2.style.display = "block"
        link3.style.display = "block"
        link4.style.display = "block"
        link5.style.display = "block"
    }

})
menu_btn.addEventListener('dblclick', function () {
    menu_btn.classList.toggle('is-active');
    mobile_menu.classList.toggle('is-active');
    if (menu.style.display == "none") {
        menu.style.display = "none"
        link1.style.display = "none"
        link2.style.display = "none"
        link3.style.display = "none"
        link4.style.display = "none"
        link5.style.display = "none"
        console.log("hah")

    }
    else {

        link1.style.display = "block"
        link2.style.display = "block"
        link3.style.display = "block"
        link4.style.display = "block"
        link5.style.display = "block"
    }

})


function search() {
    document.querySelector('.m-search').style.left = '50%';
    console.log('*****')
    document.querySelector('.search-mobile').classList.toggle('is-active');
    document.querySelector('.cancel').classList.toggle('is-active');
}

function cancel() {
    document.querySelector('.m-search').style.left = '200%';
    document.querySelector('.search-mobile').classList.toggle('is-active');
    document.querySelector('.cancel').classList.toggle('is-active');
    // .style.display = 'none'
}


document.addEventListener('click', function (e) {
    console.log(e.target)
    if (menu.style.display == "block") {
        if (mobile_menu.contains(e.target) == false && e.target != menu_btn && e.target != menu) {
            menu_btn.classList.toggle('is-active');
            mobile_menu.classList.toggle('is-active');

            console.log(e.target)

        }
    }

})