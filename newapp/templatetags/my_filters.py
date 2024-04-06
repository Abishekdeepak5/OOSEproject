# myapp/templatetags/custom_filters.py

from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='format_time')
def format_time(time_value, time_format='%H:%M'):
    if time_value:
        return time_value.strftime(time_format)
    return ''

@register.filter(name='format_date')
def format_date(date_value, date_format='%Y-%m-%d'):
    if date_value:
        return date_value.strftime(date_format)
    return ''
