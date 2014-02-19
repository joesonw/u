# coding=utf-8
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from universal import explodePerms,getSig,pretty_time
from django.conf import settings as _s
import urllib2,urllib
from django.utils import simplejson as _j
from api.renren import getToken as renren_token
from api.qqt import getToken as qqt_token
from api.wb import getToken as wb_token
from api.renren import feed
from api.wb import statuses
import time as RealTime
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, time,timedelta

def home(request):
	_ss = request.session
	result={}
	if not 'renren_access_token' in _ss:
		return HttpResponseRedirect("/auth/renren")
	if not 'wb_access_token' in _ss:
		return HttpResponseRedirect("/auth/wb")
	
	renren_threads = feed.get(_ss['renren_access_token'])
	threads=[]
	wb_threads = statuses.home_timeline(_ss['wb_access_token'])
	wb_threads = wb_threads['statuses']
	for item in renren_threads:
		item['time_diff'],item['time_stamp']=pretty_time(datetime.strptime(item['update_time'],"%Y-%m-%d %H:%M:%S"))
		if 'attachment' in item:
			if item['attachment']:
				item['attachment']=item['attachment'][0]
		if item['comments']['count']!=0:
			for i in item['comments']['comment']:
				xx,i['time']=pretty_time(datetime.strptime(i['time'],"%Y-%m-%d %H:%M"))
		if 'trace' in item:
			if item['trace'] and item['feed_type'] in [21,23,32]:
				prefix=item['trace']['text']
				for i in item['trace']['node']:
					prefix=prefix.replace(i['name'],'<a target="_blank" href="http://www.renren.com/'+str(i['id'])+'">'+i['name']+'</a>')
				item['prefix']=prefix
		if item['feed_type'] == 30 and 'content' in item['attachment']:
			if item['attachment']['content']:
				item['prefix']='<article class="title">'+item['attachment']['content']+'</artcle>'
		elif item['feed_type']==30:
			item['prefix']='<article class="title">&nbsp;'+item['prefix']+u'&nbsp;至&nbsp;<a target="_blank" href="'+item['href']+'">'+item['title']+'</a></artcle>'
		item['thread_type']='renren'
		threads.append(item)
	for item in wb_threads:
		item['time_diff'],item['time_stamp']=pretty_time(datetime.strptime(" ".join([x for x in item['created_at'].split(" ")[1:]]),"%b %d %H:%M:%S +0800 %Y"))
		if 'retweeted_status' in item and item['retweeted_status']:
			xx,item['retweeted_status']['time_stamp']=pretty_time(datetime.strptime(" ".join([x for x in item['retweeted_status']['created_at'].split(" ")[1:]]),"%b %d %H:%M:%S +0800 %Y"))
		item['thread_type']='wb'
		threads.append(item)
	threads=sorted(threads,key=lambda k:k['time_diff'])
	return render_to_response('home.html',{'threads':threads})
	
