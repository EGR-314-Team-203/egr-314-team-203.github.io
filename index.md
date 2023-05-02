# Team 203 Environmental Plant Box

 <link rel="shortcut icon" type="![favicon-16x16](https://user-images.githubusercontent.com/102606124/235522493-af700eea-23a7-40ff-aeed-17b66208cbc0.png)
/x-icon" href="favicon.ico?">

_Arizona State University_

_EGR 314 Spring 2023 Dr Aukes_

<p float="left">
  <img src="https://user-images.githubusercontent.com/102606124/235011500-8fd24422-6db9-473f-b02d-4069f8247802.jpg" width="100" />
  <img src="https://user-images.githubusercontent.com/102606124/235011720-f27198fc-fc83-44fd-b4d3-83de03099630.jpg" width="100" /> 
  <img src="https://user-images.githubusercontent.com/102606124/235011779-cec1f10d-a0db-4fdf-98ee-7760254603ec.jpg" width="100" />
  <img src="https://user-images.githubusercontent.com/102606124/235011804-b2df0145-375b-4e59-8eb8-d9d7dd076f01.jpg" width="100" />
</p>

_Madi Hedges, Morgan Strube, Zachary Felty, Hasan Kaysan_

_Spring 2023_

## Table of Contents
- [Introduction](#introduction)
- [Team Organization](#team-organization)
- [User Needs Benchmarking and Requirements](#user-needs-benchmarking-and-requirements)
- [Design Ideation](#design-ideation)
- [Selected Design](#selected-design)
- [Block Diagram](#block-diagram)
- [Component Selection](#component-selection)
- [Hardware Implementation](#final-hardware-implementation)
- [Software Implementation](#final-software-implementation)
- [Presentations](#presentations)
- [Appendices](#appendices)

## Table of Figures
- [Current Design](#current-design)
- [Current Diagram](#current-diagram)
- [Chosen Parts](#chosen-parts)
- [Power Budget](#power-budget)
- [Schematic and PCB](#schematic)
- [Software Proposal Diagram](#final-software-implementation)

## Introduction
This semester, the EGR 314 (Embedded Systems Design) class is focusing on weather-related measurements. All teams are tasked with creating a deliverable product that, in some sense, measures and responds to the environment around it. Our team, Team 203, is creating a plant environment box that measure the temperature and humidity within a contained planter that can adjust watering and the lid movement in order to help the plant thrive in the best conditions.

## Team Organization

### Charter

Team 203’s goals are to create a finalized working product that meets design requirements while simultaneously teaching each team member something new that they can apply to their professional careers. Working together to design, prototype, and manufacture to meet the following goals:

**Industry goals**
* Sell roughly 100,000 units a year
* Every 6 months look to improving the product with little cost or production set backs
* Increase production rate each year and lower the cost by 5%
* Research smaller electronics to allow room for improvements every few years
* Compare sales to competitors to lower or higher costs to improve sales

**Team Goals**
* Expand upon knowledge of  electronic components and how to utilize them in final product demonstration
* Make connections with fellow team members, classmates, and faculty. 
* Add projects designed or built in EGR314 to career portfolios 
* Learn various ways to get to the same point with the expanse of electronic selections
* Combining different skill sets to help each team member work on something new and learn how each system works as a whole
* Gain new programming skills with a new IDE and different language techniques

Team 203’s goals include working on a project together that will not only create a finalized working product, but will teach each team member something new and incorporate many design ideas into a final design.

### Product Mission Satement

Team 203 plans to be able to create an efficient and affordable weather station type device that will allow ease of use for the consumer and allow room for improving day to day life. This product will allow the team to be able to work together to create a finalized product that displays accurate data and demonstrates the skills learned throughout the course.


## User Needs Benchmarking and Requirements
### Organization
Based on related project searches a list of user needs was generated. The list of user needs was then subdivided into 6 categories: Physical properties, Data, Wireless features, Power, Accesibility, and Other. These categories were chosen because they seemed to encapsulate the positive and negative reviews that similar products were receiving.
### Justification
Of the 6 categories we determined the 3 most important to be: Power, Data, and Physical properties. Our team assigned weights for importance based on the frequency in which a problem occured in related products. 
### Specifications
We converted the needs into product specifications by analyzing the common pitfils of related products and assigning a general solution. An example of this would be that customers dislike cumbersome products, therefore, a product specification would be that it needs to be portable. (i.e less than 50 lbs).
### Requirements
* Maximized Battery Life
* Must weigh less than 50 lbs (22.6 kg)
* Easy to use and setup
* Stores data for future use
* Simple user interface
* Portable
* Accurate sensor readings

## Design Ideation
### Roles
Each team member in Team 203 was given the task of generating 25 or more ideas that encompassed at least one of the design requirements. The 100 ideas were posted to a online collaborative jamboard allowing the team to take inspiration from each other to effectivly brainstom ideas. Team members then organized the ideas into catgories and ranked them. The top three design concepts were democratically chosen and created into vector drawings for the next stages in prototyping.
### Brainstorming
The most effective strategy for our team used for brainstorming during this process was riffing on each others ideas. Our team found that having a general concept to ideate and improve made our collective brainstorming much simpler. The worst strategy for brainstorming our team found tended to be the "solo" method. We found that thinking of original ideas without inspiration or help from the team can be difficult and time consuming.
### Organization
The process for organizing ideas started by subdividing into three categories: Weather realted, Self-regulating, and Sensor based. The preceding rows in each category are ranked in descending order of favoritism, with the top rows containing the ideas we were most excited about. Each of the three product concept sketch ideas were democratically selected from the top row of each categories. Once the the three best concepts were chosen they were drawn into vector images

## Selected Design
### Design Overview

The team chose Design Concept 3 - The Plant Health Music Alarm for our chosen design. Our team decided to change some major components of the design, to better fit project requirments, as well as taking into acount user satisfaction and needs. The team decided to move away from the idea of an alarm, and move towards using an OLED to diplay information gathered by the sensors.

The current design that the team has gone with has been updated to allow more room for electronics and a new exterior design improvement. The design will provide a safe area for the electronics that is out of the way of the irrigation and has an easy accessible point. The exterior was altered with holes to allow more air flow in the box. Although the team wants to be able to control the environment as much as possible, without a fan or air flow in the box, there would be more challenges with keeping the plants alive.
### Current Design
<img src="https://user-images.githubusercontent.com/102606124/224888331-39c68bb7-334e-4983-ab2b-893d13ff3c94.png" width="5000" />

## Block Diagram
### Diagram Overview
Each team member was given the task of generating 25 ideas that encompassed at least one of the design requirements. The ideas were posted to a jamboard allowing the team to take inspiration from each other. Members then organized the ideas into catgories and ranked them. The top 3 design concepts were democratically chosen and created into vector drawings.
### Current Diagram

<img src="https://user-images.githubusercontent.com/102606124/235012670-d0bd4ed6-028c-4825-96a5-9dfb1ea8b307.jpg" width="800">

## Component Selection
### Selection Overview
To make a well-rounded product that does its job, as well as completes class requirements, certain components were selected. Specific parts must be surface-mount in order to be placed on a PCB, but other parts (such as the LED strip) are optional and are used for aesthetics, debugging, etc.

### Chosen Parts


| Image        | Part           | Found On      | Description |
| :---         |  :---          |  :---         | :---        |
| <img src="https://user-images.githubusercontent.com/102606124/221481217-12a9fd89-28cb-4715-8789-5646c556436f.png" width="100">|Temperature Sensor - LM75BD| [Digikey](https://www.digikey.com/en/products/detail/umw/LM75BD/16842174?utm_adgroup=Temperature%20Sensors%20-%20NTC%20Thermistors&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Sensors%2C%20Transducers_NEW&utm_term=&utm_content=Temperature%20Sensors%20-%20NTC%20Thermistors&gclid=Cj0KCQiAorKfBhC0ARIsAHDzslv9GIfb93bmvJccUv8R-opUv7Dptezt21sXMPO6fPWY4PgNtWwrrqsaAhLVEALw_wcB)|Used to measure temperature within the closed box environment|
| <img src="https://user-images.githubusercontent.com/102606124/221481478-40137153-dce3-425e-bed4-81e7c9ca116c.png" width="100">|Humdity Sensor - HIH6030-000-001|[Digikey](https://www.digikey.com/en/products/detail/honeywell-sensing-and-productivity-solutions/HIH6030-000-001/4440787)|For monitoring moisture in the closed environment, ideal humidity is set by user. If it becomes to humid, the box lid will open to get the plants some fresh air.|
|<img src="https://user-images.githubusercontent.com/102606124/221481650-23a2d1ce-d08e-4acd-8e0a-5cba31ce7f7a.png" width="100">|Switching Regulator - AZ34063UMTR-G1|[Digikey](https://www.digikey.com/en/products/detail/diodes-incorporated/AZ34063UMTR-G1/4471007)|Used to regulate voltage going to the other parts.|
|<img src="https://user-images.githubusercontent.com/102606124/221481985-f09361f5-76eb-44bf-9022-381ef95a5b04.png" width="100">|Motor Driver - IFX9201SGAUMA1|[Digikey](https://www.digikey.com/en/products/detail/infineon-technologies/IFX9201SGAUMA1/5415542)|For controlling the motor| 
|<img src="https://user-images.githubusercontent.com/102606124/221486272-bac0162a-c0cf-4e14-9c0c-af7d522646a0.png" width="100">|Motors - 12SG-N20VA|[RobotShop](https://www.robotshop.com/products/3v-1001-micro-metal-gearmotor-77rpm?gclid=Cj0KCQiArsefBhCbARIsAP98hXSDu0w-45Optkd4sC3l0MZlbCK-X6YCTygz1RPMedzvn13zsovS0NEaAoAUEALw_wcB)|A motor is used in order to push the top of the plant box open so that the plants inside can get fresh air.|
|<img src="https://user-images.githubusercontent.com/102606124/221482152-89d21a39-7167-4e0b-88a4-dddbbbc30947.png" width="100">|LED (Green) - LTST-C230KGKT| [Digikey](https://www.digikey.com/en/products/detail/liteon/LTST-C230KGKT/386855)|Used for diagnosing power and subsystems.| 
|<img src="https://user-images.githubusercontent.com/102606124/221482300-cab08df1-ea34-4f6a-a94d-a1c95b04632d.png" width="100">|LED Strip - 4851|[Digikey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4851/13688273)|For providing artificial light to the plants in the contained environment.|
|<img src="https://user-images.githubusercontent.com/102606124/221482484-3cac8b8b-0ea3-4493-9297-5ebb1dc6fa6a.png" width="100">|6V Water Pump - FIT0563| [Digikey](https://www.digikey.com/en/products/detail/dfrobot/FIT0563/8827828)|If the humidity drops too low (threshold set by the user), the plants will be watered with this pump.|
|<img src="https://user-images.githubusercontent.com/102606124/221489314-4aaf85d0-613e-440b-a003-dd4436a1df9d.png" width="100">|Microcontroller - PIC18F27Q84| [Digikey](https://www.digikey.com/en/products/detail/microchip-technology/PIC18F27Q84T-I-SS/12807268)|The microcontroller that will guide all of the subsystems.|
|<image src="https://user-images.githubusercontent.com/102606124/235523386-c3d64512-8c01-4f88-ad40-bd2bc77e2a91.png" width="100">|9V to 3.3V Vaoltage Regulator - LM2576D2TR4-3.3G|[Digikey](https://www.digikey.com/en/products/detail/onsemi/LM2576D2TR4-3-3G/1476725)|Used for regulating the incoming 9V from the wall plug to the 3.3V parts.|
|<img src="https://user-images.githubusercontent.com/102606124/235523773-170ba8d7-4195-4859-8064-db873d8da27a.png" width="100">|LED (Red)- SML-LXL1209SIC-TR|[Digikey](https://www.digikey.com/en/products/detail/lumex-opto-components-inc/SML-LXL1209SIC-TR/515913)|Used for diagnosing code and displaying temperature/humidity states.|
|<img src="https://user-images.githubusercontent.com/102606124/235524684-5fb4d76d-bdb7-4db9-9ddf-be671577aa09.png" width="100">|1000 UH Inductor - 744373965101|[Digikey](https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/744373965101/7323643)|Used in the voltage regulating section of the PCB.|
|<img src="https://user-images.githubusercontent.com/102606124/235525387-e48742af-181f-4dc9-8ae3-0ae0098d3484.png" width="100">|Shottky Diode - B340B-13-F|[Digikey](https://www.digikey.com/en/products/detail/diodes-incorporated/B340B-13-F/768869)|Used in the voltage regulating section of the PCB; lets current flow only one-way.|
|<img src="https://user-images.githubusercontent.com/102606124/235525476-6bf8a7ad-8ab1-45c5-a361-8e394feba77b.png" width="100">|Barrel Jack - RAPC722X|[Digikey](https://www.digikey.com/en/products/detail/switchcraft-inc/RAPC722X/804747)|Allows power from a wall plug to be put onto the PCB.|
|<img src="https://user-images.githubusercontent.com/102606124/235525990-060b31fc-3edc-4e50-805b-51099a16f2bf.png" width="100">|Fuse Holder - 05200101Z|[Digikey](https://www.digikey.com/en/products/detail/littelfuse-inc/05200101Z/554336)|Protects the PCB from a power surge.|

### Power Budget
In order to ensure that all systems can be used, a power budget was created. This power budget ensures we have all aspects (voltage, Amps, etc.) to power each part of our system.
 
<img src="https://user-images.githubusercontent.com/122824540/235560686-243ce0ad-cd22-43a8-9022-b8910e97695e.jpg" width="800" height="700">

## Final Hardware Implementation
### Schematic
Including each team member's individual schematioc and combining them together with team based work components, this schematic is the most recently updated version is shown below.
 
 <img src="https://user-images.githubusercontent.com/122824540/235548872-c151e3a7-c93a-46e8-9d67-03faaac35b3b.jpg" width="800" height="700">


 <img src="https://user-images.githubusercontent.com/122824540/235550859-94e8a467-cd32-4284-8b6e-5e576195b8f8.jpg" width="800" height="700">

A .pdf version of this schematic can also be downloaded in [Appendix E](#Appendices)

### User Needs and Requirements Satisfaction Implementation
By focusing on the User Needs observed above, the team combined all of the necessary components that were able to focus on these needs, such as have an accessible power supply and easily readable data from your phone. Both the Humidity and Temperature sensor are both able to help provide necessary readings for the user to be able to see and measure any up to date information. From this, the motor is able to act accordingly to the measurements or the user's preferences. The Switching Voltage Regulator, Humidity and Temperature Sensor and the Motor Driver, all lay down in the project requirements, and were easily able to be implemented to the idea of the user being able to control the environment of set plants.
 
### Design and Decision Making
Majority of the decisions for the components are discussed in the Component Selection, of this page. When deciding which components ran off of I2C or SPI, the logical decision was to have the Humidity and Temperature sensors both I2C, as they will both be chained together and will both determine the actions of the motor driver, which was SPI. The ESP32 was assigned to work through UART, as this was what was done in class, through Thonny or Vscode. These decisions were able to help organize and decipher who was doing which subsystem from the requirements. 
 
### Future Improvements
 If the team had the chance to create a Version 2.0 of this design, a few ideas were put together on what the team could have implemented into a new board. There would be more debugging capabilities added to allow for an easier time to differentiate the sensors and motor driver. The board had 1 LED that was able to act as a debugging tool for the team, while the first communication tests were not working. This LED would be programmed to blink, be set high or low, and let the team know when either the Humidity or temperature sensor were reading specific values. Although the sensors were daisy chained to each other through the microcontroller, two separate LEDs would have sped up the process. 

In addition, there were a few schematic changes, that did not affect the team's performance but would have allotted for a simpler and cleaner look on the board. The barrel jack was swapped out after the final schematic was submitted, causing the power pin to be oriented differently. The component was able to work, but had to be floating slightly to allow the plugin to come off the side of the board, and not directly across as the layout was set up. In addition, the capacitor and inductor correlating to the voltage regulator were directly causing alignment issues when programming the ESP32. Due to these components being so large, the ESP32 had to be taken off the board before being programmed.  

Finally, as it can be seen in the schematic above, there was an incorrect trace on the Microcontroller for pins 19 and 20, that was missed before sending over to JLCPCB. After the board was delivered, the team identified the short and had to cut the trace out for the ground pin in order to be able to properly power the microcontroller. 

![96491657638](https://user-images.githubusercontent.com/102606124/235582025-5e98a78e-da36-4571-8278-dc0f922223c5.png)  ![image_14](https://user-images.githubusercontent.com/102606124/235582001-af04cc74-19eb-440d-a06b-3866c3b65c19.png) 
 
Majority of these changes would not have altered the outcome of how the final project design turned out, but would have made the time taken to manage these little tasks, to lessen, so the team could focus on programming and debugging. 

### Bill of Materials
For the team's most recent version of the Bill of Materials, it can be found in [Appendix E](#Appendices)
 
## Final Software Implementation
Below is a diagram of how the software should run on the microcontroller and subcircuits. The goal is to have the box lid open if the moisture sensor or temperature sensor detects a value that is higher than the user set. This will tell the microcontroller to trigger the motors to open the lid to keeps the plants in an ideal environment.
![TEAM 203 COMPLETE SOFTWARE (1)](https://user-images.githubusercontent.com/102606124/221484119-72a156be-3abc-4f81-9cb6-9f7a0149567d.png)

### User Needs and Requirements Satisfaction
 The Team was able to analyze the needs and requirements, along with the Hardware Implementation to work through creating a product that met the criteria. The sensors needed to read accurate data, and this was worked through by checking addresses with the data sheet and analyzing the trends in the data. Such as if the temperature sensor was close to what the room thermostat was or lining up with other team's readings.

### Design and Decision Making Process
 The team based the software implementation and proposal around a chronological view point. This would make the most sense to the team and anyone else reading the code, without knowing much about the project. Taking the sensors and motor from above, the team planned to have the motor be driven based on readings from the humidity and temperature sensors.
 
### Top 5 Biggest Changes to Software Design
1. The first change the team had made was removing the OLED to read and display the data with the ESP32 Wifi and Bluetooth solely. This change simplified the whole system and allowed the team to be able to focus on the ESP32 and enhance the readings that the OLED would not be able to do.
2. Another change the team made to the software design was the addition of surface mount LED based timer interrupt. This was implemented before the sensor based interrupts for system verification. 
3. The team added to the software design by including the ability to read incoming data on RX line to change read sensor data with ESP32. This was important as it allowed the user to change data to adjust other functions in the main code. 
4. For debugging purposes, the team originally planned to have several leds for each subsystem. In the end, due to space, there were only 2 LEDs incorporated in the hardware design, which affected the software. In doing so, one LED was indicated for power and the other helped debug the humidity and temperature sensors, in addition to the interrupts.
5. Led lights separated from the whole system allows for the team to turn on the project's internal lighting separate from the main code to debug power connection. Since the LED’s serve no function other than turning on and off, this is unnecessary in the main loop. 

 
### Future Changes
 If the team were to be able to improve the software design, Team 203 would aim to have a more chronological set code, that can be easier to read and allow more features. The interrupts were last minute add-ins, but the original idea was to be able to have this cause when the motor would turn on and off. This should be improved upon because the team could learn more from this implementation and be able to control the motor more than they would have if it would have worked. This personalized ISR would have been organized to be called when the humidity or temperature was moved out of range of the plants specifications, and could be implemented multiple times on different occasions.

In addition, the code could be divided up between what would happen in various scenarios, and have the personalized functions for each sensor and the motor driver. In doing so, this can help clean up the code and make it more readable. As well, it could simplify any debugging issues, because the team could easily be able to determine where the code was stuck at. The temperature and humidity sensors are separated, and at one point was divided into functions, but without the functioning motor, it became too much code, for what little it could do. With the motor being functional, the team could have spent more time organizing it so that there would be no confusions. 

Additional peripherals that could be added is including the OLED screen and an extra fan. The OLED was worked on, and from class had been implemented, but due to timing reasons, the team was unable to add it into the final design. The extra fan idea was overlooked as it did not meet requirements for the project and was extra work the team would have had to focus on. This feature, however, could have helped change the conditions of the sensors faster, to not only be able to see an update, but also help improve the overall project idea of cooling down the environment inside. 

Overall, the software implementation of this project was simplified more than what the project path could have taken, and what the team would have wanted. Due to technical issues with the motor driver, majority of the team was spent on debugging this rather than improving upon the code. If there were to be a version 2.0, the team had spoken about dividing sooner than later to have been able to work on the code more. 
 
### MQTT Topic Table and Corresponding Code
 The Topic Table can be found in [Appendix F](#Appendices) and the code for the project can be found in [Appendix G](#Appendices) and [Appendix H](#Appendices)

## System Verification
 Below is the final System Verification Table that is updated with each subsystem checked off by the Teaching Assistants. 
 <img src="https://user-images.githubusercontent.com/122824540/235564797-2297d1fd-6a37-4caa-957a-4a07f800246a.jpg" width="800" height="600">

## Presentations

 [For Checkpoint 1, look here](link to appendix with video)
 
## Lessons Learned
 1. The team needed everyone to look through not only their subsystem but each other's subsystem before submitting any PCB design.
 2. When starting out, the team had to ensure there was enough time for each subsystem to be working before starting on the team board.
 3. The team should have spent more time focusing on the code as a whole rather than everyone working to solve a single subsystem.
 4. Next time, the team would work through the first team protoboard before submitting the final board. This did not affect the final product as it had few errors, but it would have saved time while working on the final board.
 5. In the code, the interrupts would have involved the motor being turned on and off based on the readings of the sensors, rather than an interrupt counter.
 6. Rather than having the entirety of the board on top of the plant box, the team should have created daughter boards for the sensors and then the motor driver to create a better end product. This was feedback from an external reviewer the team looked into, but did not have the time to pursue.
 7. There are various plants that need different conditions than the sunflowers needed, so implementing a way to alter a rangwe of temperature and humidity for the plants could have been a preset for the user.
 8. The team could have experimented with interfaces outside of the project requirements to be able to help improve the product, like following through with the fully operating water pump.
 9. The team learned for next time to focus more on ensuring that the bidirectional control was operating without failure, and could show a more pronounced result.
 10. Next time, the team would learn more about the humidity sensor to work to get more updated readings or find a way to change the humidity in the atmosphere that was more pronounced. 
 
## Recommendations for Future Students
 While the 300 level prject classes will come with growing pains, we promise that you will have learned so much by the end of the year. That said, you have to put in a lot of work. Every person on your team will have to pull equal weight in order to be successful- any slackers will heavily impact you. In that regard, choose your teammates based on their character, not just because they are your friend or are "very smart." You need people that will be able to help you stay on track, give and receive critique, and still be on speaking terms at the end of the day. Metaphorically, this year will be a *long* voyage and you need a top-tier ship crew you don't want to throw overboard if they don't compile code correctly. To summarize this into a bulleted list:

1. Chose teammates based on character (not just "smarts" or if they're your friend)
2. Put in your best effort! Not everything has to or will be perfect, but it shows when you put your best in.
3. Be creative! It's okay to have different ideas, design, and get artsy with your project! (It looks more presentable than a nest of jumper cables, we learned from experience.)
4. Expect to fail and try again. This course will test your ability to overcome adversity.
5. Be ready to learn. This year will be a challenge, but if you are willing to learn in and out of class, you'll be successful.

Sometimes it can get difficult to keep the destination in mind, but remember you aren't alone. TAs, classmates, and your own team will be there to help. Get ready to set course and have a good voyage! (I couldn't help using the sailing ship metaphor).
 
 
## Appendices

### [Appendix A: Team Organization](/Appendices/TeamOrgAppendix)

### [Appendix B: User Needs, Benchmarking, and Requirements](/Appendices/UserNeedsAppendix)

### [Appendix C: Design Ideation](/Appendices/DesignIdeaAppendix)

### [Appendix D: Microcontroller Selection](/Appendices/MicrocontrollerAppendix)

### [Appendix E: Hardware Proposal](/Appendices/HardwarePropAppendix)
 
### [Appendix F: MQTT Topic Table](/Appendices/MQTTtopicAppendix)

### [Appendix G: MPLab X Code and Configuration](/Appendices/Code/mplab_code)

### [Appendix H: ESP32 Code](/Appendices/Code/ESP32)

