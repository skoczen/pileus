
# Django settings for mycelium project.
DEBUG = False
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

import os, sys
from os.path import abspath, dirname, join
gettext = lambda s: s

PROJECT_ROOT = join(abspath(dirname(__file__)), "../")
STATIC_ROOT = join(abspath(PROJECT_ROOT),"media")
MEDIA_ROOT = abspath(STATIC_ROOT)
LIB_DIR = join(PROJECT_ROOT, 'lib')
APPS_DIR = join(PROJECT_ROOT, 'apps')
sys.path.insert(0, abspath(PROJECT_ROOT))
sys.path.insert(0, LIB_DIR)
sys.path.insert(0, APPS_DIR)


DEFAULT_FROM_EMAIL = 'GoodCloud'
SERVER_EMAIL = 'support@agoodcloud.com'
SEND_BROKEN_LINK_EMAILS = True

ADMINS = [
     ('Steven Skoczen', 'steven@agoodcloud.com'),
]
MANAGERS = ADMINS
SENTRY_ADMINS = ADMINS

TIME_ZONE = ""
LANGUAGE_CODE = 'en'
LANGUAGES = (
        # ('fr', gettext('French')),
        # ('de', gettext('German')),
        ('en', gettext('English')),
)
SITE_ID = 1

USE_I18N = True
# USE_L10N = True



# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd^bkm43rw#gmxbs4bvf)8)2)n=l9obc9-*022=hcm_s0w2bikt'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'johnny.middleware.LocalStoreClearMiddleware',
    'johnny.middleware.QueryCacheMiddleware',
    'johnny.middleware.CommittingTransactionMiddleware',

    # "mezzanine.core.middleware.DeviceAwareUpdateCacheMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
        
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    # "mezzanine.core.middleware.DeviceAwareFetchFromCacheMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelector",
)



AUTHENTICATION_BACKENDS = (
    # 'accounts.backends.AccountAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

COMMENTS_DISQUS_API_PUBLIC_KEY = "viSis4dDO5hqhxsHSDez5jY5I6LfNbDZm7y3Q4YQNHvmlxuPViLO3BX0ni4GsXUJ"
COMMENTS_DISQUS_API_SECRET_KEY = "x49kPmlykYQRGZMPBmzjvsLAln7KiD2f5r21A7cYPF27aW2vl5k1WcPWfoownEPu"
COMMENTS_DISQUS_SHORTNAME = "goodcloud"

SSL_ENABLED = True

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    
    # "cms.context_processors.media",
    "qi_toolkit.context_processors.add_env_to_request",
    "qi_toolkit.context_processors.add_favicon_to_request",    

    "mezzanine.conf.context_processors.settings",
)

DATE_INPUT_FORMATS = ('%m/%d/%Y', '%Y-%m-%d', '%m/%d/%y', '%b %d %Y',
'%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y',
'%B %d, %Y', '%d %B %Y', '%d %B, %Y')

ROOT_URLCONF = 'urls'
# SUBDOMAIN_URLCONFS = {
#     # The format for these is 'subdomain': 'urlconf'
#     None: 'urls.marketing',
#     'www': 'urls.marketing',
#     'dev': 'urls.marketing',
#     'flightcontrol': 'urls.dashboard',
#     # 'api': 'myproject.urls.api',
# }
# PUBLIC_SUBDOMAINS = [
#     None,
#     "www",
#     "dev",
#     "flightcontrol",
# ]
# REMOVE_WWW_FROM_SUBDOMAIN = True

PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

INSTALLED_APPS = (
    'django_monkeypatches',     # 100-char username field.

    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.comments',
    "django.contrib.redirects",
    "django.contrib.sitemaps",

    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.pages",
    "mezzanine.twitter",
    PACKAGE_NAME_GRAPPELLI,
    PACKAGE_NAME_FILEBROWSER,


    'qi_toolkit',
    'analytical',
    'django_extensions',
    'pagination',
    'south',
    'gunicorn',
    'sorl.thumbnail',
    'django_nose',
    'djcelery',
    'django_jenkins',
    'django_ses',
    'mediasync',
    'sentry',
    'sentry.client',

    'marketing_site',
    'email_list',

    'djangosanetesting',
)



TEMPLATE_DIRS = (
    "%stemplates" % (PROJECT_ROOT),
)

# Django-analytical
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-20296975-1'
ANALYTICAL_INTERNAL_IPS = ['127.0.0.1', '192.168.2.164']
# HUBSPOT_PORTAL_ID = '98343'
# HUBSPOT_DOMAIN = 'agoodcloud.app9.hubspot.com'

MAILCHIMP_API_KEY = "fa5bdaa6065aa4fd8975781bceaddd26-us2"

# LOGIN_REDIRECT_URL = "/dashboard/"
# AUTH_PROFILE_MODULE = "accounts.UserAccount"


GOOGLE_MAPS_KEY = "ABQIAAAAHhU2Kv9Iz8Fh-GRXaplHqxRHA9ICmOpg9-1g76S5BMdlTE0SKRRfIwbO5xyH_2XiYLy9Wt8qQ9Ymz"


SESSION_COOKIE_AGE = 1209600
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
# SESSION_SAVE_EVERY_REQUEST = True

# qi toolkit
DEFAULT_SMOKE_TEST_OPTIONS = {
    'verbose'           : False,
}


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--where=apps', '-s']

FORCE_SELENIUM_TESTS = False
# SELENIUM_BROWSER_COMMAND = "safari"
SELENIUM_BROWSER_COMMAND = "*chrome"
LIVE_SERVER_PORT = 8099
SELENIUM_PORT = 64444

SOUTH_LOGGING_ON = True
SOUTH_LOGGING_FILE = "/dev/null"

THUMBNAIL_FORMAT = "PNG"
THUMBNAIL_COLORSPACE = None

# jonny cache
JOHNNY_MIDDLEWARE_KEY_PREFIX='jc_pileus'
MAN_IN_BLACKLIST = []

# celery / rabbitmq
# BROKER_HOST = "localhost"
# BROKER_PORT = 5672
# BROKER_USER = "mycelium"
# BROKER_PASSWORD = "68WXmV6K49r8veczVaUK"
# BROKER_VHOST = "digitalmycelium"
# CELERY_RESULT_BACKEND = "amqp"
BROKER_BACKEND = "redis"
BROKER_HOST = "localhost"  # Maps to redis host.
BROKER_PORT = 6379         # Maps to redis port.
BROKER_VHOST = "7"         # Maps to database number.
CELERY_RESULT_BACKEND = "redis"
REDIS_HOST = BROKER_HOST
REDIS_DB = BROKER_VHOST
REDIS_PORT = BROKER_PORT

CELERY_IGNORE_RESULT = True
import djcelery
djcelery.setup_loader()

# for initial sync
# CELERY_RESULT_BACKEND = "database"

# sorl
THUMBNAIL_PREFIX = "_cache/"


# DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJTNZWCZDOIDWFR4A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = "goodcloud-public"
AWS_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME


CDN_MEDIA_URL = "https://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME


GIT_CURRENT_SHA = None
# django-mediasync

BASE_JS = [
    "js/lib/modernizr-1.6.min.js",
    "js/contrib/jquery-1.4.3.min.js",
    "js/contrib/jquery-ui.js",
    "js/contrib/jquery.django.csrf.js",
    "js/plugins.js",
    "js/script.js",
    "js/contrib/date.js",
]
COMMON_JS = [
    "js/contrib/jquery.autogrow.js",
    "js/contrib/jquery.ba-bbq.min.js",
]
BASE_CSS = [
    "css/style.css",
    "css/main.css",
    "css/contrib/jquery-ui-1.8.10.custom.css",
    "css/mycelium_elements.css",
]

MEDIASYNC = {
    'BACKEND': 'mediasync.backends.s3',
    'AWS_KEY': AWS_ACCESS_KEY_ID,
    'AWS_SECRET': AWS_SECRET_ACCESS_KEY,
    'AWS_BUCKET': AWS_STORAGE_BUCKET_NAME,
    # 'CACHE_BUSTER': GIT_CURRENT_SHA,
    # 'AWS_PREFIX': GIT_CURRENT_SHA, 
    # 'PROCESSORS': (
    #     'mediasync.processors.slim.css_minifier',
    #     'mediasync.processors.slim.js_minifier',
    # ),
    'PROCESSORS': (
        'mediasync.processors.yuicompressor.css_minifier',
        'mediasync.processors.yuicompressor.js_minifier',
    ),
    # 'PROCESSORS': ('mediasync.processors.closurecompiler.compile',),

    'YUI_COMPRESSOR_PATH': join(abspath(LIB_DIR), 'yuicompressor.jar'),
    'JOINED': {
        'js/base.js': BASE_JS,

        'js/marketing_base.js': BASE_JS + COMMON_JS + [

        ],
        'js/marketing_core.js': [
                "js/marketing_site/marketing_site.js",
                "js/marketing_site/signup.js",
                "js/marketing_site/marketing_tabs.js",
        ],
        'css/marketing_base.css': BASE_CSS + [
                "css/marketing_site.css",
                "css/contrib/1140/1140.css",
                "css/login.css",
                "css/signup.css",
        ]
    }

}
MEDIASYNC['SERVE_REMOTE'] = True




######################
# MEZZANINE SETTINGS #
######################

# The following Mezzanine settings are already defined in
# mezzanine.conf.defaults, but can be uncommented below in
# order to override their defaults.

# Controls the ordering and grouping of the admin menu.
# from django.utils.translation import ugettext as _
# ADMIN_MENU_ORDER = (
#     (_("Content"), ("pages.Page", "blog.BlogPost",
#        "generic.ThreadedComment", (_("Media Library"), "fb_browse"),)),
#     (_("Site"), ("sites.Site", "redirects.Redirect", "conf.Setting")),
#     (_("Users"), ("auth.User", "auth.Group",)),
# )

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# Name of the current theme to host during theme development.
# THEME = ""


