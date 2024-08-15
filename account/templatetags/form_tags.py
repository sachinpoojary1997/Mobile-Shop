from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(feild, css_class):
    return feild.as_widget(attrs={"class": css_class})
