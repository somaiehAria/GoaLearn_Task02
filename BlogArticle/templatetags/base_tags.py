import datetime
from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "Somaieh Articles Blog"

@register.inclusion_tag("Blog/partials/category_navBar.html")
def category_navbar():
    return {
        "category": Category.objects.all()
    }