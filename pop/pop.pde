Bubble b1;

void setup() {
  size(640, 360);
  b1 = new Bubble(50);
}

void draw() {
  background(0);

  // bubble management 
  b1.all();
}

void mousePressed() {
  // bubble explodes 
  if (b1.over()) {
    b1.fall();
  }
}

// ========================================================================================================

class Bubble {

  // constants: these are values that state can have (must be unique (0,1,2...))
  final int RISE    = 0;   // the word final makes them constants 
  final int FALL    = 1; 
  final int RESTART = 2; 
  // variable: current value of the state
  int state=RISE;  // not a state of the program, but the state of the bubble

  float tempSize;
  float w;
  float h;
  boolean move = true;
  float maxW;
  float maxH;
  float minW;
  float minH;
  float wspeed;
  float hspeed;
  float riseY = random(0.8, 3);
  float riseStart;
  float start = random(0, 640);
  float gravity = 0.3;
  float rad;

  Fallout[] fallouts; //might want to use a list (ArrayList)


  Bubble(float tempSize) { // <----------------- Bubble takes value from tab 1 and makes tempSize

    w = tempSize;
    h = tempSize;
    riseStart = tempSize + height;

    rad=tempSize/2;
    maxW = w*1.1+random(0, maxW/2);
    maxH = h*1.1+random(0, maxH/1);
    minW = w/1.1;
    minH = h/1.1;
    wspeed = w/100;
    hspeed = h/75;
  }

  void all() {
    // all (or script()) 

    stroke(255, 255);

    //print("Y ", mouseY);
    //print("  RS ", b1.riseStart);
    //print("  X ", mouseX);
    //println("  Start", b1.start);

    switch(state) {

    case RISE: 
      // rise
      show(); 
      move();
      top(); 
      break; 

    case FALL:
      //fall 
      riseY = riseY - gravity;
      riseStart = riseStart - riseY;
      // new small ball
      ellipse(start, riseStart, 
        3, 3); 
      //shrapnels 
      showExplosion();
      // lower screen border?
      if (riseStart>height+133) {  
        state = RESTART;
      }
      break; 

    case RESTART: 
      // restart 
      state = RISE; 
      riseY = random(0.8, 3); 
      riseStart = tempSize + height+100;
      start = random(w, width-w);
      break;

    default: 
      // What does this state do? When does it run?
      // It just picks up an error, when we forgot a state. 
      // Error 
      println("Error. Unknown state ");
      exit();    
      break; 
      //
    }//switch 
    //
  } // method 

  void show() {
    //noFill();
    //stroke(255);
    noFill();
    stroke(255, 255); 
    strokeWeight(1);
    ellipse (start, riseStart, 
      w, h);

    if (move) {
      w = w + wspeed;

      if ((w > maxW) || (w < minW)) { // Makes bubble wobble.
        wspeed = wspeed * -1;
      }

      if (move) {
        h = h + hspeed;
      }
      if ((h > maxH) || (h < minH)) { // Makes bubble wobble.
        hspeed = hspeed * -1;
      }
    }
  }

  void move() {
    riseStart = riseStart - riseY;
  }

  void top() {
    if (riseStart < tempSize - tempSize -100) { 
      state=RESTART;
    }
  }

  void fall() {
    state=FALL;
    explode();
  }

  boolean over() {
    // returns true or false; true when mouse is on balloon.
    return 
      (mouseX < start + w/2) && 
      (mouseX > start - w/2) &&
      (mouseY < riseStart + h/2) && 
      (mouseY > riseStart - h/2);
  }

  void showExplosion() {
    for (int i = 0; i < fallouts.length; i++) {
      fallouts[i].display();
      fallouts[i].move();
    }//for
  }

  void explode() {

    // init a new explosion 

    // final float RADIUS = rad;
    println(rad);

    //2PI would only shoot down, PI is up down, 
    //halfPi is in 4 dirs and so on
    //you can also just use some random number like 0.3256
    //but try keeping it within 0-2PI

    // full reset 
    fallouts = new Fallout[0];

    // How many shrapnels? Random : 
    final int upperBound = int(random(8, 44)); 

    // angle step accordingly 
    final float ANGLE_INCREMENT = TWO_PI/upperBound;

    // angle 
    float angle=0; 

    for (int i=0; i<=upperBound; i++) {

      // make a new bullet at CURRENT POSITION : start, riseStart
      Fallout newFallout = new Fallout(
        start, riseStart, // start pos 
        cos(angle)*random(.9, 3.8), sin(angle)*random(.9, 3.8) // speed of movement 
        );

      // append it to array
      fallouts = (Fallout[]) append(fallouts, newFallout);
      angle=i*ANGLE_INCREMENT;
    }//for
  }//method
  //
} //class

// ========================================================================================================

class Fallout { 

  // Bullet

  float posX, posY;
  float dirX, dirY;

  int fade = 255; 

  float sizeFallout=random(0.3, 2.8);

  color colorFallout = color(random(255), random(255), random(255)) ;  

  Fallout ( float x_, float y_, 
    float dx_, float dy_) {

    posX = x_;
    posY = y_;
    dirX = dx_;
    dirY = dy_;
  }

  void display() {
    fill(colorFallout, fade); 
    noStroke();
    ellipse(posX, posY, 
      sizeFallout, sizeFallout);
  }

  void move() {
    posX+=dirX;
    posY+=dirY;
    fade-=1; // fade could be at random speed
  }
  //
}//class
//