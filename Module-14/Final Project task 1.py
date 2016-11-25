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
            print 'Welcome back!'
            selection = -1

        elif selection == 2:
            print 'You are a New Customer'
            selection = -1

        elif selection == 3:
            print 'Welcome Guest!'
            selection = -1

        else:
            print 'Try again, select from the choices listed'
            selection = 0
