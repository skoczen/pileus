from base import *
ENV = "STAGING"
ROLE = ENV
SITE_ID = 3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pileus',
        'USER': 'pileusdb',
        'PASSWORD': '7eN7PsYUqmF4ymWjQnIHCTRYnA3QsIg96He',        
        'HOST': 'int-mysql-master.digitalmycelium.com',
        'PORT': '3306',
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pileus',
        'USER': 'pileusdb',
        'PASSWORD': '7eN7PsYUqmF4ymWjQnIHCTRYnA3QsIg96He',        
        'HOST': 'int-mysql-slave.digitalmycelium.com',
        'PORT': '3306',
    },
}
DATABASE_ROUTERS = ['balancer.routers.PinningWMSRouter']

DATABASE_POOL = {
    'default': 2,
    'slave': 1,
}
MASTER_DATABASE = 'default'
BASE_DOMAIN = "digitalmycelium.com"

MEDIA_URL = 'http://media.digitalmycelium.com/'
MANUAL_MEDIA_URL = 'http://digitalmycelium.com/media/'
STATIC_URL = MEDIA_URL
ADMIN_MEDIA_PREFIX = "/admin-media/"
FAVICON_URL = "%simages/favicon.png" % MEDIA_URL
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

BROKER_HOST = "int-Redis.digitalmycelium.com"  # Maps to redis host.
BROKER_VHOST = "6"                       # Maps to database number.
REDIS_HOST = BROKER_HOST
REDIS_DB = BROKER_VHOST


# CACHES = {
#     'default': {
#         'BACKEND' : 'johnny.backends.memcached.MemcachedClass',
#         'LOCATION': '127.0.0.1:11211',
#         'PREFIX':ENV,
#         'JOHNNY_CACHE':True,
#     }
# }

# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
# CACHE_BACKEND = 'johnny.backends.memcached://127.0.0.1:11211'
CACHE_BACKEND = 'johnny.backends.memcached://int-Memcached1010.digitalmycelium.com:11211'

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_STORAGE_BUCKET_NAME = "goodcloud-public-staging"
AWS_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME
CDN_MEDIA_URL = "https://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME

# django-mediasync
MEDIASYNC['AWS_BUCKET'] = AWS_STORAGE_BUCKET_NAME
MEDIA_URL = CDN_MEDIA_URL
STATIC_URL = MEDIA_URL
STATIC_ROOT = MEDIA_ROOT


 
from git import Repo
try:
    GIT_CURRENT_SHA = Repo(PROJECT_ROOT).commit("%s_release" % ROLE.lower()).hexsha
except:
    GIT_CURRENT_SHA = Repo(PROJECT_ROOT).head.reference.commit.hexsha
MEDIASYNC["AWS_PREFIX"] = GIT_CURRENT_SHA

from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())

