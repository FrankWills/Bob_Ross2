import pygame
#TODO: decide if numpy actually improves performance on translations or not
import numpy

class bob_ross2():

    screen_size = (1920, 1080) #TODO: make this draw from windows metrics

    # the color currently selected
    current_color = [255,255,255]

    # list of dot objects to be drawn
    dot_list = []

    # variables used for circle translations
    center = (int(screen_size[0]/2), int(screen_size[1]/2))
    angle_mod = 1 # set to a fraction of pi for symmetry


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
        pass

    def random_trans():
        pass


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
