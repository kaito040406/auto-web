from django.urls import path

from . import views

urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/',views.IndexView.as_view(), name="index"),
    path('create/',views.IndexView.as_view(), name="create"),
]