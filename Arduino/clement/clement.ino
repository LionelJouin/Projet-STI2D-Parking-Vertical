// enable > 2                               l'entrée enable du lecteur est connectée à la sortie 2 de l'arduino
// scout > 0                                la sortie du lecteur est connectée à l'entrée Rx de l'arduino

int  val = 0;                               // définir la variable val
char code[10];                              // code lu sur 10 octets
int badge = 0;                              // définir la variable badge
int buzzer = 9;                             // buzzer port 8
int freq = 1800;                            // définir une fréquence égale à 1800Hz

   void setup()
 { 
     Serial.begin(2400);                    // Connexion à 2400 bauds 
     pinMode(2,OUTPUT);                     // Broche numérique 2 en mode sortie pour la connecter au lecteur
     digitalWrite(2, LOW);                  // NL 0 > lecteur prêt à lire
     pinMode(buzzer, OUTPUT);               // active le buzzer
 }  
   

 void loop() 
{ 

  if(Serial.available() > 0)                // Si il y a des données dans le lecteur
  {          
  
    if((val = Serial.read()) == 10)         // Lire les données, si il y a déja un code >
    {   
      
      badge = 0;                            // > le remettre à 0
      while(badge<10)                       // Tant que le code est inférieur à 10 octects
      {             
      
        if( Serial.available() > 0)         // Si il y a des données à lire
            { 
              val = Serial.read();          // on lit ces données et on les stock dans VAL
              code[badge] = val;            // écrire dans la variable code, la valeur des 10 octets        
              badge++;                      // incremente badge afin d'obtenir 10 octets 
          
            } 
      } 
      
      if(badge == 10)                       // Une fois qu'on a lu les 10 octects 
     
      {              
        Serial.print("Code d'acces : ");    // ecrire : code d'acces dans le moniteur
        Serial.println(code);               // ecrire a la suite le code du badge
      } 
           
           badge = 0;                       // remettre le badge à 0
           digitalWrite(2, HIGH);           // Désactive le lecteur de badge
           bip(1);                          // appel de la fonction bip
           digitalWrite(2, LOW);            // lecteur de nouveau prêt à lire
   
    } 
  } 
} 

void bip(int a) 
{  
  if(a==1)
  {
    tone(buzzer, 1800);              // génère un signal carré au buzzer
    delay(250);  
    noTone(buzzer);
    delay(250);
    tone(buzzer, 1800);              // génère un signal carré au buzzer
    delay(250);  
    noTone(buzzer);
  } 
  
  else if (a==2) 
  {
    tone(buzzer, 1800);
    delay(750);
    noTone(buzzer);
  }
}
