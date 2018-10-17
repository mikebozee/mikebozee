from django import template

register = template.Library()

from ..models import Education


@register.filter(name='sort_educations')
def sort_educations(queryset, order):
	return queryset.order_by(order)