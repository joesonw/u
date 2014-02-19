from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover,dajaxice_config
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

dajaxice_autodiscover()
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'u.views.home', name='home'),
    # url(r'^u/', include('u.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dajaxice/', include('dajaxice.urls')),
    url(r'^resources/(?P<path>.*)$','django.views.static.serve',{'document_root':'resources'}),
    
    url(r'^test/$', 'dt.views.index'),
    url(r'^login/renren/$','user_lib.views.Renren_login'),
    url(r'^login/renren/auth/','user_lib.views.Renren_login_auth'),
    url(r'^login/qqt/$','user_lib.views.QQT_login'),
    url(r'^login/qqt/auth/','user_lib.views.QQT_login_auth'),
    url(r'^login/wb/$','user_lib.views.WB_login'),
    url(r'^login/wb/auth/','user_lib.views.WB_login_auth'),
    url(r'^login/','user_lib.views.Bind_login'),
    url(r'^register/$','views.index.register'),
)

urlpatterns += staticfiles_urlpatterns()