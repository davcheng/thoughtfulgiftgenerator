from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fingro.views.home', name='home'),
    # url(r'^fingro/', include('fingro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^results/', 'blog.views.results'),
	url(r'^submit/', 'blog.views.results'),
	url(r'^$', 'blog.views.index'),
    # url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),


)
