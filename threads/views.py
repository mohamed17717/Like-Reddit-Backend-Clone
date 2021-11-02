from django.shortcuts import render
from django.http import HttpResponse


def index(request, pk):
  return HttpResponse(f'<h1>Welcome {request.user}, This is thread {pk}</h1>')
