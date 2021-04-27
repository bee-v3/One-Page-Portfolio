from django import template

register = template.Library()

def first_name(arg):
    return arg.split(" ", 1)[0]
    
register.filter('first_name', first_name)