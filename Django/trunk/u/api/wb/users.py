from universal import explodeParams
import urllib,urllib2
import time
from django.conf import settings as _s
from django.utils import simplejson as _j


def show(token,**kwargs):
	url = _s.WB_API_URL+"users/show.json?"
	params['access_token']=token
	if 'uid' in kwargs:
		params['uid']=kwargs['uid']
	if 'screen_name' in kwargs:
		params['screen_name'] in kwargs
	url += explodeParams(params)
	pass