from django.shortcuts import render
# , get_object_or_404, redirect
# from django.template import loader
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # One good old style of programming functions
    # Define your context variable, then render
    return render(request, "index.html", {})