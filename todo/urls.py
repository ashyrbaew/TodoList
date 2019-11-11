from django.urls import path
from . import views


app_name = 'todo'

urlpatterns = [
    path('', views.Index, name ='index'),
    path('<int:item_id>/', views.Visiblity, name ='visiblity'),
    # path('', views.addnew, name='newlist'),
]
