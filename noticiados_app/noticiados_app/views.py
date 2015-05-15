#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import *


#  Vistas
def start(request):
    init_state()
    return render(request, 'start.html', {})

def preguntando(request, respuesta=None):
    # Si respuesta es no nulo
    # viene de una pregunta anterior (ver state)
    state =  get_state()
    if respuesta:
        pregunta = PREGUNTAS[state['pregunta']]
        correcta = bool(pregunta["opciones"][int(respuesta)] == pregunta["respuesta"])

    state['pregunta'] += 1
    pregunta = PREGUNTAS[state['pregunta']]
    save_state(state)
    return render(request, 'preguntando.html', {'pregunta': pregunta, 'state': state})

def end(request):
    return render(request, 'end.html', {})
