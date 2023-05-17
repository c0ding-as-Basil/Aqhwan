from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('services/', views.services, name='services'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('services/<int:service_id>/add_comment/',
         views.add_comment, name='add_comment'),
    path('services/<int:service_id>/like_service/',
         views.like_service, name='like_service'),

]
