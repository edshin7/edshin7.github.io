//Edward Shin
//15-104 Section A
//edwardsh@andrew.cmu.edu
//Project 05

var centerX;   //x center of canvas
var centerY;   //y center of canvas
var x;         //x of astroid curve point
var y;         //y of astroid curve point
var numStars;  //number of stars (points) making curve
var alphaB;    //transparency/opacity of background

function setup() {
  
  createCanvas(800, 800);
  angleMode(DEGREES);      //set to degrees for ease of use
  background(30);
  
  centerX = width/2;
  centerY = height/2;
  numStars = 40;
  alphaB = 255;
  
}

function draw() {
  
  fill(30, alphaB);
  rect(0, 0, width, height);
  
  push();
  astroidCurve(10, 300, 100, 0 ,720);    //astroid curve #1
  pop();
  
  push();
  astroidCurve(200, 10, 200, 720 ,0);    //astroid curve #2
  pop();
  
}

function astroidCurve(sLeng, eLeng, radius, sAng, eAng){    //constructing astroid curve
  
  var ang = map(mouseX, 0, width, sAng ,eAng);       //angle for rotation
  
  
  translate(centerX + radius * cos(-ang), centerY + radius * sin(-ang));
  rotate(ang);
  
  
  for(var s = 1; s < numStars; s++){      //make the stars (points) along astroid curve
    
    var leng = map(mouseY, 0, height, sLeng, eLeng);     //distance of points from center
    var theta = map(s, 0, numStars, 0 ,360);             //angle of curve
    
    x = leng * pow(cos(theta), 3);          //equations for astroid curve
    y = leng * pow(sin(theta), 3);
    
    strokeWeight(5);      
    stroke(255);
    point(x, y);        //point of "star"
    
    noFill()
    strokeWeight(2);
    stroke(255, 50);
    ellipse(x, y, 20, 20);        //ring of "star"
    
  }
  
}

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