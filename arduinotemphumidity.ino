#include <DHT.h>

#define DHTPIN 2          // Pin to which DHT11 is connected
#define DHTTYPE DHT11     // Defining the type of sensor

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600);  // Initialize serial port
    dht.begin();         // Initialize sensor
}

void loop() {
    if (Serial.available()) { // Check if data is available on the serial port
        String command = Serial.readStringUntil('\n'); // Read command until newline
        if (command == "GET_DATA") { // If the command is received
            float h = dht.readHumidity();    // Read humidity
            float t = dht.readTemperature(); // Read temperature

            // Check if the data was received correctly
            if (isnan(h) || isnan(t)) {
                Serial.println("Failed to read data from sensor");
            } else {
                Serial.print("Temperature: ");
                Serial.print(t);
                Serial.print(" °C, Humidity: ");
                Serial.print(h);
                Serial.println(" %");
            }
        }
    }
}
