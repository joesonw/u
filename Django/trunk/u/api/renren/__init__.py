from django.conf import settings as _s
import urllib2,urllib
from django.utils import simplejson as _j	
from universal import explodePerms,getSig
import time,copy
import sys
def getToken(code,redirect_uri):
	request_url=_s.RENREN_AUTH_URL+"token?grant_type=authorization_code"
	request_url+="&redirect_uri="+redirect_uri
	request_url+="&client_secret="+_s.RENREN_SECRET
	request_url+="&code="+code
	request_url+="&client_id="+_s.RENREN_APIKEY
	url=urllib2.urlopen(request_url)
	result=url.read()
	result=_j.loads(result)
	return result
