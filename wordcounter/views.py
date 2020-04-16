from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.POST.get('fulltext')
    wordlist = fulltext.split()

    dictionary = {}

    for word in wordlist:
        if word in dictionary:
            #Increase
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'dictionary': dictionary.items()})
