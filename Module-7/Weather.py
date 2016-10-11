# Declare global variables to hold temps
yearly_average_temp = 0
higher_than_average = dict()

# Average temp in Sydney, Australia
monthly_average_temp = {"January": 72, "February": 73, "March": 70, "April": 66, "May": 61, "June": 56, "July": 55, "August": 57, "September": 61, "October": 64, "November": 68, "December": 71}

def average_temp_sydney(month):
    total = 0
    global yearly_average_temp
    for key in month:
        total = total + month[key]
    yearly_average_temp = total / len(monthly_average_temp)
    print ("The average temperature in Sydney, Australia is " + str(yearly_average_temp) + " degrees fahrenheit.")

def high_temp(n):
    global yearly_average_temp
    for temp in n:
        if n[temp] > yearly_average_temp:
            higher_than_average[temp] = (n[temp])
    print ('\nThe months that the temperatures are higher than the average temperature '
          'in Sydney are: \n')
    print str(higher_than_average)

average_temp_sydney(monthly_average_temp)
high_temp(monthly_average_temp)
