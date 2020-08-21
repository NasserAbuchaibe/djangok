from django.http import HttpResponse

def helloW(HttpRequest):
    return HttpResponse("My first view in Django")

def testDjango(HttpRequest):
    return HttpResponse("Django is cool")
