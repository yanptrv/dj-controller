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
  seek1 = map(seek1, 0, 1023, 0, 100);
  seek2 = map(seek2, 0, 1023, 0, 100);
  lcd.setCursor(0, 0);
  lcd.print("Volume: ");
  lcd.setCursor(0, 1);
  lcd.print(volume1);
  ifchanged();
  if (volumechanged1 == true) {
    Serial.println('a');
    volumechanged1 = false;
    lcd.clear();
    delay(0.2);
    Serial.println(volume1);
  }
  if (volumechanged2 == true) {
    Serial.println('b');
    volumechanged2 = false;
    lcd.clear();
    delay(0.2);
    Serial.println(volume2);
  }
  if (seekchanged1 == true) {
    Serial.println('c');
    seekchanged1 = false;
    delay(0.2);
    Serial.println(seek1);
  }
  if (seekchanged2 == true) {
    Serial.println('d');
    seekchanged2 = false;
    delay(0.2);
    Serial.println(seek2);
  }

}
