# coding=utf-8
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from universal import explodePerms,getSig
from django.conf import settings as _s
import urllib2, mimetools, mimetypes
import webbrowser
import hashlib
from urllib import urlencode
from django.utils import simplejson as _j
import time
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

def register(request):
	return render_to_response('register.html')
	
def upload(request):
	params={}
	params['access_token']=request.session['renren_access_token']
	params['v']='1.0'
	params['format']='json'
	params['call_id']=str(time.time())
	params['method']='photos.getAlbums'
	params['uid']=request.session['renren_user']['id']
	params['sig']=getSig(params)
	result=urllib2.urlopen(_s.RENREN_API_URL,urlencode(params))
	result=_j.loads(result.read())
	return HttpResponse(str(result[0]))
	