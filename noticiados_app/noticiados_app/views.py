#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import *
# from django.contrib import messages


#  Vistas
def start(request):
    init_state()
    return render(request, 'start.html', {})

def preguntando(request, respuesta=None):
    # Si respuesta es no nulo
    # viene de una pregunta anterior (ver state)
    state =  get_state()
    pregunta = proxima_pregunta(state)
    save_state(state)
    return render(request, 'preguntando.html', {'pregunta': pregunta, 'state': state})

def respuesta(request, respuesta):
    # Si respuesta es no nulo
    # viene de una pregunta anterior (ver state)
    state =  get_state()
    pregunta = pregunta_actual(state)

    respuesta = pregunta["opciones"][int(respuesta)]
    correcta = bool(respuesta.lower() == pregunta["respuesta"].lower())
    if not correcta:
        state['vidas'] -= 1
    state['correctas'].append(correcta) 

    fin = bool(len(state['correctas']) == N_PREGS_POR_NIVEL)
    save_state(state)
    return render(request, 'respuesta.html', {'pregunta': pregunta, 'state': state,
                                                'correcta': correcta, 'fin': fin,
                                                'respuesta': respuesta})


def end(request):
    return render(request, 'end.html', {})
