import pandas as pd
import os
import json

    
def get_details(s):
    a = os.path.basename(s)
    a = a.split('-')
    if a[2].__contains__('.xlsx'):
        a[2] = a[2][:-5]
    return a[0], a[1], a[2] # 0: materia | 1: unidad \ 2: categoria
        
def classify_dataframe(f):
    df = pd.read_excel(f)
    materia, unidad, categ = get_details(f)
    df['Categoria'] = pd.Series([categ]*len(df))
    df['Materia'] = pd.Series([materia]*len(df))
    df['Unidad'] = pd.Series([unidad]*len(df))
    return df

def get_json_pregs():
    dirname= 'Excels/'
    for root, dirs, files in os.walk(dirname):
        f = files
    
    names = [os.path.join(dirname, filename) for filename in f]
    dfs = [classify_dataframe(name) for name in names]
    
    df = pd.concat(dfs, axis=0)
    
    pr = []
    for i, row in df.iterrows():
        d = {}
        d.update({'Respuestas':row[1:5]})
        d.update({'Preguntas':row['Preguntas']})
        d.update({'Categoria':row['Categoria']})
        d.update({'Materia':row['Materia']})
        d.update({'Unidad':row['Unidad']})
        
        pr = pr + [d]
    
    return json.dumps(pr)
