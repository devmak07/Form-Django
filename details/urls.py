from django.urls import path
from . import views

app_name = 'details'

urlpatterns = [
    path('login/', views.loginPage, name='loginPage'),
    path('register/', views.register_view, name='register_view'),
    path('', views.create_form_detail, name='create_form_detail'),
    path('update_form_detail/<int:pk>/', views.update_form_detail, name='update_form_detail'),
    path('read_list/', views.read_list, name='read_list'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('logout/', views.logout_view, name='logout_view'),
]
