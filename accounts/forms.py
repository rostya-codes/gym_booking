from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username:
            raise ValidationError("Username cannot contain spaces.")
        if not username.strip():
            raise ValidationError("Username cannot be empty or contain only spaces.")
        return username


class LoginForm(forms.Form):
    identifier = forms.CharField(label="Username or Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    # Валидация на наличие пробела в идентификаторе
    def clean_identifier(self):
        identifier = self.cleaned_data['identifier']
        if ' ' in identifier:
            raise ValidationError("Username cannot contain spaces.")
        return identifier

    def clean(self):
        cleaned_data = super().clean()
        identifier = cleaned_data.get('identifier')
        password = cleaned_data.get('password')

        User = get_user_model()

        # Проверяем, является ли введенный идентификатор email или username
        user = None
        try:
            # Пытаемся найти пользователя по email
            user = User.objects.get(email=identifier)
        except User.DoesNotExist:
            try:
                # Если не нашли по email, ищем по username
                user = User.objects.get(username=identifier)
            except User.DoesNotExist:
                pass  # No user found, will raise ValidationError later

        # Пробуем аутентифицировать пользователя, если нашли его в базе
        if user:
            user = authenticate(username=user.username, password=password)

        if user is None:
            raise ValidationError("Invalid login credentials")

        self.user = user
        return cleaned_data

    def get_user(self):
        return self.user


class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username:
            raise ValidationError("Username cannot contain spaces.")
        if not username.strip():
            raise ValidationError("Username cannot be empty or contain only spaces.")
        return username
