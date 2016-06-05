// Edward Shin
// 15-104 Section A
// edwardsh@andrew.cmu.edu
// Project-02
 
var backColor = 180;
var hairAngle = 90;
var foreheadWidth = 300;
var foreheadHeight = 300;
var faceWidth = 250; 
var faceHeight = 300; 
var eyeSize = 50; 
var eyeHeight = eyeSize;
var eyeAngle = 0;
var mouthWidth = 50;
var mouthHeight = 50;
var mouthHeight2 = 20;
var mouthAngle = 0;
var choice = 1;
 
function setup(){
    createCanvas (480, 640); 
    noStroke();
    angleMode(DEGREES);
}
 
function draw(){
    background(backColor); 
    
    fill(0);
    arc(width/2, 250, 400, 400, -90, -90 + hairAngle);      //hair
    arc(width/2, 250, 400, 400, -90 - hairAngle, -90);
    
    fill(255);
    ellipse(width/2, 250, foreheadWidth, foreheadHeight);   //forehead
    ellipse(width/2, 350, faceWidth, faceHeight);           //cheek and jaw part
    
    noFill();
    stroke(0);
    strokeWeight(3);
    var eyeLX = width/2 - faceWidth * 0.25;
    var eyeRX = width/2 + faceWidth * 0.25;
    arc(eyeLX, height/2, eyeSize, eyeHeight, eyeAngle, eyeAngle + 180, CHORD);     //left eye
    arc(eyeRX, height/2, eyeSize, eyeHeight, -eyeAngle, -eyeAngle + 180, CHORD);   //right eye
    
    //Note: Depending on "eyeAngle's" number, the arcs could
    //be the whites of the eyes or eyebrows or an obscured 
    //intersection between them and the pupils
    
    
    strokeWeight(12);      
    point(eyeLX - 3, 325);         //pupils
    point(eyeRX + 3, 325);

    strokeWeight(3);
    if(choice == 1){
     arc(width/2, 400, mouthWidth, mouthHeight, mouthAngle, mouthAngle + 180);          //mouth (smile)
     arc(width/2, 400, mouthWidth, mouthHeight2, mouthAngle, mouthAngle - 180);
    }
    else if(choice == 2){
     arc(width/2, 400, mouthWidth, mouthHeight, mouthAngle - 180, mouthAngle);          //mouth (frown)
     arc(width/2, 400, mouthWidth, mouthHeight2, mouthAngle - 180, mouthAngle);
    }
    else if(choice == 3){
     arc(width/2, 400, mouthWidth, mouthHeight, mouthAngle - 180, mouthAngle);          //mouth (exclamation)
     arc(width/2, 400, mouthWidth, mouthHeight2, mouthAngle, mouthAngle + 180);
    }
    
}
 
function mousePressed(){
    // when the user clicks, these variables are reassigned
    // to random values within specified ranges. For example,
    // "faceWidth" gets a random value between 150 and 300. 
    
    backColor = random(75, 180);
    hairAngle  = random(5, 160); 
    foreheadwidth = random(200, 350);
    foreheadHeight = random(175, 350);
    faceWidth = random(150,  300); 
    faceHeight = random(200, 400); 
    eyeSize = random(40,  60); 
    eyeAngle = random(10, 180);
    eyeHeight = random(10, 40);
    mouthWidth = random(30, 70);
    mouthHeight = random(0, 70);
    mouthHeight2 = random(0, 70);
    choice = int(random(1,4));
    
}