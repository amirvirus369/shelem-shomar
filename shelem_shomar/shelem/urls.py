from django.urls import path
from . import views
app_name = 'shelem_main'
urlpatterns = [
    path('',views.shelem_main)
]