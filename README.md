# MPU6050-data-logger-GUI
A simple GUI based MPU6050 with Arduino data logger 

## Introduction
Hey there, This is a simple GUI interface for MPU6050 for logging data given from the sensor into a CSV file

## Getting started
Firstly you need to have a Arduino nano and a MPU6050 and connect the pins as follow:

* `VCC -> 5V`
* `GND -> GND`
* `A4 -> SDA`
* `A5 -> SCL`

connect your Arduino to your system via USB and now we can move to the software part, start with opening Arduino IDE and locate `Arduino. CPP` in `Arduino` folder in Projects repository, copy the code in it to your IDE and save the file and upload it to Arduino.
If everything is done successfully now you can download the `.py` file in the repository.

## Configuring the serial port
Open the `.py` file in any IDE and look for line 7 or this code `ser = serial.Serial("COM4", 115200) # change your serial port with COM4` and here you have changed your serial port and you may execute the code
if you have done everything right you may be greeted with an interface like this 

![screen shot 1](/images/gui.PNG)

or

![screen shot 2](/images/gui1.PNG)

if you have to disconnect the Arduino in the middle of the process 

and that's it for today, see you soon!

# Donate
* PayPal -> balharav3@gmail.com
* UPI -> 19vishalindustries-1@okhdfcbank

Thank You
