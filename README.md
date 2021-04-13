# Robo spider
Repository for hosting a hobbyst spider robot project.

The project is built around a Raspberry Pi Pico development board.
 
It's also using Cytron Maker Drive DC engine control board, HC-SR04 ultrasonic distance sensor and a bidirectional logic level convertion board.
The movement and mehcanics is based on DC motors and mechanics from two DFRobot Spider Robot kits.
The power supply is a cheap 3,7 V LiPol battery - currently 2200 mAh.

I'm also using a TP4056 LiPol charger.

For the connections I'm using some cheap chinese cables, two medium sized solderless breadboards and four electrical quick couplers.

Robot is programmed in MicroPython and uses a HC-SR04 driver library created by Roberto Sánchez (https://github.com/rsc1975/micropython-hcsr04).

Feel free to use this idea, improve it and publish your modified versions.

Bellow you can find link to the part listed above (on their producers or distrubutors web pages).

Raspberry Pi Pico: https://www.raspberrypi.org/products/raspberry-pi-pico/

Cytron Maker Drive: https://www.cytron.io/p-maker-drive-simplifying-h-bridge-motor-driver-for-beginner

HC-SR04 sensor: https://www.adafruit.com/product/3942?gclid=Cj0KCQjwgtWDBhDZARIsADEKwgMJtLBymzIgNfOoiBddAZCEFAebiDkvQ5Y_2iLcDb9uH_d2BtJIb4UaAhXeEALw_wcB

Logic level convertion board: https://www.banggood.com/pl/10Pcs-Logic-Level-Converter-Bi-Directional-IIC-4-Way-Level-Conversion-Module-p-1033750.html?cur_warehouse=CN&rmmds=category

Battery: https://botland.store/li-po-batteries/12662-akyga-li-pol-battery-2200mah-1s-37v-jst-bec-connector-socket-59x37x9mm.html

TP4056 charger: https://botland.store/charger-modules-for-li-po-batteries/6944-lipol-charger-tp4056-1s-37v-microusb-with-protection.html

Spider Robot kit: https://botland.store/create-a-robot/5960-dfrobot-spider-kit-diy-kit.html

The connection schematics picture was created in Fritzing (https://fritzing.org/) - great peace of software for hobbysts.
All of the coding and software deployment was made using Visual Studio Code (https://code.visualstudio.com/) with the Pico-Go extension (http://pico-go.net/).
