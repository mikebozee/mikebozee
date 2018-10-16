from django import template

register = template.Library()

from ..models import Project


@register.filter(name='sort_projects')
def sort_projects(queryset, order):
	return queryset.order_by(order)