# Django settings for u project.

QQT_APIKEY="801295742"
QQT_SECRET="0b1f590aa2241e1a15fce31c4ba90473"
QQT_AUTH_URL="https://open.t.qq.com/cgi-bin/oauth2/"
QQT_API_URL="http://open.t.qq.com/api/"

WB_APIKEY="4245996411"
WB_SECRET="6648c49aca640d70c08ea647342c4016"
WB_AUTH_URL="https://api.weibo.com/oauth2/"
WB_API_URL="https://api.weibo.com/2/"

RENREN_SECRET='1a55813f776c425c8588a7b7871b95d8'
RENREN_APIKEY='edff1d2f1c6240ddb2e04f9dc28739b7'
RENREN_PERMS=[
	'read_user_blog',
	'read_user_checkin',
	'read_user_feed',
	'read_user_guestbook',
	'read_user_invitation',
	'read_user_like_history',
	'read_user_message',
	'read_user_notification',
	'read_user_photo',
	'read_user_status',
	'read_user_album',
	'read_user_comment',
	'read_user_share',
	'read_user_request',
	'publish_blog',
	'publish_checkin',
	'publish_feed',
	'publish_share',
	'write_guestbook',
	'send_invitation',
	'send_request',
	'send_message',
	'send_notification',
	'photo_upload',
	'status_update',
	'create_album',
	'publish_comment',
	'operate_like'
				]
RENREN_AUTH_URL="http://graph.renren.com/oauth/"
RENREN_API_URL="http://api.renren.com/restserver.do"

DEBUG = True
TEMPLATE_DEBUG = DEBUG
AUTH_USER_MODEL = "user_lib.Member"
DAJAXICE_MEDIA_PREFIX="dajaxice"

DAJAXICE_DEBUG = True
DAJAX_FUNCTIONS = (
		'dajax_lib.ajax.register',
		'dajax_lib.ajax.retreive_auth',
		'dajax_lib.ajax.call_api',
)
DAJAX_JS_FRAMEWORK = "jQuery"
ADMINS = (
     ('joesonw', 'joesonw@gmail.com'),
)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'djwongdjango',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'djwongdjango',
        'PASSWORD': 'Jj@920403',
        'HOST': '97.74.31.18',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l!v+=i$s=ttt-v20)#$oh(p$=alk=zqx#)3h3e&9=!r0t5fegx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',   
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'u.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'u.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "templates",
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'thread_lib', 
    'api',
    'api.renren',
    'api.qqt',
    'api.wb',
    'user_lib',
    'views',
    'universal',
    'dajax_lib',
    'dajaxice',
    'dajax',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
