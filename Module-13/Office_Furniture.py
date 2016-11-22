class OfficeFurniture(object):

    def __init__(self, category, material, length, width, height, price, quantity):

        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price
        self.__quantity = quantity

# Special methods

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

# Public methods

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_item_price(self):
        return self.__price * self.__quantity

    def __str__(self):
        line_item = self.__category + ' Material: ' + self.__material + ' Length: ' + str(self.__length) + \
                    ' Width: ' + str(self.__width) + ' Height: ' + str(self.__height) + ' Quantity: ' + \
                    str(self.__quantity) + ' Individual price: ${:0,.2f},'.format(self.__price) + \
                    ' Total = ${:0,.2f}'.format(self.get_item_price())
        return line_item

# Sub class


class Desk(OfficeFurniture):

    def __init__(self, category, material, length, width, height, drawers, location, price, quantity):
        OfficeFurniture.__init__(self, category, material, length, width, height, price, quantity)

        self.__drawers = drawers
        self.__location = location

    def set_drawers(self, drawers):
        self.__drawers = drawers

    def set__location(self, location):
        self.__location = location

    def get_drawers(self):
        return self.__drawers

    def get_location(self):
        return self.__location

    def __str__(self):
        line_item = 'Product: ' + self.get_category() + ' Material: ' + self.get_material() + ' Length: ' + str(self.get_length()) \
                    + ' Width: ' + str(self.get_width()) + ' Height: ' + str(self.get_height()) + ' Number of drawers: ' + str(self.get_drawers()) \
                    + ' Drawer location: ' + self.get_location() + ' Individual price: ${:0,.2f}'.format(self.get_price()) + ' Quantity: ' + str(self.get_quantity()) \
                    + ' Total = ${:0,.2f}'.format(self.get_item_price())
        return line_item
