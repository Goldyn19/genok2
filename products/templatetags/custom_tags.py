from django import template

register = template.Library()

@register.filter
def while_loop(value):
    return range(value)

@register.filter
def add(value, arg):
    return value + arg