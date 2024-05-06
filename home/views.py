from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples=[
        {'name' : 'abhijeet rajpal', 'age': 25},
        {'name' :'alamgir shahjahan', 'age': 30},
        {'name' :'muhammad hunain', 'age': 50},
        {'name' :'volkav', 'age': 15},
        {'name' :'anupam mittal', 'age': 55},
        {'name' :'nasir hussain', 'age': 12},
    ]
    for people in peoples:
        print(people)
    return render(request , "index.html", context={'peoples': peoples})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def success_page(request):
    return HttpResponse("Hey i am a success page")
