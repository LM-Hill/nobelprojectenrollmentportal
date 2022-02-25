from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.login_page),
    path('register', views.registration_page),
    path('create_user', views.create_user),
    path('login_user', views.login_user),
    path('logout', views.logout_user),
    path('teamroster', views.teamroster),
    path('<int:user_id>/delete', views.delete_user),
    path('<int:user_id>/edit', views.edit_user),
    path('<int:user_id>/update', views.update_user),
]