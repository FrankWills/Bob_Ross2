import pygame
#TODO: decide if numpy actually improves performance on translations or not
import random
import dot
from math import *


screen_size = (1920, 1080) #TODO: make this draw from windows metrics

# the color currently selected
current_color = [0,0,0]
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
    for dot in dot_list:
        dot.set_color(current_color)


def draw_dots(screen, dots):
    for dot in dots:
        pygame.draw.circle(screen, dot.get_color(), dot.get_pos(), dot.get_size(), dot.get_size())

def main():
    exit = False # determines when to exit the loop

    # pygame initialization
    screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
    pygame.display.set_caption("BOB ROSS")
    pygame.init()
    screen.fill((255, 255, 255))

    # global variable initialization
    global current_color
    global current_size
    global dot_list

    # effect variables
    spinning = False
    waving = False
    randing = False

    while exit is not True:
        # checking inputs and applying effects
        for event in pygame.event.get():
            pass

        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        if mouse[0]:
            dot_list.append(dot.dot(mouse_pos[0], mouse_pos[1], current_color, current_size))

        if mouse[2]:
            if len(dot_list) > 0:
                dot_list.pop()

        if keys[pygame.K_1]:
            current_color = [255, 0, 0]

        if keys[pygame.K_2]:
            current_color = [255, 255, 0]

        if keys[pygame.K_3]:
            current_color = [0, 255, 0]

        if keys[pygame.K_4]:
            current_color = [0, 255, 255]

        if keys[pygame.K_5]:
            current_color = [0, 0, 255]

        if keys[pygame.K_6]:
            current_color = [0, 0, 0]

        if keys[pygame.K_7]:
            current_color = [255, 255, 255]

        if keys[pygame.K_o]:
            spinning = True

        if keys[pygame.K_p]:
            spinning = False

        if keys[pygame.K_l]:
            waving = True

        if keys[pygame.K_SEMICOLON]:
            waving = False

        if keys[pygame.K_PERIOD]:
            randing = True

        if keys[pygame.K_SLASH]:
            randing = False


        # size modification
        if keys[pygame.K_LEFTBRACKET] and current_size > 1:
            current_size -= 1
        if keys[pygame.K_RIGHTBRACKET]:
            current_size += 1

        if keys[pygame.K_r]:
            rainbow()

        if keys[pygame.K_t]:
            screen.fill((255, 255, 255))

        if keys[pygame.K_ESCAPE]:
            exit = True

        if spinning:
            circle_trans()

        if waving:
            wave_trans()

        if randing:
            random_trans()

        # drawing and updating
        draw_dots(screen, dot_list)
        pygame.display.update()


    pygame.draw.circle(screen, current_color, (10,10), current_size, current_size)
    pygame.display.quit()
    pygame.quit()

main()
