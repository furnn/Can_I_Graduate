from django.urls import path
from . import views

urlpatterns=[
    path('', views.test1, name='index'),
    path('mypage', views.mypage, name='mypage'),
    path('11', views.test1, name='test1'),
    path('33', views.test3, name='test3'),
]