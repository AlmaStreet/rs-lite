#include <Servo.h>


Servo myServoMouse;
Servo myServoBoardZ;
Servo myServoBoardSpace;
Servo myServoBoardC;

long delayTime;
long delayBetweenKeys;
long secTime;
long minTime;
long clickTime;
int i = 0;
//String command;

unsigned long intervalMouse;
unsigned long previousMillisMouse = 0;

unsigned long intervalNumpad17;
unsigned long previousMillisNumpad17 = 0;

unsigned long intervalBoard;
unsigned long previousMillisBoard = 0;



void setup() {
  randomSeed(analogRead(0));
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

  myServoMouse.attach(5);
  myServoBoardZ.attach(9);
  myServoBoardSpace.attach(10);
  myServoBoardC.attach(13);

  myServoMouse.write(75);
  myServoBoardZ.write(100);
  myServoBoardSpace.write(67);
  myServoBoardC.write(142);

  myServoMouse.detach();
  myServoBoardZ.detach();
  myServoBoardSpace.detach();
  myServoBoardC.detach();

}

void loop() {

  if (Serial.available()) {
    char command = Serial.read();
    if (command == 'm') {
      myServoMouse.attach(5);

      for (i = 75; i > 55; i--) {
        myServoMouse.write(i); // Pressing Angle of Servo Arm
        delay(10);
      }
      clickTime = random(50, 100); // Mouse Press between 0.2-0.5s
      delay(clickTime);
      for (i = 55; i < 75; i++) {
        myServoMouse.write(i); // Resting Angle of Servo Arm
        delay(10);
      }

      myServoMouse.detach();
    }
    else if (command == 'c') { // ===== Attach (eat cake) =====
      myServoBoardC.attach(13);
      for (i = 160; i > 131; i--) {
        myServoBoardC.write(i); // Resting Angle of Servo Arm
        delay(8);
      }
      clickTime = random(150, 300); // Mouse Press between 0.2-0.5s
      delay(clickTime);
      for (i = 131; i < 160; i++) {
        myServoBoardC.write(i); // Pressing Angle of Servo Arm
        delay(8);
      }

      myServoBoardC.detach();
    }
    else if (command == 'z') {
      myServoBoardZ.attach(9);

      for (i = 86; i > 63; i--) {
        myServoBoardZ.write(i); // Resting Angle of Servo Arm
        delay(8);
      }
      clickTime = random(150, 300); // Mouse Press between 0.2-0.5s
      delay(clickTime);
      for (i = 63; i < 86; i++) {
        myServoBoardZ.write(i); // Pressing Angle of Servo Arm
        delay(8);
      }

      myServoBoardZ.detach();
    }
    else {
      Serial.write("Invalid input");
    }
  }

  // unsigned long currentMillis = millis(); // grab current time
  //// ==================== click ====================
  //// ==================== click ====================
  //// ==================== click ====================
  //if ((unsigned long)(currentMillis - previousMillisMouse) >= intervalMouse) {
  //
  //// ===== ATTACH Mouse =====
  //  myServoMouse.attach(5);
  //
  //// Mouse Activity (close area loot)
  //  for(i = 75; i > 43; i--) {
  //    myServoMouse.write(i); // Pressing Angle of Servo Arm
  //    delay(10);
  //  }
  //  clickTime = random(50, 100); // Mouse Press between 0.2-0.5s
  //  delay(clickTime);
  //
  //  for(i = 43; i < 75; i++) {
  //    myServoMouse.write(i); // Resting Angle of Servo Arm
  //    delay(10);
  //  }
  //  delayBetweenKeys = random(1000, 1600); // Board Press between 1-1.6s
  //  delay(delayBetweenKeys);
  //
  //// ===== DETACH Mouse =====
  //  myServoMouse.detach();
  //
  //
  //
  ////Wait between
  // intervalMouse = random(340000, 370000); // New Random Board Resting Time (Between 44s to 53s) REAL
  //// intervalMouse = random(2000, 5000); // New Random Board Resting Time (Between 5s to 7s) TEST
  //  previousMillisMouse = millis();
  // }
  //
  //
  //// ==================== Elven Shard (Z) ====================
  // if ((unsigned long)(currentMillis - previousMillisNumpad17) >= intervalNumpad17) {
  //
  //// ===== ATTACH Z =====
  //  myServoBoardZ.attach(9);
  //
  //  for(i = 100; i < 118; i++) {
  //    myServoBoardZ.write(i); // Pressing Angle of Servo Arm
  //    delay(10);
  //  }
  //  clickTime = random(200, 500); // Board Press between 0.2-0.9s
  //  delay(clickTime);
  //
  //  for(i = 118; i > 100; i--) {
  //    myServoBoardZ.write(i); // Resting Angle of Servo Arm
  //    delay(10);
  //  }
  //  delayBetweenKeys = random(900, 1600); // Board Press between 0.8-1.3s
  //  delay(delayBetweenKeys);
  //
  //// ===== DETACH Z =====
  //  myServoBoardZ.detach();
  //
  //
  //  intervalNumpad17 = random(90000, 160000); // New Random Board Resting (1m30s to 2m40s) REAL
  ////  intervalNumpad17 = random(1500, 2000); // New Random Board Resting (1.5s to 2s) TEST
  //  previousMillisNumpad17 = millis();
  // }
  //
  //
  //
  //
  //// ==================== Porter (1) ====================
  // if ((unsigned long)(currentMillis - previousMillisBoard) >= intervalBoard) {
  //
  //// ===== ATTACH One =====
  //  myServoBoardC.attach(13);
  //
  //// One (drink overload)
  //  for(i = 133; i < 155; i++) {
  //    myServoBoardC.write(i); // Pressing Angle of Servo Arm
  //    delay(8);
  //  }
  //  clickTime = random(150, 300); // Mouse Press between 0.2-0.5s
  //  delay(clickTime);
  //
  //  for(i = 155; i > 133; i--) {
  //    myServoBoardC.write(i); // Resting Angle of Servo Arm
  //    delay(8);
  //  }
  //  delayBetweenKeys = random(1000, 1600); // Board Press between 1-1.6s
  //  delay(delayBetweenKeys);
  //
  //// ===== DETACH One =====
  //  myServoBoardC.detach();
  //
  ////Wait between
  // intervalBoard = random(2000, 3200); // New Random Board Resting Time (Between D/A)
  ////  intervalBoard = random(30000, 60000); // New Random Board Resting Time (       1 1 11   Testing)
  //
  //  previousMillisBoard = millis();
  // }
  /* Test bed

  */






}
