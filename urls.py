from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import marketing_site.views as marketing_views
import mezzanine.blog.views as mezzanine_views
admin.autodiscover()

from django.template import add_to_builtins
add_to_builtins('mediasync.templatetags.media')

# from mezzanine.core.views import direct_to_template

# Adds ``MEDIA_URL`` to the context.
handler500 = "mezzanine.core.views.server_error"



urlpatterns = patterns('',)



if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


# override for qi urls to allow indexing
from qi_toolkit import robots
urlpatterns += patterns('',          
    url(r'^robots.txt',     robots.robots_txt,      kwargs={'allow':True,},    name='robots_txt'),
)

try:
    if settings.FAVICON_URL != "":
        urlpatterns += patterns('',          
            (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': settings.FAVICON_URL}),
        )
except:
    pass

urlpatterns += patterns('',
    url(r'^',              include('marketing_site.urls',      app_name="marketing_site",  namespace="marketing_site"),),
    url(r'^$',              marketing_views.home,             name='home'),
    url(r'^',              include('email_list.urls')),                                    
    # url(r'^',              include('accounts.urls.marketing',  app_name="accounts",        namespace="accounts")),    
    url(r'^sign-up$', 'django.views.generic.simple.redirect_to', {'url': "signup.%s" % settings.BASE_DOMAIN}, name="signup"),

    url(r'^blog/$',         "mezzanine.blog.views.blog_post_list",         name='blog'),
    url(r'^administration/', include(admin.site.urls)),
    url(r'^sentry/', include('sentry.web.urls')),
    url(r'^webhooks/',     include('webhooks.urls',            app_name="webhooks",        namespace="webhooks")),
    url(r'^', include('django_ses.urls')),
    url(r'^', include('mediasync.urls')),
    ("^", include("mezzanine.urls")),
)