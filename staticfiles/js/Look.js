
const img = document.getElementById("img")

function image() {
    const img = document.getElementById("img")
    console.log(img.value)
    if (img.value == undefined) {

        img.style.width = '100%'
        img.style.position = "absolute"
        img.style.zIndex = 20
        img.value = 'popup'



    }
}
img.addEventListener('click', image)
