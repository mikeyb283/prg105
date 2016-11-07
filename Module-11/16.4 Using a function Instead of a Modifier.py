class Time:
    def __init__(self):
        # type: () -> Time
        self.minute = None
        self.second = None
        self.hour = None


def add_time(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def change_time_by(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time. minute = divmod(minutes, 60)
    return time


def pure_function(time, inc):
    time1 = time
    time1 += inc
    return time1


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print ('\nStart time: ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

time.seconds = add_time(time)

inc_sec = raw_input('\nModify the time by _ seconds: ')


inc_seconds = pure_function(time.seconds, int(inc_sec))


time = change_time_by(inc_seconds)


if time.hour > 12:
    time.hour -= 12

print ('\nNew time ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
