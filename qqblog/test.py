from django.db import IntegrityError
from django.test import TestCase
from shop.models import Post

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
