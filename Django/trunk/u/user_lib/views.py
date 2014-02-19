# Create your views here.
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from universal import explodePerms,getSig
from django.conf import settings as _s
import urllib2,urllib
from django.utils import simplejson as _j
from api.renren.users import getVisitors
from api.renren import getToken as renren_token
from api.qqt import getToken as qqt_token
from api.wb import getToken as wb_token
import time
from django.contrib.auth.decorators import login_required

def Bind_login(request):
	_g = request.GET
	if not 'platform' in _g:
		raise Http404
	if not _g['platform']:
		raise Http404
	
#@login_required(login_url="/login/")
def Renren_login(request):
	_g=request.GET
	if not 'code' in _g:
		url =_s.RENREN_AUTH_URL
                url += "grant?client_id="+_s.RENREN_APIKEY
                url += "&scope="+explodePerms(_s.RENREN_PERMS)
                url += "&response_type=code"
                redirect_uri="http://u.djwong.net:8000/auth/renren/?next="
                if 'next' in _g:
                        if _g['next']:
                                redirect_uri+=_g['next']
                else:
                        redirect_uri += "/"
                                
                url += "&redirect_uri="+urllib.quote(redirect_uri)
                return HttpResponseRedirect(url)
	if not _g['code']:
		raise Http404()
	else:	
		redirect_uri="http://u.djwong.net:8000/auth/renren/?next="
		if 'next' in _g:
                        if _g['next']:
                                redirect_uri+=_g['next']
                else:
                        redirect_uri+="/"
		result = renren_token(_g['code'],urllib.quote(redirect_uri))
		_ss=request.session
		_ss['renren_access_token']=result['access_token']
		_ss['renren_expires']=result['expires_in']+time.time()
		_ss['renren_user']=result['user']
		if 'next' in _g:
			if 'call_back' in _g['next']:
				func = _g['next'].split(".")[1][:-1]
				return HttpResponse('<script>window.opener.'+func+';window.close();</script>')
    	return HttpResponseRedirect(_g['next'])

#@login_required(login_url="/login/")
def QQT_login(request):
	_g=request.GET
	if not 'code' in _g:
                url=_s.QQT_AUTH_URL+"authorize?response_type=code"
                url+="&client_id="+_s.QQT_APIKEY
                redirect_uri="http://u.djwong.net:8000/auth/qqt/?next="
                if 'next' in _g:
                        if _g['next']:
                                redirect_uri+=_g['next']
                else:
                        redirect_uri += "/"
                        
                url+="&redirect_uri="+urllib.quote(redirect_uri)
                return HttpResponseRedirect(url)
	if not _g['code']:
                raise Http404()
        else:
		redirect_uri="http://u.djwong.net:8000/auth/qqt/?next="
		if 'next' in _g:
                        if _g['next']:
                                redirect_uri+=_g['next']
                else:
                        redirect_uri+='/'
		result = qqt_token(_g['code'],urllib.quote(redirect_uri))
		_ss=request.session
		_ss['qqt_access_token']=result['access_token']
		_ss['qqt_expires']=float(result['expires_in'])+time.time()
		_ss['qqt_openid']=result['openid']
		_ss['qqt_name']=result['name']
		_ss['qqt_nick']=result['nick']
		if 'next' in _g:
			if 'call_back' in _g['next']:
				func = _g['next'].split(".")[1][:-1]
				return HttpResponse('<script>window.opener.'+func+';window.close();</script>')
		return HttpResponseRedirect(_g['next'])
		

#@login_required(login_url="/login/")
def WB_login(request):
	_g=request.GET
	if not 'code' in _g:                
                url=_s.WB_AUTH_URL+"authorize?client_id="+_s.WB_APIKEY
                url+="&response_type=code"
                redirect_uri="http://u.djwong.net:8000/auth/wb/?next="
                if 'next' in _g:
                        if _g['next']:
                                redirect_uri+=_g['next']
                else:
                        redirect_uri += "/"
                url+="&redirect_uri="+urllib.quote(redirect_uri)
                return HttpResponseRedirect(url)
	if  not _g['code']:
                raise Http404()
        else:
		redirect_uri="http://u.djwong.net:8000/auth/wb/?next="
		if 'next' in _g:
                        if _g['next']:
                                redirect_uri+=_g['next']
                else:
                        redirect_uri += "/"
		result=wb_token(_g['code'],redirect_uri)
		_ss = request.session
		_ss['wb_access_token']=result['access_token']
		_ss['wb_remind_in']=result['remind_in']
		_ss['wb_expires']=float(result['expires_in'])+time.time()
		_ss['wb_uid']=result['uid']
		if 'next' in _g:
			if 'call_back' in _g['next']:
				func = _g['next'].split(".")[1][:-1]
				return HttpResponse('<script>window.opener.'+func+';window.close();</script>')
		return HttpResponseRedirect(_g['next'])
		
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
