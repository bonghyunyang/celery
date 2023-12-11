# api/urls.py

from django.urls import path

from api.views import Test, get_task_status

urlpatterns = [
    path('test', Test.as_view(), name='test'),
    path('tasks/<str:task_id>', get_task_status, name='get_task_status')
]