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

ESTADO_INICIAL = {
            'vidas': 3,
            'nivel': 1,
        }

def start(request):
    return render(request, 'start.html', {})

def preguntando(request, pregunta=PREGUNTAS[0], estado=ESTADO_INICIAL):
    return render(request, 'preguntando.html', {'pregunta': pregunta, 'estado': estado})

def end(request):
    return render(request, 'end.html', {})
