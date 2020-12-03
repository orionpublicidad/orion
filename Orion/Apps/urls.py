"""Apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

#Ruta
from Views.HomePageViews import *
from Views.QuienesSomosViews import *
from Views.ServiciosViews import *
from Views.ContactViews import *
#from Views.LoginViews import *
#from Urls.LoginUrls import *




#from Orion.homepage.views import IndexView
#from Orion.views.viewsQuiSom import *
#from Orion.modules.moconfi.comproba.views_comproba import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='homepage'),
    path('quienessomos', QuienesSomosView.as_view(), name='quienessomos'),
    path('servicios', ServiciosView.as_view(), name='servicios'),
    path('contacto', ContactView.as_view(), name='contacto'),
    path('login/', include('Urls.LoginUrls')),


    #path('modules/', include('Orion.modules.moconfi.comproba.urls_comproba')),
    #path('empresa/list/', listempresa),
    #path('comproba/list/', ComprobaListView.as_view(), name='ComprobaList'),
    #path('comproba/add/', ComprobaCreateView.as_view(), name='ComprobaAdd'),
    #path('comproba/update/<int:pk>', ComprobaUpdateView.as_view(), name='ComprobaUpdate'),
    #path('comproba/delete/<int:pk>/', ComprobaDeleteView.as_view(), name='ComprobaDelete'),
]
