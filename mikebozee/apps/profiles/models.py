from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	linkedin = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)

	def __str__(self):
		return self.first_name + ' ' + str(self.last_name)

	def _get_unique_slug(self):
		slug = slugify(self.title)
		unique_slug = slug
		num = 1
		while Profile.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)
