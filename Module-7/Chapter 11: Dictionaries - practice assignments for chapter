# Create a dictionary named holidays that pairs the name of
# the holiday with the date it will occur this year, include at least four
# key-value pairs
# example: holiday = {'Independence Day':  'July 4'}
holidays = {"New Years Day": "January 1", "Halloween": "October 31", "Thanksgiving": "November 24", "Christmas": "December 25"}

# print holiday -  does the order match what you put it in?
print holidays  # No, it does not match the same order entered.

# run the len function on holiday - how does it calculate the results? ** print(len(holiday))
print(len(holidays))  # Each key-value pair is calculated as 1.

# Write the code to use the "in" function to find one of the keys in your dictionary. Make sure to surround the
# code with a print statement so that the result prints on screen
print "New Years Day" in holidays

# now write the code to look for a key that is not in the dictionary. Make sure to surround the code
# with a print statement so the result prints on screen
print "Memorial Day" in holidays

# now write the code to find a value in your dictionary, use the print statement to show the results
print holidays["New Years Day"]

# print all of the values in the dictionary
date = holidays.values()
print date

# 11.2 Looping and Dictionaries
# Write the histogram code and test it by passing in a word that has at least two of one letter
# Print the result of running the histogram code
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram("bookkeeper")
print h

# Exercise 11.2 Rewrite the histogram code using the get method, test with the same word, name the function histogram2
# hint assign the result of d.get(c,0) to a value then add one to the value of d[c]
def histogram2(s):
    d = dict()
    for c in s:
        d.get(c, 0)
        d[c] = 1
        d[c] += 1
    return d
h = histogram2("bookkeeper")
print h

# Looping and Dictionaries
# use a for statement to print your holiday dictionary
# What prints? The keys or the values?
for days in holidays:  # The keys printed.
    print days

print ("\n\n\n")  # leave this code so that there are blank lines before the next exercise
# now write code that prints all of the keys and all of their values in the holiday dictionary
# if you use the print statement then values separated by commas they appear on the same line
for days in holidays:
    print days, holidays.get(days)


print ("\n\n\n")  # leave this code so that there are blank lines before the next exercise
# Reverse Lookup
# Type the code for the Reverse Lookup from 11.3 below
# Test the code by calling it with the holiday dictionary and one of your values (print the result)
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError
print reverse_lookup(holidays, "January 1")

# Call the code a second time with a value that doesn't exist, run the program
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError
#print reverse_lookup(holidays, "August 18")

# Copy and paste the error code here, add # as needed to make the error a comment
#Traceback (most recent call last):
#  File "/Users/michaelballing/OneDrive/Documents/MCC/PRG-105/PycharmProjects/PRG-105-FA2016/Module 7/Chapter 11: Dictionaries - practice assignments for chapter.py", line 84, in <module>
#    print reverse_lookup(holidays, "August 18")
#  File "/Users/michaelballing/OneDrive/Documents/MCC/PRG-105/PycharmProjects/PRG-105-FA2016/Module 7/Chapter 11: Dictionaries - practice assignments for chapter.py", line 83, in reverse_lookup
#    raise ValueError
#ValueError

# leave the line of code that caused the error, but put a # in front of it to make it a comment

# 11.4 Dictionaries and lists
# Type in the code to invert a dictionary
# Call the invert_dict function with the holiday dictionary
# print the results
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
print invert_dict(holidays)

print ("\n\n")

# Exercise 11.5 Exercise 11.5. Read the documentation of the dictionary method setdefault and use it to write a
# more concise version of invert_dict. Solution: http://thinkpython.com/code/invert_dict. py .
def invert_dict(d):
    inverse = {}
    for key, val in d.iteritems():
        inverse.setdefault(val, []).append(key)
    return inverse
print invert_dict(holidays)
