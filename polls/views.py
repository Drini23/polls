from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Question, Choice
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse


# Create your views here.


def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User is authenticated, so log them in.
            login(request, user)
            return redirect("polls:shpia")
        else:
            return HttpResponse("Invalid credentials")
    context = {"login_view": "active"}
    return render(request, "polls/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('polls:shpia')

class SingUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('polls:shpia')
    template_name = 'polls/singup.html'

@login_required(login_url='polls:login')
def index(request):
    zgjidhje = Choice.objects.all()
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list, 'zgjidhje': zgjidhje})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

@login_required(login_url='polls:login')
def results(request):
    choices = Choice.objects.all()
    context = {'choices': choices}
    return render(request, 'polls/results.html', context)

@login_required(login_url='polls:login')
def vote(request):
    if request.method == 'POST':
        # Get the selected choice's ID from the form
        choice_id = request.POST.get('choice')

        # Retrieve the Choice object based on the selected ID
        choice = get_object_or_404(Choice, pk=choice_id)

        # Update the vote count for the selected choice
        choice.votes += 1
        choice.save()

        # Redirect to a results page or another view
        return redirect('polls:results')  # Change 'polls:results' to the correct results view name

    # If it's a GET request or after processing the form, display the voting form
    choices = Choice.objects.all()
    return render(request, 'polls/vote.html', {'choices': choices})


def shpia(request):
    return render(request, 'polls/shpia.html', )
