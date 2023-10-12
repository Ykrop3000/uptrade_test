from django import template
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import F, Subquery, OuterRef, AutoField, Prefetch
from django.template import RequestContext

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name: str):
    menu_items = MenuItem.objects.all()
    menu = [i for i in menu_items if i.title == menu_name][0]
    return {
        "menu": menu,
        "menu_items": menu_items,
    }


@register.inclusion_tag('sub_menu.html', takes_context=True)
def get_children(context, items: list, parent, level:int=0):
    result = []
    for item in items:
        if item.parent_id == parent.id:
            result.append(item)
    return {
        "context": context,
        "menu_items": items,
        "children": result,
        "level": level+1,
        "parent": parent
    }


@register.simple_tag(takes_context=True)
def is_active_menu_item(context: RequestContext, path):
    if path in context.request.path and len(path) != 0:
        return 'active'
    else:
        return ''
