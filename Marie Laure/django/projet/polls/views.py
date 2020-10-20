from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.

# Utilisation de classes pour générer deux vues génériques : ListView et DetailView.
# Elles permettent l’abstraction des concepts « afficher une liste d’objets »
# et « afficher une page détaillée pour un type particulier d’objet »


class IndexView(generic.ListView):
    # Par défaut, ListView utilise un gabarit appelé <nom app>/<nom modèle>_list.html
    # Ici, on lui dit d'utiliser le gabarit qu'on a créé
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Renvoie la liste des 5 dernières questions (hors questions futures)"""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # On indique à Django sur quel Model il doit agir (voir models.py)
    model = Question
    # On lui dit d'utiliser le gabarit qu'on a créé
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        N'affiche que les questions déjà publiées.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# Utilisation d'une fonction pour générer une vue


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
