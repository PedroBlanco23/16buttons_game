const byte rowsPins[] = {5,4,3,2};
const byte columnsPins[]= {6,7,8,9};


const int columns = 4;
const int rows = 4;



void setup() {
  Serial.begin(9600);
  for (int i = 0; i < columns; i++) {
    pinMode(columnsPins[i], INPUT_PULLUP);
  }

  for (int i = 0; i < rows; i++) {
    pinMode(rowsPins[i], OUTPUT);
    digitalWrite(rowsPins[i], HIGH);
  }
  

}

void loop() {
  for(int i = 0; i<rows; i++) {
    digitalWrite(rowsPins[i], LOW);
    for(int j = 0; j<columns; j++) {
      if(digitalRead(columnsPins[j]) == LOW) {
        Serial.print(i+1);
        Serial.print(" ");
        Serial.println(j+1);
      }
    }
 
    digitalWrite(rowsPins[i], HIGH);
    delay(50);
  } 

}
