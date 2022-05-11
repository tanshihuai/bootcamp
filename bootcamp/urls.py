from django.contrib import admin
from django.urls import path, include
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("register.urls")),
    path('', include("django.contrib.auth.urls")),
]
