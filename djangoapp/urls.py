from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('travels/', views.travels, name='travels'),
    path('travel/<int:id>', views.travel, name='travel'),
    path('ticket/<int:id>', views.ticket, name='ticket'),


    # path('admin_page', views.vehicle, name='vehicle'),


    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
