from django.db import models

class Email(models.Model):
	address = models.CharField(max_length=200)
	def __str__(self):
		return self.address
