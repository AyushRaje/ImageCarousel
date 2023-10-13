from django.urls import path
from main import views
urlpatterns = [
    path('index/<int:i>/',views.index,name='index'),
    path('vote/<int:i>/',views.vote,name='vote'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]
