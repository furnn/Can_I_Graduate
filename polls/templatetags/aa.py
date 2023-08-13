from django import template

register=template.Library()

@register.simple_tag
def app(value, arg2):
    value.append(arg2)

@register.simple_tag
def same(value, arg2):
    value[0]=arg2