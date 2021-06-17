from django import forms
from django.forms import fields
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='Use the email which is submitted to World Konkani Centre')

    class Meta:
        model = User
        fields = ['email', 'batch', 'gender', 'name', 'image', 'date_of_birth', 'college_name', 'password1',
                  'password2']
        help_texts = {
            'image': _('Your profile picutre can be accessed by all the Campers'),
            'email': _('Use the email which is submitted to World Konkani Centre'),

        }
        labels = {
            'batch': _('VKSSF Batch'),
            'image': _('Profile picture'),
            'name': _('Full name')
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(help_text='Use the email which is submitted to World Konkani Centre')

    class Meta:
        model = User
        fields = ['email', 'batch', 'gender', 'name', 'image', 'date_of_birth', 'college_name']

        help_texts = {
            'image': _('Your profile picutre can be accessed by all the Campers'),
            'email': _('Use the email which is submitted to World Konkani Centre'),

        }
        labels = {
            'batch': _('VKSSF Batch'),
            'image': _('Profile picture'),
            'name': _('Full name')
        }


class CampsUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['camps']
        help_texts = {
            'camps': _('Please select the only one camp')
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['team']
