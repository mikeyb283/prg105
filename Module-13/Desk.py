import Office_Furniture


def main():
    desk = Office_Furniture.Desk('Desk', 'Metal', 24, 24, 30, 5, 'Two drawers on each side, one in the center', 99.99, 7)

    print 'Product: ' + desk.get_category()
    print 'Material: ' + desk.get_material()
    print 'Length: ' + str(desk.get_length())
    print 'Width: ' + str(desk.get_width())
    print 'Height: ' + str(desk.get_height())
    print 'Number of drawers: ' + str(desk.get_drawers())
    print 'Location of drawers: ' + desk.get_location()
    print 'Price: ${:0,.2f}'.format(desk.get_price())
    print 'Quantity: ' + str(desk.get_quantity())

    print desk

main()
