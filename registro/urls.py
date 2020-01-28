from django.urls import path
from . import views

urlpatterns=[
    path('',views.registro,name='registro'),
    path('/logout',views.logout,name='logout'),
    path('/troca_senha',views.troca_senha,name='troca_senha'),
    path('/new_password',views.new_password,name='new_password')
]
