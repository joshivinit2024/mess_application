from django.urls import path
# from .views import signup, login, check_login, get_all_users
from . import views  # Assuming views are in the same app

urlpatterns = [
    # path('signup/', signup, name='signup'),
    # path('login/', login, name='login'),
    # path('check_login/', check_login, name='check_login'),
    # path('users/', get_all_users, name='get_all_users')    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('check_login/', views.check_login, name='check_login'),
    path('get_all_users/', views.get_all_users, name='get_all_users'),
    path('details_handler/', views.details_handler, name='details_handler'),
]