from django import template

register = template.Library()

from ..models import Reference


@register.filter(name='slugify_relationships')
def slugify_relationships(value):
	relationships = list(value)
	relationships_string = ''

	for relationship in relationships:
		relationship = relationship.replace('\'', '')
		relationship = relationship.replace(' ', '-')
		relationship = relationship.lower()
		relationships_string = relationships_string + ' ' + relationship

	return relationships_string