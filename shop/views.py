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
            spy = spyon(remoteIp=request.META['REMOTE_ADDR'], browser=request.META['HTTP_USER_AGENT'])
            spy.save()
            return redirect('shop.views.add')
    else:
            userName = User.objects.get(username=request.user.username)
            order = Order.objects.get(user=userName)
            totalPrice = order.get_total_price()
            spy = spyon(remoteIp=request.META['REMOTE_ADDR'], browser=request.META['HTTP_USER_AGENT'])
            spy.save()
            return render_to_response('cart.html', locals(), context_instance = RequestContext(request))    
            
def delete(request):
    if request.method == 'POST':
        form = OrderForm(request.POST or None)
        if form.is_valid():    
            userName = User.objects.get(username=request.user.username)
            order = Order.objects.get(user=userName)
            CartItem.objects.get(cartid=request.POST.get('deleteID')).delete()
            spy = spyon(remoteIp=request.META['REMOTE_ADDR'], browser=request.META['HTTP_USER_AGENT'])
            spy.save()
            return redirect('shop.views.add')
        else:
            userName = User.objects.get(username=request.user.username)
            order = Order.objects.get(user=userName)
            spy = spyon(remoteIp=request.META['REMOTE_ADDR'], browser=request.META['HTTP_USER_AGENT'])
            spy.save()
            return render_to_response('registration/base.html', locals(), context_instance = RequestContext(request))
    return redirect('shop.views.add')    
    
def display(request):
    sppyy = spyon.objects.get(remoteIp=request.META['REMOTE_ADDR'])
    if sppyy != null:
        sppyy.browser = request.META['HTTP_USER_AGENT']
        sppyy.save()
    else:
        spy = spyon(remoteIp=request.META['REMOTE_ADDR'], browser=request.META['HTTP_USER_AGENT'])
        spy.save()
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))