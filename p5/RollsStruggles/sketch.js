//Edward Shin
//15-104 Section A
//edwardsh@andrew.cmu.edu
//Project 07


//-----------------------------------------/ Objects

var Belt = function Belt(x, y){     //belt units of conveyer belt
  
  this.len = 40;                                //length of belt unit
  this.startX1 = x;                             //starting x of top belt
  this.endX1 = this.startX1 + this.len;         //ending x of top belt
  this.startX2 = width - x;                     //starting x of bottom belt
  this.endX2 = this.startX2 - this.len;         //ending x of bottom belt
  this.y1 = y;                                  //y of top belt
  this.y2 = this.y1 + 40;                       //y of bottom belt
  this.step = -2;                               //amount to move by
  
  this.draw = function(){        //draws the belt
    
    stroke(0);
    strokeWeight(3);
    line(this.startX1, this.y1, this.endX1, this.y1);      //line for top belt
    line(this.startX2, this.y2, this.endX2, this.y2);      //line for bottom belt

  };
  
  this.move = function(){                 //moving the belt left (top) and right (bottom)
    
    this.startX1 += this.step;
    this.endX1 += this.step;
    this.startX2 -= this.step;
    this.endX2 -= this.step;
    
  };
  
};

var Wheel = function Wheel(x, y){         //wheel/gear of conveyor belt
  this.x = x;                             //center x of wheel
  this.y = y;                             //center y of wheel
  this.size = 34;                         //size of wheel
  this.angleS1 = 0;                       //starting angle of first half of wheel
  this.angleE1 = this.angleS1 + 90;       //ending angle of first half of wheel
  this.angleS2 = this.angleS1 + 180;      //starting angle of second half of wheel
  this.angleE2 = this.angleE1 + 180;      //ending angle of second half of wheel
  this.speedR;                            //speed of rotation
  
  this.draw = function(){       //draws the wheel
    
    this.speedR = -2 * frameCount;      
    
    push();
    translate(this.x, this.y);
    rotate(this.speedR);
    
    fill(100);
    stroke(50);
    strokeWeight(2);
    arc(0, 0, this.size, this.size, this.angleS1, this.angleE1, PIE);    //first half of wheel
    arc(0, 0, this.size, this.size, this.angleS2, this.angleE2, PIE);    //second half of wheel
    
    noFill();
    stroke(0);
    strokeWeight(3);
    ellipse(0, 0, this.size, this.size);     //wheel frame
    pop();
    
    stroke(0, 100);
    line(this.x, this.y,this.x, height);     //rod holding up wheel
    
  };
  
};

var Ball = function Ball(x, y){      //ball (design based on pokeball from Pokemon)
  
  this.size1 = int(random(20, 80));      //random size of ball
  this.size2 = 0.3 * this.size1;         //center circle 30 percent size of ball size
  this.x = x;                            //center x
  this.y = y - (this.size1/2);           //center y
  this.angleS = 0;                       //starting anle of colored hemisphere
  this.angleE = 180;                     //ending angle of colored hemisphere
  this.r = random(0, 255);               //random red value
  this.g = random(0, 255);               //random blue value
  this.b = random(0, 255);               //random green value
  this.speed = random(1, 2);             //random speed
  this.speedR;                           //rotation speed
  
  this.draw = function(){           //draws ball
    
    this.speedR = frameCount * this.speed;
    
    push();
    translate(this.x, this.y);
    rotate(this.speedR);
    
    fill(255);
    stroke(0);
    strokeWeight(3);
    ellipse(0, 0, this.size1, this.size1);         //ball base
    
    fill(this.r, this.g, this.b);
    stroke(50);
    arc(0, 0, this.size1, this.size1, this.angleS, this.angleE, PIE);       //colored hemisphere
    
    fill(255);
    stroke(0);
    ellipse(0, 0, this.size2, this.size2);       //center circle
    
    pop();
    
  };
  
  this.move = function(){        //moves to the left by a random speed
    
    this.x += (-this.speed);
    
  };
  
};

//----------------------------------/  Global Variables

var wheels = [];
var nWheels = 5;
var belts = [];
var nBelts = 17;
var balls = [];

var beltFloor;           //y value for floor of the belt

//----------------------------------/ Setup(), draw(), and other functions

function setup(){
  
  createCanvas(800, 400);
  angleMode(DEGREES);
  
  beltFloor = (height/2) + 40;
  buildScene();

}

function draw(){
  background(150, 150, 180);
  
  updateScene();
  
}


function buildScene(){     //building the scene with the elements
  buildBelt();
  buildWheels();
}

function updateScene(){    //continuously updating to animate
  updateBelt();
  updateWheels();
  makeBall();
  updateBalls();
}

function buildBelt(){      //set the belt units
  
  var belt;
  
  for(var b = 0; b < nBelts; b++){
    
    var spot = 50 * b;
    
    belt = new Belt(spot, beltFloor);
    belts.push(belt);
  }
  
}

function updateBelt(){           //update belt units
  
  for(var b = 0; b < belts.length; b++){
    
    var startPoint = width;
    var endPoint = -10;
    
    belts[b].draw();
    belts[b].move();
    
    if(belts[b].endX1 < endPoint){       //remove when exiting the screen
      belts.splice(b, 1);
      belts.push(new Belt(startPoint, beltFloor));
    }
  }
}

function buildWheels(){        //setting the wheels
  
  var wheel;
  
  for(var w = 0; w < nWheels; w++){
    var x = 100 + (w * 150);
    var y = beltFloor +  20;
    
    wheel = new Wheel(x, y);
    wheels.push(wheel);
  }
}

function updateWheels(){      //update to the wheels
  
  for(var w = 0; w < wheels.length; w++){
    wheels[w].draw();
  }
}

function makeBall(){          //make a ball when the chance comes
  
  var ballChance = 0.007;
  var x = width/2;
  
  if(random(0, 1) < ballChance){
    balls.push(new Ball(width + 100, beltFloor));
  }
  
}

function updateBalls(){       //make the balls roll against the belt
  
  for(var bl = 0; bl < balls.length; bl++){
    
    var endPoint = -100;
    
    balls[bl].draw();
    balls[bl].move();
    
    if(balls[bl].x < endPoint - balls[bl].size){
      balls.splice(bl, 1);
    }
  }
}

