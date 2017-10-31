from django.conf.urls import url
from api_app.api import ApiUserLoginResource, ApiUserRegisterResource, ApiUserLogoutResource


urlpatterns = [
    url(r'^login/$', ApiUserLoginResource.as_detail(), name='login'),
    url(r'^register/$', ApiUserRegisterResource.as_detail(), name='register'),
    url(r'^logout/$', ApiUserLogoutResource.as_detail(), name='logout'),

]


