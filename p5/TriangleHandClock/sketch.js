//Edward Shin
//15-104 Section A
//edwardsh@andrew.cmu.edu
//Project-04

var centerX;   //x center of clock
var centerY;   //y center of clock
var diam;

var sDist;     //distance for seconds coordinate from center
var mDist;     //distance for minutes coordinate from center
var hDist;     //distance for hours coordinate from center

var secondX;   // x coordinate for seconds point
var secondY;   // y coordinate for seconds point
var minuteX;   // x coordinate for minutes point
var minuteY;   // y coordinate for minutes point
var hourX;     // x coordinate for hours point
var hourY;     // y coordinate for hours point

var r;         //r value for triangle color
var g;         //g value for triangle color
var b;         //b value for triangle color

var displayTime;   //boolean value for showing time text

function setup() {
  createCanvas(800, 800);
  angleMode(DEGREES);     //angleMode() set to degrees for ease of edit
  strokeJoin(MITER);
  
  centerX = width/2;
  centerY = height/2;
  diam = 600;
  
  r = random(0, 255);
  if(r < 70){
      b = random(150, 255);
      g = random(150, 255);
    }
    else{
      b = random(0, 255);
      g = random(0, 255);
    }
//  b = random(65, 255);
  
  displayTime = false;

}

function draw() {
  background(220);
  
  clockFace();       //draws a gray circular clock face
  triangleTime();    //a triangle made of coordintes for seconds, minutes, and hours
  update();          //update color everytime second() goes back to 0
  
}

function clockFace(){
  
  fill(80);
  noStroke();
  ellipse(centerX, centerY, diam, diam);
  
}

function triangleTime(){
  
  sDist = (diam/2) - 20;
  mDist = (diam/2) - 40;
  hDist = (diam/2) - 140;
  
  secondX = centerX + sDist * cos(second() * 6 - 90);
  secondY = centerY + sDist * sin(second() * 6 - 90);
  minuteX = centerX + mDist * cos(minute() * 6 - 90);
  minuteY = centerY + mDist * sin(minute() * 6 - 90);
  hourX = centerX + hDist * cos(hour() * 30 - 90);
  hourY = centerY + hDist * sin(hour() * 30 - 90);
  
  noStroke();
  fill(r, g, b, 100);
  triangle(secondX, secondY, minuteX, minuteY, hourX, hourY);
  
  if(displayTime == true){
    textSize(30);
    
    fill(r, g, b, 100);
    ellipse(secondX, secondY, 20, 20);
    fill(r, g, b);
    text("S: " + nf(second()), secondX + 20, secondY - 20);
    
    fill(r, g, b);
    ellipse(minuteX, minuteY, 20, 20);
    fill(r, g, b);
    text("M: " + nf(minute()), minuteX + 20, minuteY - 20);
    
    fill(r, g, b, 100);
    ellipse(hourX, hourY, 20, 20);
    fill(r, g, b);
    text("H: " + nf(hour()), hourX + 20, hourY - 20);
  }
}

function update(){
  
  frameRate(1);   //set so there isn't a frenzy of random colors all at once.
  
  if(second() == 59){
    r = random(0, 255);

    if(r < 70){
      b = random(150, 255);
      g = random(150, 255);
    }
    else{
      b = random(0, 255);
      g = random(0, 255);
    }

  }
  
}

function keyPressed(){        //press "T" to show or hide time text
  if(key == "T"){
    if(displayTime == true){
      displayTime = false;
    }
    else if(displayTime == false){
      displayTime = true;
    }
  }
}