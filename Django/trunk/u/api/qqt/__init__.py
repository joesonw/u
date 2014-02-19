from django.conf import settings as _s
import urllib2,urllib
from django.utils import simplejson as _j	
from universal import explodeParams
import time,copy
import sys

def getToken(code,redirect_uri):
	request_url=_s.QQT_AUTH_URL+"access_token?grant_type=authorization_code"
	request_url+="&redirect_uri="+redirect_uri
	request_url+="&client_secret="+_s.QQT_SECRET
	request_url+="&code="+code
	request_url+="&client_id="+_s.QQT_APIKEY
	url=urllib2.urlopen(request_url)
	result=url.read()
	arr=result.split("&")
	result={}
	result['access_token']=arr[0].split("=")[1]
	result['expires_in']=arr[1].split("=")[1]
	result['refresh_token']=arr[2].split("=")[1]
	result['openid']=arr[3].split("=")[1]
	result['name']=arr[4].split("=")[1]
	result['nick']=arr[5].split("=")[1]
	return result