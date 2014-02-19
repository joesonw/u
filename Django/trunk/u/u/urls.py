from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover,dajaxice_config
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

dajaxice_autodiscover()
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home',),
    # url(r'^u/', include('u.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dajaxice/', include('dajaxice.urls')),
    url(r'^resources/(?P<path>.*)$','django.views.static.serve',{'document_root':'resources'}),
    
    url(r'^test/$', 'dt.views.index'),
    url(r'^auth/renren/','user_lib.views.Renren_login'),
    url(r'^auth/qqt/','user_lib.views.QQT_login'),
    url(r'^auth/wb/','user_lib.views.WB_login'),
    #url(r'^login/','user_lib.views.Bind_login'),
    url(r'^register/$','views.index.register'),
    url(r'^upload/$','views.index.upload'),
)

urlpatterns += staticfiles_urlpatterns()
