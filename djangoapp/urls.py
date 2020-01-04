from django.urls import path
from django.contrib.auth.views import LoginView

from . import views as appviews

urlpatterns = [
    path('', LoginView.as_view(template_name='index.html')),
    path('logout/', appviews.logout)
]
