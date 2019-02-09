from django.shortcuts import render
from django.http import HttpResponse

def listaDeTarefas(request):
    return HttpResponse('Lista de tarefas')
