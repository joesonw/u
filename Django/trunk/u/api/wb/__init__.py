from django.conf import settings as _s
import urllib2,urllib
from universal import explodeParams
from django.utils import simplejson as _j
import time,copy
import sys

def getToken(code,redirect_uri):
	params={}
	params['grant_type']='authorization_code'
	params['redirect_uri']=redirect_uri
	params['client_id']=_s.WB_APIKEY
	params['client_secret']=_s.WB_SECRET
	params['code']=code
	url=urllib2.urlopen(_s.WB_AUTH_URL+"access_token",urllib.urlencode(params))
	result=url.read()
	result=_j.loads(result)
	return result