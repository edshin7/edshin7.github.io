//Edward Shin

// Dancing Stars II

// Started 07-06-2016


var centerX;   //x center of canvas
var centerY;   //y center of canvas
var x;         //x of astroid curve point
var y;         //y of astroid curve point
var numStars;  //number of stars (points) making curve
var alphaB;    //transparency/opacity of background
var rotAngle;  // new angle for rotation of astroids
var angleStep; // amount astroid should rotate by

var numBackStars; // stars in the background
var backStars;

var userRad;  // radius of user ring
var userTrans; // user ring transparency
var userWeight; // user line weight

function setup() {
  createCanvas(1420, 720);
  angleMode(DEGREES);      //set to degrees for ease of use
  noCursor();
  background(10);
  
  centerX = mouseX;
  centerY = mouseY;
  numStars = 20;
  alphaB = 255;
  rotAngle = 0;
  angleStep = 2;
  
  numBackStars = 100;
  backStars = [];
  
  userRad = 25;
  userTrans = 40;
  userWeight = 3;
  
  setBackStars();
  
}

function draw() {
  
  fill(0, alphaB);
  rect(0, 0, width, height);
  drawBackStars();
  drawUser();
  
  updateCenter();
  updateAngle();
  
  astroidCurve(30, 150, 175, 0, 360);    //astroid curve #1
  astroidCurve(70, 20, 75, 270, -90);    //astroid curve #2
  astroidCurve(5, 40, 225, -225, 315);   //astroid curve #3
  astroidCurve(50, 90, 30, 45, 765);    //astroid curve #4
  astroidCurve(90, 180, 100, -90, 630);   //astroid curve #5
  
}


// set random positions for the background stars
function setBackStars(){
  for(var i = 0; i < numBackStars; i++){
    var x = random(1, width);
    var y = random(1, height);
    
    backStars.push([x, y]);
  }
}


// draw background stars and make them twinkle
function drawBackStars(){
  for(var i = 0; i < backStars.length; i++){
    var x = backStars[i][0];
    var y = backStars[i][1];
    
    // strokeWeight set randomly constantly for twinkling effect
    var lnWeight = random(1, 3);
    
    stroke(255);
    strokeWeight(lnWeight);
    point(x, y);
  }
}


// using a transparent ring to mark the user's position
// instead of a cursor for aesthetics
function drawUser(){
  stroke(255, userTrans);
  strokeWeight(userWeight);
  ellipse(mouseX, mouseY, userRad, userRad);
}


// draw astroid curve of stars to create a "constellation"
// formula:
// x = a * cos(theta)^3
// y = a * sin(theta)^3
function astroidCurve(sLeng, eLeng, radius, sAng, eAng){    //constructing astroid curve
  push();
  
  var ang = map(mouseX, 0, width, sAng ,eAng);       //angle for orbiting cursor position
  
  
  translate(centerX + radius * cos(ang), centerY + radius * sin(ang));
  rotate(rotAngle);
  
  
  for(var s = 0; s < numStars; s++){      //make the stars (points) along astroid curve
    
    var leng = map(mouseY, 0, height, sLeng, eLeng);     //distance of points from center
    // var leng = 150;
    var theta = map(s, 0, numStars, 0 ,360);             //angle of curve
    
    var x = leng * pow(cos(theta), 3);          //equations for astroid curve
    var y = leng * pow(sin(theta), 3);
    
    strokeWeight(5);      
    stroke(255);
    point(x, y);        //point of "star"
    
    noFill()
    strokeWeight(2);
    stroke(255, 50);
    ellipse(x, y, 20, 20);        //ring of "star"
    
  }
  
  pop();
}


// center is updated in a way that would allow 
// the astroids to follow with a more natural flow
function updateCenter(){
  var diffX = mouseX - centerX;
  var diffY = mouseY - centerY;
  var distFactor = 0.0125;
  
  // covering x-coordinate
  if(round(abs(diffX)) > 0){
    centerX += diffX * distFactor;
  }
  
  // covering y-coordinate
  if(round(abs(diffY)) > 0){
      centerY += diffY * distFactor;
  }
  
}


// update angles that rotate the astroids
function updateAngle(){
  rotAngle += angleStep;
  
  if(rotAngle == 360){
    rotAngle = 0;
  }
}


// controlling background transparency
function keyPressed(){
  
  //press one of three keys to experience the 
  //astroid curves differently
  
  if(key == "1"){     //press "1" to set backround rect fully opaque
    alphaB = 255;
  }
  if(key == "2"){     //press "2" to set background rect to partially transparent
    alphaB = 30;
  }
  if(key == "3"){     //press "3" to set background rect to fully transparent
    alphaB = 0;
  }
}




