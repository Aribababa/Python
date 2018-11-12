 
// Incluímos la librería para poder controlar el servo
#include <Servo.h>
 
/* Ejes que se controlarán*/
Servo Tilt;
Servo Pan;

/* Posiciones de los ejes */
unsigned char tilt_angle = 91;
unsigned char pan_angle = 90;

/* Recepción de los datos*/
unsigned char serial_index = 0;
unsigned char txBuffer[32];

unsigned char transmition_complete = 0;
 
void setup() {
  /* Recepcion de la posicion de los datos */
  Serial.begin(9600);
 
  // Iniciamos el servo para que empiece a trabajar con el pin 9
  Tilt.attach(9);
  Pan.attach(10);

/* Posicion inicial de la cámara */
  Tilt.write(tilt_angle);
  Pan.write(pan_angle);
  delay(2000);
  
}
 
void loop() {
  /* Si se puede realizar una accino de control */
  if(transmition_complete){
    
    
    pan_control(txBuffer[(serial_index-2)%32]);
    delay(100); /* Para que se alcnze a estbilizar el Pn*/
    tilt_control(txBuffer[(serial_index-3)%32]);

    transmition_complete = 0; /* Ya se termino de relizar el ajuste */
      
  }
}


/** Funciones de control **/
void tilt_control(char data){
     char error_tilt = 128 - data;  /* Error con respeto a la referencia */

     /* Fuzzificación y defuzzificacion de la velocidad*/
    if(error_tilt < -16){
      if(tilt_angle > 80 && error_tilt < - 64){ tilt_angle-=2; }   
      if(tilt_angle > 80 && error_tilt < - 32){ tilt_angle-=1; }
      if(tilt_angle > 80 && error_tilt < - 16){ tilt_angle-=1; }
    } 
    
    /* Fuzzificación y defuzzificacion de la velocidad*/
    if (error_tilt > 16){
      if(tilt_angle < 110 && error_tilt > 64){ tilt_angle+=2; }   
      if(tilt_angle < 110 && error_tilt > 32){ tilt_angle+=1; }
      if(tilt_angle < 110 && error_tilt > 16){ tilt_angle+=1; }
    }
    
    Tilt.write(tilt_angle);
}

void pan_control(char data){
     char error_pan = 128 - data; /* Error con respeto a la referencia */

    /* Fuzzificación y defuzzificacion de la velocidad*/
    if(error_pan < -16){
      if(pan_angle > 10 && error_pan < -16 ){pan_angle-=1;}
      if(pan_angle > 10 && error_pan < -48 ){pan_angle-=3;}
      if(pan_angle > 10 && error_pan < -64 ){pan_angle-=5;}
      
    } 
    
    /* Fuzzificación y defuzzificacion de la velocidad*/
    if (error_pan > 16){
      if(pan_angle < 170 && error_pan > 16){pan_angle+=1;}
      if(pan_angle < 170 && error_pan > 48){pan_angle+=3;}
      if(pan_angle < 170 && error_pan > 64){pan_angle+=5;}
    }
    
    Pan.write(pan_angle);
}

/** Interrupciones del sistema **/
void serialEvent(void){
  if (Serial.available()){
    txBuffer[serial_index] = (char)Serial.read();  

    if (txBuffer[serial_index] == 255) {
       transmition_complete = 1;
    }
    serial_index = (serial_index + 1)%32;
  }
}
