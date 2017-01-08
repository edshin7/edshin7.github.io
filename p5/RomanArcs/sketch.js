// Assignment 4: Clock
// Edward Shin
// 09-28-2016


var backG;
var backA;

var clockX;
var clockY;
var clockRadius;

var secX;
var secY;
var minX;
var minY;
var hourX;
var hourY;

var secColor;
var minColor;
var hourColor;

var baseSpeed;

var secArc;
var minArc;
var hourArc;

var lastMin;
var lastHour;
var pulseTheta;
var rippleSize;
var rippleWeight;
var rippleAlph;


function setup() {
  createCanvas(800, 600);
  smooth();
  angleMode(DEGREES);
  
  backG = 20;
  backA = 150;
  
  clockX = width / 2;
  clockY = height / 2 + 10;
  clockRadius = 240;
  clockRadius2 = 100;
  
  secX = clockX + clockRadius2 * cos(90);
  secY = clockY + clockRadius2 * sin(90);
  minX = clockX + clockRadius * cos(330);
  minY = clockY + clockRadius * sin(330);
  hourX = clockX + clockRadius * cos(210);
  hourY = clockY + clockRadius * sin(210);
  
  secColor = [200, 200, 200];
  minColor = [50, 200, 100];
  hourColor = [50, 150, 220];
  
  baseSpeed = 0.5;
  
  secArc = new TimeArc(secX, secY, secColor, baseSpeed / 4);
  minArc = new TimeArc(minX, minY, minColor, baseSpeed / 2);
  hourArc = new TimeArc(hourX, hourY, hourColor, baseSpeed * 1.125);
  
  lastMin = minute();
  lastHour = hour();
  pulseTheta = 0;
  rippleSize = hourArc.radiusL;
  rippleWeight = 7;
  rippleAlph = 80;
}


function draw() {
  background(backG, backA);
  fill(backG, backA);
  noStroke();
  
  pulseMin();
  rippleHour();
  drawTimeArcs();
  playTimeArcs();
}


function drawTimeArcs(){
  secArc.draw(second());
  minArc.draw(minute());
  hourArc.draw(hour());
  
}


function playTimeArcs(){
  secArc.play();
  minArc.play();
  hourArc.play();
}


// pulse every minute
function pulseMin(){
  
  if(lastMin != minute() && lastHour == hour()){
    noFill();
    stroke(minArc.arcColor[0], minArc.arcColor[1], minArc.arcColor[2], 50);
    strokeWeight(7);
    var size = minArc.radiusL + ((minArc.radiusL / 2) * sin(pulseTheta));
    
    ellipse(minArc.x, minArc.y, size, size);
    
    pulseTheta += 4;
    
    if(pulseTheta >= 180){
      lastMin = minute();
      pulseTheta = 0;
    }
  }
}


// ripple every hour
function rippleHour(){
  if(lastHour != hour()){
    noFill();
    stroke(hourArc.arcColor[0], hourArc.arcColor[1], hourArc.arcColor[2], rippleAlph);
    strokeWeight(rippleWeight)
    ellipse(hourArc.x, hourArc.y, rippleSize, rippleSize);
    
    rippleSize += 5;
    rippleWeight -= 0.05;
    rippleAlph -= 0.3;
    
    if(rippleAlph <= -5){
      lastHour = hour();
      rippleSize = hourArc.radiusL;
      rippleWeight = 5;
      rippleAlph = 80;
    }
    
  }
}


// a set of Arcs that visulaize Roman Numerals (RN) as arcs/circles
var TimeArc = function TimeArc(x, y, timeColor, speed){
  this.x = x;
  this.y = y;
  this.arcColor = timeColor;
  this.subColor = [190, 0, 0, 170];
  
  this.outWeight = 3;
  this.weightI = 4;
  this.weightV = 5;
  this.weightX = 6;
  this.weightL = 7;
  
  this.radiusI = 70;
  this.radiusV = this.radiusI + 35;
  this.radiusX = this.radiusV + 55;
  this.radiusL = this.radiusX + 75;
  
  this.startI = 0;
  this.startV = 0;
  this.startX = 0;
  this.startL = 0;
  
  this.speedI = speed;
  this.speedV = speed * 1.5;
  this.speedX = speed * 2;
  this.speedL = speed * 2.5;
  
  this.gap = 60;  // degrees in which the arcs are separated
  
  this.draw = function(time){
    fill(this.arcColor[0], this.arcColor[1], this.arcColor[2], 30);
    strokeCap(ROUND);
    
    this.drawOutline();
    this.drawArcI(time);
    this.drawArcV(time);
    this.drawArcX(time);
    this.drawArcL(time);
  }
  
  this.play = function(){
    this.rotateArcs();
  }
  
  // draw outline for arc positions
  this.drawOutline = function(){
    stroke(200, 200, 200, 0.5);
    strokeWeight(this.outWeight);
    ellipse(this.x, this.y, this.radiusI, this.radiusI);
    ellipse(this.x, this.y, this.radiusV, this.radiusV);
    ellipse(this.x, this.y, this.radiusX, this.radiusX);
    ellipse(this.x, this.y, this.radiusL, this.radiusL);
  }
  
  // draw arc representing RN I
  this.drawArcI = function(time){
    stroke(this.arcColor[0], this.arcColor[1], this.arcColor[2]);
    strokeWeight(this.weightI);
    
    var numArcs = time % 5;
    
    if(numArcs === 4){
      stroke(this.subColor[0], this.subColor[1], this.subColor[2], this.subColor[3]);
      arc(this.x, this.y, this.radiusI, this.radiusI, this.startI, this.startI + 360 - this.gap);
    }
    
    else {
      var angle = (360 - numArcs * this.gap) / numArcs;
      var start = this.startI;
      var end = this.startI + angle;
      
      for(var i = 0; i < numArcs; i++){
        arc(this.x, this.y, this.radiusI, this.radiusI, start, end);
        
        start = end + this.gap;
        end = start + angle;
      }
    }
    
  }
  
  // draw arc representing RN V
  this.drawArcV = function(time){
    stroke(this.arcColor[0], this.arcColor[1], this.arcColor[2]);
    strokeWeight(this.weightV);
    
    if(time % 10 >= 4 && time % 10 < 9){
        
      arc(this.x, this.y, this.radiusV, this.radiusV, this.startV, this.startV + 360 - this.gap);
    }
  }
  
  // draw arc representing RN X
  this.drawArcX = function(time){
    stroke(this.arcColor[0], this.arcColor[1], this.arcColor[2]);
    strokeWeight(this.weightX);
    
    var numArcs = floor(time / 10);
    
    if(time == 39 || time == 49){
      numArcs = 4;
      if(time == 49){
        numArcs = 2;
      }
      
      var angle = (360 - numArcs * this.gap) / numArcs;
      var start = this.startX;
      var end = this.startX + angle;
      
      for(var i = 0; i < numArcs; i++){
        if(i == numArcs - 1 && time == 49){
          stroke(this.subColor[0], this.subColor[1], this.subColor[2], this.subColor[3])
        }
        arc(this.x, this.y, this.radiusX, this.radiusX, start, end);
        
        start = end + this.gap;
        end = start + angle;
      }
    }
    
    else if(time >= 40 && time <= 48){
      stroke(this.subColor[0], this.subColor[1], this.subColor[2], this.subColor[3]);
      arc(this.x, this.y, this.radiusX, this.radiusX, this.startX, this.startX + 360 - this.gap);
    }
    
    else if(time === 59){
      arc(this.x, this.y, this.radiusX, this.radiusX, this.startX, this.startX + 360 - this.gap);
    }
    
    else if(time < 39){
      if(time % 10 === 9){
        numArcs = ceil(time / 10);
      }
      
      var angle = (360 - numArcs * this.gap) / numArcs;
      var start = this.startX;
      var end = this.startX + angle;
      
      for(var i = 0; i < numArcs; i++){
        arc(this.x, this.y, this.radiusX, this.radiusX, start, end);
        
        start = end + this.gap;
        end = start + angle;
      }
    }
  }
  
  // draw arc representing RN L
  this.drawArcL = function(time){
    stroke(this.arcColor[0], this.arcColor[1], this.arcColor[2]);
    strokeWeight(this.weightL);
    
    if(time >= 40){
      arc(this.x, this.y, this.radiusL, this.radiusL, this.startL, this.startL + 360 - this.gap);
    }
  }
  
  // rotate the timeArcs
  this.rotateArcs = function(){
    this.startI += this.speedI;
    this.startV -= this.speedV;
    this.startX += this.speedX;
    this.startL -= this.speedL;
    
    //reset starts after a full revolution
    if(this.startI >= 360){
      this.startI = 0;
    }
    if(this.startV <= -360){
      this.startV = 0;
    }
    if(this.startX >= 360){
      this.startX = 0;
    }
    if(this.startL <= -360){
      this.startL = 0;
    }
  }
}




