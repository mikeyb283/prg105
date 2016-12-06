noFile = 'no_file.txt'

try:
    with open(noFile, 'r') as f:
        noFile_data = f.read()
        print 'Finding ' + noFile
    if not noFile_data:
        print 'Data not found: ' + noFile
except IOError as e:
    print 'Import error ' + noFile + ' not found'

while True:
    try:
        number = raw_input('\nEnter a number: ')
        number = int(number)
        break
    except ValueError:
        print 'Not a valid number, enter a number.'
print ('The number you entered was: %.i' % number)
