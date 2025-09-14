from django.http import HttpResponse


def home_view(request):
    return HttpResponse("This is some simple text displayed by a Django view.")