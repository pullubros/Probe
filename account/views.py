from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template.context_processors import csrf
from account.forms import MyRegistrationForm


def home(request):
    return render(request, "home.html")


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/question/all')
    else:
        return HttpResponseRedirect('/account/invalid')


def loggedin(request):
    return render(request, 'loggedin.html')


def invalid_login(request):
    return render(request, 'invalid_login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print(args)
    return render_to_response('register_user.html', args)


def register_success(request):
    return render_to_response('register_success.html')
