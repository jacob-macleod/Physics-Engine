# Physics-Engine
A basic physics engine running in the terminal made in Python

This Engine simulates:
* Velocity of a moving object
* Change in velocity and acceleration when a moving object collides with a stationary object
* This engine operates in the X axis

The user may decide:
* The mass of the object simulated 
* Its starting location 
* Its initial velocity
* The time period involved, measured in ephochs

Please note that there are two main problems with this engine.

Firstly, when an object collides with another object, changing the original object's acceleration, the acceleration increases for ever. However, in the real world, there are various factors such as friction and drag that effect this velocity which are not accounted for. In addition, momentum is not taken into account.

Secondly, it is currently not possible to define initial acceleration for the object, although this feature is being developed.
