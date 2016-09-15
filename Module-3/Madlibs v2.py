# Madlibs v2
print ("Enter your name")
name = raw_input()
if name == '':
    name = "Jack"

print ("Enter your sibling's name")
name2 = raw_input()
if name2 == '':
    name2 = "Jill"

print ("Enter a location")
place = raw_input()
if place == '':
    place = "the hill"

print ("Enter a object")
thing = raw_input()
if thing == '':
    thing = "pail of water"

print ("Enter a body part") # Keep it classy please!
body_part = raw_input()
if body_part == '':
    body_part = "crown"

print ("Choose speed, fast or slow")
speed = raw_input()
if speed == '':
    speed = "fast"

print ("Enter a verb")
action = raw_input()
if action == '':
    action = "tumbling"

print ("Enter a second verb")
action2 = raw_input()
if action2 == '':
    action2 = "patched"

print ("Enter a househould supply")
supplies = raw_input()
if supplies == '':
    supplies = "vinegar"

print ("Enter a second household supply")
supplies2 = raw_input()
if supplies2 == '':
    supplies2 = "brown paper"

# Vers:
print (name + " and " + name2 + " went up to " + place + ",")
print("To fetch " + thing + ",")
print(name + ' ' + 'fell down and broke his' ' ' + body_part + ",")
print ("And " + name2 + " came " + action + " after.")
print("Up " + name + " got, and to home he did trot,")
print ("As " + speed + " as he could caper,")
print ("To old Dame Dob, who " + action2 + " his " + body_part + ",")
print ("With " + supplies + " and " + supplies2 + "!")
