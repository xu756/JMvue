from django.contrib import admin
from django.urls import path
from Api import views
urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    path('api/login',views.login)
]
