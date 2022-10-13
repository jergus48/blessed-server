const root = document.querySelector("#app");


class Bubble {
  constructor() {
    this.bubbleSpan = undefined;
    this.handleNewBubble();
    this.color = this.randomColor();
    
    this.posY = this.randomNumber(innerHeight - 20, 20);
    this.posX = this.randomNumber(innerWidth - 20, 20);

    this.bubbleSpan.style.top = this.posY + "px";
    this.bubbleSpan.style.left = this.posX + "px";

    // setting height and width of the bubble
    this.height = this.randomNumber(35, 20);
    this.width = this.height;

    this.bubbleEnd.call(this.bubbleSpan, this.randomNumber(6000, 3000));
  }

  // creates and appends a new bubble in the DOM
  handleNewBubble() {
    this.bubbleSpan = document.createElement("span");
    
    this.bubbleSpan.classList.add("bubble");
    root.append(this.bubbleSpan);
    this.handlePosition();
    this.bubbleSpan.addEventListener("click", this.bubbleEnd);
  }

  handlePosition() {
    // positioning the bubble in different random X and Y
    const randomY = this.randomNumber(60, -60);
    const randomX = this.randomNumber(60, -60);

    this.bubbleSpan.style.backgroundColor = this.color;
    this.bubbleSpan.style.height = this.height + "px";
    this.bubbleSpan.style.width = this.height + "px";

    this.posY = this.randomNumber(innerHeight - 20, 20);
    this.posX = this.randomNumber(innerWidth - 20, 20);

    this.bubbleSpan.style.top = this.posY + "px";
    this.bubbleSpan.style.left = this.posX + "px";

    const randomSec = this.randomNumber(4000, 200);
    setTimeout(this.handlePosition.bind(this), randomSec); // calling for re-position of bubble
  }

  randomNumber(max, min) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }

  randomColor() {
    const darkgray = 'rgba(52, 52, 52)'
    const white = 'rgba(255, 255, 255)'
    const gray = 'rgba(52, 52, 52)'
    const black = 'rgba(0, 0, 0)'
    // return `rgba(
    //     ${this.randomNumber(0, 255)},
    //     ${this.randomNumber(0, 255)},
        
    //     ${this.randomNumber(0.1, 1)})`;
    const min = 1;
    const max = 5;
    const intNumber = Math.floor(Math.random() * (max - min)) + min;
    if (intNumber == 1){
        return darkgray}
    else if (intNumber == 2){
        return black}
     else if (intNumber == 3){
        return white}
     else if (intNumber == 4){
        return gray}

  }

  bubbleEnd(removingTime = 0) {
    setTimeout(
      () => {
        requestAnimationFrame(() => this.classList.add("bubble--bust"));
      },
      removingTime === 0 ? removingTime : removingTime-100
    );

    setTimeout(() => {
      requestAnimationFrame(() => this.remove());
      requestAnimationFrame(() => new Bubble());
      
    }, removingTime);
  }
}

// creating many bubble instance
let num = 0
setInterval(function () {
  requestAnimationFrame(() =>{ if (num < 50){new Bubble(),num=num+1,console.log(num)}});
}, 1500);