#  BackendCode - Cookies
Documentation: https://docs.djangoproject.com/fr/3.2/intro/ <br>
By @tcotidiane33 & @yaya
## Models
### Premium
```python
class Pack(models.Model):
	name = models.CharField(max_length=255)
	items = models.IntegerField(default=1)
	
	class Meta:
		"""Meta definition for Pack."""

		verbose_name = "Pack"
		verbose_name_plural = "Pack"

	def __str__(self):
		return self.name

class Premium(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField(default=0)
	Packitems = models.ManyToManyField(Pack)

	class Meta:
		"""Meta definition for Premium."""

		verbose_name = "Premium"
		verbose_name_plural = "Premium"

	def __str__(self):
		return self.name
```
### Service
```python
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

	class Meta:
		"""Meta definition for Stacks."""

		verbose_name = "Stacks"
		verbose_name_plural = "Stacks"

	def __str__(self):
		return self.name

class Experts(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	description = models.TextField()
	phone = models.CharField(max_length=25)
	whatsapp = models.CharField(max_length=25)
	telegram = models.CharField(max_length=25)
	# image = models.ImageField(upload_to="images/experts/", height_field=None, width_field=None)
	satcks = models.ManyToManyField(Stacks)

	class Meta:
		"""Meta definition for Experts."""

		verbose_name = "Experts"
		verbose_name_plural = "Experts"

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
	description = models.TextField()
	tarifs = models.ManyToManyField(Tarifs)
	favoris = models.BooleanField(default=False)
	experts = models.ManyToManyField(Experts)

	class Meta:
		"""Meta definition for Services."""

		verbose_name = "Services"
		verbose_name_plural = "Services"

	def __str__(self):
		return self.name	
```
### Store
```python
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
```