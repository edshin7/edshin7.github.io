/*
Edward Shin
15-104 Section A
edwardsh@andrew.cmu.edu
Capstone Project
12-10-2015
*/



var squares = [];     //array of squares representing keys
var ripples = [];     //array of ripples
var letters = [];     //array of letters

var numKeys = 26;
var spacing;   //spacing between squares
var x1;      //x start type 1
var x2;      //x start type 2
var x3;      //x start type 3
var y1;      //y start type 1
var y2;      //y start type 2
var y3;      //y start type 3

var y4;      //y start type 4
var y5;      //y start type 5
var y6;      //y start type 6

function setup() {
  createCanvas(800, 700);
  rectMode(CENTER);
  textAlign(CENTER);

  spacing = 75;
  x1 = 60;
  x2 = x1 + 10;
  x3 = x1 + 30;
  y1 = 150;
  y2 = y1 + spacing;
  y3 = y2 + spacing;

  y4 = 440;
  y5 = y4 + spacing;
  y6 = y5 + spacing; 

  setSquares();
}

function draw() {
  fill(0 , 10, 40, 20);
  rect(width/2, height/2, width, height);

  setRipples();
  drawRipples();
  drawSquares();
  drawLetters();
  checkSize();

}

function setSquares(){      //position squares
  for(var i = 0; i < numKeys; i++){
    
    var sq;

    if(i < 10){
      sq = new Square(x1 + (spacing * i), y1);
      squares.push(sq);
    }
    else if(i >= 10 && i < 19){
      sq = new Square(x2 + (spacing * (i - 10)), y2);
      squares.push(sq);
    }
    else{
      sq = new Square(x3 + (spacing * (i - 19)), y3);
      squares.push(sq);
    }
  }
}

function setRipples(){       //set random ripples
  var rChance = 0.005;
  var x = random(-5, width + 5);
  var y = random(-5, height + 5);
  var col = color(90, 110, 120, 15);
  
  if(random(0, 1) < rChance){
    ripples.push(new Ripple(x, y, col));
  }
}

function drawSquares(){      //draw the squares based on setSquares()
  for(var i = 0; i < squares.length; i++){
    squares[i].draw();
  }
}

function drawRipples(){      //draw ripples from setRipples or keyPressed()
  for(var i = 0; i < ripples.length; i++){
    ripples[i].draw();
    ripples[i].grow();
    if(ripples[i].size > ripples[i].endSize){
      ripples.splice(i ,1);
    }
  }
}
function drawLetters(){      //draw letters based on 
  for(var i = 0; i < letters.length; i++){
    letters[i].draw();
    letters[i].shrink();
    if(letters[i].size < letters[i].endSize){
      letters.splice(i, 1);
    }
  }
}

function checkSize(){      //check squares/letters size and grow/vanish if square is less than maxSize
  for(var i = 0; i < squares.length; i++){
    if(squares[i].size < squares[i].maxSize){
      squares[i].grow();
    }
  }
}

function keyPressed(){     //press a key to create ripple and affect square corresponding to key

  var len = 0;

	switch(key){
		case "A":
      letters.unshift(new Letter(squares[10].x, y5, squares[10].col, "A"));
			ripples.push(new Ripple(squares[10].x, squares[10].y, squares[10].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[10].shrink();
			break;

		case "B":
      letters.unshift(new Letter(squares[23].x, y6, squares[23].col, "B"));
			ripples.push(new Ripple(squares[23].x, squares[23].y, squares[23].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[23].shrink();
			break;

		case "C":
      letters.unshift(new Letter(squares[21].x, y6, squares[21].col, "C"));
      ripples.push(new Ripple(squares[21].x, squares[21].y, squares[21].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[21].shrink();
			break;

		case "D":
      letters.unshift(new Letter(squares[12].x, y5, squares[12].col, "D"));
      ripples.push(new Ripple(squares[12].x, squares[12].y, squares[12].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[12].shrink();
			break;

		case "E":
      letters.unshift(new Letter(squares[2].x, y4, squares[2].col, "E"));
      ripples.push(new Ripple(squares[2].x, squares[2].y, squares[2].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[2].shrink();
			break;

		case "F":
      letters.unshift(new Letter(squares[13].x, y5, squares[13].col, "F"));
      ripples.push(new Ripple(squares[13].x, squares[13].y, squares[13].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[13].shrink();
			break;

		case "G":
      letters.unshift(new Letter(squares[14].x, y5, squares[14].col, "G"));
      ripples.push(new Ripple(squares[14].x, squares[14].y, squares[14].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[14].shrink();
			break;

		case "H":
      letters.unshift(new Letter(squares[15].x, y5, squares[15].col, "H"));
      ripples.push(new Ripple(squares[15].x, squares[15].y, squares[15].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[15].shrink();
			break;

		case "I":
      letters.unshift(new Letter(squares[7].x, y4, squares[7].col, "I"));
      ripples.push(new Ripple(squares[7].x, squares[7].y, squares[7].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[7].shrink();
			break;

		case "J":
      letters.unshift(new Letter(squares[16].x, y5, squares[16].col, "J"));
      ripples.push(new Ripple(squares[16].x, squares[16].y, squares[16].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[16].shrink();
			break;

		case "K":
      letters.unshift(new Letter(squares[17].x, y5, squares[17].col, "K"));
      ripples.push(new Ripple(squares[17].x, squares[17].y, squares[17].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[17].shrink();
			break;

		case "L":
      letters.unshift(new Letter(squares[18].x, y5, squares[18].col, "L"));
      ripples.push(new Ripple(squares[18].x, squares[18].y, squares[18].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[18].shrink();
			break;

		case "M":
      letters.unshift(new Letter(squares[25].x, y6, squares[25].col, "M"));
      ripples.push(new Ripple(squares[25].x, squares[25].y, squares[25].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[25].shrink();
			break;

		case "N":
      letters.unshift(new Letter(squares[24].x, y6, squares[24].col, "N"));
      ripples.push(new Ripple(squares[24].x, squares[24].y, squares[24].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[24].shrink();
			break;

		case "O":
      letters.unshift(new Letter(squares[8].x, y4, squares[8].col, "O"));
      ripples.push(new Ripple(squares[8].x, squares[8].y, squares[8].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[8].shrink();
			break;

		case "P":
      letters.unshift(new Letter(squares[9].x, y4, squares[9].col, "P"));
      ripples.push(new Ripple(squares[9].x, squares[9].y, squares[9].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[9].shrink();
			break;

		case "Q":
      letters.unshift(new Letter(squares[0].x, y4, squares[0].col, "Q"));
      ripples.push(new Ripple(squares[0].x, squares[0].y, squares[0].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[0].shrink();
			break;

		case "R":
      letters.unshift(new Letter(squares[3].x, y4, squares[3].col, "R"));
      ripples.push(new Ripple(squares[3].x, squares[3].y, squares[3].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[3].shrink();
			break;

		case "S":
      letters.unshift(new Letter(squares[11].x, y5, squares[11].col, "S"));
      ripples.push(new Ripple(squares[11].x, squares[11].y, squares[11].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[11].shrink();
			break;

		case "T":
      letters.unshift(new Letter(squares[4].x, y4, squares[4].col, "T"));
      ripples.push(new Ripple(squares[4].x, squares[4].y, squares[4].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[4].shrink();
			break;

		case "U":
      letters.unshift(new Letter(squares[6].x, y4, squares[6].col, "U"));
      ripples.push(new Ripple(squares[6].x, squares[6].y, squares[6].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[6].shrink();
			break;

		case "V":
      letters.unshift(new Letter(squares[22].x, y6, squares[2].col, "V"));
      ripples.push(new Ripple(squares[22].x, squares[22].y, squares[22].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[22].shrink();
			break;

		case "W":
      letters.unshift(new Letter(squares[1].x, y4, squares[1].col, "W"));
      ripples.push(new Ripple(squares[1].x, squares[1].y, squares[1].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[1].shrink();
			break;

		case "X":
      letters.unshift(new Letter(squares[20].x, y6, squares[20].col, "X"));
      ripples.push(new Ripple(squares[20].x, squares[20].y, squares[20].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[20].shrink();
			break;

		case "Y":
      letters.unshift(new Letter(squares[5].x, y4, squares[5].col, "Y"));
      ripples.push(new Ripple(squares[5].x, squares[5].y, squares[5].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[5].shrink();
			break;

		case "Z":
      letters.unshift(new Letter(squares[19].x, y6, squares[19].col, "Z"));
      ripples.push(new Ripple(squares[19].x, squares[19].y, squares[19].col));
      ripples.unshift(new Ripple(letters[len].x, letters[len].y, letters[len].col));
      squares[19].shrink();
			break;

		case " ":     //randomizing square colors
      squares.splice(0, squares.length);
      setSquares();
      drawSquares();
			break;

		default:
			break;

	}
}

//--------------------------/Objects


var Square = function Square(x, y){     //keyboard squares
	this.x = x;   
	this.y = y;   
	this.size = 50;      
  this.maxSize = 50;   
  this.minSize = 10;   
	this.r = random(120, 255);      
  this.g = random(120, 255);      
  this.b = random(120, 255);      
  this.a = 45;                    
  this.col = color(this.r, this.g, this.b, this.a);    
  this.maxFactor = 0.4;                                  
  this.aFactor = 45 / this.maxSize;                    

  this.draw = function(){          //draw the square
  	fill(this.r, this.g, this.b, this.a);
  	noStroke();
  	rect(this.x, this.y, this.size, this.size);

  }

  this.grow = function(){         //grow the square
	 this.size += this.maxFactor;
   this.a += this.aFactor;
  }

	this.shrink = function(){       //shrink the square
		this.size = this.minSize;
    this.a = 0;
	}

}

var Ripple = function Ripple(x, y, c){     //ripples made randomly or by keyPressed()
  this.x = x;
  this.y = y;
  this.size = 0;
  this.endSize = int(random(100, 300));
  this.r = red(c);
  this.g = green(c);
  this.b = blue(c);
  this.a = 40;
  this.col = color(this.r, this.g, this.b, this.a);
  this.weight = random(3, 7);
  this.gFactor = random(2, 4);

  this.draw = function(){    //draw the ripple
    noFill();
    strokeWeight(this.weight);
    stroke(this.col);
    rect(this.x, this.y, this.size, this.size);
  }

  this.grow = function(){   //grow the ripple
    this.size += this.gFactor;
  }

}

var Letter = function Letter(x, y, c, l){     //the letters
  this.x = x;
  this.y = y;
  this.size = 30;
  this.endSize = 0;
  this.l = l;
  this.r = red(c);
  this.g = green(c);
  this.b = blue(c);
  this.a = 45;
  this.col = color(this.r, this.g, this.b, this.a);
  this.minFactor = -0.2;
  this.aFactor = 45 / this.maxSize;

  this.draw = function(){      //draw the letter
    fill(this.col);
    textSize(this.size);
    text(this.l, this.x, this.y);
  }

  this.show = function(){      //show the letter
    this.size = this.maxSize;
    this.a = 45;
  }

  this.shrink = function(){    //make the letter vanish
    this.size += this.minFactor;
    this.a += this.aFactor;
  }
}