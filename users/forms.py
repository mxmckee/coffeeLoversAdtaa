from django import forms
from django.contrib.auth import authenticate
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AdtaaUser
from django.utils.translation import gettext_lazy as _


class AdtaaUserForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = AdtaaUser
        fields = [
            'email', 'username', 'password1', 'password2', 'accessRequested'
        ]


class AdtaaAuthenticationForm(AuthenticationForm):
    error_messages = {
        'inactive': _('This account has not been activated yet.  You will receive an email when activated.'),
        'invalid_login': _('Not a valid username/password combination'),
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
    #
    #     if username is not None and password:
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             if not user.is_active:
    #                 raise forms.ValidationError(
    #                     self.error_messages['inactive'],
    #                     code='inactive',
    #                 )
    #
    #
    #
    #         else:
    #             raise forms.ValidationError(
    #                 self.error_messages['invalid_login'],
    #                 code='invalid_login',
    #                 params={'username': self.username_field.verbose_name},
    #             )
    #
    #     return self.cleaned_data



        self.user_cache = authenticate(self.request, username=username, password=password)
        if self.user_cache is not None:
            try:
                user_temp = AdtaaUser.objects.get(username=username)
            except:
                user_temp = None

            if user_temp is not None:
                self.confirm_login_allowed(user_temp)
        else:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name},
            )

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )