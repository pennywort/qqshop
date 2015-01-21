from django.db import IntegrityError
from django.test import TestCase
import datetime
from django.contrib.auth.models import User
from shop.models import Post
from shop.models import CartItem
from shop.models import Order
from shop.models import AcceptedOrder

class ProductTest(TestCase):
  def test_post(self):
    with self.assertRaises(IntegrityError):
      p = Post()
      p.save()
  def test_double(self):
    with self.assertRaises(IntegrityError):
      p = Post.objects.create(
        priceOfProduct = 2391.01
      )
	  
class CartItemTest(TestCase):
  def test_cart_item(self):
    with self.assertRaises(IntegrityError):
      p = CartItem.objects.create(
        product = Post(),
      )
	  
class OrderTest(TestCase):	  
  def test_order(self):
    p = Order(
        date_added = datetime.datetime.today(),
		user = User(username="tester")
		)
    self.assertEqual(p.get_user(), "tester" )

