void setup() {
  pinMode(13, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop() {
  digitalWrite(3, HIGH);   
  delay(1200);     
  digitalWrite(13,HIGH);   
  delay(200);
  digitalWrite(13, LOW);
  delay(200);
  digitalWrite(13,HIGH);   
  delay(200);
  digitalWrite(13, LOW);
  delay(200);
   digitalWrite(13,HIGH);   
  delay(200);
  digitalWrite(13, LOW);
  delay(200);
  digitalWrite(13,HIGH);   
  delay(200);
  digitalWrite(13, LOW);
  delay(200);
  digitalWrite(3, LOW);
  delay(500);
}
         


