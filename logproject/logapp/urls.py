from . import views
from django.urls import path

urlpatterns = [
    path('logs', views.log_view, name="Logger with formates"),
    path('calculator', views.calculator, name='calculator'),
]