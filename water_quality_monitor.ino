// ---------- Pin Definitions ----------
const int GREEN_LED = 18;
const int RED_LED   = 19;
const int BUZZER    = 21;

// Sensor pins
const int TURBIDITY_PIN = 34; 
const int COLOR_R_PIN = 32;   
const int COLOR_G_PIN = 33;   
const int COLOR_B_PIN = 35;   

// ---------- Threshold Values ----------
const int CLEAN_THRESHOLD     = 1200;
const int MODERATE_THRESHOLD  = 2000;

// ---------- Variables ----------
int turbidityValue = 0;
int rVal = 0;
int gVal = 0;
int bVal = 0;

void setup() {
  Serial.begin(115200); 
  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  delay(1000);
}

void loop() {
  turbidityValue = analogRead(TURBIDITY_PIN);
  
  // Map 0-4095 ADC to 0-255 RGB
  rVal = map(analogRead(COLOR_R_PIN), 0, 4095, 0, 255);
  gVal = map(analogRead(COLOR_G_PIN), 0, 4095, 0, 255);
  bVal = map(analogRead(COLOR_B_PIN), 0, 4095, 0, 255);

  if (turbidityValue < CLEAN_THRESHOLD) {
    digitalWrite(GREEN_LED, HIGH); digitalWrite(RED_LED, LOW); digitalWrite(BUZZER, LOW);
  } else if (turbidityValue < MODERATE_THRESHOLD) {
    digitalWrite(GREEN_LED, LOW); digitalWrite(RED_LED, HIGH); digitalWrite(BUZZER, LOW);
  } else {
    digitalWrite(GREEN_LED, LOW); digitalWrite(RED_LED, HIGH); digitalWrite(BUZZER, HIGH);
  }

  // JSON SERIAL OUTPUT
  Serial.print("{");
  Serial.print("\"turbidity\":"); Serial.print(turbidityValue);
  Serial.print(",\"r\":"); Serial.print(rVal);
  Serial.print(",\"g\":"); Serial.print(gVal);
  Serial.print(",\"b\":"); Serial.print(bVal);
  Serial.println("}");

  delay(2000);
}