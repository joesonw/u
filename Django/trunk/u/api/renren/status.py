from universal import explodePerms,getSig,pretty_time
import urllib,urllib2
import time
from django.conf import settings as _s
from django.utils import simplejson as _j
from datetime import datetime
v="1.0"
format="JSON"

def getComment(token,status_id,owner_id):
	params={}
	params['access_token']=token
	params['v']=v
	params['status_id']=status_id
	params['owner_id']=owner_id
	params['format']=format
	params['call_id']=int(time.time())
	params['method']='status.getComment'
	params['sig']=getSig(params)
	result=urllib2.urlopen(_s.RENREN_API_URL,urllib.urlencode(params))
	result=_j.loads(result.read())
	for i in result:
		xx,i['time']=pretty_time(datetime.strptime(i['time'],"%Y-%m-%d %H:%M:%S"))
	return result