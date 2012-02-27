from django.conf.urls.defaults import patterns, include, url
import ins

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ins.views.home'),
    url(r'^subject/(?P<subject_id>\d+)/$', 'ins.views.subject'),
    url(r'^instruction/(?P<instruction_id>\d+)/$', 'ins.views.instruction'),
    url(r'^admin/', include(admin.site.urls)),
)
