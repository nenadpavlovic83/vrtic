from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',
        views.loginview,
        name='login'),

    path('logout/',
        auth_views.LogoutView.as_view(),
        name='logout'),
    path("signup/", views.signup, name='signup'),
]
