from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('travels/', views.travels, name='travels'),
    path('travel/<int:id>', views.travel, name='travel'),
    path('ticket/<int:id>', views.ticket, name='ticket'),

    path('travel/edit/<int:id>', views.travel_edit, name='travel_edit'),
    path('travel/delete/<int:id>', views.travel_delete, name='travel_delete'),
    path('vehicle/delete/<int:id>', views.vehicle_delete, name='vehicle_delete'),


    path('panel/', views.panel, name='panel'),


    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
