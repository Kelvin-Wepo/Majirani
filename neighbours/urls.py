from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('business/',views.business, name='business'),
    path('nineOneone/',views.contact, name='nineOneone'),
    path('register/',views.register, name='register'),
    path('post',views.post,name='post'),
]