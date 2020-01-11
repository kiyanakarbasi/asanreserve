from django.urls import path
from django.contrib.auth.views import LoginView

from . import views as views

urlpatterns = [
    path('', views.index),
    path('travels/', views.travels),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', views.logout),
]
