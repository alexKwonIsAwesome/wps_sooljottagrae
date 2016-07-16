from django.conf.urls import url, include
from django.contrib import admin

from users.views import *
from apis.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^user/', include("users.urls", namespace="users")),
    url(r'^posts/', include("posts.urls", namespace="posts")),

    url(r'^api/', include("apis.urls", namespace="apis")),
    url(r'docs/', include('rest_framework_swagger.urls')),

    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
]
