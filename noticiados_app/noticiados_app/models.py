#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import simplejson as json
from copy import deepcopy
from random import shuffle
import simplejson as json
from settings import PROJECT_DIR
#import settings.py


# Preguntas
# PREGUNTAS_PATH = os.path.join(PROJECT_DIR, "preguntas.json")
PREGUNTAS_PATH = os.path.join(PROJECT_DIR, "preguntas2.json")
PREGUNTAS = json.load(open(PREGUNTAS_PATH))
shuffle(PREGUNTAS)

# PREGUNTAS_NIVEL = [
#     [p for p in PREGUNTAS if p['nivel']==1],
#     [p for p in PREGUNTAS if p['nivel']==2]
# ]

PREGUNTAS_NIVEL = [PREGUNTAS, PREGUNTAS]

N_PREGS_POR_NIVEL = 10


# Estados
STATE_PATH = os.path.join(PROJECT_DIR, "state.json")

ESTADO_INICIAL = {
            'vidas': 3,
            'nivel': 1,
            'pregunta': -1,
            'correctas': [],
            'vidas_string': '❤ ❤ ❤'
        }

def init_state():
    shuffle(PREGUNTAS)
    state = deepcopy(ESTADO_INICIAL)
    save_state(state)
    return state

def get_state():
    return json.load(open(STATE_PATH))

def save_state(state):
    json.dump(state, open(STATE_PATH, 'w'))

def proxima_pregunta(state):
    state['pregunta'] += 1
    return PREGUNTAS_NIVEL[state['nivel']][state['pregunta']]

def pregunta_actual(state):
    return PREGUNTAS_NIVEL[state['nivel']][state['pregunta']]
