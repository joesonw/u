from universal import explodePerms,getSig
import urllib,urllib2
import time
from django.conf import settings as _s
from django.utils import simplejson as _j

v="1.0"
format="JSON"
def getInfo(token,uids="",fields=""):
	params={}
	if uids:
		params['uids']=uids
	if fields:
		params['fields']=fields
	params['access_token']=token
	params['v']=v
	params['format']=format
	params['call_id']=int(time.time())
	params['method']='users.getInfo'
	params['sig']=getSig(params)
	result=urllib2.urlopen(_s.RENREN_API_URL,urllib.urlencode(params))
	result=_j.loads(result.read())
	return result
	
def getLoggedInUser(token):
	params={}
	params['access_token']=token
	params['v']=v
	params['format']=format
	params['call_id']=int(time.time())
	params['method']='users.getLoggedInUser'
	params['sig']=getSig(params)
	result=urllib2.urlopen(_s.RENREN_API_URL,urllib.urlencode(params))
	result=_j.loads(result.read())
	return result
	
def getProfileInfo(token,uid,fields=""):
	params={}
	if fields:
		params['fields']=fields
	params['access_token']=token
	params['v']=v
	params['format']=format
	params['call_id']=int(time.time())
	params['method']='users.getProfileInfo'
	params['uid']=uid
	params['sig']=getSig(params)
	result=urllib2.urlopen(_s.RENREN_API_URL,urllib.urlencode(params))
	result=_j.loads(result.read())
	return result
	
def getVisitors(token,page=0,count=0):
	params={}
	if page:
		params['page']=page
	if count:
		params['count']=count
	params['access_token']=token
	params['v']=v
	params['format']=format
	params['call_id']=int(time.time())
	params['method']='users.getVisitors'
	params['sig']=getSig(params)
	result=urllib2.urlopen(_s.RENREN_API_URL,urllib.urlencode(params))
	result=_j.loads(result.read())
	return result