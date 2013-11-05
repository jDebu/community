from django.db import models
import datetime

class Pizza(models.Model):
	pizza_id= models.PositiveIntegerField()
	pizza_nombre=models.CharField(max_length=256)
	pizza_precio=models.CharField(max_length=64)
	#fecha=models.DatetimeField(default=datetime,datetime.now)

	def __unicode__(self):
		return "%s, %s (%s)" % (self.pizza_id, self.pizza_nombre, self.pizza_precio)

	class Meta:
		ordering=['pizza_id']
	