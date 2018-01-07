# the class of each dot drawn on the bob ross 2 screen


class dot ():

    x_pos = 0
    y_pos = 0
    color = [0,0,0]

    def __init__(new_x_pos, new_y_pos, new_color):
        x_pos = new_x_pos
        y_pos = new_y_pos
        color = new_color

    # get methods
    def get_pos():
        return (x_pos, y_pos)

    def get_color():
        return color

    # set methods
    def set_coords(new_x_pos, new_y_pos):
        x_pos = new_x_pos
        y_pos = new_y_pos

    def set_color(new_color):
        color = new_color
