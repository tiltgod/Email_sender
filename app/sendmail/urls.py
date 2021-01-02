from django.urls import path

from . import views

app_name = 'sendmail'

urlpatterns = [
    path('sendmail/', views.sendmail),
]
