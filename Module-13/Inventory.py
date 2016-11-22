import Office_Furniture


def main():
    conference_table = Office_Furniture.OfficeFurniture('Conference Table', 'Steel', 96, 30, 29, 108.99, 5)

    print 'Product: ' + conference_table.get_category()
    print 'Material: ' + conference_table.get_material()
    print 'Length: ' + str(conference_table.get_length())
    print 'Width: ' + str(conference_table.get_width())
    print 'Height:' + str(conference_table.get_height())
    print 'Price: ' + str(conference_table.get_price())
    print 'Quantity: ' + str(conference_table.get_quantity())

    print conference_table

main()
