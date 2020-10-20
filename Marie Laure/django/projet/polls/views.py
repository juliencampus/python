from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

# Create your views here.


def index(request):
    # On récupère les 5 dernières questions en BDD
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # On renvoie la variable latest_question_list vers la vue
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # On récupère les questions en BDD dont la clé primaire correspond à l'ID passé en paramètre
    question = get_object_or_404(Question, pk=question_id)
    try:
        # On teste s'il y a une correspondance en BDD entre la clé primaire du choix qui a été fait dans le formulaire
        # et les choix présents en BDD

        # request.POST est un objet similaire à un dictionnaire qui vous permet d’accéder aux données envoyées par leurs clés.
        # request.POST['choice'] renvoie l’ID du choix sélectionné, sous forme d’une chaîne de caractères.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # S'il ne trouve pas de correspondance, on renvoie le formulaire de vote
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Si on trouve une correspondance, on ajoute +1 à la colonne "vote" de la table Choice, puis on enregistre
        selected_choice.votes += 1
        selected_choice.save()
        # On redirige vers la page "results" pour que l'utilisateur ne puisse pas voter plusieurs fois en revenant en arrière
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
