#include <SPI.h>
#include <Ethernet.h>
 
/* Détails technique de la connexion ethernet */
byte mac[] = { 0x90, 0xA2, 0xDA, 0x0D, 0x05, 0xDD };
byte ip[] = { 172,18,41, 100 }; // 172.18.41.100
byte gateway[] = { 172,18,1, 1 };

int a = 10;
int type_recv = 1;
char recv;

char *code[] = { "0100B87A09" };
int code_valide = 1;
//char *code_acceptes[] = { "0100B87A09", "0000c2f7ee" };
int nb_places = 14;
char *places_occupees[] = { "10000000000000" };
int place_car = 1;

// Attachement d'un objet "server" sur le port 1337
EthernetServer server(1337);
 
void setup()
{
  // Configuration de la ethernet shield et du server
  Ethernet.begin(mac, ip, gateway);
  server.begin();
 
  // Mise en sortie de la broche avec notre led (par défaut éteinte)
  pinMode(9, OUTPUT);
  digitalWrite(9, LOW);
  
  Serial.begin(9600);
}
 
void loop()
{
  // Attente de la connexion d'un client
  EthernetClient client = server.available();
  if (client && client.connected()) {
 
    // si le client nous envoie quelque chose
    if (client.available() > 0) {
 
      // On regarde ce que le client nous demande
      /*switch(client.read()){
      case 'A': // allumer la led
        Serial.print("A\n"); 
        break;
      case 'a': // éteindre la led
        Serial.print("a\n"); 
        break;
      }*/
      /*
      if (add == 1) {
        while (a<10) {
          code[a] = char(client.read());
          a++;
          if (a==10) { Serial.print(code);add=1; }
        }
      } else if (del == 1) {
      }
      */
      
      recv = char(client.read());
      
      if (type_recv == 1) {
        if (recv=='Z') {        // Ajout d'un code accepte (codes_acceptes)
          //type_recv = 0;
        } else if (recv=='z') { // supprime un code accepte (codes_acceptes)
          //type_recv = 0;
        } else if (recv=='Y') { // Active une place de parking (places_actives)
          //type_recv = 0;
        } else if (recv=='y') { // desactive une place de parking (places_actives)
          //type_recv = 0;
        } else if (recv=='X') { // active le parking (etat_parking)
          //type_recv = 0;
        } else if (recv=='x') { // desactive le parking (etat_parking)
          //type_recv = 0;
        } else if (recv=='W') { // Associer un badge a une place (places_codes)
          //type_recv = 0;
        } else if (recv=='w') { // Enlever l'association d'un badge a une place (places_codes)
          //type_recv = 0;
        } else if (recv=='V') { // test envoie cote arduino | reception cote 
          //char *code_valide[] = { "0100b87a09", "0000c2f7ee" };
          /*
          char *code[] = { "0100B87A09" };
          int code_valide = 1;
          int nb_places = 14;
          char *places_occupees[] = { "10000000000000" };
          int place_car = 1;
          */
          //client.print(code_valide[1]);
          client.print(code[0]);
          delay(2);  
          client.print(code_valide);
          delay(2);  
          client.print(nb_places);
          delay(2);  
          client.print(places_occupees[0]);
          delay(2);  
          client.print(place_car);
        }
      }
      
      
      //Serial.print( recv );
      //Serial.print( "\n" );
    }
  }
}

