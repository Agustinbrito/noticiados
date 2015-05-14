#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

import os
import json


PREGUNTAS_PATH = "/home/pablo/Proyectos/noticiados/preguntas/"

def cargar_preguntas():
    pregs = []
    for f in os.listdir(PREGUNTAS_PATH):
        pregs += json.load(open(PREGUNTAS_PATH + f))
    return pregs

PREGUNTAS = cargar_preguntas()

def home(request):
    return render(request, 'base.html', {})

def preguntando(request):
    return HttpResponse(PREGUNTAS)

def fin(request):
    return HttpResponse("A jugar!")
