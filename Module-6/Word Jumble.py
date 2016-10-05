import random
airplanes = ['CESSNA', 'PIPER','CIRRUS', 'BOEING', 'AIRBUS', 'EMBRAER', 'CANADAIR', 'MCDONNELL DOUGLAS', 'LEARJET',
             'GULFSTREAM', 'BEECHCRAFT', 'ALLIED AVIATION', 'HUGHES', 'WACO', 'DASSAULT']
selection = random.choice(airplanes)
answer = selection

jumble = list(selection)

for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,

guess = raw_input('\n Using the list of airplanes guess which kind of plane is jumbled!\n')
guess = guess.upper()

while guess != answer:
    guess != answer
    guess = raw_input('\n Using the list of airplanes guess kind of plane is jumbled!\n')
    guess = guess.upper()
else:
    print ('Correct')
