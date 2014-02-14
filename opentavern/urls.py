from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from tavern import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.index, name='index'),
                       url(r'^accounts/', include("django.contrib.auth.urls")),
                       url(r'^groups/(?P<slug>[\w-]+)', views.group_details, name='group_details'),
                       url(r'^events/(?P<slug>[\w-]+)', views.event_details, name='event_details'),
                       url(r'^create_group/', views.create_group, name='create_group'),
                       url(r'^(?P<slug>[\w-]+)/tavern_group_update', views.tavern_group_update, name='tavern_group_update'),
                       url(r'^create_event/', views.create_event, name='create_event'),
                       url(r'^(?P<slug>[\w-]+)/tavern_event_update', views.tavern_event_update, name='tavern_event_update'),
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
