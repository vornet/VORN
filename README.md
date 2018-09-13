# VORN 
Versatile Objective-based Robotic Navigator 

![Alt text](/VORN-in-action.gif?raw=true "VORN in action!")

VORN is a passion project of mine.  I love autonomous vehicles and always wanted to build one.  Finially have the time and available hardware to build one.

The goal of VORN is to look for an object, grab it, and bring it back to me.  As part of the process, I'll be building the software in a very modular way so that each layer can be re-purpose later.  Essentially, I'm building a framework.  More on this later.

First, the hardware.  This bot is based on MakeBlock Ultimate 2.0 10-in-1 Kit.  It comes with a MegaPi which is an Auduino-based board that can mounted on top of a Raspberry PI, and provides power and communication (via serial) between the two boards.

The MegaPi handles driving and executing the lower level motors and sensors, while the Raspberry PI handles higher level functionlity such as navigation, machine learning, and image detection. It also manages the vision camera, which is a Raspberry Pi camera.

More details to come!