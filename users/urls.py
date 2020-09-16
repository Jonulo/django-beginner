# Django
from django.urls import path

# View
from users import views

urlpatterns = [
    # Managment
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
    ),
    # Posts
    # Lo ponemos hasta abajo porque django resuelve las url
    # en forma de lista y chocaria con url que esten con 
    # parametros previamente puestos
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    )
]