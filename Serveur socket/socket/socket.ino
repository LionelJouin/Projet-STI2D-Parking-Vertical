#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
// byte mac[] = { 0x90, 0xA2, 0xDA, 0x0D, 0x05, 0xDD };
byte mac[] = { 0x90, 0xA2, 0xDA, 0x0D, 0x9E, 0x24 };
byte ip[] = { 172,18,41,50 };

char *TempPlace = "";
char *TempCode = "";
int aa = 0;

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
        //Serial.write(command);
        if (command=='Z') { // Z0100b87a09
          TempCode = "";
          aa = 0;
          while (a<10) {
            TempCode[a] = client.read();
            aa++;
          }
          Serial.print("Ajoute un code : ");
          Serial.print(TempCode);
        } else if (command=='z') { // z0100b87a09
          TempCode = "";
          aa = 0;
          while (a<10) {
            TempCode[a] = client.read();
            aa++;
          }
          Serial.print("Supprime un code");
          Serial.print(TempCode);
        } else if (command=='Y') { // Y12
          TempPlace = "";
          char TempVar;
          aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.print("Active la place : ");
          Serial.print(atoi(TempPlace));
        } else if (command=='y') { // y12
          TempPlace = "";
          char TempVar;
          aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.print("desactive la place : ");
          Serial.print(atoi(TempPlace));
        } else if (command=='X') { // X
          Serial.print("Active le parking");
        } else if (command=='x') { // x
          Serial.print("desactive le parking");
        } else if (command=='W') { // W0100b87a0912
          TempCode = "";
          aa = 0;
          while (a<10) {
            TempCode[a] = client.read();
            aa++;
          }
          TempPlace = "";
          char TempVar;
          aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.print("Associe le badge : ");
          Serial.print(TempCode);
          Serial.print(" à la place : ");
          Serial.print(atoi(TempPlace));
        } else if (command=='w') { // w0100b87a0912
          TempCode = "";
          aa = 0;
          while (a<10) {
            TempCode[a] = client.read();
            aa++;
          }
          TempPlace = "";
          char TempVar;
          aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.print("Enlever l'association du badge : ");
          Serial.print(TempCode);
          Serial.print(" à la place : ");
          Serial.print(atoi(TempPlace));
        } else if (command=='V') { // V0100b87a0912
          TempCode = "";
          aa = 0;
          while (a<10) {
            TempCode[a] = client.read();
            aa++;
          }
          TempPlace = "";
          char TempVar;
          aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.write("la place : ");
          Serial.print(TempCode);
          Serial.write("est prise par le badge : ");
          Serial.print(atoi(TempPlace));
        } else if (command=='v') { // v12
          TempPlace = "";
          char TempVar;
          aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.print("decharger la place : ");
          Serial.print(atoi(TempPlace));
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
