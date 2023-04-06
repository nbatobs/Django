from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    #path('login/',views.login_user, name = 'login'),
    path('logout/',views.logout_user, name = 'logout'),
<<<<<<< HEAD
    path('register/',views.register_user, name = 'register'),
=======
>>>>>>> 96b17488572a68bfdecc38fc3f7f361340ccc592

]