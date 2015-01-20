from django.db import models
from django.contrib import admin
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
import decimal

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
		
class CartItem(models.Model):
	cart_id = models.AutoField(primary_key=True)
	cartid = models.CharField(max_length = 20)
	quantity = models.IntegerField(default = 0)
	product = models.ForeignKey(Post)
	user = models.ForeignKey(User)
	price =  models.DecimalField(max_digits=12, decimal_places=2, blank=False)
	def __unicode__(self):
		return "cart for " + self.user.username
	
class Order(models.Model):
	products = models.ManyToManyField(CartItem, blank=True)
	date_added = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User)
	totalPrice = models.DecimalField("Total price", max_digits=12, decimal_places=2, default=0)
	iprice = models.IntegerField("IPRICE", default=0)
	def get_total_price(self):
		for prdct in self.products.all():
	             self.iprice += prdct.price
		return self.iprice
		
	def get_user(self):
		return self.user
		
	def get_products(self):
		return self.products
		
	def get_date_added(self):
		return self.date_added

	def __unicode__(self):
		return "orders for " + self.user.username + str(self.get_total_price())
		
	def create_user_cart(sender, instance, created, **kwargs):  
		if created:  
		   cart, created = Order.objects.get_or_create(user=instance)  
	post_save.connect(create_user_cart, sender=User) 
	
class AcceptedOrder(models.Model): 
	is_accepted = models.BooleanField(blank=True, default=False)
	productlist = models.ManyToManyField(CartItem, blank=True)
	dateadded = models.DateTimeField("Date added", blank=True, null=True)
	user = models.ForeignKey(User, blank = True)
	def accept(self):
		self.is_accepted = True