#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int volume1, lastvolume1, volume2, lastvolume2;
bool volumechanged1 = false, volumechanged2 = false;
int seek1, lastseek1, seek2, lastseek2;
bool seekchanged1 = false, seekchanged2 = false;
int flag = 0, i = 0, play1Flag = 1, pause1Flag = 1, prev1Flag = 1, next1Flag = 1, stop1Flag = 1, play2Flag = 1, pause2Flag = 1, prev2Flag = 1, next2Flag = 1, stop2Flag = 1;

void ifchanged() {
  if (lastvolume1 != volume1) {
    lastvolume1 = volume1;
    volumechanged1 = true;
  }
  if (lastvolume2 != volume2) {
    lastvolume2 = volume2;
    volumechanged2 = true;
  }
  if (lastseek1 != seek1) {
    lastseek1 = seek1;
    seekchanged1 = true;
  }
  if (lastseek2 != seek2) {
    lastseek2 = seek2;
    seekchanged2 = true;
  }
}

void setup() {
  for (int z = 3; z <= 12; ++z) {
    pinMode(z, INPUT);
  }
//  pinMode(3, INPUT);
//  pinMode(4, INPUT);
//  pinMode(5, INPUT);
//  pinMode(6, INPUT);
//  pinMode(7, INPUT);
//  pinMode(8, INPUT);
//  pinMode(9, INPUT);
//  pinMode(10, INPUT);
//  pinMode(11, INPUT);
//  pinMode(12, INPUT);
  pinMode(A8, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  volume1 = analogRead(A8);
  volume2 = analogRead(A1);
  seek1 = analogRead(A2);
  seek2 = analogRead(A3);
  volume1 = map(volume1, 0, 1023, 100, 0);
  volume2 = map(volume2, 0, 1023, 0, 100);
  seek1 = map(seek1, 0, 1023, 100, 0);
  seek2 = map(seek2, 0, 1023, 100, 0);
  if (flag == 0) {;
    lcd.setCursor(0, 0);
    lcd.print("DJCON =)");
    lcd.setCursor(0, 1);
    lcd.print("Made by: Yan,Aon");
  }
  else if (flag == 1) {
    lcd.setCursor(0, 0);
    lcd.print("Volume 2: ");
    lcd.setCursor(0, 1);
    lcd.print(volume1);
  }
  else if (flag == 2) {
    lcd.setCursor(0, 0);
    lcd.print("Volume 1: ");
    lcd.setCursor(0, 1);
    lcd.print(volume2);
  }
  ifchanged();
  if (volumechanged1 == true) {
    Serial.println("vol1");
    volumechanged1 = false;
    delay(0.2);
    Serial.println(volume1);
    if (i) {
          flag = 1;
    }
    lcd.clear();
    i = 1;
  }
  if (volumechanged2 == true) {
    Serial.println("vol2");
    volumechanged2 = false;
    lcd.clear();
    delay(0.2);
    Serial.println(volume2);
    if (i) {
          flag = 2;
    }
    lcd.clear();
    i = 1;
  }
  if (seekchanged1 == true) {
    Serial.println("seek1");
    seekchanged1 = false;
    delay(0.2);
    Serial.println(seek1);
  }
  if (seekchanged2 == true) {
    Serial.println("seek2");
    seekchanged2 = false;
    delay(0.2);
    Serial.println(seek2);
  }
  
  if (digitalRead(12) != 0) {
    if(play1Flag){
      Serial.println("play1"); 
    }
    play1Flag = 0;
  } else if (digitalRead(12) == 0) {
    play1Flag = 1;
  }
  
  if (digitalRead(11) != 0) {
    if(pause1Flag){
      Serial.println("pause1"); 
    }
    pause1Flag = 0;
  } else if (digitalRead(11) == 0) {
    pause1Flag = 1;
  }

  if (digitalRead(10) != 0) {
    if(prev1Flag){
      Serial.println("prev1"); 
    }
    prev1Flag = 0;
  } else if (digitalRead(10) == 0) {
    prev1Flag = 1;
  }

  if (digitalRead(9) != 0) {
    if(next1Flag){
      Serial.println("next1"); 
    }
    next1Flag = 0;
  } else if (digitalRead(9) == 0) {
    next1Flag = 1;
  }
  
  if (digitalRead(8) != 0) {
    if(stop1Flag){
      Serial.println("stop1"); 
    }
    stop1Flag = 0;
  } else if (digitalRead(8) == 0) {
    stop1Flag = 1;
  }

  if (digitalRead(7) != 0) {
    if(play2Flag){
      Serial.println("play2"); 
    }
    play2Flag = 0;
  } else if (digitalRead(7) == 0) {
    play2Flag = 1;
  }
  
  if (digitalRead(6) != 0) {
    if(pause2Flag){
      Serial.println("pause2"); 
    }
    pause2Flag = 0;
  } else if (digitalRead(6) == 0) {
    pause2Flag = 1;
  }

  if (digitalRead(5) != 0) {
    if(prev2Flag){
      Serial.println("prev2"); 
    }
    prev2Flag = 0;
  } else if (digitalRead(5) == 0) {
    prev2Flag = 1;
  }

  if (digitalRead(4) != 0) {
    if(next2Flag){
      Serial.println("next2"); 
    }
    next2Flag = 0;
  } else if (digitalRead(4) == 0) {
    next2Flag = 1;
  }
  
  if (digitalRead(3) != 0) {
    if(stop2Flag){
      Serial.println("stop2"); 
    }
    stop2Flag = 0;
  } else if (digitalRead(3) == 0) {
    stop2Flag = 1;
  }
}
