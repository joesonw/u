from django.conf import settings as _s
import urllib2,urllib
from django.utils import simplejson as _j	
from universal import explodeParams,getSig
import time,copy
import sys

def get(token,feed_type=""):
	params={}
	params['access_token']=token
	params['format']='JSON'
	params['v']='1.0'
	params['call_id']=time.time()
	params['method']='feed.get'
	if feed_type=="":
		params['type']='10,11,20,21,22,23,30,31,32,33,34,35,36,40,41,50,51,52,53,54,55'
	else:
		params['type']=feed_type
	params['sig']=getSig(params)
	url = urllib2.urlopen(_s.RENREN_API_URL,urllib.urlencode(params))
	result = url.read()
	result = _j.loads(result)
	return result


