from categorygame.models import *
from django import template

register = template.Library()


@register.simple_tag()
def tag_categoris():
    return Category.objects.all()
