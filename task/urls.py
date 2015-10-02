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
    url(r'^index/', views.index, name='index'),
)
