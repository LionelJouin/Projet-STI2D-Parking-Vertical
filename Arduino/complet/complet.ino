#include <SPI.h>
#include <Ethernet.h>

#define NBCodes 30
#define DelaiEnvoie 52
#define PinCommande 8
#define PinLecteur 2
#define PinReset 5

int PlacesActives[15]={1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}; // 1: active | 0: non active
int PlacesDispos[15]={1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};  // 1: disponible | 0: non disponible
int PlacesPredef[15]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};  // 1: predefinie | 0: non predefinie
char PlacesCodes[15][11]={"0000000000","0000000000","0000000000","0000000000","0000000000","0000000000","0000000000","0000000000","0000000000","0000000000","0000000000","0000000000","0000000000","0000000000","0000000000"}; // code attribuer a chaques places | 0000000000: aucun code
int PlaceDuCode_PlacesCodes = 1000;

int PlacesParking[15]={31,41,51,33,34,35,43,32,54,53,52,44,45,55,42};

char CodeAutoriser[NBCodes][11];
int NombreCodes = 0;
int PlaceDuCode_CodeAutoriser = 1000;

int  val = 0;                               // définir la variable val
char code[11];                              // code lu sur 10 octets
int badge = 0;                              // définir la variable badge
int buzzer = 9;                             // buzzer port 9
int freq = 1800;                            // définir une fréquence égale à 1800Hz

byte mac[] = { 0x90, 0xA2, 0xDA, 0x0D, 0x9E, 0x24 };
byte ip[] = { 172,18,41,50 };
char TempPlace[3];
char TempCode[11];
int aa = 0;
int badgedetecte = 0;
int EtatConfig = 0;
EthernetServer server(1337);

char TempCodeSending[11];
char TempPlaceSending[3];

void setup() {
  Serial.begin(9600);
  pinMode(PinCommande, OUTPUT);
  digitalWrite(PinCommande, HIGH);
  
  Serial1.begin(2400);                    // Connexion à 2400 bauds 
  pinMode(PinLecteur,OUTPUT);             // Broche numérique 2 en mode sortie pour la connecter au lecteur
  digitalWrite(PinLecteur, LOW);          // NL 0 > lecteur prêt à lire
  pinMode(buzzer, OUTPUT);                // active le buzzer
  
  Serial.println("Gestion");
  Serial1.println("Lecteur Badge");
  
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
 
}


void loop() {
  
  if(Serial1.available() > 0) {         // Si il y a des données dans le lecteur         
    if((val = Serial1.read()) == 10) {  // Lire les données, si il y a déja un code >
      badge = 0;                        // > le remettre à 0
      while(badge<10) {                 // Tant que le code est inférieur à 10 octects           
        if( Serial1.available() > 0) {  // Si il y a des données à lire
          val = Serial1.read();         // on lit ces données et on les stock dans VAL
          code[badge] = val;            // écrire dans la variable code, la valeur des 10 octets        
          badge++;                      // incremente badge afin d'obtenir 10 octets 
        } 
      }
      code[11] = '\0'; 
      if(badge == 10) {                     // Une fois qu'on a lu les 10 octects           
        Serial1.print("Code d'acces : ");   // ecrire : code d'acces dans le moniteur
        Serial1.println(code);              // ecrire a la suite le code du badge
        digitalWrite(PinLecteur, HIGH);     // Désactive le lecteur de badge
        CodeDetecte(code);
        digitalWrite(PinLecteur, LOW);      // lecteur de nouveau prêt à lire
      } 
      badge = 0;                            // remettre le badge à 0
    } 
  }
  
  
  EthernetClient client = server.available();
  if (client) {
    /*if (EtatConfig==0) {
      EthernetConfig(0);
      EtatConfig = 1;
    }*/
    if (client.connected()) {
      if (client.available()) {
        char command = client.read(); // lit la commande
        EthernetRecv(client, command); // execute la commande
      }
    }
  }
  
}


/*
---------------------------------------------------------------------------
GESTION CODES AUTORISE
---------------------------------------------------------------------------
*/
void AjouteCodeAutorise(char code[10]) { // ajoute un code au tableau CodeAutoriser
  if (VerifieCodeAutorise(code)==1000) {
    for(int a = 0;a<10;a++) {
      CodeAutoriser[NombreCodes][a] = code[a];
    }
    NombreCodes++;
    /*Serial.print("\nLe code : ");
    Serial.print(code);
    Serial.print(" a ete ajoute");*/
  }
}

void SupprimeCodeAutorise(char code[10]) { // supprime un code du tableau CodeAutoriser et remet en forme
  if (VerifieCodeAutorise(code)!=1000) {
    for(int a = VerifieCodeAutorise(code);a<NombreCodes;a++) {   
      for(int b = 0;b<10;b++) {
        CodeAutoriser[a][b] = code[b];
      }
    }
    for(int a = 0;a<10;a++) {
      CodeAutoriser[NombreCodes][a] = '\0';
    }
    NombreCodes--;
    /*Serial.print("\nLe code : ");
    Serial.print(code);
    Serial.print(" a ete supprime");*/
  }
}

int VerifieCodeAutorise(char code[10]) { // verifie si code existe et retourne son emplacement dans le tableau CodeAutoriser
  PlaceDuCode_CodeAutoriser = 1000;
  for(int a = 0;a<NombreCodes;a++) {
    if (strcmp(CodeAutoriser[a], code)==0) {
      PlaceDuCode_CodeAutoriser = a;
    }
  }
  return PlaceDuCode_CodeAutoriser;
}

/*
---------------------------------------------------------------------------
GESTION PARKING
---------------------------------------------------------------------------
*/
void CodeDetecte(char code[10]) {
  if (VerifieCodeAutorise(code)!=1000) {
    if (VerifieCodeParking(code)!=1000) { // voiture sortante ou place predef
      if (PlacesPredef[VerifieCodeParking(code)]==1) { // place predef
        if (PlacesDispos[VerifieCodeParking(code)]==1) { // voiture place predef entrante
          PlacesDispos[VerifieCodeParking(code)] = 0;
          EnvoieCommande(VerifieCodeParking(code));
          bip(1);
          EthernetClient client = server.available();
          TempCodeSending = strcat("U", code); 
          TempPlaceSending = strcat("S", VerifieCodeParking(code)); 
          if (client) {
            if (client.connected()) {
              if (client.available()) {
                EthernetSend(client, TempCodeSending);
                delay(50);
                EthernetSend(client, TempPlaceSending);
                delay(50);
                EthernetSend(client, "s1");
                delay(50);
                EthernetSend(client, "u1");
              }
            }
          }
          // fin
        } else { // voiture place predef sortante
          PlacesDispos[VerifieCodeParking(code)] = 1;
          bip(1);
          EthernetClient client = server.available();
          TempCodeSending = strcat("U", code); 
          TempPlaceSending = strcat("S", VerifieCodeParking(code)); 
          if (client) {
            if (client.connected()) {
              if (client.available()) {
                EnvoieCommande(VerifieCodeParking(code));
                EthernetSend(client, TempCodeSending);
                delay(50);
                EthernetSend(client, TempPlaceSending);
                delay(50);
                EthernetSend(client, "s0");
                delay(50);
                EthernetSend(client, "u1");
              }
            }
          }
          // fin
        }
      } else { // voiture sortante 
        PlacesDispos[VerifieCodeParking(code)] = 1;
        EnvoieCommande(VerifieCodeParking(code));
        SupprimeCodeParking(VerifieCodeParking(code));
        bip(1);
        EthernetClient client = server.available();
        TempCodeSending = strcat("U", code); 
        TempPlaceSending = strcat("S", VerifieCodeParking(code)); 
        if (client) {
          if (client.connected()) {
            if (client.available()) {
              EthernetSend(client, TempCodeSending);
              delay(50);
              EthernetSend(client, TempPlaceSending);
              delay(50);
              EthernetSend(client, "s0");
              delay(50);
              EthernetSend(client, "u1");
            }
          }
        }
        TempCodeSending[11] = []; 
        TempPlaceSending[3] = []; 
        // fin
      }
    } else { // voiture entrante
      for(int a = 0;a<15;a++) { // cherche une place
        if(PlacesPredef[a]==0 && PlacesDispos[a]==1 && PlacesActives[a]==1) { // place trouvee
          EnvoieCommande(a);
          PlacesDispos[a] = 0;
          AjouteCodeParking(code, a);
          bip(1);
          a = 15;
          EthernetClient client = server.available();
          TempCodeSending = strcat("U", code); 
          TempPlaceSending = strcat("S", VerifieCodeParking(code)); 
          if (client) {
            if (client.connected()) {
              if (client.available()) {
                //EthernetSend(client, String("U"+String(code)));
                EthernetSend(client, TempCodeSending);
                delay(50);
                EthernetSend(client, TempPlaceSending);
                delay(50);
                EthernetSend(client, "s1");
                delay(50);
                EthernetSend(client, "u1");
              }
            }
          }
          TempCodeSending[11] = []; 
          TempPlaceSending[3] = []; 
          // fin
        }
      }
    }
  } else { // code non valide
    bip(2);
    EthernetClient client = server.available();
    TempCodeSending = strcat("U", code); 
    if (client) {
      if (client.connected()) {
        if (client.available()) {
          EthernetSend(client, TempCodeSending);
          delay(50);
          EthernetSend(client, "u0");
        }
      }
    }
    // fin
  }
}

void EnvoieCommande(int place) {
  Serial.print("\nEnvoie de : ");
  Serial.print(PlacesParking[place]);
  Serial.print(" impulsions");
  for(int a = 0;a<PlacesParking[place];a++) {
    delay(DelaiEnvoie);
    digitalWrite(PinCommande, LOW);
    delay(DelaiEnvoie);
    digitalWrite(PinCommande, HIGH);
  }
}

void AjouteCodeParking(char code[10], int place) { // ajoute un code au tableau PlacesCodes
  for(int a = 0;a<10;a++) {
    PlacesCodes[place][a] = code[a];
  }
}

void SupprimeCodeParking(int place) { // supprime un code du tableau PlacesCodes
  for(int a = 0;a<10;a++) {
    PlacesCodes[place][a] = '0';
  }
}

int VerifieCodeParking(char code[10]) { // verifie si code existe et retourne son emplacement dans le tableau PlacesCodes
  PlaceDuCode_PlacesCodes = 1000;
  for(int a = 0;a<15;a++) {
    if (strcmp(PlacesCodes[a], code)==0) {
      PlaceDuCode_PlacesCodes = a;
    }
  }
  return PlaceDuCode_PlacesCodes;
}



/*
---------------------------------------------------------------------------
BUZZER
---------------------------------------------------------------------------
*/
void bip(int a) {  
  if(a==1) {
    tone(buzzer, 1800);              // génère un signal carré au buzzer
    delay(250);  
    noTone(buzzer);
    delay(250);
    tone(buzzer, 1800);              // génère un signal carré au buzzer
    delay(250);  
    noTone(buzzer);
  } else if (a==2)  {
    tone(buzzer, 1800);
    delay(750);
    noTone(buzzer);
  }
}



/*
---------------------------------------------------------------------------
ETHERNET
---------------------------------------------------------------------------
*/
void EthernetRecv(EthernetClient client, char command) {
  if (command=='Z') { // Z0100b87a09 - Envoyer un nouveau code- OUI
    int aa = 0;
    while (aa<10) {
      TempCode[aa] = client.read();
      aa++;
    }
    TempCode[11] = '\0';
    AjouteCodeAutorise(TempCode);
    Serial.println("Ajoute un code : ");
    Serial.println(TempCode);
    Serial.println( "\n" );
  } else if (command=='z') { // z0100b87a09 - Supprimer un code - OUI
    int aa = 0; 
    while (aa<10) {
      TempCode[aa] = client.read();
      aa++;
    }
    TempCode[11] = '\0';
    SupprimeCodeAutorise(TempCode);
    Serial.println("Supprime un code : ");
    Serial.println(TempCode);
    Serial.println( "\n" );
  } else if (command=='Y') { // Y12 - Activer une place du parking - OUI
    char TempVar;
    TempPlace[0] = client.read();
    TempVar = client.read();
    if(TempVar != (char)-1) {
      TempPlace[1] = TempVar;
    } else {
      TempPlace[1] = '\0';
    }
    TempPlace[2] = '\0';
    PlacesActives[atoi(TempPlace)] = 1;
    Serial.println("Active la place : ");
    Serial.println(TempPlace);
    Serial.println(NombreCodes);
  } else if (command=='y') { // y12 - Desactiver une place du parking - OUI
    char TempVar;
    TempPlace[0] = client.read();
    TempVar = client.read();
    if(TempVar != (char)-1) {
      TempPlace[1] = TempVar;
    } else {
      TempPlace[1] = '\0';
    }
    TempPlace[2] = '\0';
    PlacesActives[atoi(TempPlace)] = 0;
    Serial.println("desactive la place : ");
    Serial.println(TempPlace);
  } else if (command=='X') { // X - Activer le parking - OUI
    digitalWrite(PinLecteur, LOW);
    Serial.println("Active le parking");
  } else if (command=='x') { // x - Desactiver le parking - OUI
    digitalWrite(PinLecteur, HIGH);
    Serial.println("desactive le parking");
  } else if (command=='W') { // W0100b87a0912 - Associer un badge a une place - OUI
    int aa = 0;
    while (aa<10) {
      TempCode[aa] = client.read();
      aa++;
    }
    TempCode[11] = '\0';
    char TempVar;
    aa = 0;
    TempPlace[0] = client.read();
    TempVar = client.read();
    if(TempVar != (char)-1) {
      TempPlace[1] = TempVar;
    } else {
      TempPlace[1] = '\0';
    }
    AjouteCodeAutorise(TempCode);
    PlacesPredef[atoi(TempPlace)] = 1;
    strcpy(PlacesCodes[atoi(TempPlace)], TempCode);
    Serial.println("Associe le badge : ");
    Serial.println(String(TempCode));
    Serial.println(" à la place : ");
    Serial.println(TempPlace);
  } else if (command=='w') { // w0100b87a0912 - Enlever l'association d'un badge a une place - OUI
    int aa = 0;
    while (aa<10) {
      TempCode[aa] = client.read();
      aa++;
    }
    TempCode[11] = '\0';
    char TempVar;
    aa = 0;
    TempPlace[0] = client.read();
    TempVar = client.read();
    if(TempVar != (char)-1) {
      TempPlace[1] = TempVar;
    } else {
      TempPlace[1] = '\0';
    }
    TempPlace[2] = '\0';
    PlacesPredef[atoi(TempPlace)] = 0;
    strcpy(PlacesCodes[atoi(TempPlace)], "0000000000");
    Serial.println("Enlever l'association du badge : ");
    Serial.println(TempCode);
    Serial.println(" à la place : ");
    Serial.println(atoi(TempPlace));
  } else if (command=='V') { // V0100b87a0912 - Place prise - OUI
    int aa = 0;
    while (aa<10) {
      TempCode[aa] = client.read();
      aa++;
    }
    TempCode[11] = '\0';
    char TempVar;
    aa = 0;
    TempPlace[0] = client.read();
    TempVar = client.read();
    if(TempVar != (char)-1) {
      TempPlace[1] = TempVar;
    } else {
      TempPlace[1] = '\0';
    }
    TempPlace[2] = '\0';
    strcpy(PlacesCodes[atoi(TempPlace)], TempCode);
    PlacesDispos[atoi(TempPlace)] = 0;
    Serial.println("la place : ");
    Serial.println(TempCode);
    Serial.println("est prise par le badge : ");
    Serial.println(TempPlace);
  } else if (command=='v') { // v12 - decharger la place - OUI
    char TempVar;
    TempPlace[0] = client.read();
    TempVar = client.read();
    if(TempVar != (char)-1) {
      TempPlace[1] = TempVar;
    } else {
      TempPlace[1] = '\0';
    }
    TempPlace[2] = '\0';
    if (PlacesDispos[atoi(TempPlace)]==0) {
      CodeDetecte(PlacesCodes[atoi(TempPlace)]);
    }
  } else if (command=='r') { // r - redemarrer le systeme - OUI
    pinMode(PinReset, OUTPUT); 
    digitalWrite(PinReset, LOW);
    Serial.println("redemarrage");
  }
}

void EthernetSend(EthernetClient client, String command) {
  Serial.println("envoie de donnees");
  client.print(command);
}

void EthernetConfig(int etat) {
  if (etat==0) { // configuration non chargee, on demande un synchronisation
    //EthernetSend("R0");
  } else if (etat==1) { // configuration chargee, on synchronise
    //EthernetSend("R1");
  }
}
