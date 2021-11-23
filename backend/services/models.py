from django.db import models
from django.urls import reverse

# Create your models here.

class Competences(models.Model):
	name = models.CharField(max_length=255)

	class Meta:
		"""Meta definition for Competences."""

		verbose_name = "Competences"
		verbose_name_plural = "Competences"

	def __str__(self):
		return self.name

class Stacks(models.Model):
	name = models.CharField(max_length=255)
	competences = models.ManyToManyField(Competences)
	slug = models.SlugField(max_length=200, unique=True, null=True)

	class Meta:
		"""Meta definition for Stacks."""

		verbose_name = "Stacks"
		verbose_name_plural = "Stacks"

	def __str__(self):
		return self.name

class Experts(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	slug = models.SlugField(max_length=200, null=True)
	email = models.EmailField(unique=True)
	description = models.TextField()
	phone = models.CharField(max_length=25)
	whatsapp = models.CharField(max_length=25)
	telegram = models.CharField(max_length=25)
	note = models.IntegerField(default=3)
	# image = models.ImageField(upload_to="images/experts/", height_field=None, width_field=None)
	stacks = models.ManyToManyField(Stacks)

	class Meta:
		"""Meta definition for Experts."""

		verbose_name = "Experts"
		verbose_name_plural = "Experts"

	def get_absolute_url(self):
		return reverse('services:details_experts', args=[self.slug])

	def __str__(self):
		return self.name

class Tarifs(models.Model):
	name = models.CharField(max_length=25)
	items = models.IntegerField(default=1)
	price = models.CharField(max_length=10)

	class Meta:
		"""Meta definition for Tarifs."""

		verbose_name = "Tarifs"
		verbose_name_plural = "Tarifs"

	def __str__(self):
		return self.name

class Services(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=200, null=True)
	description = models.TextField()
	pub_date = models.DateTimeField('date published', null=True)
	tarifs = models.ManyToManyField(Tarifs)
	favoris = models.BooleanField(default=False)
	experts = models.ManyToManyField(Experts)

	class Meta:
		"""Meta definition for Services."""

		verbose_name = "Services"
		verbose_name_plural = "Services"
		ordering = ('-pub_date',)

	def get_absolute_url(self):
		return reverse('services:details', args=[self.slug])

	def __str__(self):
		return self.name	