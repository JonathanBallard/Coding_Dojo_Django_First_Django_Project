from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey.html')

def newSurvey(request):
    return redirect('/surveys/')