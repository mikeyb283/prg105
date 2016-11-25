def returning_customer():
    print 'You have selected "Returning Customer"'


def new_customer():
    print 'You have selected "New Customer"'


def guest_customer():
    print 'You have selected "Guest Customer"'
    print '\n Welcome Guest!'


def unidentified_customer():
    print 'Try again, select from the choices listed'
    return

selection = 0

while selection >= 0:
    print '==============================='
    print '1. Returning Customer'
    print '2. New Customer'
    print '3. Guest Customer'
    print '================================'

    selection = input('Please select your customer type: ')

    while selection > 0:

        if selection == 1:
            returning_customer()
            selection = -1

        elif selection == 2:
            new_customer()
            selection = -1

        elif selection == 3:
            guest_customer()
            selection = -1

        else:
            unidentified_customer()
            selection = 0
