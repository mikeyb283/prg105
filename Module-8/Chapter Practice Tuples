#   12.1
#   Create a tuple filled with 5 numbers assign it to the variable n
n = 5,4,3,2,1
    # the ( ) are optional

#   Create a tuple named tup using the tuple function
tup = tuple()

#    Create a tuple named first and pass it your first name
first = tuple("Mike")

#    print the first letter of the first tuple by using an index
print first[0]

#    print the last two letters of the first tuple by using the slice operator (remember last letters means use
#    a negative number)
print first[-2:]

#   12.2
#   Given the following code, swap the variables then print the variables
var1 = tuple("hey")
var2 = tuple("you")
var1, var2 = var2, var1
print str(var1) + str(var2)

#   Split the following into month, day, year, then print the month, day and year
date = 'Jan 15 2016'
month, day, year = date.split(' ')
print str(month) + '/' + str(day) + '/' + str(year)
#   12.3
#   pass the function divmod two values and store the result in the var answer, print answer
answer = divmod(10,4)
print answer

#   12.4
#   create a tuple t4 that has the values 7 and 5 in it, then use the scatter parameter to pass
#   t4 into divmod and print the results
t4 = (7,5)
results = divmod(*t4)
print results

#   12.5
#    zip together your first and last names and store in the variable zipped
#    print the result
zipped = zip("Mike", "Balling")
print zipped

#   12.6
#   Store a list of tuples in pairs for six months and their order (name the var months): [('Jan', 1), ('Feb', 2), etc
months = [("Jan", 1), ("Feb", 2), ("Mar", 3), ("Apr", 4), ("May", 5), ("Jun", 6)]
# create a dictionary from months, name the dictionary month_dict then print it
calendar_dict = dict(months)
print calendar_dict

#   12.7
#   From your book:

my_words = ("The", "quest", "for", "the", "holy", "grail")
def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res
print sort_by_length(my_words)
# Create a list of words named my_words that includes at least 5 words  and test the code above
# Print your result
