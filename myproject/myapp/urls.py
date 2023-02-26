from django.urls import path
from .views import index, register, recognize, users
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('recognize/', views.recognize, name='recognize'),
    #path('register/', register, name='register'),
    #path('recognize/', recognize, name='recognize'),
    path('users/', views.users, name='users'),
    #path('add_user/', views.add_user, name='add_user'),
    #path('users/<int:user_id>/', views.user, name='user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    
]