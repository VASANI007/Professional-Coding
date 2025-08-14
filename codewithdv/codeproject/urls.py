"""
URL configuration for codeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from codeapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage, name='indexpage'),
    path('singlepage/<int:id>',views.singlepage),
    path('contactpage',views.contactpage),
    path('ourgallerypage',views.ourgallerypage),
    path("aboutpage",views.aboutpage),
    path("categorypage/<int:id>",views.categorypage),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)