from django import template

register = template.Library()

def get_discount(price, discount, *args, **kwargs):
    return price * (100 - discount) / 100