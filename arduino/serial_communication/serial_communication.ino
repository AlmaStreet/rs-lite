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