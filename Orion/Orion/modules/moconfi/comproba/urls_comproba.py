from django.urls import path
from Orion.modules.moconfi.comproba.views_comproba import *
from Orion.dashboard.views import *

app_name = 'modules'

urlpatterns = [
    path('comproba/list/', ComprobaListView.as_view(), name='ComprobaList'),
    path('comproba/add/', ComprobaCreateView.as_view(), name='ComprobaAdd'),
    path('comproba/list/<int:pk>', ComprobaUpdateView.as_view(), name='ComprobaUpdate'),
    path('comproba/delete/<int:pk>/', ComprobaDeleteView.as_view(), name='ComprobaDelete'),
    #home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]