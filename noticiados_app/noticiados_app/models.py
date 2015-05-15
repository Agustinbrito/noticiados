import os
import simplejson as json
from copy import deepcopy
from random import shuffle
import simplejson as json
from settings import PROJECT_DIR


# Preguntas
PREGUNTAS_PATH = os.path.join(PROJECT_DIR, "preguntas.json")
PREGUNTAS = json.load(open(PREGUNTAS_PATH))
# shuffle(PREGUNTAS)

PREGUNTAS_NIVEL = [
    [p for p in PREGUNTAS if p['nivel']==1],
    [p for p in PREGUNTAS if p['nivel']==2]
]

N_PREGS_POR_NIVEL = 5


# Estados
STATE_PATH = os.path.join(PROJECT_DIR, "state.json")

ESTADO_INICIAL = {
            'vidas': 3,
            'nivel': 1,
            'pregunta': -1,
            'correctas': []
        }

def init_state():
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
