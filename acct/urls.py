from django.conf.urls import url
from django.contrib import admin
#from playme.core import views as core_views
from acct import views as core_views
from django.contrib.auth import views as auth_views
from django.conf import settings

# SET THE NAMESPACE!
app_name = 'acct'


urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'signup/$', core_views.signup, name='signup'),
    url(r'^account/$', core_views.account, name='account'),
    url(r'^profile/$', core_views.view_profile, name='profile'),
    url(r'^login/$', core_views.login, name='user_login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^edit_account/$', core_views.edit_account, name='edit_account'),
    url(r'^edit_profile/$', core_views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', core_views.change_password, name='change_password'),
]
