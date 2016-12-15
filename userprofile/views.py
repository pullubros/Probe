from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from userprofile.models import UserProfile


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST or None, request.FILES or None, instance=request.user.profile)
        if form.is_valid():
            form.save()
            p = request.user.id
            return HttpResponseRedirect('/account/profile/get/%s' % p)
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('profile.html', args)


def view_profile(request, userprofile_id=1):
    return render(request, 'view_profile.html', {'userprofile': UserProfile.objects.get(id=userprofile_id)})


def userprofiles(request):
    args = {}
    args.update(csrf(request))
    args['userprofiles'] = UserProfile.objects.all()
    return render_to_response('profiles.html', args)


def userprofile(request, userprofile_id):
    return render(request, 'show_profile.html', {'userprofile': UserProfile.objects.get(id=userprofile_id)})


def show_profile(request):
    p = request.user.id
    return HttpResponseRedirect('/account/profile/get/%s' % p)


def follow(request, userprofile_id=1):
    x = UserProfile.objects.get(id=userprofile_id)
    p = request.user
    t = x.user.id
    x.followers.add(p)
    x.save()
    return HttpResponseRedirect('/account/profile/get/%s' % t)


def show_followers(request, userprofile_id=1):
    return render(request, 'show_followers.html', {'userprofile': UserProfile.objects.get(id=userprofile_id)})
