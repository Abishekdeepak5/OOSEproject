# myapp/templatetags/date_filters.py
from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter(name='add_time')
def add_time(date_value, hours):
    try:
        date_obj = datetime.strptime(date_value, '%a, %d %b %Y')
        new_date_obj = date_obj + timedelta(hours=float(hours))
        return new_date_obj.strftime('%a, %d %b %Y')
    except ValueError:
        return ''

@register.filter(name='format_time')
def format_time(time_value, time_format='%H:%M'):
    if time_value:
        return time_value.strftime(time_format)
    return ''

@register.filter(name='format_date')
def format_date(date_value, date_format='%a, %d %b'):
    if date_value:
        input_datetime = datetime.strptime(date_value, "%Y-%m-%d")
        # output_date_string = input_datetime.strftime("%a, %d %b %Y")
        output_date_string = input_datetime.strftime(date_format)
        return output_date_string
    return ''

@register.filter(name='add_time_return_time')
def add_time_return_time(cur_time,time_str):
    try:
        cur_time=str(cur_time)
        datetime_obj = datetime.strptime(cur_time, '%H:%M:%S')
        time_delta = datetime.strptime(str(time_str), '%H:%M:%S').time()
        result_datetime = datetime_obj + timedelta(hours=time_delta.hour, minutes=time_delta.minute, seconds=time_delta.second)
        return result_datetime.strftime('%H:%M ')
    except ValueError:
        return ''

@register.simple_tag
def multiple_args_tag(date_value, time_value, add_time):
    try:
        datetime_str=str(date_value)+' '+str(time_value)
        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        time_delta = datetime.strptime(str(add_time), '%H:%M:%S').time()
        result_datetime = datetime_obj + timedelta(hours=time_delta.hour, minutes=time_delta.minute, seconds=time_delta.second)
        # return result_datetime.strftime('%Y-%m-%d')
        return result_datetime.strftime('%a, %d %b')

    except:
        return ''
@register.simple_tag
def tot_seat(end,start):
    try:
        return end-start+1
    except:
        return ''