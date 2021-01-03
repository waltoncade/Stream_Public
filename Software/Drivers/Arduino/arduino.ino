int incomingByte = 0;
int light_one_green = 2;
int light_one_red = 3;
int light_two_green = 12;
int light_two_red = 13;
int usb_one = 8;
int usb_two = 9;
int usb_three = 10;
int usb_four = 11;
int shock_1 = 4;
int shock_2 = 5;
int hat_1 = 6;
int hat_2 = 7;
int count = 0;
int playerid = 1;
int char_index = 0;
int num_chars = 5;
char msg[5];


void setup() {
  Serial.begin(9600);
  pinMode(light_one_green, OUTPUT);
  pinMode(light_one_red, OUTPUT);
  pinMode(light_two_green, OUTPUT);
  pinMode(light_two_red, OUTPUT);
  pinMode(usb_one, OUTPUT);
  pinMode(usb_two, OUTPUT);
  pinMode(usb_three, OUTPUT);
  pinMode(usb_four, OUTPUT);
  pinMode(shock_1, OUTPUT);
  pinMode(shock_2, OUTPUT);
  pinMode(hat_1, OUTPUT);
  pinMode(hat_2, OUTPUT);
  digitalWrite(shock_1, HIGH);
  digitalWrite(shock_2, HIGH);
  digitalWrite(hat_1, HIGH);
  digitalWrite(hat_2, HIGH);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    msg[char_index] = incomingByte;
    if (incomingByte == 'r') {
      handler(msg);
      incomingByte = 0;
      char_index = -1;
    }
    char_index++;
    if (char_index >= num_chars) {
      char_index = num_chars - 1;
    }
  }
}

void handler(char msg[5]) {
  if (strcmp("BCr", msg)==0) {
    player_two();
    playerid = 2;
  }
  else if (strcmp("CCr", msg)==0) {
    player_one();
    playerid = 1;
  }
  else if (strcmp("TZr", msg)==0){
    shock(0);
  }
  else if (strcmp("CZr", msg)==0){
    shock(1);
  }
  else if (strcmp("BZr", msg)==0){
    shock(2);
  }
  else if (strcmp("PSr", msg)==0){
    shock(playerid);
  }
  else if (strcmp("TDr", msg)==0){
    beer(0);
  }
  else if (strcmp("CDr", msg)==0){
    beer(1);
  }
  else if (strcmp("BDr", msg)==0){
    beer(1);
  }
}

void player_two() {
  Serial.println("Player 2");
  digitalWrite(usb_three, HIGH);
  delay(50);
  digitalWrite(usb_four, HIGH); 
  delay(600);
  digitalWrite(light_one_green, HIGH);
  digitalWrite(light_one_red, LOW);
  digitalWrite(light_two_green, LOW);
  digitalWrite(light_two_red, HIGH);
  digitalWrite(usb_one, LOW);
  digitalWrite(usb_two, LOW);
}

void player_one() {
  Serial.println("Player 1");
  digitalWrite(usb_one, HIGH);
  delay(250);
  digitalWrite(usb_two, HIGH);
  delay(450);
  digitalWrite(light_one_green, LOW);
  digitalWrite(light_one_red, HIGH);
  digitalWrite(light_two_green, HIGH);
  digitalWrite(light_two_red, LOW);
  digitalWrite(usb_three, LOW);  
  digitalWrite(usb_four, LOW);
}

void shock(int who){
  if (who == 1){
    Serial.println("shock1");
    digitalWrite(shock_1, LOW);
    delay(3000);
    digitalWrite(shock_1, HIGH);
  }
  else if (who == 2) {
    Serial.println("shock2");
    digitalWrite(shock_2, LOW);
    delay(3000);
    digitalWrite(shock_2, HIGH);
  }
  else{
    Serial.println("shockboth");
    digitalWrite(shock_1, LOW);
    digitalWrite(shock_2, LOW);
    delay(3000);
    digitalWrite(shock_1, HIGH);
    digitalWrite(shock_2, HIGH);
  }
}

void beer(int who){
  if (who == 1){
    digitalWrite(hat_1, LOW);
    delay(3000);
    digitalWrite(hat_1, HIGH); 
  }
  else if (who == 2){
    digitalWrite(hat_2, LOW);
    delay(3000);
    digitalWrite(hat_2, HIGH); 
  }
  else{
    digitalWrite(hat_1, LOW);
    digitalWrite(hat_2, LOW);
    delay(3000);
    digitalWrite(hat_1, HIGH);
    digitalWrite(hat_2, HIGH); 
  }
}

/*void trans() {
  Serial.println("Player Transition");
  for (count = 0; count < 10; count++) {
    digitalWrite(light_one_red, LOW);
    digitalWrite(light_one_green, LOW);
    digitalWrite(light_two_red, LOW);
    digitalWrite(light_two_green, LOW);
    delay(100);
    digitalWrite(light_one_red, HIGH);
    digitalWrite(light_one_green, HIGH);
    digitalWrite(light_two_red, HIGH);
    digitalWrite(light_two_green, HIGH);
    delay(100);
  }
}*/
