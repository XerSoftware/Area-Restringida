from django.db import models

# Create your models here.
class CodigoAcceso(models.Model):
	ean13 = models.CharField(max_length=13)
	def __str__(self):
		return self.ean13
