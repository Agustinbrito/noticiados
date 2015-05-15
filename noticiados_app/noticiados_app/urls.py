from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', 'noticiados_app.views.home', name='home'),
    url(r'^preguntando/$', 'noticiados_app.views.preguntando', name='preguntando'),
    url(r'^fin/$', 'noticiados_app.views.fin', name='fin'),
    # url(r'^admin/', include(admin.site.urls)),
)
