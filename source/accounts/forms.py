from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    email = forms.EmailField(label='Email', required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists', code='user_email_exists')
        except User.DoesNotExist:
            return email

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if not(first_name or last_name):
            raise ValidationError('Нужно заполнить хотябы одно поле из first_name или last_name')
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class UserChangeForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар', required=False)
    about_me = forms.CharField(max_length=3000, required=False, label='О себе', widget=widgets.Textarea)
    git_http = forms.URLField(label='Профиль на гитхаб', required=False)

    def clean_git_http(self):
        git_http = self.cleaned_data['git_http']
        if git_http == '' or not git_http.startswith('https://github.com/'):
            raise forms.ValidationError('ссылка не на гитхаб')
        return git_http

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)
        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        user = super().save(commit)
        self.save_profile(commit)
        return user

    def save_profile(self, commit=True):
        profile = self.instance.profile
        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data[field])
        if not profile.avatar:
            profile.avatar = None
        if commit:
            profile.save()
        return profile

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'about_me', 'git_http']
        profile_fields = ['avatar', 'about_me', 'git_http']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']