from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from registration.users import UserModel

@login_required
def profile(request):
	user = UserModel().objects.get(username= request.user)
	variables = {}
	variables['group'] = str(user.groups)
	print user
	print user.email
	print user.groups
	return HttpResponse('m here')