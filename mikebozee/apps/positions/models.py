import datetime

from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class Position(models.Model):
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	location = models.CharField(max_length=50)
	start_date = models.DateField()
	end_date = models.DateField(default=datetime.date.today, blank=True, null=True)
	text = RichTextUploadingField()
	created_date = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(max_length=50, unique=True)
	image = models.ImageField(blank=True, null=True)

	tags = TaggableManager()

	def __str__(self):
		return self.title

	def _get_unique_slug(self):
		slug = slugify(self.title + self.company)
		unique_slug = slug
		num = 1
		while Position.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)
