#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
// byte mac[] = { 0x90, 0xA2, 0xDA, 0x0D, 0x05, 0xDD };
byte mac[] = { 0x90, 0xA2, 0xDA, 0x0D, 0x9E, 0x24 };
byte ip[] = { 172,18,41,50 };

//char *TempPlace = "";
//char *TempCode = "";
char TempPlace[2];
char TempCode[10];
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
          
        char command = client.read();
        //Serial.write(command);
        if (command=='Z') { // Z0100b87a09
          int aa = 0;
          while (aa<10) {
            TempCode[aa] = client.read();
            aa++;
          }
          Serial.print("Ajoute un code : ");
          Serial.print(TempCode);
          Serial.print( "\n" );
        } else if (command=='z') { // z0100b87a09
          int aa = 0; 
          while (aa<10) {
            TempCode[aa] = client.read();
            aa++;
          }
          Serial.print("Supprime un code : ");
          Serial.print(TempCode);
          Serial.print( "\n" );
        } else if (command=='Y') { // Y12
          free(TempPlace);
          char *TempPlace = "";
          memset(TempPlace, 0, sizeof(TempPlace));
          char TempVar;
          int aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.println("Active la place : ");
          Serial.println(TempPlace);
        } else if (command=='y') { // y12
          free(TempPlace);
          char *TempPlace = "";
          memset(TempPlace, 0, sizeof(TempPlace));
          char TempVar;
          int aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.println("desactive la place : ");
          Serial.println(TempPlace);
        } else if (command=='X') { // X
          Serial.println("Active le parking");
        } else if (command=='x') { // x
          Serial.println("desactive le parking");
        } else if (command=='W') { // W0100b87a0912
          free(TempCode);
          char *TempCode = "";
          int aa = 0;
          while (aa<10) {
            TempCode[aa] = client.read();
            aa++;
          }
          free(TempPlace);
          char *TempPlace = "";
          char TempVar;
          aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.println("Associe le badge : ");
          Serial.println(String(TempCode));
          Serial.println(" à la place : ");
          Serial.println(TempPlace);
        } else if (command=='w') { // w0100b87a0912
          free(TempCode);
          char *TempCode = "";
          int aa = 0;
          while (aa<10) {
            TempCode[aa] = client.read();
            aa++;
          }
          free(TempPlace);
          char *TempPlace = "";
          char TempVar;
          aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.println("Enlever l'association du badge : ");
          Serial.println(TempCode);
          Serial.println(" à la place : ");
          Serial.println(atoi(TempPlace));
        } else if (command=='V') { // V0100b87a0912
          free(TempCode);
          char *TempCode = "";
          int aa = 0;
          while (aa<10) {
            TempCode[aa] = client.read();
            aa++;
          }
          free(TempPlace);
          char *TempPlace = "";
          char TempVar;
          aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.println("la place : ");
          Serial.println(TempCode);
          Serial.println("est prise par le badge : ");
          Serial.println(TempPlace);
        } else if (command=='v') { // v12
          free(TempPlace);
          char *TempPlace = "";
          char TempVar;
          int aa = 0;
          TempPlace[0] = client.read();
          TempVar = client.read();
          if(TempVar != (char)-1) {
            TempPlace[1] = TempVar;
          }
          Serial.println("decharger la place : ");
          Serial.println(atoi(TempPlace));
        } else if (command=='r') { // r
          Serial.println("redemarrage");
        }
        Serial.println( "\n" );
      }
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
    Serial.println("client disconnected");
  }
}