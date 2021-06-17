from django.http import Http404
from django.shortcuts import render, redirect

from users.models import Profile, Team
from .forms import MultiBadgeForm
from django.contrib.auth.decorators import login_required

from .models import Points
from webpages.models import Banner, Visibility
from webpages.utils import return_camp_id


@login_required
def give_award(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            form = MultiBadgeForm()
            return render(request, 'award/give_award.html', context={'form': form})
        else:
            form = MultiBadgeForm(request.POST)
            if form.is_valid():
                users = form.cleaned_data.get('users')
                teams = form.cleaned_data.get('teams')
                heading = form.cleaned_data.get('heading')
                pr_type = form.cleaned_data.get('type')
                points = form.cleaned_data.get('points')
                show = form.cleaned_data.get('show')
                if len(users) != 0:
                    for user in users:
                        Points.objects.create(user=user, heading=heading, type=pr_type, points=points, show=show)
                elif teams:
                    Points.objects.create(team=teams, heading=heading, type=pr_type, points=points, show=show)
                return redirect('give_award')
    else:
        raise Http404()


# display the list of points given including only top 3
def award_list(request, camp):
    camp_id = return_camp_id(camp)
    awards = Points.objects.filter(show=True, camp=camp_id)
    users = awards.filter(team=None)
    teams = awards.filter(user=None)
    display = Visibility.objects.filter(camp=camp_id).first().awards
    image = Banner.objects.filter(camp=camp_id).first().awards

    context = {
        "teams": teams,
        'users': users,
        'display': display,
        'banner': image, 
        'camp_id': camp_id,
        'title': f'{camp.upper()} AWARD LIST'
    }
    return render(request, 'award/award_list.html', context=context)


# show the leaderboard of teams and profiles use points in corresponding models to order
def leaderboard(request, camp):
    camp_id = return_camp_id(camp)
    team_profiles = ""
    team_points = ""
    profiles = Profile.objects.filter(camps=camp_id).order_by('-points')[:10]
    teams = Team.objects.filter(camp=camp_id).order_by("-team_points")[:10]
    if request.user.profile.team:
        team_profiles = Profile.objects.filter(team=request.user.profile.team).order_by('-points')
        team_points = Team.objects.get(id=request.user.profile.team.id)

    display = Visibility.objects.filter(camp=camp_id).first().leaderboard
    image = Banner.objects.filter(camp=camp_id).first().leaderboard

    context = {
        'profiles': profiles,
        'teams': teams,
        'team_profiles': team_profiles,
        'team_details': team_points,
        'display': display,
        'banner': image,
        'camp_id': camp_id,
        'title': f'{camp.upper()} LEADERBOARD'
    }

    return render(request, 'award/leaderboard.html', context=context)
