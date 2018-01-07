import pygame
#TODO: decide if numpy actually improves performance on translations or not
import numpy
import random
from math import *

class bob_ross2():

    screen_size = (1920, 1080) #TODO: make this draw from windows metrics

    # the color currently selected
    current_color = [255,255,255]
    current_size = 5

    # list of dot objects to be drawn
    dot_list = []

    # variables used for circle translations
    center = (int(screen_size[0]/2), int(screen_size[1]/2))
    angle_mod = 1 # set to a fraction of pi for symmetry

    # variables used for wave translations
    x_mod = 2 # the amount translated in the x before waving
    y_mod = 2 # the amount translated in the y before waving
    x_amp = 1 # the amplitude of the waving in the x direction
    y_amp = 1 # the amplitude of the waving in the y direction

    ## Translational Effects
    def circle_trans():
        for dot in dot_list:
            dot_pos = dot.get_pos()
            new_x = ((dot_pos[0] - center[0]) * cos(angle_mod))
            -((dot_pos[1] - center[1]) * sin(angle_mod)) + center[0]

            new_y = ((dot_pos[1] - center[1]) * cos(angle_mod))
            + ((dot_pos[0] - center[0]) * sin(angle_mod)) + center[1]

            dot.set_pos(new_x, new_y)

    def wave_trans():
        for dot in dot_list:
            dot_pos = dot.get_pos()
            new_x = dot_pos[0] + x_mod + (sin(y) * y_amp)
            new_y = dot_pos[1] + y_mod + (sin(x) * x_amp)

            dot.set_pos(new_x, new_y)

    def random_trans():
        for dot in dot_list:
            dot_pos = dot.get_pos()
            new_x = random.random() * screen_size[0]
            new_y = random.random() * screen_size[1]

            dot.set_pos(new_x, new_y)


    ## Color Effects
    def rainbow():
        pass

    def sync_color():
        pass


    def draw_dots(dot_list):
        pass

    def __main__():
        exit = False # determines when to exit the loop

        # pygame initialization
        screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
        pygame.display.set_caption("BOB ROSS")
        pygame.init()

        while exit is not True:
            # checking inputs and applying effects
