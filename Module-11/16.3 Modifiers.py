class Time:
    def __init__(self):
        self.minute = None
        self.second = None
        self.hour = None


def add_time(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def chang_time_by(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def modify(time, inc):
    time += inc
    return time


time = Time()
time.hour = 00
time.minute = 00
time.second = 00

print ('\nStart time: ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))


time.seconds = add_time(time)

inc_sec = raw_input('\nModify the time by _ seconds: ')


inc_seconds = modify(time.seconds, int(inc_sec))


time = chang_time_by(inc_seconds)


if time.hour > 12:
    time.hour -= 12

print ('\nNew time ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
