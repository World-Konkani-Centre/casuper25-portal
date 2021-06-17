from django import forms
from django.db.models.functions import Lower
from django.db.models import Q
from users.models import User

from rewards.models import Type
from users.models import Team


class MultiBadgeForm(forms.Form):
    teams = forms.ModelChoiceField(queryset=Team.objects.all(), required=False)
    heading = forms.CharField(max_length=100)
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    points = forms.IntegerField(required=True)
    show = forms.BooleanField(required=False, help_text="Select only for top 3, which will be shown in the awards list")
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all().order_by(Lower('name')).filter(~Q(profile__team__id =39)), required=False)
