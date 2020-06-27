from django import template
register = template.Library()
@register.filter(name='replacespace')
def replace_space(value):
    value1=str(value).replace(" ","")
    return value1
register.filter('replacespace',replace_space)