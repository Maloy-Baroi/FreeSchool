from django.urls import path
from App_login import views

app_name = 'App_login'

urlpatterns = [
    path('signup', views.signup_system, name='signup'),
    path('category_signup', views.category_signup, name='category_signup'),
    path('login', views.login_sys, name='login'),
    path('logout', views.logout_sys, name='logout'),
]
