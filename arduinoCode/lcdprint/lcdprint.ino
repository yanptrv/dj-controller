#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int volume1, lastvolume1, volume2, lastvolume2;
bool volumechanged1 = false, volumechanged2 = false;
int seek1, lastseek1, seek2, lastseek2;
bool seekchanged1 = false, seekchanged2 = false;

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
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  volume1 = analogRead(A0);
  volume2 = analogRead(A1);
  seek1 = analogRead(A2);
  seek2 = analogRead(A3);
  volume1 = map(volume1, 0, 1023, 0, 100);
  volume2 = map(volume2, 0, 1023, 0, 100);
  seek1 = map(seek1, 0, 1023, 0, 100);
  seek2 = map(seek2, 0, 1023, 0, 100);
  lcd.setCursor(0, 0);
  lcd.print("Volume: ");
  lcd.setCursor(1, 0);
  lcd.print(volume1);
  lcd.setCursor(1, 1);
  lcd.print(volume2);
  ifchanged();
  if (volumechanged1 == true) {
    Serial.println("v1");
    Serial.println(volume1);
    volumechanged1 = false;
  }
  if (volumechanged2 == true) {
    Serial.println("v2");
    Serial.println(volume2);
    volumechanged2 = false;
  }
  if (seekchanged1 == true) {
    Serial.println("s1");
    Serial.println(seek1);
    seekchanged1 = false;
  }
  if (seekchanged2 == true) {
    Serial.println("s2");
    Serial.println(seek2);
    seekchanged2 = false;
  }
  
  delay(100);
  lcd.clear();

}
