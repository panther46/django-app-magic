"""magic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from magicdb import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name="index"),
    path('index/card', views.single_card, name="single_card"),
    path('gotit/', views.i_got_it, name="i_got_it"),
    path('not_mine/', views.not_mine, name="not_mine"),
    path('mine/', views.mine, name="mine"),
    path('check/', views.check, name="check"),
    path('bulkinsert/', views.bulk_insert_or_remove, name="bulk"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#colocar una funcion lambda para redirigir index a un get con page=1
