Bob_Ross2
============

Another fun pygame based doodler

------------

# Types of Effects

## Translational Effects

### Circle

The standard format from bob ross 1. Draws each dot in position and then rotates
a given interval around a specified center.

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
