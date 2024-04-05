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
