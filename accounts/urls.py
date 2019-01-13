from django.contrib import admin
from django.urls import path
from . import views
app_name= "accounts"
urlpatterns = [

    path("login/",views.log_in,name="login"),

    path("signup/",views.sign_up,name="signup"),
    path("logout",views.log_out,name="logout"),
    path("studentform",views.studentform,name = "studentform")

]
