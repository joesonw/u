from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from django.utils import simplejson as _j
from django.conf import settings as _s
from api import renren
from api import wb
from api import qqt
from api.wb import statuses
from api.renren import status
from universal import explodePerms

@dajaxice_register(method='get')
def register(request,email,pwd):
	return _j.dumps({'result':True})
	
@dajaxice_register
def retreive_auth(request):
	_ss = request.session
	result={}
	if 'renren_access_token' in _ss.keys():
		if _ss['renren_access_token']!='':
			result['renren']=_ss['renren_access_token']
	if 'wb_access_token' in _ss.keys():
		if _ss['wb_access_token']!='':
			result['wb']=_ss['wb_access_token']
	if 'qqt_access_token' in _ss.keys():
		if _ss['qqt_access_token']!='':
			result['qqt']=_ss['qqt_access_token']
	return _j.dumps({'result':result})
	
@dajaxice_register(method='get')
def call_api(request,request_method,**kwargs):
	function_str = request_method+"("
	if kwargs['lib']=="renren":
		del kwargs['lib']
		kwargs['token']=request.session['renren_access_token']
	elif kwargs['lib']=="wb":
		del kwargs['lib']
		kwargs['token']=request.session['wb_access_token']
	for key in kwargs:
		function_str+=(str(key)+"="+"'"+str(kwargs[key])+"'"+",")
	function_str=function_str[:-1]
	function_str+=")"
	result=eval(function_str)
	result_d={}
	result_d['result']=result
	for k in kwargs:
		result_d[k]=kwargs[k]
	return _j.dumps(result_d)
	