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
    try:
        customer_file = open('CustomerList.txt', 'r+')
        customer_list = list(customer_file)
        file_contents = len(customer_list)
        customer_file.close()
        print 'You have selected "New Customer"\n'
        print 'Enter the following information to create a new account: '
        print (24 * '=')
        print ('\n')
        customer_first = raw_input('First Name: ')
        customer_last = raw_input('Last Name: ')
        customer_street = raw_input('Street Address: ')
        customer_city = raw_input('City: ')
        customer_state = raw_input('State: ')
        customer_zip = raw_input('Zip Code: ')
        customer_phone = raw_input('Last four digits only: ')
        str_phone = str(file_contents + 1) + customer_phone
        print (24 * '=')
        print ('\n')
        print 'Thanks for entering your info. \n'
        new_cust = str_phone + ',' + customer_first + ',' + customer_last + ',' + customer_street + \
            ',' + customer_city + ',' + customer_state + ',' + customer_zip + ',\n'
        print (new_cust)
        customer_file = open('CustomerList.txt', 'a+')
        customer_file.write(new_cust)
        customer_file.close()

        print ('\n\n' + customer_first + ' your customer number is: ' + str_phone)

    except ValueError:
        print 'file not found'


def guest_customer():
    print 'You have selected "Guest Customer"'
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
