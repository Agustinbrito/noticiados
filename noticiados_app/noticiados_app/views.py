#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

import os
import simplejson as json

from random import shuffle
from settings import PROJECT_DIR

PREGUNTAS_PATH = os.path.join(PROJECT_DIR, "preguntas.json")
PREGUNTAS = json.load(open(PREGUNTAS_PATH))
shuffle(PREGUNTAS)

PREGUNTAS_NIVEL = [
    [p for p in PREGUNTAS if p['nivel']==1],
    [p for p in PREGUNTAS if p['nivel']==2]
]

N_PREGS_POR_NIVEL = 5

ESTADO_INICIAL = {
            'vidas': 3,
            'nivel': 1,
            'pregunta': 0
        }

def start(request):
    return render(request, 'start.html', {})

def preguntando(request, estado=ESTADO_INICIAL):
    pregunta = PREGUNTAS[estado['pregunta']]

    estado['pregunta'] += 1
    return render(request, 'preguntando.html', {'pregunta': pregunta, 'estado': estado})

def end(request):
    return render(request, 'end.html', {})
