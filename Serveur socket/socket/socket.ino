#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
// byte mac[] = { 0x90, 0xA2, 0xDA, 0x0D, 0x05, 0xDD };
byte mac[] = { 0x90, 0xA2, 0xDA, 0x0D, 0x9E, 0x24 };
byte ip[] = { 172,18,41,50 };

// Initialize the Ethernet server library
// with the IP address and port you want to use
// (port 80 is default for HTTP):
EthernetServer server(1337);

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }


  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
}


void loop() {
  // listen for incoming clients
  EthernetClient client = server.available();
  if (client) {
    Serial.println("new client");
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        //Serial.print( "gfhtgf" );
        //char c = client.read();
        //Serial.write(c);
        /*if (c=='Y') {
          char cs = client.read();
          char d = client.read();
          Serial.write(c);
          Serial.write(cs);
          if(d != (char)-1) {
            Serial.write(d);
          }
          }*/
          
        char command = client.read();
        if (command=='Z') {
          Serial.write("Ajoute un code");
        } else if (command=='z') {
          Serial.write("Supprime un code");
         } else if (command=='Y') {
          Serial.write("Active une place");
        } else if (command=='y') {
          Serial.write("desactive une place");
        } else if (command=='X') {
          Serial.write("Active le parking");
        } else if (command=='x') {
          Serial.write("desactive le parking");
        } else if (command=='W') {
          Serial.write("Associe un badge a une place");
        } else if (command=='w') {
          Serial.write("Enlever l'association d'un badge a une place");
        } else if (command=='V') {
          Serial.write("place prise");
        } else if (command=='v') {
          Serial.write("decharger la place");
        }
        Serial.print( "\n" );
      }
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
    Serial.println("client disconnected");
  }
}
