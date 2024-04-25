from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('json/', views.jsonMessage.as_view(), name='json_endpoint'),
    path('todo', views.TodoDetail.as_view(), name='todos'),
]