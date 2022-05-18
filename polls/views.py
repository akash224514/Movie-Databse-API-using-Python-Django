from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Question,Movie

import requests

import django


def avengers(request):

    return HttpResponse("avengers view.")




def batman(request):
    return HttpResponse("batman view.")



def index(request):
    count = 0
    moviename = "avengers"

    url = 'https://www.omdbapi.com/?t=' + moviename +  '&apikey=38682202'

    resp = requests.get(url).json()
    print(resp)
    print(resp['Title'])

    q = Question()
    q.question_text = resp['Title']
    q.save()
    query_results = Question.objects.all();
    for q in query_results:
        print(q.question_text)
    print (query_results)


    qstring= query_results[len(query_results)-1].question_text

    temp = qstring.replace('\n', '<br>')

    print ("temp")
    print (query_results)

    questions =  Question.objects.all();
    #return HttpResponse("Hello, world. You're at the polls index."  + "\t" + temp )

    context = {'latest_question_list': questions}
    return render(request, 'polls/index.html', context)


    #return render(request, 'polls/index.html', {'questions': questions})


def search(request):
    try:
        query = request.GET['query']
        if query == 'avengers':
            return HttpResponse(Movie)
        if query == 'batman':
            return HttpResponse(Movie)
    except:
        print(request)
        searchfield =''
        searchfield = (request.POST.get('search'))
        print (searchfield)
        url = 'https://www.omdbapi.com/?t='+ str(searchfield) +'&apikey=38682202'
        resp = requests.get(url).json()
        print("resp:", resp)
        #get from resp
        title =  resp['Title']
        year =  resp['Year']
        genre = resp['Genre']
        writer = resp['Writer']
        plot = resp['Plot']
        director = resp['Director']
        awards = resp['Awards']
        Type =   resp['Type']
        actors = resp['Actors']
        #set to model
        m = Movie()
        m.title = title
        m.year = year
        m.genre = genre
        m.writer = writer
        m.plot = plot
        m.director = director
        m.awards = awards
        m.Type = Type
        m.Actors = actors
        m.save()
        return render(request,'polls/search.html')


def add(request):
    m = Movie()
    m.title = "superman"
    m.save()
    f = MovieForm(request.POST, instance=m)
    f.save()
    return HttpResponse()


def get(request):
    movies =  Movie.objects.all();
    context = {'movies': movies}
    return render(request, 'polls/print.html', context)


def getdata(request):
    movies =  Movie.objects.all();
    context = {'movies': movies}
    return render(request, 'polls/print.html', context)
