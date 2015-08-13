from django.db import models

class ItemManager(models.Manager):
	def create_item(self, name, unit, grade):
		item = self.create(name=name, unit=unit, grade=grade)
		return item

class Item(models.Model):
	name = models.CharField(max_length=200)
	unit = models.CharField(max_length=20)
	grade = models.CharField(max_length=20)

	objects = ItemManager()

	@classmethod
	def create(cls, name, unit, grade):
		item = cls(name, unit, grade)
		return item


