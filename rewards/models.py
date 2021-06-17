from django.db import models
from users.models import User

from users.models import Team, Camp


class Type(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(default='default.jpg', upload_to='badge_image')

    def __str__(self):
        return f'{self.name}'


class Points(models.Model):
    camp = models.ForeignKey(Camp, default=1,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    heading = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    show = models.BooleanField(default=False)

    def __str__(self):
        if self.user:
            if self.user.name:
                return f'{self.user.name}-{self.points}'
            else:
                return f'{self.user}-{self.points}'
        return f'{self.team}-{self.points}'
