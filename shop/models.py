from django.db import models
from django.contrib import admin
class Post(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField("Product name", max_length = 140)
	articleNumber = models.CharField("Article number", max_length = 20)
	body = models.TextField("Short description")
	description = models.TextField("Full description", blank = True)
	date = models.DateTimeField("Adding date", blank = True)
	photo = models.ImageField("Product photo", upload_to='upload/', blank=True)
	priceOfProduct = models.DecimalField(max_digits=12, decimal_places=2)
	def __unicode__(self):
		return self.title + " " + self.articleNumber


