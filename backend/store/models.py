from django.db import models
from django.urls import reverse

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=255)
    # image = models.ImageField(upload_to="images/", height_field=None, width_field=None)
 
    class Meta:
        """Meta definition for Images."""

        verbose_name = "Images"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.name

class Produit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    image = models.ManyToManyField(Images)
    number = models.IntegerField(default=1)
    price = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    class Meta:
        """Meta definition Produit."""

        verbose_name = "Produit"
        verbose_name_plural = "Produit"

    def get_absolute_url(self):
        return reverse('produit:detail', args=[self.slug])

    def __str__(self):
        return self.name