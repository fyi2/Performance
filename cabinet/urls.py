from django.conf.urls import url
from django.contrib import admin
#from playme.core import views as core_views
from cabinet import views as fc_views
from django.contrib.auth import views as auth_views
from django.conf import settings
# SET THE NAMESPACE!
app_name = 'cabinet'


urlpatterns = [
  url(r'^$', fc_views.note_list, name='note_list'),
  url(r'^new$', fc_views.note_create, name='note_new'),
  url(r'^tag$', fc_views.tag_create, name='tag_new'),
  url(r'^edit/(?P<pk>\d+)$', fc_views.note_update, name='note_edit'),
  url(r'^delete/(?P<pk>\d+)$', fc_views.note_delete, name='note_delete'),

]
