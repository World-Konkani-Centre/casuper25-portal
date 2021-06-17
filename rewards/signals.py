from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


from .models import Points


@receiver(post_save, sender=Points)
def update_team_points(sender, instance, created, **kwargs):
    if created:
        if instance.user:
            team = instance.user.profile.team
            if team:
                team.team_points = team.team_points + instance.points
                team.save()
                instance.user.profile.points = instance.user.profile.points + instance.points
                instance.user.profile.save()
        elif instance.team:
            team = instance.team
            team.team_points = team.team_points + instance.points
            team.save()


@receiver(pre_delete, sender=Points)
def reduce_points(sender, instance, using, **kwargs):
    if instance.user:
        team = instance.user.profile.team
        if team:
            team.team_points = team.team_points - instance.points
            team.save()
            instance.user.profile.points = instance.user.profile.points - instance.points
            instance.user.profile.save()
    elif instance.team:
        team = instance.team
        team.team_points = team.team_points - instance.points
        team.save()


