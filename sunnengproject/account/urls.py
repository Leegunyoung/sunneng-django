from django.urls import path
from django.urls. resolvers import URLPattern
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout")
    
]