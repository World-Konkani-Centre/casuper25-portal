import re
from django.contrib import messages
from django.contrib.auth import logout
from users.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileUpdateForm, UserUpdateForm, UserRegisterForm, CampsUpdateForm
from django.contrib.auth.decorators import login_required

from .models import Profile
from webpages.utils import return_camp_id
from webpages.models import Banner, Registration


# register
def my_register(request, camp):
    camp_id = return_camp_id(camp)
    is_open = Registration.objects.filter(camp=camp_id).first()
    image = Banner.objects.filter(camp=camp_id).first().campers
    if request.user.is_authenticated:
        messages.info(request, f'Your already registered to our Website, You can check your enrolled camp.')
        return redirect('camp-registration')
    if request.POST:
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            messages.success(request,
                             f'You have successfully registered for SOTP 2021. You can login now with your email: {username}')
            form.save()
            form.instance.profile.camps.add(camp_id)
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'title': f'{camp.upper()} Register',
        'camp': is_open,
        'banner': image
    }
    return render(request, 'authorization/register.html', context)


@login_required
def camp_registration(request):
    form = CampsUpdateForm(instance=request.user.profile)
    if request.POST:
        form = CampsUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Camp preference is successfully updated')
            return redirect('index')
    context = {
        'form': form,
        'title': 'Camp Update'
    }
    return render(request, 'profile/camps-registered.html', context)

# logout
def my_logout(request):
    logout(request)
    return redirect('index')


@login_required
def my_profile(request):
    global u_form, p_form, profile
    user = get_object_or_404(User, id=request.user.id)

    if request.POST:
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user,
        'title': "Profile",
    }
    return render(request, 'profile/profile.html', context=context)


# show all them members in the profile
@login_required
def members(request, camp):
    camp_id = return_camp_id(camp)
    p_1 = Profile.objects.filter(role='Committee').order_by('user__name')
    p_2 = Profile.objects.filter(camps=camp_id).filter(role='Camper').order_by('user__name')
    image = Banner.objects.filter(camp=camp_id).first().campers

    context = {
        'committee': p_1,
        'campers': p_2,
        'banner': image,
        'camp_id': camp_id
    }
    return render(request, 'profile/members.html', context=context)
