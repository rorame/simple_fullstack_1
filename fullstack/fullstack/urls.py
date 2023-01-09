from django.contrib import admin
from django.urls import path

from backend.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', BookApiList.as_view())
]
