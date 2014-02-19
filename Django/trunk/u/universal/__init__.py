# coding=utf-8
import hashlib
from datetime import datetime, date, time,timedelta
from django.conf import settings as _s
encode_chart = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM+-0123456789'

def shortURL(url):
	m = int(md5(url)[8:24],16)
	b = str(bin(m))[2:]
	b = ((64-len(b))*'0'+b)[:-4]
	result=""
	for i in range(0,60,6):
		index=int(b[i:i+6],2)
		result+=encode_chart[index]
	return result
		
		

def md5(arg):
	m = hashlib.md5()
	m.update(arg)
	return m.hexdigest()
	
def explodePerms(arr):
	re=""
	l=len(arr)
	for i in range(0,l-1):
		re+=arr[i]+"+"
	re+=arr[l-1]
	return re

def getSig(params):
	s=""
	for k in sorted(params.iterkeys()):
		s+=(str(k)+"="+str(params[k]))
	s+=_s.RENREN_SECRET
	return md5(s)

def explodeParams(arr):
	result=""
	for k in sorted(arr.iterkeys()):
		result+=(str(k)+"="+str(arr[k])+"&")
	result=result[:-1]
	return result
def escape(s):
        result=s
        result=result.replace("%","%25")
        result=result.replace("+","%2B")
        result=result.replace(" ","%20")
        result=result.replace("/","%2F")
        result=result.replace("?","%3F")
        result=result.replace("#","%23")
        result=result.replace("&","%26")
        result=result.replace("=","%3D")
        return result

def pretty_time(s_time):
	cur_time = datetime.utcnow() + timedelta(hours=8)
	diff = cur_time-s_time
	if diff.days==0 and diff.seconds < 60:
		return diff,u'刚才'
	if diff.days==0 and diff.seconds < 3600:
		return diff,(str((diff.seconds/60))+u' 分钟之前')
	if diff.days==0 and diff.seconds < 86400:
		return diff,(str((diff.seconds/3600))+u' 小时之前')
	if diff.days<7:
		return diff,(str((diff.days))+u' 天之前')
	return diff,s_time.strftime("%Y.%m.%d %H:%M:%S")
