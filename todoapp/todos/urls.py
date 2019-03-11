from django.urls import path
from todos.views import TodoListCreateAPIView, TodoDetailAPIView

app_name = 'todos'

urlpatterns = [
    path('', TodoListCreateAPIView.as_view(), name="list"),
    path('<int:pk>/', TodoDetailAPIView.as_view(), name="detail"),
]
