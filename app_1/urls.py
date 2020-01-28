from django.urls import path
from . import views

urlpatterns=[
path('',views.home,name='home'),
path('adicao',views.adicao,name='adicao')
]
