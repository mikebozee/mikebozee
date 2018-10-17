from django import template

register = template.Library()

from ..models import Article


@register.filter(name='sort_articles')
def sort_articles(queryset, order):
	return queryset.order_by(order)