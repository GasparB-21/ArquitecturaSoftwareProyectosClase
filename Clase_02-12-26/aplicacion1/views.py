from django.shortcuts import render, HttpResponse

# Create your views here.
def vista_tutorial(request):
    return HttpResponse("¡Bienvenido al tutorial de Django!")

def vista_tutorial_1(request):
    return HttpResponse("¡Bienvenido!")

def vista_tutorial_2(request):
    return HttpResponse("¡Hola!")
    