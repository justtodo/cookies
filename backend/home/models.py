from django.db import models
from django.urls import reverse

# Create your models here.

class Packs(models.Model):
	name = models.CharField(max_length=255)
	items = models.IntegerField(default=1)
	
	class Meta:
		"""Meta definition for Pack."""

		verbose_name = "Packs"
		verbose_name_plural = "Packs"

	def __str__(self):
		return self.name

class Premium(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField(default=0)
	packs = models.ManyToManyField(Packs)

	class Meta:
		"""Meta definition for Premium."""

		verbose_name = "Premium"
		verbose_name_plural = "Premium"

	def __str__(self):
		return self.name