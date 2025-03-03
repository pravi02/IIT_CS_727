from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0

@register.filter(name='percentage')
def percentage(value, total):
    try:
        # Return the percentage of value out of total
        return (float(value) / float(total)) * 100 if total != 0 else 0
    except (ValueError, ZeroDivisionError):
        return 0