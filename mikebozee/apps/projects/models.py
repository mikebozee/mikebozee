from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Project(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	slug = models.SlugField(max_length=50, unique=True)

	def __str__(self):
		return self.title

	def _get_unique_slug(self):
		slug = slugify(self.title)
		unique_slug = slug
		num = 1
		while Project.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		self.published_date = timezone.now()
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)

	def was_published_recently(self):
		return self.published_date >= timezone.now() - datetime.timedelta(days=7)

	
