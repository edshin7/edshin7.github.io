// Camera Music
// Music in the form of motion; Customed to however the user would like

// Written by Edward Shin

// Finished: 08-20-2016

var myCaptureDevice;

var blocks;
var archs;
var balls;
var ripplers;
var ripples;
var bubblers;
var bubbles;
var spinners;
var shifters;

var numBubbles;
var minBubbles;
var maxBubbles;

var mouseInXBounds;
var mouseInYBounds;

var error;

var modes;
var mode;
var control;
var notes = [];
var picColor;
var colorIsSet;
var startMessage;


function preload(){
  notes[0] = loadSound("sounds/drum.mp3");
  notes[0].setVolume(3);
  notes[1] = loadSound("sounds/zoink.mp3");
  notes[1].setVolume(4);
  notes[2] = loadSound("sounds/boink.mp3");
  notes[2].setVolume(0.5);
  notes[3] = loadSound("sounds/drip.mp3");
  notes[3].setVolume(3);
  notes[4] = loadSound("sounds/xylo.mp3");
  notes[4].setVolume(4);
  notes[5] = loadSound("sounds/pop.mp3");
  notes[5].setVolume(0.5);
  notes[6] = loadSound("sounds/tone.mp3");
  notes[6].setVolume(3);
  notes[7] = loadSound("sounds/brr.mp3");
  notes[7].setVolume(4);
}


function setup() {
  createCanvas(640, 720);
  angleMode(DEGREES);
  
  myCaptureDevice = createCapture(VIDEO);
  myCaptureDevice.size(640, 480); // attempt to size the camera. 
  myCaptureDevice.hide(); // this hides an unnecessary extra view.
  
  blocks = [];  // Stores all instruments and visuals in lists
  archs = [];
  balls = [];
  ripplers = [];
  ripples = [];
  bubblers = [];
  bubbles = [];
  spinners = [];
  shifters = [];
  
  minBubbles = 7;
  maxBubbles = minBubbles * 2;
  
  error = 0.2; //the percentage the pick color can be off by
  
  modes = ["1", "2", "3", "4", "5", "6", "7", "P", "E"]; // modes only for instruments
  mode = "1";
  control = new Control(myCaptureDevice.height, mode);
  
  pickColor = null;    // the color of the item you will use to make the instruments play
  colorIsSet = false;
  startMessage = "Click on the object's COLOR you want to use to play music.\n\n" + 
                "Set INSTRUMENTS using the mouse, and then PLAY.\n\n" +
                "This works best in a WHITE background.";
}


function draw() {
  background(220);
  
  push();
  translate(width, 0);
  scale(-1, 1);
  myCaptureDevice.loadPixels(); // this must be done on each frame.
  image(myCaptureDevice, 0, 0);  // draw the camera at 1:1 resolution
  pop();
  
  drawExtraCanvas();
  updateMouseCondition();
  
  if(colorIsSet){
    drawInstruments();
    playInstruments();
  }
  
  control.draw();
}

// updates whether mouse is in the webcam window
function updateMouseCondition(){
  mouseInXBounds = (mouseX > 0 && mouseX < myCaptureDevice.width);
  mouseInYBounds = (mouseY > 0 && mouseY < myCaptureDevice.height);
}

// setting the item color color if not done yet
function setInteraction(){
  if(!colorIsSet){
    pickColor = myCaptureDevice.get(myCaptureDevice.width - mouseX, mouseY);
    colorIsSet = true;
    startMessage = "";
  }
}


// transparent canvas to better show the instruments while 
// allowing obscure view of the user and his/her movements
function drawExtraCanvas(){
  fill(255, 170);
  noStroke();
  rect(0, 0, width, height);
  
  fill(0);
  textSize(20);
  textAlign(CENTER, BASELINE);
  textStyle(BOLD);
  text(startMessage, myCaptureDevice.width / 2, myCaptureDevice.height / 2);
}


function drawInstruments(){
  drawBlocks();
  drawArchs();
  drawBalls();
  drawRipplers();
  drawRipples();
  drawBubblers();
  drawBubbles();
  drawSpinners();
  drawShifters();
}


function playInstruments(){
  if(mode == "P"){
    playBlocks();
    playArchs();
    playBalls();
    playRipplers();
    playBubblers();
    playSpinners();
    playShifters();
  }
}


// makeInstruments depending on appropriate mode
function makeInstruments(){
  if(colorIsSet === true){
    switch(mode){
      case "1":
        makeBlock();
        break;
        
      case "2":
        makeArch();
        break;
        
      case "3":
        makeBall();
        break;
      
      case "4":
        makeRippler();
        break;
        
      case "5":
        makeBubbler();
        break;
        
      case "6":
        makeSpinner();
        break;
        
      case "7":
        makeShifter();
        break;
        
      default:
        break;
    }
  }
}


function eraseInstrument(){
  if(mode == "E"){
    eraseBlock();
    eraseArch();
    eraseBall();
    eraseRippler();
    eraseBubbler();
    eraseSpinner();
    eraseShifter();
  }
}


function drawBlocks(){
  for(var i = 0; i < blocks.length; i++){
    blocks[i].draw();
  }
}


function playBlocks(){
  for(var i = 0; i < blocks.length; i++){
    blocks[i].play(pickColor, error);
  }
}


function makeBlock(){
  blocks.push(new Block(mouseX, mouseY));
}


function eraseBlock(){
  for(var i = 0; i < blocks.length; i++){
    if(blocks[i].mouseInRange()){
      blocks.splice(i, 1);
      break;
    }
  }
}


function drawArchs(){
  for(var i = 0; i < archs.length; i++){
    archs[i].draw();
  }
}


function playArchs(){
  for(var i = 0; i < archs.length; i++){
    archs[i].play(pickColor, error);
  }
}


function makeArch(){
  archs.push(new Arch(mouseX, mouseY));
}


function eraseArch(){
  for(var i = 0; i < archs.length; i++){
    if(archs[i].mouseInRange()){
      archs.splice(i, 1);
      break;
    }
  }
}


function drawBalls(){
  for( var i = 0; i < balls.length; i++){
    balls[i].draw();
  }
}


function playBalls(){
  for( var i = 0; i < balls.length; i++){
    balls[i].play(pickColor, error);
  }
}


function makeBall(){
  balls.push(new Ball(mouseX, mouseY, myCaptureDevice.width, myCaptureDevice.height));
}


function eraseBall(){
  for(var i = 0; i < balls.length; i++){
    if(balls[i].mouseInRange()){
      balls.splice(i, 1);
      break;
    }
  }
}


function drawRipplers(){
  for(var i = 0; i < ripplers.length; i++){
    ripplers[i].draw();
  }
}


function playRipplers(){
  for(var i = 0; i < ripplers.length; i++){
    if(ripplers[i].play(pickColor, error) === true){
      makeRipple(ripplers[i].x, ripplers[i].y);
    }
  }
}


function makeRippler(){
  ripplers.push(new Rippler(mouseX, mouseY));
}


function eraseRippler(){
  for(var i = 0; i < ripplers.length; i++){
    if(ripplers[i].mouseInRange()){
      ripplers.splice(i, 1);
      break;
    }
  }
}


function drawRipples(){
  for(var i = 0; i < ripples.length; i++){
    ripples[i].draw();
    ripples[i].play();
    if(ripples[i].isGone()){
      ripples.splice(i, 1);
    }
  }
}

function makeRipple(x, y){
  ripples.push(new Ripple(x, y))
}


function drawBubblers(){
  for(var i = 0; i < bubblers.length; i++){
    bubblers[i].draw();
  }
}


function playBubblers(){
  for(var i = 0; i < bubblers.length; i++){
    var oldX = bubblers[i].x;
    var oldY = bubblers[i].y;
    
    bubblers[i].play(pickColor, error);
    
    if(bubblers[i].exploded){
      makeBubbles(oldX, oldY);
    }
  }
}


function makeBubbler(){
  bubblers.push(new Bubbler(mouseX, mouseY, myCaptureDevice.width, myCaptureDevice.height));
}


function eraseBubbler(){
  for(var i = 0; i < bubblers.length; i++){
    if(bubblers[i].mouseInRange()){
      bubblers.splice(i, 1);
      break;
    }
  }
}


function drawBubbles(){
  for(var i = 0; i < bubbles.length; i++){
    bubbles[i].draw();
    bubbles[i].play();
    
    if(bubbles[i].isPopped()){
      bubbles.splice(i, 1);
    }
  }
}


function makeBubbles(x, y, r, g, b){
  numBubbles = round(minBubbles, maxBubbles);
  for(var i = 0; i < numBubbles; i++){
    bubbles.push(new Bubble(x, y, r, g, b));
  }
}


function drawSpinners(){
  for(var i = 0; i < spinners.length; i++){
    spinners[i].draw();
  }
}


function playSpinners(){
  for(var i = 0; i < spinners.length; i++){
    spinners[i].play(pickColor, error);
  }
}


function makeSpinner(){
  spinners.push(new Spinner(mouseX, mouseY));
}


function eraseSpinner(){
  for(var i = 0; i < spinners.length; i++){
    if(spinners[i].mouseInRange()){
      spinners.splice(i, 1);
      break;
    }
  }
}


function drawShifters(){
  for(var i = 0; i < shifters.length; i++){
    shifters[i].draw();
  }
}


function playShifters(){
  for(var i = 0; i < shifters.length; i++){
    shifters[i].play(pickColor, error);
  }
}


function makeShifter(){
  shifters.push(new Shifter(mouseX, mouseY));
}


function eraseShifter(){
  for(var i = 0; i < shifters.length; i++){
    if(shifters[i].mouseInRange()){
      shifters.splice(i , 1);
      break;
    }
  }
}


function mousePressed(){
  if(mouseInXBounds && mouseInYBounds){
    makeInstruments();
    eraseInstrument();
    setInteraction();
  }
}


function keyPressed(){
  if(colorIsSet && (key in modes || key == "P" || key == "E")){
    mode = key;
    control.update(key);
  }
}


////////////////////////////////////////
////////////////////////////////////////
////////////////////////////////////////
/////////////// Objects ////////////////
////////////////////////////////////////
////////////////////////////////////////
////////////////////////////////////////


// string-like instrument part
function Block(x, y){
  this.x = x;
  this.y = y;
  this.minSide = 50;
  this.maxSide = 70;
  this.side = this.minSide;
  this.minWeight = 4;
  this.maxWeight = 8;
  this.lnWeight = this.minWeight;
  
  this.g1 = 170;
  this.b1 = 230;
  this.g2 = 240;
  this.b2 = 150;
  
  this.rValue = 40;
  this.gValue = this.g1;
  this.bValue = this.b1;
  this.aValue = 100;
  
  this.isPlayed = false;
  
  this.draw = function(){
    fill(this.rValue, this.gValue, this.bValue, this.aValue);
    stroke(this.rValue, this.gValue, this.bValue);
    strokeWeight(this.lnWeight);
    rectMode(CENTER);
    rect(this.x, this.y, this.side, this.side);
    
    strokeWeight(this.lnWeight * 2);
    point(this.x, this.y);
  }
  
  this.play = function(pickColor, error){
    // position inverted because image was inverted, but not pixel color positions
    var checkColor = myCaptureDevice.get(myCaptureDevice.width - this.x, this.y);
    var r = checkColor[0];
    var g = checkColor[1];
    var b = checkColor[2];
    
    if(r >= red(pickColor) - (255 * error) && r <= red(pickColor) + (255 * error) &&
      g >= green(pickColor) - (255 * error) && g <= green(pickColor) + (255 * error) &&
      b >= blue(pickColor) - (255 * error) && b <= blue(pickColor) + (255 * error)){
        
      this.lnWeight = this.maxWeight;
      this.side = this.maxSide;
      this.gValue = this.g2;
      this.bValue = this.b2;
      
      if(!this.isPlayed){
        notes[0].play();
        this.isPlayed = true;
      }
    }
    else{
      this.lnWeight = this.minWeight;
      this.side = this.minSide;
      this.gValue = this.g1;
      this.bValue = this.b1;
      this.isPlayed = false;
    }
  }
  
  // used to tell if mouse is nearby; used to give the okay for erasing
  this.mouseInRange = function(){
    var distance = dist(mouseX, mouseY, this.x, this.y);
    
    return distance < (this.side / 2);
  }

}


// an instrument made with an orbiting arc
function Arch(x, y){
  this.x = x;
  this.y = y;
  this.startAngle = round(random(-45, 45));
  this.endAngle = round(random(90, 180));
  this.totalAngle = this.endAngle - this.startAngle;
  
  this.angle1 = this.startAngle;
  this.angle2 = this.endAngle;
  
  this.minStep = random(1, 3);
  this.maxStep = this.minStep * 10;
  this.step = this.minStep;
  this.sFactor = 0.99;
  
  this.radius = 10;
  this.minRadius2 = 25;
  this.maxRadius2 = 200;
  this.radius2 = this.minRadius2;
  
  this.lnWeight = round(random(3, 6));
  
  this.rValue = 150;
  this.gValue = 50;
  this.bValue = 130;
  
  this.isPlayed = false;
  
  
  this.draw = function(){
    fill(this.rValue, this.gValue, this.bValue);
    noStroke();
    ellipse(this.x, this.y, this.radius * 2, this.radius * 2);
    
    noFill();
    stroke(this.rValue, this.gValue, this.bValue);
    strokeWeight(this.lnWeight);
    strokeCap(SQUARE);
    arc(this.x, this.y, this.radius2 * 2, this.radius2 * 2, this.startAngle, this.endAngle);
  }
  
  
  this.play = function(pickColor, error){
    // position inverted because image was inverted, but not pixel color positions
    var checkColor = myCaptureDevice.get(myCaptureDevice.width - this.x, this.y);
    var r = checkColor[0];
    var g = checkColor[1];
    var b = checkColor[2];
    
    if(r >= red(pickColor) - (255 * error) && r <= red(pickColor) + (255 * error) &&
      g >= green(pickColor) - (255 * error) && g <= green(pickColor) + (255 * error) &&
      b >= blue(pickColor) - (255 * error) && b <= blue(pickColor) + (255 * error)){
        
      this.step = this.maxStep;
      
      if(!this.isPlayed){
        notes[1].play();
        this.isPlayed = true;
      }
    }
    
    else{
      if(round(this.step) < this.minStep){
        this.step = this.minStep;
      }
      else{
        this.step *= this.sFactor;
      }
      
      this.isPlayed = false;
    }
    
    if(this.startAngle >= 360){
      this.startAngle = 0;
      
      if(this.step > this.minStep){
        this.radius2 = random(this.minRadius2, this.maxRadius2);
      }
    }
    this.startAngle += this.step;
    this.endAngle = this.startAngle + this.totalAngle;
    
  }
  
  // used to tell if mouse is nearby; used to give the okay for erasing
  this.mouseInRange = function(){
    var distance = dist(mouseX, mouseY, this.x, this.y);
    
    return distance < this.minRadius2;
  }
  
}


// a ball that makes music when in contact with user or walls
function Ball(x, y, wid, hei){
  this.x = x;
  this.y = y;
  this.wid = wid;
  this.hei = hei;
  this.radius = 25;
  
  this.rValue = 50;
  this.gValue = 180;
  this.bValue = 100;
  this.aValue = 50;
  
  this.lnWeight = 5;
  
  this.xStep = 0;
  this.yStep = 0;
  this.stepFactor = 5;
  this.decel = 0.995;
  this.stepReset = 3.75;
  
  this.isPlayed = false;
  
  this.draw = function(){
    fill(this.rValue, this.gValue, this.bValue, this.aValue);
    stroke(this.rValue, this.gValue, this.bValue);
    strokeWeight(this.lnWeight);
    ellipse(this.x, this.y, this.radius * 2, this.radius * 2);
    
    strokeWeight(this.lnWeight * 2);
    point(this.x, this.y);
  }
  
  
  this.play = function(pickColor, error){
    this.rebound();
    this.updateSteps(pickColor, error);
    this.move();
  }
  
  
  this.move = function(){
    this.x = round(this.x + this.xStep);
    this.y = round(this.y + this.yStep);
  }
  
  
  // update step when in contact with user
  this.updateSteps = function(pickColor, error){
    // position inverted because image was inverted, but not pixel color positions
    var checkColor = myCaptureDevice.get(myCaptureDevice.width - this.x, this.y);
    var r = checkColor[0];
    var g = checkColor[1];
    var b = checkColor[2];
    
    if(r >= red(pickColor) - (255 * error) && r <= red(pickColor) + (255 * error) &&
      g >= green(pickColor) - (255 * error) && g <= green(pickColor) + (255 * error) &&
      b >= blue(pickColor) - (255 * error) && b <= blue(pickColor) + (255 * error) &&
      abs(this.xStep < this.stepReset)){
        
      var chance = ceil(random(4));
      switch(chance){
        case 1:
          this.xStep = this.stepFactor;
          this.yStep = this.stepFactor;
          break;
          
        case 2:
          this.xStep = -this.stepFactor;
          this.yStep = this.stepFactor;
          break;
        case 3:
          this.xStep = this.stepFactor;
          this.yStep = -this.stepFactor;
          break;
        default:
          this.xStep = -this.stepFactor;
          this.yStep = -this.stepFactor;
          break;
      }
      
      if(!this.isPlayed){
        notes[2].play();
        this.isPlayed = true;
      }
    }
    
    this.isPlayed = false;
    this.xStep *= this.decel;
    this.yStep *= this.decel;
  }
  
  
  // rebound off walls
  this.rebound = function(){
    var left = this.x - this.radius;
    var right = this.x + this.radius;
    var up = this.y - this.radius;
    var down = this.y + this.radius;
    
    if((left <= 0 && this.xStep < 0) || (right >= this.wid && this.xStep > 0)){
      this.xStep = -this.xStep;
      notes[2].play();
    }
    
    if((up <= 0 && this.yStep < 0) || (down >= this.hei && this.yStep > 0)){
      this.yStep = -this.yStep;
      notes[2].play();
    }
  }
  
  // get angle by arc formula
  this.getAngle = function(x1, y1){
    var x2 = this.x + this.radius;
    var y2 = this.y;
    var distance = dist(x1, y1, x2, y2);
    var angle = acos(1 - (pow(distance, 2) / (2 * pow(this.radius, 2))));
    
    return angle;
  }
  
  // used to tell if mouse is nearby; used to give the okay for erasing
  this.mouseInRange = function(){
    var distance = dist(mouseX, mouseY, this.x, this.y);
    
    return distance < this.radius;
  }
}


function Ripple(x, y){
  this.x = x;
  this.y = y;
  this.radius = 2;
  this.rFactor = 1.08;
  
  this.rValue = 230;
  this.gValue = 140;
  this.bValue = 50;
  this.aValue = 255;
  this.aFactor = 0.4;
  this.lnWeight = 2;
  
  this.draw = function(){
    noFill();
    stroke(this.rValue, this.gValue, this.bValue, this.aValue);
    strokeWeight(this.lnWeight);
    ellipse(this.x, this.y, this.radius, this.radius);
  }
  
  this.play = function(){
    this.radius *= this.rFactor;
    this.aValue -= this.aFactor;
  }
  
  this.isGone = function(){
    if(this.aValue < 0){
      return true;
    }
    
    else{
      return false;
    }
  }
}


function Rippler(x, y){
  this.x = x;
  this.y = y;
  
  this.radius = 10;
  this.radius2 = 25;
  
  this.rValue = 230;
  this.gValue = 140;
  this.bValue = 50;
  
  this.minWeight = 4;
  this.maxWeight = 8;
  this.lnWeight = this.minWeight;
  
  this.count = 100;
  this.maxCount = 100;
  
  this.isPlayed = false;
  
  this.draw = function(){
    noFill();
    stroke(this.rValue, this.gValue, this.bValue);
    strokeWeight(this.lnWeight);
    
    ellipse(this.x, this.y, this.radius * 2, this.radius * 2);
    ellipse(this.x, this.y, this.radius2 * 2, this.radius2 * 2);
  }
  
  this.play = function(pickColor, error){
    // position inverted because image was inverted, but not pixel color positions
    var checkColor = myCaptureDevice.get(myCaptureDevice.width - this.x, this.y);
    var r = checkColor[0];
    var g = checkColor[1];
    var b = checkColor[2];
    
    if(r >= red(pickColor) - (255 * error) && r <= red(pickColor) + (255 * error) &&
      g >= green(pickColor) - (255 * error) && g <= green(pickColor) + (255 * error) &&
      b >= blue(pickColor) - (255 * error) && b <= blue(pickColor) + (255 * error)){
      
      if(!this.isPlayed){
        notes[3].play();
        this.isPlayed = true;
      }
      
      this.lnWeight = this.maxWeight;
      if(this.count == this.maxCount){
        this.count = 0;
        return true;
      }
      
      else{
        this.count++;
        return false;
      }
    }
    
    else{
      this.lnWeight = this.minWeight;
      this.count = 100;
      this.isPlayed = false;
      return false;
    }
  }
  
  // used to tell if mouse is nearby; used to give the okay for erasing
  this.mouseInRange = function(){
    var distance = dist(mouseX, mouseY, this.x, this.y);
    
    return distance < this.radius2;
  }
}


// Bubbles that make noise when they "pop"
function Bubble(x, y){
  this.x = x;
  this.y = y;
  
  this.radius = random(20, 50);
  this.lnWeight = 2;
  
  this.rValue = random(100, 255);
  this.gValue = random(100, 255);
  this.bValue = random(100, 255);
  this.aValue = 100;
  
  this.xStep = random(-2, 2);
  this.yStep = random(-2, 2);
  
  this.count = 0;
  this.maxCount = random(100, 150);
  
  this.draw = function(){
    fill(this.rValue, this.gValue, this.bValue, this.aValue);
    stroke(this.rValue, this.gValue, this.bValue);
    strokeWeight(this.lnWeight);
    ellipse(this.x, this.y, this.radius, this.radius);
  }
  
  this.play = function(){
    this.move();
    this.count++;
  }
  
  this.move = function(){
    this.x += this.xStep;
    this.y += this.yStep;
  }
  
  this.isPopped = function(){
    var xIsOut = (this.x - this.radius < 0) || (this.x + this.radius > myCaptureDevice.width);
    var yIsOut = (this.y - this.radius < 0) || (this.y + this.radius > myCaptureDevice.height)
    
    if(this.count >= this.maxCount || xIsOut || yIsOut){
      this.aValue = this.lnWeight = 0;
      notes[5].play();
      return true;
    }
    
    return false;
  }
}


// creates Bubbles
function Bubbler(x, y, wid, hei){
  this.x = x;
  this.y = y;
  this.wid = wid;
  this.hei = hei;
  
  this.side = 50;
  this.radius = 10;
  this.lnWeight = 2;
  
  this.rValue = 210;
  this.gValue = 140;
  this.bValue = 170;
  this.aValue = 150;
  this.aValue2 = 255;
  
  this.exploded = false;
  
  this.draw = function(){
    rectMode(CENTER);
    fill(this.rValue, this.gValue, this.bValue, this.aValue);
    stroke(this.rValue, this.gValue, this.bValue, this.aValue2);
    strokeWeight(this.lnWeight);
    rect(this.x, this.y, this.side, this.side, 
          this.radius, this.radius, this.radius, this.radius);

    ellipse(this.x, this.y, this.radius * 2, this.radius * 2);
    
    
  }
  
  this.play = function(pickColor, error){
    // position inverted because image was inverted, but not pixel color positions
    var checkColor = myCaptureDevice.get(myCaptureDevice.width - this.x, this.y);
    var r = checkColor[0];
    var g = checkColor[1];
    var b = checkColor[2];
    
    if(r >= red(pickColor) - (255 * error) && r <= red(pickColor) + (255 * error) &&
      g >= green(pickColor) - (255 * error) && g <= green(pickColor) + (255 * error) &&
      b >= blue(pickColor) - (255 * error) && b <= blue(pickColor) + (255 * error)){
        
      this.x = round(random(this.side / 2, this.wid - (this.side / 2)));
      this.y = round(random(this.side / 2, this.hei - (this.side / 2)));
      this.exploded = true;
      
      notes[4].play();
    }
    
    else{
      this.exploded = false;
    }
  }
  
  // used to tell if mouse is nearby; used to give the okay for erasing
  this.mouseInRange = function(){
    var distance = dist(mouseX, mouseY, this.x, this.y);
    
    return distance < (this.side / 2);
  }
}


function Spinner(x, y){
  this.x = x;
  this.y = y;
  this.offset = 15;
  this.maxWid = this.wid = this.hei = 60;
  this.y1 = this.y - this.hei/2 - this.offset;
  this.y2 = this.y + this.hei/2 + this.offset;
  this.lnWeight = 2;
  this.lnWeight2 = this.lnWeight * 2;
  
  this.maxStep = 7;
  this.step = 0;
  this.dir = -1;
  this.sFactor = 0.99;
  this.stopStep = 0.5;
  
  this.rValue = 120;
  this.gValue = 110;
  this.bValue = 250;
  this.aValue = 120;
  
  this.isPlayed = false;
  
  this.draw = function(){
    fill(this.rValue, this.gValue, this.bValue, this.aValue);
    stroke(this.rValue, this.gValue, this.bValue);
    strokeWeight(this.lnWeight);
    rectMode(CENTER);
    rect(this.x, this.y, this.wid, this.hei);
    
    strokeWeight(this.lnWeight2);
    strokeCap(PROJECT);
    line(this.x, this.y1, this.x, this.y2);
  }
  
  this.play = function(pickColor, error){
    // position inverted because image was inverted, but not pixel color positions
    var checkColor = myCaptureDevice.get(myCaptureDevice.width - this.x, this.y);
    var r = checkColor[0];
    var g = checkColor[1];
    var b = checkColor[2];
    
    if((r > red(pickColor) - (255 * error)) && (r < red(pickColor) + (255 * error)) &&
      (g > green(pickColor) - (255 * error)) && (g < green(pickColor) + (255 * error)) &&
      (b > blue(pickColor) - (255 * error)) && (b < blue(pickColor) + (255 * error))){
        
      this.step = this.maxStep * this.dir;
      
      if(!this.isPlayed){
        notes[6].play();
        this.isPlayed = true;
      }

    }
    
    else{
      this.slowDown();
      this.isPlayed = false;
    }
    
    this.spin();
  }
  
  this.spin = function(){
    var widSum = this.wid + this.step;
    
    if((widSum >= this.maxWid) || (widSum <= 0)){
      this.dir = -this.dir;
      this.step *= this.dir;
    }
    
    this.wid += this.step;
  }
  
  this.slowDown = function(){
    if(abs(this.step) < this.stopStep){
      this.step = 0;
    }
    else{
      this.step *= this.sFactor;
    }
  }
  
  // used to tell if mouse is nearby; used to give the okay for erasing
  this.mouseInRange = function(){
    var distance = dist(mouseX, mouseY, this.x, this.y);
    
    return distance < (this.maxWid / 2);
  }
}


function Shifter(x, y){
  this.x = x;
  this.y = y;
  this.side = 60;
  this.x1 = this.x - (this.side / 2);
  this.y1 = this.y - (this.side / 2);
  this.x2 = this.x1 + this.side;
  this.y2 = this.y1 + this.side;
  
  this.newX1;
  this.newY1;
  this.newX2;
  this.newY2;
  
  this.lnWeight = 10;
  
  this.stepFactor1 = 0.1;
  this.stepFactor2 = 0.025;
  
  this.rValue = 200;
  this.gValue = 240;
  this.bValue = 100;
  this.aValue = 210;
  
  this.isPlayed = false;
  this.isMoving = false;
  
  this.draw = function(){
    fill(this.rValue, this.gValue, this.bValue, this.aValue);
    noStroke();
    rectMode(CORNERS);
    rect(this.x1, this.y1, this.x2, this.y2);
    
    stroke(this.rValue, this.gValue, this.bValue);
    strokeWeight(this.lnWeight);
    point(this.x, this.y);
  }
  
  this.play = function(pickColor, error){
    // position inverted because image was inverted, but not pixel color positions
    var checkColor = myCaptureDevice.get(myCaptureDevice.width - this.x, this.y);
    var r = checkColor[0];
    var g = checkColor[1];
    var b = checkColor[2];
    
    if((r > red(pickColor) - (255 * error)) && (r < red(pickColor) + (255 * error)) &&
      (g > green(pickColor) - (255 * error)) && (g < green(pickColor) + (255 * error)) &&
      (b > blue(pickColor) - (255 * error)) && (b < blue(pickColor) + (255 * error))){
      
      var margin = this.side / 2;
      this.x = round(random(margin, myCaptureDevice.width - margin))
      this.y = round(random(margin, myCaptureDevice.height - margin))
      this.newX1 = this.x - margin;
      this.newY1 = this.y - margin;
      this.newX2 = this.newX1 + this.side;
      this.newY2 = this.newY1 + this.side;
      this.isMoving = true;
      
      if(!this.isPlayed){
        notes[7].play();
        this.isPlayed = true;
      }

    }
    
    else{
      this.isPlayed = false;
    }
    
    this.move();
  }
  
  // move the rectangle by two of its corners while distorting its proportions
  this.move = function(){
    if(this.isMoving){
      var diffX1 = this.newX1 - this.x1;
      var diffY1 = this.newY1 - this.y1;
      var diffX2 = this.newX2 - this.x2;
      var diffY2 = this.newY2 - this.y2;
      
      this.x1 += diffX1 * this.stepFactor1;
      this.y1 += diffY1 * this.stepFactor1;
      this.x2 += diffX2 * this.stepFactor2;
      this.y2 += diffY2 * this.stepFactor2;
      
      
      if(dist(this.x1, this.y1, this.newX1, this.newY1) < 1 &&
        dist(this.x2, this.y2, this.newX2, this.newY2) < 1){
          
        this.x1 = this.newX1;
        this.y1 = this.newY1;
        this.x2 = this.newX2;
        this.y2 = this.newY2;
        this.isMoving = false;
      }
    }
  }
  
  // used to tell if mouse is nearby; used to give the okay for erasing
  this.mouseInRange = function(){
    var distance = dist(mouseX, mouseY, this.x, this.y);
    
    return (distance < this.side / 2);
  }
}


// Control Board showing instructions and information about the application
function Control(y, mode){
  this.x = 0;
  this.y = y;
  this.controlWid = width;
  this.controlHei = height - this.y;
  this.margin = 7;
  
  this.x1 = this.x + this.margin;
  this.y1 = this.y + this.margin;
  this.x2 = width / 2;
  this.y2 = this.y1;
  
  this.mode = mode;
  this.wordSize = 15;
  this.mode1Text = "Blocks:\n\n" + "Hitting these will create sound\n" + "and light up the Blocks."
  this.mode2Text = "Archs:\n\n" + "Hitting these will create sound\n" + "and vary out the arcs' radii."
  this.mode3Text = "Balls:\n\n" + "Hitting these will cause them to\n" + "bounce. They create sound every\n" +
                    "everytime they hit the wall or the user";
  this.mode4Text = "Rippler:\n\n" + "Touch it to create ripples. and sound";
  this.mode5Text = "Bubbler:\n\n" + "Touch it to create bubbles and\n" + "move it to a random location.\n" + 
                    "When the bubbles pop, they create sound.";
  this.mode6Text = "Spinner:\n\n" + "Touch it to create the impression\n" + "of a revolving door."
  this.mode7Text = "Shifter:\n\n" + "Touch it to shift it by its corners."
  this.modePText = "PLAY TO YOUR HEARTS CONTENT.\n\n" + "DANCE TO YOUR WILD IMAGINATIONS."
  this.modeEText = "Erase at your leisure."
  
  this.modeText = this.mode1Text;
  this.instructions = "Controls/Options:\n\n" + 
                      "Press 1 to add Blocks\n" + 
                      "Press 2 to add Archs\n" + 
                      "Press 3 to add Balls\n" +
                      "Press 4 to add Rippler\n" + 
                      "Press 5 to add Bubbler\n" +
                      "Press 6 to add Spinner\n" +
                      "Press 7 to add Shifter\n" +
                      "Press E to Erase\n" +
                      "Press P to play";
                      
  this.draw = function(){
    fill(0);
    noStroke();
    rectMode(CORNER);
    rect(this.x, this.y, this.controlWid, this.controlHei);
    
    fill(255);
    textAlign(LEFT, TOP);
    textSize(this.wordSize);
    text(this.modeText, this.x1, this.y1);
    text(this.instructions, this.x2, this.y2);
  }
  
  // update the application's mode and the text
  this.update = function(newMode){
    this.mode = newMode;
    
    switch(this.mode){
      case "1":
        this.modeText = this.mode1Text;
        break;
      case "2":
        this.modeText = this.mode2Text;
        break;
      case "3":
        this.modeText = this.mode3Text;
        break;
      case "4":
        this.modeText = this.mode4Text;
        break;
      case "5":
        this.modeText = this.mode5Text;
        break;
      case "6":
        this.modeText = this.mode6Text;
        break;
      case "7":
        this.modeText = this.mode7Text;
        break;
      case "P":
        this.modeText = this.modePText;
        break;
      case "E":
        this.modeText = this.modeEText;
      default:
        break;
    }
  }
}






