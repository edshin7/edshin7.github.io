// Assignment 2: Order to Chaos
// Edward Shin
// 09-14-2016

var nodes;
var numNodes;
var numUsableNodes;
var minUsableNodes;
var maxUsableNodes;
var colorList;
var numColors;

var margin;
var backA;
var maxBackA;

function setup() {
  createCanvas(800, 600);
  smooth();
  
  nodes = [];  // vertices for the triangles
  numNodes = 23;
  numUsableNodes = 3;
  minUsableNodes = 3;
  maxUsableNodes = numNodes;
  colorList = []; // list of colors for the triangles
  numColors = floor(numNodes / 2);
  
  margin = 100; // margin set for mapping
  backA = 255; // alpha value for the background color
  maxBackA = 150; 
  
  createNodes();
  createColorList();
}


function draw() {
  updateBackA();
  background(40, backA);
  
  updateUsableNodes();
  playNodes();
  drawTriangles();
}


// create a list of colors at random RGB values
function createColorList(){
  for(var i = 0; i < numColors; i++){
    var rValue = random(100, 255);
    var gValue = random(100, 255);
    var bValue = random(100, 255);
    
    colorList.push([rValue, gValue, bValue]);
  }
}


// update color list with new RGB values
function updateColorList(){
  for(var i = 0; i < numColors; i++){
    var rValue = random(100, 255);
    var gValue = random(100, 255);
    var bValue = random(100, 255);
    
    colorList[i] = ([rValue, gValue, bValue]);
  }
}


// create nodes for setup
function createNodes(){
  for(var i = 0; i < numNodes; i++){
    nodes.push(new Node());
  }
}


// draw and play the nodes
function playNodes(){
  for(var i = 0; i < numUsableNodes; i++){
    nodes[i].draw();
    nodes[i].play();
  }
}


// update the background alpha based on mapped mouseY
function updateBackA(){
  backA = map(mouseY, margin, height - margin, maxBackA, 0);
}


// update number of nodes used for the triangles based on mapped mouseX
function updateUsableNodes(){
  // a constraint to prevent any errors when the mouse goes outside the window
  mouseX2 = constrain(mouseX, margin, width - margin);  
  numUsableNodes = floor(map(mouseX2, margin, width - margin, minUsableNodes, maxUsableNodes));
}


//draw triangles based on number of nodes available every 2 nodes
function drawTriangles(){
  colorIndex = 0;
  
  for(var i = 0; i < numUsableNodes - 2; i += 2){
    var x1 = nodes[i].x;
    var y1 = nodes[i].y;
    var x2 = nodes[i + 1].x;
    var y2 = nodes[i + 1].y;
    var x3 = nodes[i + 2].x;
    var y3 = nodes[i + 2].y;
    
    var r = colorList[colorIndex][0];
    var g = colorList[colorIndex][1];
    var b = colorList[colorIndex][2];
    
    noFill();
    noStroke();
    fill(r, g, b, 80);
    triangle(x1, y1, x2, y2, x3, y3);
    
    colorIndex++;
  }
}


function mousePressed(){
  updateColorList();
}


// objects


// object that serves as points for the triangles
function Node(){
  this.x = random(width);
  this.y = random(height);
  this.xStep = random(-3, 3);
  this.yStep = random(-3, 3);
  
  this.draw = function(){
    stroke(255, 100);
    strokeWeight(5);
    point(this.x, this.y);
  }
  
  this.play = function(){
    this.move();
    this.rebound();
  }
  
  this.move = function(){
    this.x += this.xStep;
    this.y -= this.yStep;
  }
  
  this.rebound = function(){
    if(this.x < 0 || this.x > width){
      this.xStep *= -1;
    }
    if(this.y < 0 || this.y > height){
      this.yStep *= -1;
    }
  }
}






