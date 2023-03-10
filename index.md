---
title: Team 203 Enviromental Conditioner
---

# Team 203 Enviromental Conditioner

_Arizona State University_

_EGR 314 Spring 2023 Dr Aukes_

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
- [Hardware Proposal](#hardware-proposal)
- [Software Proposal](#software-proposal)
- [Presentations](#presentations)
- [Appendices](#appendices)

## Table of Figures
- [Current Design](#current-design)
- [Current Diagram](#current-diagram)
- [Chosen Parts](#chosen-parts)
- [Power Budget](#power-budget)
- [Schematic](#schematic)
- [Software Proposal Diagram](#software-proposal)

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

The current design that the team has gone with has been updated to allow more room for electronics and a new exterior design improvement. The design will provide a safe area for the electronics that is out of the way of the irrigation and has an easy accessible point. The exterior was altered with holes to allow more air flow in the box. Although the team wants to be able to control the environment as much as possible, without a fan or air flow in the box, there would be more challenges with keeping the plats alive.
### Current Design
![Copy of plant_box_hedges](https://user-images.githubusercontent.com/102606124/224888331-39c68bb7-334e-4983-ab2b-893d13ff3c94.png)

## Block Diagram
### Diagram Overview
Each team member was given the task of generating 25 ideas that encompassed at least one of the design requirements. The ideas were posted to a jamboard allowing the team to take inspiration from each other. Members then organized the ideas into catgories and ranked them. The top 3 design concepts were democratically chosen and created into vector drawings.
### Current Diagram

<img src="https://user-images.githubusercontent.com/102606124/221485012-f229a9d3-714c-4173-8c21-c358432b3d4b.png" width="1000" height="500">

## Component Selection
### Selection Overview
To make a well-rounded product that does its job, as well as completes class requirements, certain components were selected. Specific parts must be surface-mount in order to be placed on a PCB, but other parts (such as the LED strip) are optional and are used for aesthetics, debugging, etc.

### Chosen Parts
Temperature Sensor - LM75BD [Found on Digikey](https://www.digikey.com/en/products/detail/umw/LM75BD/16842174?utm_adgroup=Temperature%20Sensors%20-%20NTC%20Thermistors&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Sensors%2C%20Transducers_NEW&utm_term=&utm_content=Temperature%20Sensors%20-%20NTC%20Thermistors&gclid=Cj0KCQiAorKfBhC0ARIsAHDzslv9GIfb93bmvJccUv8R-opUv7Dptezt21sXMPO6fPWY4PgNtWwrrqsaAhLVEALw_wcB)

<img src="https://user-images.githubusercontent.com/102606124/221481217-12a9fd89-28cb-4715-8789-5646c556436f.png" width="200" height="200">

Humdity Sensor - HIH6030-000-001[Found on Digikey](https://www.digikey.com/en/products/detail/honeywell-sensing-and-productivity-solutions/HIH6030-000-001/4440787)

<img src="https://user-images.githubusercontent.com/102606124/221481478-40137153-dce3-425e-bed4-81e7c9ca116c.png" width="200" height="200">

Switching Regulator - AZ34063UMTR-G1 [Found on Digikey](https://www.digikey.com/en/products/detail/diodes-incorporated/AZ34063UMTR-G1/4471007)

<img src="https://user-images.githubusercontent.com/102606124/221481650-23a2d1ce-d08e-4acd-8e0a-5cba31ce7f7a.png" width="200" height="200">

Motor Driver - IFX9201SGAUMA1 [Found on Digikey](https://www.digikey.com/en/products/detail/infineon-technologies/IFX9201SGAUMA1/5415542)

<img src="https://user-images.githubusercontent.com/102606124/221481985-f09361f5-76eb-44bf-9022-381ef95a5b04.png" width="200" height="200">

Motors - 12SG-N20VA [Found on RobotShop](https://www.robotshop.com/products/3v-1001-micro-metal-gearmotor-77rpm?gclid=Cj0KCQiArsefBhCbARIsAP98hXSDu0w-45Optkd4sC3l0MZlbCK-X6YCTygz1RPMedzvn13zsovS0NEaAoAUEALw_wcB)

<img src="https://user-images.githubusercontent.com/102606124/221486272-bac0162a-c0cf-4e14-9c0c-af7d522646a0.png" width="200" height="200">

LED (Green) - LTST-C230KGKT [Found on Digikey](https://www.digikey.com/en/products/detail/liteon/LTST-C230KGKT/386855)

For diagnosing subcircuits.

<img src="https://user-images.githubusercontent.com/102606124/221482152-89d21a39-7167-4e0b-88a4-dddbbbc30947.png" width="200" height="200">

LED Strip - 4851 [Found on Digikey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4851/13688273)

For providing artificial light to the plants in the contained environment.

<img src="https://user-images.githubusercontent.com/102606124/221482300-cab08df1-ea34-4f6a-a94d-a1c95b04632d.png" width="200" height="200">

6V Water Pump - FIT0563 [Found on Digikey](https://www.digikey.com/en/products/detail/dfrobot/FIT0563/8827828)

<img src="https://user-images.githubusercontent.com/102606124/221482484-3cac8b8b-0ea3-4493-9297-5ebb1dc6fa6a.png" width="200" height="200">

Microcontroller - PIC18F27Q84 [Found on Digikey](https://www.digikey.com/en/products/detail/microchip-technology/PIC18F27Q84T-I-SS/12807268)

<img src="https://user-images.githubusercontent.com/102606124/221489314-4aaf85d0-613e-440b-a003-dd4436a1df9d.png" width="200" height="200">


### Power Budget
In order to ensure that all systems can be used, a power budget was created. This power budget ensures we have all aspects (voltage, Amps, etc.) to power each part of our system.

<img src="https://user-images.githubusercontent.com/102606124/221492170-6a5ddf5d-8faa-487d-9b23-51a00a330cb4.png" width="800" height="700">

## Hardware Proposal
### Schematic
Including each team member's individual schematioc and combining them together with team based work components, this schematic is the most recently updated version is shown below.

![image (13)](https://user-images.githubusercontent.com/102606124/224888041-c8c5f5da-e65a-4f4d-b7e4-c0a168b9334c.png)

A .pdf version of this schematic can also be downloaded in [Appendix E](/HardwarePropAppendix)


### Bill of Materials
For the team's most recent version of the Bill of Materials, it can be found in [Appendix E](/HardwarePropAppendix)

## Software Proposal
Below is a diagram of how the software should run on the microcontroller and subcircuits. The goal is to have the box lid open if the moisture sensor or temperature sensor detects a value that is higher than the user set. This will tell the microcontroller to trigger the motors to open the lid to keeps the plants in an ideal environment.
![TEAM 203 COMPLETE SOFTWARE (1)](https://user-images.githubusercontent.com/102606124/221484119-72a156be-3abc-4f81-9cb6-9f7a0149567d.png)


## Presentations
{% raw %} {% include youtube.html id="NVca4oIyfms" %}
{% endraw %}

{% include youtube.html id="NVca4oIyfms" %}

## Appendices

### [Appendix A: Team Organization](/TeamOrgAppendix)

### [Appendix B: User Needs, Benchmarking, and Requirements](/UserNeedsAppendix)

### [Appendix C: Design Ideation](/DesignIdeaAppendix)

### [Appendix D: Microcontroller Selection](/MicrocontrollerAppendix)

### [Appendix E: Hardware Proposal](/HardwarePropAppendix)
