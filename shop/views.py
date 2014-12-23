from django.shortcuts import render_to_response
from django.template import RequestContext
 
def index(request):
    return render_to_response('shop/templates/base.html', context_instance=RequestContext(request))
# Create your views here.
def index(request):
    return render_to_response('shop/templates/base.html')