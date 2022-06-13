from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('taskitems/', include('taskitems.urls')),
    path('', include('taskrqe.urls')),
]
