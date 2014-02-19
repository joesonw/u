from universal import explodeParams
import urllib,urllib2
import time
from django.conf import settings as _s
from django.utils import simplejson as _j


def home_timeline(token,**kwargs):
	params={}
	request_url = _s.WB_API_URL+"statuses/home_timeline.json?"
	params['access_token']=token
	request_url += explodeParams(params)
	print request_url
	url=urllib2.urlopen(request_url)
	result=url.read()
	result=_j.loads(result)
	return result