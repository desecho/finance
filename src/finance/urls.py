from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

from financeapp.views import report, logout, home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),

    url(r'^report/(?P<year>\d+)/(?P<month>\d+)/$', report, name='report'),

    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
]
