from django.urls import path
from . import views
from  .views import CreateFormEmail



urlpatterns = [
    path('send/', CreateFormEmail.as_view(), name="send"),
    path('home/', views.home, name="home"),
    path('welcome/', views.welcome, name="welcome"),
    # path('send/', views.send, name="send"),
    # path('send_mail/', views.send , name="send_mail")
]