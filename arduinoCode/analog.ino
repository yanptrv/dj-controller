#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int vol;
int volppc;
int lastvol = 0;

void setup() {
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  vol = analogRead(A0);
    lastvol = vol;
    volppc = map(vol, 0, 1023, 100, 0);
    lcd.setCursor(0,0);
    if (volppc == 99 || volppc == 9) {
      lcd.clear();
    }
    lcd.print(String("Volume: ") + int(volppc));
    Serial.println(volppc);
    delay(0.1);
}
