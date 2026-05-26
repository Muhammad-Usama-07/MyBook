from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# ─────────────────────────────────────────
# REGISTRATION FORM
# ─────────────────────────────────────────
class RegisterForm(UserCreationForm):
    """
    Form for creating a new MyBook account.
    Extends Django's built-in UserCreationForm which handles:
    - password validation (min length, not too common, etc.)
    - password confirmation (type it twice)
    - password hashing automatically
    """

    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'form-control',
        })
    )

    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'form-control',
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-control',
        })
    )

    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'role-radio'}),
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name',
            'username', 'email',
            'role',
            'password1', 'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style the password fields
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password',
            'class': 'form-control',
        })


# ─────────────────────────────────────────
# LOGIN FORM
# ─────────────────────────────────────────
class LoginForm(AuthenticationForm):
    """
    Form for logging in to MyBook.
    Extends Django's AuthenticationForm which handles:
    - checking username/password against database
    - inactive account checking
    - rate limiting (too many failed attempts)
    """

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
            'autofocus': True,
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        })
    )