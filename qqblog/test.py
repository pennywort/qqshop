from django.db import IntegrityError
from django.test import TestCase
from shop.models import Post
from shop.models import CartItem

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