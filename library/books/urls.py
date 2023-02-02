from django.urls import path
from . import views
from django.contrib.auth.views import auth_logout

urlpatterns = [
    path('',views.base, name='base'),
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('books/',views.search_books, name='books'),
    path('turn_books/', views.turn_books, name='turn_books'),

]
