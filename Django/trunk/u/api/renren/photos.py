from universal import explodePerms,getSig
import urllib,urllib2
import time
from django.conf import settings as _s
from django.utils import simplejson as _j

v="1.0"
format="JSON"
def upload(token,filename,caption="",aid="",place_id=""):
	register_openers()
	params={}
	image=open(filename, "rb")
	params['method']='photos.upload'
	params['api_key']=_s.RENREN_APIKEY
	params['call_id']=str(time.time())
	params['v']='1.0'
	params['format']='json'
	params['access_token']=token
	params['sig']=getSig(params)
	BOUNDARY = mimetools.choose_boundary()
	L = []
	for k,v in params.items():
		L.append('--'+BOUNDARY)
		L.append('Content-Disposition: form-data; name="%s"' % k)
		L.append('')
		L.append(v)
	L.append('--'+BOUNDARY)
	L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('upload', filename))
	L.append('Content-Type: image/jpg')
	L.append('')
	L.append(image.read())
	L.append('--' + BOUNDARY + '--')
	L.append('')
	body = "\r\n".join([str(x) for x in L])
	content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
	header = {'Content-Type':content_type,'Content-Length':str(len(body))}
	request = urllib2.Request(_s.RENREN_API_URL,body,header)
	result = urllib2.urlopen(request)
	result = result.read()
	image.close()
	return result
	
def getComments(token,uid,**kwargs):
	params={}
	if 'aid' in kwargs:
		params['aid']=kwargs['aid']
	if 'pid' in kwargs:
		params['pid']=kwargs['pid']
	if not ('pid' in kwargs and 'aid' in kwargs):
		return None
	params['access_token']=token
	params['v']=v
	params['format']=format
	params['call_id']=time.time()
	params['method']='photos.getComments'
	params['sig']=getSig(params)
	result=urllib2.urlopen(_s.RENREN_API_URL,urllib.urlencode(params))
	result=_j.loads(result.read())
	return result