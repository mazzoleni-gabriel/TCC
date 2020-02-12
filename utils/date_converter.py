

def to_string(date):
    date_format = "%Y-%m-%d"
    time_format = "%H:%M:%S"
    return date.strftime("%s %s" % (date_format, time_format))
