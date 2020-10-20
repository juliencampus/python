from django.shortcuts import render

def index(request):
	    context = {"context_variable": context_variable}
    return render(request,'index.html', context)
