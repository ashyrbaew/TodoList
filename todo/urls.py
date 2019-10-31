from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoIndex, name ='IndexPage'),
    path('<int:item_id>/', views.ChangeStatus, name ='ChangeStatus'),
]
