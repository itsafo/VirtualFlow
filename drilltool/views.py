from django.shortcuts import render
# , get_object_or_404, redirect
# from django.template import loader
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # One good old style of programming functions
    # Define your context variable, then render
    return render(request, "index.html", {})


# +++++++++++++++ CALCULATION FUNCTIONS ++++++++++++++
def drill(request):
    # One good old style of programming functions
    # Define your context variable, then render
    if request.method == 'POST':
	    val1 = int(request.POST['num1'])
	    val2 = int(request.POST['num2'])
	    res = val1 + val2
    return render(request, "drill.html", {'result':res})
