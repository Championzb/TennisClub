from django.shortcuts import render_to_response
from admin import UserCreationForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from models import MyUser
from django.contrib import auth
from django.http import HttpResponse
from django.template import RequestContext
from LeagueMatch.models import LeagueMatch


def Register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Account/Register_Success')
	else:
		form = UserCreationForm()

	args = {}
	args.update(csrf(request))

	args['form']=form

	return render_to_response('register.html', args)

def Register_Success(request):
	return render_to_response('register_success.html')

def Login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def Login_Success(request):
	return render_to_response('login_success.html',
							{'email': request.user.email,
							 'league_matches': LeagueMatch.objects.all()})
	
def auth_view(request):
	email = request.POST.get('email', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(email=email,password=password)
	
	if user is not None: 
		auth.login(request, user)	
		return HttpResponseRedirect('/Account/Login_Success')
	else:
		return HttpResponseRedirect('/Account/Login_Failure')

def Login_Failure(request):
	return render_to_response('login_failure.html')
