#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int volume, lastvolume;
bool volumechanged = false;

void ifchanged() {
  if (lastvolume != volume) {
    lastvolume = volume;
    volumechanged = true;
  }
}

void setup() {
  pinMode(A0, INPUT);
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  volume = analogRead(A0);
  lcd.setCursor(0, 0);
  volume = map(volume, 0, 1023, 0, 100);
  lcd.print(volume);
  ifchanged();
  if (volumechanged == true) {
    Serial.println('v');
    Serial.println(volume);
    volumechanged = false;
  }
  delay(100);
  lcd.clear();

}
