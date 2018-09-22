from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField


class Recommendation(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	text = RichTextUploadingField()
	created_date = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(max_length=50, unique=True)
	image = models.ImageField(blank=True, null=True)
	link = models.URLField(blank=True, null=True)
	# position = models.ManyToManyField('positions.Position', blank=True, null=True)

	def __str__(self):
		return self.first_name + ' ' + str(self.last_name)

	def _get_unique_slug(self):
		slug = slugify(self.first_name + ' ' + str(self.last_name))
		unique_slug = slug
		num = 1
		while Recommendation.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)	