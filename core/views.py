from django.shortcuts import HttpResponse

# Create your views here.

def teste1(request):
    return HttpResponse("We're testing drf")

def teste2(request):
    return HttpResponse("We're testing drf test2")
