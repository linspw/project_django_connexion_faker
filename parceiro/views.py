from django.http import HttpResponse
from django.http.response import JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_users(request):
    return JsonResponse({ "data": "deu certo" })
