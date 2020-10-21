from django.shortcuts import render

def index(request, contexte_variabale=None):
    contexte = {"contexte_variable": contexte_variabale}
    return render(request,'index.html', contexte)
