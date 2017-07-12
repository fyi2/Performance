from django.conf.urls import url
from django.contrib import admin
#from playme.core import views as core_views
from todo import views as td_views
from django.contrib.auth import views as auth_views
from django.conf import settings
# SET THE NAMESPACE!
app_name = 'todo'


urlpatterns = [
  url(r'^$', td_views.task_list, name='task_list'),

]
