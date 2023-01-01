const menu_btn = document.querySelector('.hamburger');
const menubar = document.querySelector('.bar');
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
    if (mobile_menu.style.display == "block") {
        mobile_menu.style.display = "none"
        link1.style.display = "none"
        link2.style.display = "none"
        link3.style.display = "none"
        link4.style.display = "none"
        link5.style.display = "none"


    }
    else {
        mobile_menu.style.display = "block"
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
    if (mobile_menu.style.display == "block") {
        menu.style.display = "none"
        link1.style.display = "none"
        link2.style.display = "none"
        link3.style.display = "none"
        link4.style.display = "none"
        link5.style.display = "none"


    }
    else {
        mobile_menu.style.display = "block"
        link1.style.display = "block"
        link2.style.display = "block"
        link3.style.display = "block"
        link4.style.display = "block"
        link5.style.display = "block"
    }

})
// menubar.addEventListener('click', function () {
//     menu_btn.classList.toggle('is-active');
//     mobile_menu.classList.toggle('is-active');
//     console.log('xxxxxx')
//     if (menu.style.display == "block") {
//         console.log('none')
//         menu.style.display = "none"
//         link1.style.display = "none"
//         link2.style.display = "none"
//         link3.style.display = "none"
//         link4.style.display = "none"
//         link5.style.display = "none"


//     }
//     else {
//         console.log('block')
//         mobile_menu.style.display = "block"
//         link1.style.display = "block"
//         link2.style.display = "block"
//         link3.style.display = "block"
//         link4.style.display = "block"
//         link5.style.display = "block"
//     }

// })
// menubar.addEventListener('dblclick', function () {
//     menu_btn.classList.toggle('is-active');
//     mobile_menu.classList.toggle('is-active');
//     console.log('xxxxxx')
//     if (menu.style.display == "block") {
//         console.log('none')
//         menu.style.display = "none"
//         link1.style.display = "none"
//         link2.style.display = "none"
//         link3.style.display = "none"
//         link4.style.display = "none"
//         link5.style.display = "none"


//     }
//     else {
//         console.log('block')
//         menu.style.display = "block"
//         link1.style.display = "block"
//         link2.style.display = "block"
//         link3.style.display = "block"
//         link4.style.display = "block"
//         link5.style.display = "block"
//     }

// })


function search() {
    document.querySelector('.m-search').style.left = '50%';
    document.querySelector('.m-search').style.display = 'flex';
    document.querySelector('.search-mobile').classList.toggle('is-active');
    document.querySelector('.cancel').classList.toggle('is-active');
}

function cancel() {
    document.querySelector('.m-search').style.display = 'none';
    document.querySelector('.search-mobile').classList.toggle('is-active');
    document.querySelector('.cancel').classList.toggle('is-active');
    // .style.display = 'none'
}


document.addEventListener('click', function (e) {

    if (mobile_menu.style.display == "block") {
        if (mobile_menu.contains(e.target) == false && e.target != menu_btn && e.target != menu) {
            menu_btn.classList.toggle('is-active');
            mobile_menu.classList.toggle('is-active');
            menu.style.display = "none"



        }
    }

})