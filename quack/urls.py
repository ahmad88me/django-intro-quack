"""quack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from quack import views

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url('list_ducks', views.list_ducks),
    url('add_duck', views.add_duck),
    url('delete_duck', views.delete_duck),
    url('login', views.login_view),
    url('logout', views.logout_view),
    url('add_to_me', views.add_to_me),
    url('myducks', views.myducks),
    url('remove', views.remove_from_me),
    url('', views.home),
]


import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



