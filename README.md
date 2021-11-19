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
### Person
### Expert