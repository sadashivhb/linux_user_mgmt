from django.conf.urls import patterns, include, url
from django.contrib import admin
import usermgmt
from usermgmt import views

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'home', views.home, name='home'),
    url(r'index/', views.index, name='index'),
    url(r'addsuccess/', views.addsuccess, name='addsuccess'),
    url(r'usermod/', views.usermod, name='usermod'),
    url(r'usermodsucc/', views.usermodsucc, name='usermodsucc'),
    url(r'userdel/', views.userdel, name='userdel'),
    url(r'userdelsucc/', views.userdelsucc, name='userdelsucc'),
    url(r'usergrant/', views.usergrant, name='usergrant'),
    url(r'usergrantsucc/', views.usergrantsucc, name='usergrantsucc'),
    url(r'register/', views.register, name='register'),
)
