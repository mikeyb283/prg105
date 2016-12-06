def find_customer(customer):
    try:
        with open('CustomerList.txt', 'r') as r:
            file_in = r.readlines()
            for item in file_in:
                record = item.split(",")
                if customer == record[0]:
                    return record
        return 'none'
    except IOError:
        print 'CustomerList.txt does not exist.'


def get_customer():
    customer = raw_input('Enter your customer number: \n')
    return customer


def display_menu():
    print '==============================='
    print '1. Returning Customer'
    print '2. New Customer'
    print '3. Guest Customer'
    print '================================'


def menu_selection():
    selection = input('Please select your customer type: \n')
    while selection < 1 or selection > 3:
        display_menu()
        selection = input('Select customer type from the choices listed: ')
    return selection


def returning_customer():
    print 'You have selected "Returning Customer"'
    my_customer = get_customer()
    customer_record = find_customer(my_customer)
    if customer_record == 'none':
        print 'Record not found. Try again'
        returning_customer()
    else:
        for item in customer_record:
            print item


def new_customer():
    print 'We are excited to welcome you as a new customer!'


def guest_customer():
    print '\n Welcome Guest!'


def main():
    display_menu()
    selection = menu_selection()

    if selection == 1:
        returning_customer()
    elif selection == 2:
        new_customer()
    else:
        guest_customer()


main()
