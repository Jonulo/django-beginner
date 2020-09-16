# from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

#Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

# Forms
from users.form import ProfileForm, SignupForm

# En esta forma de crear las vistas (class-based) para requerir el login
# solo hacemos que herede de la clase loginrequiredmixin
class UserDetailView(LoginRequiredMixin, DetailView):

    template_name = 'users/detail.html'
    # en lugar de el ID (es el dato que viene de la url)
    slug_field = 'username'
    slug_url_kwarg = 'username'
    # a partir de que conjunto de datos va a traer los datos
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user= self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

# abajo esta la forma de hacerlo con function
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update user data"""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile
    
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

# Arriba esta hecho con class-based view:
# @login_required
# def update_profile(request):

#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         # Esto correra todas las validaciones de nuestra clase
#         if form.is_valid():
#             data = form.cleaned_data

#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()
            
#             # Agregamos reverse por que redirect no maneja argumentos
#             url = reverse('users:detail', kwargs={'username': request.user.username})
#             return redirect(url)
#     else:
#         form = ProfileForm()

#     return render(
#         request=request,
#         template_name = 'users/update_profile.html',
#         context={
#             'profile': profile,
#             'user': request.user,
#             'form': form
#         }
#     )

class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'
    redirect_authenticated_user = True

# def login_view(request):
    
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         print('user:',user)
#         if user is not None:
#             login(request, user)
#             return redirect('posts:feed')
#         else:
#             return render(
#                 request, 'users/login.html',
#                 {'error': 'Invalid username and password'}
#             )
    # return render(request, 'users/login.html')

# usando class-based view para signup:
class SignupView(FormView):
    """User signup view"""
    
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)


# usando funcion para el signup:
def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
        
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view"""

    template_name = 'users/logged_out.html'
    

# @login_required
# def logout_view(request):

#     logout(request)
#     return redirect('users:login')
