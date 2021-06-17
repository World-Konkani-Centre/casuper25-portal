from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Testimonial, Website, Event, Post, Schedule, Visibility, Banner, Registration
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .utils import return_camp_id


def home(request):
    testimonial = Testimonial.objects.all()
    registration = Registration.objects.filter(is_open=True)
    context = {
        'testimonial': testimonial,
        'registration': registration,
        'title': 'HOME'
    }
    return render(request, 'webpages/home.html', context=context)


@login_required
def camp(request):
    return render(request, 'webpages/camp.html', context={'title': 'KSHAMATA CAMPS'})


@login_required
def schedule(request, camp):
    camp_id = return_camp_id(camp)
    day_1 = Schedule.objects.filter(day='DAY 1').filter(camp=camp_id)
    day_2 = Schedule.objects.filter(day='DAY 2').filter(camp=camp_id)
    day_3 = Schedule.objects.filter(day='DAY 3').filter(camp=camp_id)
    display = Visibility.objects.filter(camp=camp_id).first().schedule
    image = Banner.objects.filter(camp=camp_id).first().schedule
    context = {
        'title': f'{camp.upper()} SCHEDULE',
        'display': display,
        'banner': image,
        'day_1': day_1,
        'day_2': day_2,
        'day_3': day_3,
        'camp_id': camp_id
    }

    return render(request, 'webpages/schedule.html', context=context)


@login_required
def website(request, camp):
    camp_id = return_camp_id(camp)
    websites = Website.objects.filter(camp=camp_id)
    display = Visibility.objects.filter(camp=camp_id).first().teams
    image = Banner.objects.filter(camp=camp_id).first().teams
    context = {
        'title': f'{camp.upper()} TEAMS',
        'websites': websites,
        'display': display,
        'banner': image,
        'camp_id': camp_id
    }
    return render(request, 'webpages/website.html', context=context)


@login_required
def submit(request, camp):
    camp_id = return_camp_id(camp)
    display = Visibility.objects.filter(camp=camp_id).first().events
    image = Banner.objects.filter(camp=camp_id).first().events
    form = Event.objects.filter(camp=camp_id)
    context = {
        'title': f'{camp.upper()} Events',
        'events': form ,
        'display': display,
        'banner': image,
        'camp_id': camp_id
    }
    return render(request, 'webpages/submit.html', context=context)


@login_required
def camp_home(request, camp):
    camp_id = return_camp_id(camp)
    image = Banner.objects.filter(camp=camp_id).first().register
    context = {
        'title': f'{camp.upper()} 2021 EXPERIENCE HUB',
        'banner': image,
        'camp_id': camp_id
    }
    return render(request, 'webpages/camp_home_page.html', context=context)


def camp_register(request):
    messages.error(request, 'Please login to register for these camps.')
    return redirect('login')


def blog(request):
    post = Post.objects.all()
    context = {
        'queryset': post,
        'title': 'WISHES'
    }
    return render(request, 'blog/blog.html', context)


def blog_single(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            messages.success(request, 'Your Message is Posted')
            return redirect(request.META['HTTP_REFERER'])

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/blog-single.html', context=context)
