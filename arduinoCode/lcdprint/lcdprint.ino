#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int volume, lastvolume;
bool volumechanged = false;
int seek, lastseek;
bool seekchanged = false;

void ifchanged() {
  if (lastvolume != volume) {
    lastvolume = volume;
    volumechanged = true;
  }
  if (lastseek != seek) {
    lastseek = seek;
    seekchanged = true;
  }
}

void setup() {
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  volume = analogRead(A0);
  seek = analogRead(A1);
  volume = map(volume, 0, 1023, 0, 100);
  seek = map(seek, 0, 1023, 0, 100);
  lcd.setCursor(0, 0);
  lcd.print("Volume: ");
  lcd.setCursor(1, 0);
  lcd.print(volume);
  ifchanged();
  if (volumechanged == true) {
    Serial.println('v');
    Serial.println(volume);
    volumechanged = false;
  }
  if (seekchanged == true) {
    Serial.println('s');
    Serial.println(seek);
    seekchanged = false;
  }
  
  delay(100);
  lcd.clear();

}
