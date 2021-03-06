from django.forms import widgets
from rest_framework import serializers
from modeldata.models import Item

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('name', 'unit', 'grade')
