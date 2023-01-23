var loadFile = function (event) {
  var output = document.getElementById('imgoutput');
  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function () {
    URL.revokeObjectURL(output.src) // free memory
  }
  var outputmob = document.getElementById('imgoutputmob');
  outputmob.src = URL.createObjectURL(event.target.files[0]);
  outputmob.onload = function () {
    URL.revokeObjectURL(outputmob.src) // free memory
  }
};

const nameinput = document.getElementById('nameinput');
const nameoutput = document.getElementById('nameoutput');
const nameoutputmob = document.getElementById('nameoutputmob');
const shoesin = document.getElementById('shoes');
const clothesin = document.getElementById('clothes');
const accesoriesin = document.getElementById('accesories');
const sizeout = document.getElementById('sizeoutput');
const sizeoutputmob = document.getElementById("sizeoutputmob");
const inputName = function (e) {
  nameoutput.innerHTML = e.target.value;
  nameoutputmob.innerHTML = e.target.value;
}
const inputAccesory = function (e) {
  sizeout.innerHTML = e.target.value;
  sizeoutputmob.innerHTML = e.target.value;
}

nameinput.addEventListener('input', inputName);
nameinput.addEventListener('propertychange', inputName);
accesoriesin.addEventListener('input', inputAccesory);
accesoriesin.addEventListener('propertychange', inputAccesory);
shoesin.addEventListener('change', shoes)
clothesin.addEventListener('change', clothes)


const priceinput = document.getElementById('priceinput');
const priceoutput = document.getElementById('priceoutput');
const priceoutputmob = document.getElementById('priceoutputmob');

const inputPrice = function (e) {

  priceoutput.innerHTML = e.target.value + ",0 €";
  priceoutputmob.innerHTML = "Price:" + e.target.value + ",0 €";
}

priceinput.addEventListener('input', inputPrice);
priceinput.addEventListener('propertychange', inputPrice);


const changeColor = function () {

  const color1input = document.getElementById('colorinput1');
  const color2input = document.getElementById('colorinput2');
  const gradient = document.getElementById('gradient');
  const gradient2 = document.getElementById('conditionoutput');
  const gradient3 = document.getElementById('gradient3');
  const conoutmob = document.getElementById('conditionoutputmob');
  const priceoutputmob = document.getElementById('priceoutputmob');
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
  conoutmob.style.background =
    "linear-gradient( "
    + color1input.value
    + ", "
    + color2input.value
    + ")";
  priceoutputmob.style.background =
    "linear-gradient( "
    + color1input.value
    + ", "
    + color2input.value
    + ")";

}


function shoes() {

  const shoes = document.getElementById("shoes").value;
  const sizeoutput = document.getElementById("sizeoutput");
  const sizeoutputmob = document.getElementById("sizeoutputmob");
  sizeoutput.innerHTML = shoes
  sizeoutputmob.innerHTML = shoes

}
function clothes() {
  const clothes = document.getElementById("clothes").value;
  const sizeoutput = document.getElementById("sizeoutput");
  const sizeoutputmob = document.getElementById("sizeoutputmob");
  sizeoutput.innerHTML = clothes
  sizeoutputmob.innerHTML = clothes
}
function sizes() {
  const c = document.getElementById("category").value;
  const shoes = document.getElementById("shoes");
  const clothes = document.getElementById("clothes");
  const accesories = document.getElementById("accesories");

  if (c == "Shoes") {
    console.log("Shoes")
    shoes.style.display = "inline-block"
    clothes.style.display = "none"
    accesories.style.display = "none"


  }
  else if (c == "Clothes") {
    console.log("clothes")
    clothes.style.display = "inline-block"
    shoes.style.display = "none"
    accesories.style.display = "none"

  }
  else if (c == "Accesories") {
    console.log("accesories")
    accesories.style.display = "inline-block"
    shoes.style.display = "none"
    clothes.style.display = "none"

  }

}
function prosim() {

  const con = document.getElementById('conditioninput').value;
  const conout = document.getElementById('conditionoutput');
  const conoutmob = document.getElementById('conditionoutputmob');
  conout.innerHTML = "Condition: " + con
  conoutmob.innerHTML = "Condition: " + con



}
// const stripe = Stripe(
//   "pk_live_51M6qYrIPZACj0qgM7LX0fRVD7JtxGvEURAktEIHStG3jjHCe2B3zI82Snrobbn14FIMcb7IpHh6gsVLWnZnHzId200SoZVoWCr"
// );
// const elements = stripe.elements();
// const style = {
//   base: {
//     // Add your base input styles here. For example:
//     fontSize: "16px",
//     color: "#32325d",
//   },
// };

// // Create an instance of the card Element.
// const card = elements.create("card", { style });

// // Add an instance of the card Element into the `card-element` <div>.
// card.mount("#card-element");
// const form = document.getElementById("payment-form");
// form.addEventListener("submit", async (event) => {
//   event.preventDefault();

//   const { token, error } = await stripe.createToken(card);

//   if (error) {
//     // Inform the customer that there was an error.
//     const errorElement = document.getElementById("card-errors");
//     errorElement.textContent = error.message;
//   } else {
//     // Send the token to your server.
//     stripeTokenHandler(token);
//   }
// });
// const stripeTokenHandler = (token) => {
//   // Insert the token ID into the form so it gets submitted to the server
//   const form = document.getElementById("payment-form");
//   const hiddenInput = document.createElement("input");
//   hiddenInput.setAttribute("type", "hidden");
//   hiddenInput.setAttribute("name", "stripeToken");
//   hiddenInput.setAttribute("value", token.id);
//   form.appendChild(hiddenInput);

//   // Submit the form
//   form.submit();
// };