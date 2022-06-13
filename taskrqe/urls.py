from django.urls import path

from .views import taskrqe

urlpatterns = [
    path('', taskrqe, name='taskrqe'),
]
