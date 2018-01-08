# the class of each dot drawn on the bob ross 2 screen


class dot ():

    self.x_pos = 0
    self.y_pos = 0
    self.color = [0,0,0]
    self.size = 0

    def __init__(self, new_x_pos, new_y_pos, new_color, new_size):
        self.x_pos = new_x_pos
        self.y_pos = new_y_pos
        self.color = new_color
        self.size = new_size

    # get methods
    def get_pos(self):
        return (self.x_pos, self.y_pos)

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    # set methods
    def set_coords(self, new_x_pos, new_y_pos):
        self.x_pos = new_x_pos
        self.y_pos = new_y_pos

    def set_color(self, new_color):
        self.color = new_color

    def set_size(self, new_size):
        self.size = new_size
