from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^start/$', 'noticiados_app.views.start', name='start'),
    url(r'^preguntando/$', 'noticiados_app.views.preguntando', name='preguntando'),
    url(r'^end/$', 'noticiados_app.views.end', name='end'),
)
