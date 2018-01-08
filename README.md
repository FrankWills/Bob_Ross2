Bob_Ross2
============

Another fun pygame based doodler

------------

# Dependencies

You need pygame to run this. I'm really tired right now so can you just figure
out how to install that yourself thanks

oh and you need to be on windows for the screen size to work. I could write
platform-smart code, but I'm not going to. Just manually set the screen size
and get rid of ctypes if you are on linux.

# Controls

ESC: quit

## Colors

1: Red

2: Yellow

3: Green

4: Cyan

5: Blue

6: Black

7: White


## Size

[: Smaller

]: Larger

## Effects

O/P: Rotation on/off

L/;: Wave on/off

.//: Random on/off

sorry that looks weird

# Types of Effects

## Translational Effects

### Circle

The standard format from bob ross 1. Draws each dot in position and then rotates
a given interval around a specified center.

- angle_mod: the angle of rotation in radians per tick.
Fractions of pi make symmetry

### Wave

A format that draws each dot in position and then translates a distance in a
direction in a sine wave pattern.

- x_mod: the base distance traveled in the x direction
- y_mod: the base distance traveled in the y direction
- x_amp: the amplitude of the wave in the x direction
- y_amp: the amplitude of the wave in the y direction

### Random

Draws each dot in position and then randomizes its location within the window.

## Color Effects

### Rainbow

Cycles through the colors starting at whatever color was specified and changing
whenever a new dot is created.

### Sync

All the dots are drawn in the same color for a cycle
