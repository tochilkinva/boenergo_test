from django.urls import path

from .views import additems, taskitems

urlpatterns = [
    path('', taskitems, name='taskitems'),
    path('additems/<int:count>', additems, name='additems'),
]
