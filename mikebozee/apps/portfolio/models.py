from django.db import models
from django.utils import timezone

class Project(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def was_published_recently(self):
		return self.published_date >= timezone.now() - datetime.timedelta(days=7)

	def __str__(self):
		return self.title
