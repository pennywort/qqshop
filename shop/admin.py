from django.contrib import admin
from shop.models import Post
from shop.models import CartItem
from shop.models import Order
from shop.models import spyon
from shop.models import AcceptedOrder

admin.site.register(Post)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(spyon)
admin.site.register(AcceptedOrder)