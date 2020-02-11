import logging
from django.shortcuts import render
from django.http import JsonResponse
from . import repository
from .models import Token

from . import github_instance_manager as git


# Create your views here.

def token_list(request):
    tokens = Token.objects.all().values()
    token_list = list(tokens)
    return JsonResponse(token_list, safe=False)

def test(request):
    t = git.github_user()
    return JsonResponse("OK", safe=False)

def json_most_recent_token(request):
    token = repository.most_recent_token()
    return JsonResponse(token.to_dict(), safe=False)

