//Edward Shin
//15-104 Section A
//edwardsh@andrew.cmu.edu
//Project 08


var Ripple = function Ripple(x, y, stro){       //ripple object

  this.x = x;           //x of ripple center
  this.y = y;           //y of ripple center
  this.size = 1;        //size of ripple
  this.gStep = 1;       //growing unit
  this.endSize = random(10, 25);       //ending size 
  noFill();

  //draw the ripple
  this.draw = function(){         
    stroke(stro);
    strokeWeight(2);
    ellipse(this.x, this.y, this.size, this.size);
  }

  //increase size of ripples until random ending size
  this.grow = function(){        
    if(this.size < this.endSize){
      this.size += this.gStep;
    }
  }

}

var ripples = [];        //array of ripples
var myFace;              //image of my face
var alph = 70;           //transparency of ripples
var maxNumRipples = 4000

function preload(){
	myFace = loadImage("http://i.imgur.com/rueiX2s.jpg");
}

function setup(){
  createCanvas(380, 520);
  imageMode(CENTER);
  myFace.loadPixels();

}

function draw(){
  fill(60, 70 , 100, 50);
  rect(0, 0, width, height);
  noFill();

  var x = mouseX + int(random(-40, 40));     //x of center of ripple
  var y = mouseY + int(random(-40, 40));     //y of center of ripple
  var col1 = myFace.get(x, y);                  //color value for myFace
  var r = red(col1);                            //r value of color col1
  var g = green(col1);                          //g value of color col1
  var b = blue(col1);                           //b value of color col1
  var col2 = color(r, g, b, alph);            //color with alpha for respective pixel
  
    setRipples(x, y, col2);
    playRipples();
  
}

function setRipples(x, y, stro){        //prepare ripple objects into array
  if(ripples.length <= maxNumRipples){
    ripples.push(new Ripple(x, y, stro));
  }

}

function playRipples(){           //draw and grow the ripples

  for(var r = 0; r < ripples.length; r++){
    ripples[r].draw();
    ripples[r].grow();
  }

}

function mousePressed(){
  ripples = []
}