from django.urls import path, include

from django.contrib.auth.views import LogoutView


from . import views

app_name = 'users'
urlpatterns = [
    #url auntefication
    path('', include('django.contrib.auth.urls')),

    #registration page
    path('register/', views.register, name='register'),

    #log out
     path('logout/', LogoutView.as_view(), name='logout'),
]