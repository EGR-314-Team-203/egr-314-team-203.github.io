---
title: mplab_code
---


# MPLABX Code
```
/*PIN ALLOCATIONS
RA0 - Debuggin LED
RA4 - MTRCSN (Motor SS/GPIO pin)
RB2- MTRSI (Motor serial in)
RB3- MTRSCK (Motor clock)
RC3 - SCLK (for both temp and humidity I2C)
RC4 - SDA (I2C data for both temp & humidity)
RC5 - MTRSL (Motor serial out)
RC6 - RX (Receiving)
RC7 - TX (Transmitting to ESP 32)
*/

#include "mcc_generated_files/mcc.h"
#include "mcc_generated_files/examples/i2c1_master_example.h"

//need to create ISR here like in homework with timers and interrupts
//interrupt should occur when temperature reaches xx degrees

unsigned readtemp;
unsigned temp;
uint8_t dbuff[4];
uint16_t conv = 0;
double humidity = 0;

volatile uint8_t words;
int ii;
float value;
int count=0;
 
    //if (count%100==0)
    //LED_Toggle();

void main(void) {
    
    SYSTEM_Initialize();
   // I2C1_Initialize();
   // UART1_Initialize();
  //  I2C1_InterruptHandler(I2C1_Read);
   
#define address 0b00011001000 //address for LM75b

    INTERRUPT_GlobalInterruptEnable();
    //INTERRUPT_PeripheralInterruptEnable()
    
    while (1) {

        //UART1_SetRxInterruptHandler(UART1_RX_ISR);

        //////////////// humidity /////////////////
        I2C1_ReadNBytes(0x27, dbuff, 1);
        __delay_ms(38);
        I2C1_ReadNBytes(0x27, dbuff, 4);
        conv = (dbuff[0] << 8 | dbuff[1]) & 0x3fff;
        __delay_ms(500);
        humidity = (conv / (16384.0 - 2.0)) * 100.0;

        //        if (humidity > 0) {
        //            LED_SetHigh(); ///ADD MOTOR CONTROL
        //        }
//
//        if (temp < 80) {
//            //open up lid, interrupt goes off here to send signal to motor driver
//            LED_SetHigh();
//            __delay_ms(500);
//            LED_SetLow();
//            __delay_ms(500);
//        }

//        if (temp > 80) {
//            //open up lid, interrupt goes off here to send signal to motor driver
//            LED_SetHigh();
//            __delay_ms(250);
//            //                LED_SetLow();
//            //                __delay_ms(250);
//        }

        //////////////// temperature  /////////////////
        readtemp = I2C1_Read1ByteRegister(address, 0x00);
        temp = ((readtemp * 1.8) + 32); //convert to fahrenheit
        printf("hello! Temp = %u Humidity = %2u \n\r", temp, humidity);
        __delay_ms(500);
        
        
        
        if (temp = 75)
        {
            LED_SetHigh();
            __delay_ms(1000);
        }
        else
        {
            LED_SetLow();
            __delay_ms(100);
        }
    }
        
    }
```
# MCC Pin Module
![314_Team203_MCCPinModule](https://user-images.githubusercontent.com/122768743/235579427-530d6f79-9cfc-4b0c-ad51-6ad5708e5c24.png)
# MCC Project Resources
![314_Team203_MCCProjectResources](https://user-images.githubusercontent.com/122768743/235579401-6f80d1f1-dc6c-432d-b100-f53d68476496.png)
