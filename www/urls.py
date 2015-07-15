from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'www.views.index', name='index'),
    url(r'^users/$', 'www.views.users', name='users'),
    url(r'^free/(?P<pk>\d+)/$', 'www.views.free', name='free'),
    url(r'^reserve/$', 'www.views.reserve', name='reserve'),
)
