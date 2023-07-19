from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('add_todo/',views.add_todo,name="add_todo"),
    path('logout/',views.signout,name="logout"),
    path('delete_todo/<int:id>/',views.delete_todo,name="delete_todo"),
    path('change_status_todo/<int:id>/<str:status>/',views.change_status_todo,name="change_status_todo")
]
