from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField

class Reference(models.Model):
	RELATIONSHIP_CHOICES = (
	   ('Direct supervisor', 'Direct supervisor'),
	   ('Coworker', 'Coworker'),
	   ('Client', 'Client'),
	   ('Instructor', 'Instructor'),
	   ('Mentor', 'Mentor'),
	   ('Vendor', 'Vendor'),
	)

	published = models.BooleanField(default=False)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	text = RichTextUploadingField()
	created_date = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(max_length=50, unique=True)
	image = models.ImageField(blank=True, null=True)
	link = models.URLField(blank=True, null=True)
	relationship = MultiSelectField(choices=RELATIONSHIP_CHOICES, blank=True)
	positions = models.ManyToManyField('positions.Position', blank=True)
	projects = models.ManyToManyField('projects.Project', blank=True)
	educations = models.ManyToManyField('educations.Education', blank=True)
	notes = RichTextUploadingField(blank=True, null=True)
	priority = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.first_name + ' ' + str(self.last_name)

	def _get_unique_slug(self):
		slug = slugify(self.first_name + ' ' + str(self.last_name))
		unique_slug = slug
		num = 1
		while Reference.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def full_name(reference):
		return "%s %s" % (reference.first_name, reference.last_name)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)	
