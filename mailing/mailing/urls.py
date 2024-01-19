"""
URL configuration for mailing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from .views import MailDistribution as md

from django.contrib import admin
from rest_framework import permissions
from django.urls import include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'mailing'

schema_view = get_schema_view(
        openapi.Info(
            title='API',
            default_version='v1',
            description='API documentation'),
        public=True,
        permission_classes=(permissions.AllowAny,),
        patterns=[
            path('api/', include('mailing.mailing.urls'))]
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/<int:mailing_id>/', md.send_mailing,name='send_mailing'),
    path('cancel/<int:mailing_id>/', md.cancel_mailing, name='cancel_mailing'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
