#Django
from django import forms
# Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):

    username = forms.CharField(min_length=4, max_length=50)
    # Widgets
    password = forms.CharField(
        min_length=6,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'required': True
            }
        )
    )
    password_confirmation = forms.CharField(
        min_length=6,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password Confirmation',
                'class': 'form-control',
                'required': True
            }
        )
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

    # Implementar que el USER no este en uso
    def clean_username(self):
        """ Username must be unique. """
        # cleaned_data son los datos que django ya pasó por las validaciones
        username = self.cleaned_data['username']
        # Query a la BD y exist para que regrese un boolean
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            # django se encarga de SUBIR esta excepcion(error) hasta el nivel de HTML(template)
            raise forms.ValidationError('Username is already in use')
        return username
    
    # Validar el password que depende que otro exista (password coincidan)
    def clean(self):
        """Verify password confirmation match."""
        # Super es llamar a la data antes de ser sobrescrita
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match.')

        return data
    
    # Una vez que esten las validaciones, los datos se guardaran asi:
    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
class ProfileForm(forms.Form):

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=True)
    picture = forms.ImageField()