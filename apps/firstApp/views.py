from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("placeholder to display a list of all blogs")

def new(response):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(response):
    return redirect('/')

def number(response, number):
    return HttpResponse("placeholder to display blog number: {number}")

def edit(response, number):
    return HttpResponse('placeholder to edit blog number: {number}')

def delete(response, number):
    return redirect('/')