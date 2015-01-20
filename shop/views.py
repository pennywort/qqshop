from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse
from shop.models import CartItem
from shop.models import Order
from shop.models import Post
from shop.forms import OrderForm

def add(request):
	if request.method == 'POST':
		form = OrderForm(request.POST or None)
		if form.is_valid():	
			userName = User.objects.get(username=request.user.username)
			product = Post.objects.get(id= request.POST.get('article'))
			photo = product.photo
			order = Order.objects.get(user=userName)
			cart = CartItem(product = product, quantity = 1, user = userName, price = product.priceOfProduct )
			cart.save()
			cart.cartid = cart.cart_id
			cart.save()
			order.products.add(cart) 
			order.save()
			return redirect('shop.views.add')