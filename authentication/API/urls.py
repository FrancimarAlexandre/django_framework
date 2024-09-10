from django.urls import path
from . import views
urlpatterns = [
    path('accounts/login/',views.login,name="login"),
    path('accounts/register/',views.register,name="register"),
]