from django.shortcuts import render_to_response,render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from dajaxice.core import dajaxice_autodiscover,dajaxice_config
dajaxice_autodiscover()

@csrf_protect
def index(request):
	c = {}
	c.update(csrf(request))
	return render_to_response("test.html",c,context_instance=RequestContext(request))