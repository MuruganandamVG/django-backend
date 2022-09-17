
from django.urls import path,include
from .views import UserList,FileView
from rest_framework.authtoken import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
   path('users/',UserList.as_view(),name='users'),
   path('Fileview',FileView.as_view(),name='fileview'),
   path('api-token-auth/', views.obtain_auth_token),
   
]

