# Class and self

class Fruits:
    color = None
    shape = None

    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def describe(self):
        print("This fruit is a {} shape and {} in color".format(self.shape, self.color))

    def taste(self):
        print("This {} colored fruit is {} in shape and is very tasty".format(self.color, self.shape))


fruit_obj = Fruits("circle", "red")
fruit_obj.describe()
fruit_obj.taste()

fruit_obj1 = Fruits("Oval", "Watermelon")
fruit_obj1.describe()
fruit_obj1.taste()
