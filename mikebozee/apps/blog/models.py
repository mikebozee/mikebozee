from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	slug = models.SlugField(max_length=50, unique=True)

	def publish(self):
		self.published_date = timezone.now()
		self.slug = slugify(self.title)
		self.save()

	def was_published_recently(self):
		return self.published_date >= timezone.now() - datetime.timedelta(days=7)

	def __str__(self):
		return self.title
