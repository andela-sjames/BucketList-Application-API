from django.conf.urls import patterns, include, url
from bucketlistapi import usertoken
from django.contrib import admin
from django.conf import settings
import bucketlist
import bucketlistapi

urlpatterns = [
  
    url(r'^myappadmin/', include(admin.site.urls)),
    url(r'^bucketlist/', include('bucketlist.urls')),
    url(r'^$', bucketlist.views.SignUpView.as_view(), name='signup'),
    url(r'^api/', include('bucketlistapi.urls')),
   
]

urlpatterns += [
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
     url(r'^api/auth/login/', usertoken.get_auth_token, name='gettoken')
]

handler404='bucketlist.views.custom_404'
handler500='bucketlist.views.custom_500'


