from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard),
    path('login/', views.login),
    path('signup/', views.signup),
    path('home/', views.home)
]
