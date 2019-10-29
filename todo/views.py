from django.http import HttpResponse

def TodoIndex( request ):
    return HttpResponse("hello world")