from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello Django')

def create(request, id):
    return HttpResponse('create'+id)

def read(request):
    return HttpResponse('read')

def update(request):
    return HttpResponse('update')

def delete(request):
    return HttpResponse('delete')