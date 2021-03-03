from django import template
register = template.Library()

@register.filter(name='inc')
def inc(value, incr):
    return str(int(value) + int(incr))

@register.simple_tag
def division(a, b, to_int=False):
    return int(int(a)/int(b)) if to_int else int(a)/int(b)