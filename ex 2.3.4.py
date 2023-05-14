class Pixel:

    def __init__(self, x = 0, y = 0, red = 0, green = 0, blue = 0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) / 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        colors = ['red', 'green', 'blue']
        color_values = (self._red, self._green, self._blue)
        color_name = None
        print("X: " + str(self._x) + " Y: " + str(self._y) + " Colors: " + str(color_values))
        if color_values.count(0) == 2 and max(color_values) > 50:
            color_name = colors[color_values.index(max(color_values))]
        print(color_name)


def main():
    p = Pixel(5, 6, 250, 0 ,0)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == '__main__':
    main()