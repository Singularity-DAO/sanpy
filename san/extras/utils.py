import re
import datetime


def convert_dt(timestamp_string, postfix=' 00:00:00'):

    if type(timestamp_string) == datetime.date:
        timestamp_string = timestamp_string.strftime('%Y-%m-%d')

    if type(timestamp_string) == datetime.datetime:
        timestamp_string = timestamp_string.strftime('%Y-%m-a%d %H:%M:%S')

    timestamp_string = timestamp_string.replace('Z', '').replace('T', ' ')
    timestamp_string = timestamp_string[:19]

    if re.match(r'\d\d\d\d-\d\d-\d\d.\d\d:\d\d:\d\d', timestamp_string):
        return timestamp_string[:10] + ' ' + timestamp_string[11:]
    elif re.match(r'\d\d\d\d-\d\d-\d\d', timestamp_string):
        return timestamp_string + postfix
    else:
        raise Exception(f"Unknown format: {timestamp_string} !")


def str_to_ts(x):
    if isinstance(x, datetime.datetime):
        return x
    return datetime.datetime.strptime(convert_dt(x), '%Y-%m-%d %H:%M:%S')


def parse_str_to_timedelta(time_str):
    regex = re.compile(r'((?P<days>\d+?)d)?((?P<hours>\d+?)hr)?((?P<minutes>\d+?)m)?((?P<seconds>\d+?)s)?')
    parts = regex.match(time_str.lower())
    if not parts:
        return
    parts = parts.groupdict()
    time_params = {}
    for name, param in parts.items():
        if param:
            time_params[name] = int(param)
    return datetime.timedelta(**time_params)
