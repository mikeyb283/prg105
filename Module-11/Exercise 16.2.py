# create a time class
class Time:
    """Represents the time of day
    attributes: hour, minute, second
    """

    def __init__(self):
        pass


# create function to convert time to an integer
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


# create function to determine if time1 follows time1 chronologically
def is_after(t1, t2):
    seconds1 = time_to_int(t1)
    seconds2 = time_to_int(t2)
    difference = seconds2 - seconds1
    return [True, False][difference >= 0]

# create time1 object to determine if it follows time2
time1 = Time()
time1.hour = 12
time1.minute = 20
time1.second = 45

# create time2 object to determine if it comes before time1
time2 = Time()
time2.hour = 8
time2.minute = 45
time2.second = 30

# convert time1 to seconds
time1.seconds = time_to_int(time1)

time2.seconds = time_to_int(time2)

print is_after(time1, time2)
