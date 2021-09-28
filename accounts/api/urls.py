from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.loginView,name="login"),
    path('logout/',views.logoutView,name="logout"),
    path('register/',views.registerView,name="register")
]
