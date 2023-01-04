import psycopg2 as psy
import pandas as pd



def create_list(word):
    s= set(data[word])
    l=[]
    for i in s:
        l.append([(i,)])
    return l

data = pd.read_csv('egressos_rais_2016.csv',sep=',',dtype='string',na_filter=False)

l2=[]
for i in range(len(data)):
  l=tuple(data.iloc[i][['curso_nome','nivel','codigo_inep','centro','campus','ds_situacao_curso','ds_grau_academico','turno']])
  if l not in l2:
    l2.append(l)


conn =  psy.connect("dbname=egressos user=joelder")

cur = conn.cursor()

cur.executemany("INSERT INTO sexo (nome) VALUES (%s);",create_list('sexo'))

cur.executemany("INSERT INTO turno(nome) VALUES(%s)",create_list('turno'))

cur.executemany("INSERT INTO campus(nome) VALUES(%s)",create_list('campus'))

cur.executemany("INSERT INTO centro(nome) VALUES(%s)",create_list('centro'))

cur.executemany("INSERT INTO mun_residen(nome) VALUES(%s)",create_list('mun_residen'))

cur.executemany("INSERT INTO grau_academico(nome) VALUES(%s)",create_list('ds_grau_academico'))

cur.executemany("INSERT INTO situacao_curso(nome) VALUES(%s)",create_list('ds_situacao_curso'))

cur.executemany("INSERT INTO nivel(nome) VALUES(%s)",create_list('nivel'))

conn.commit()
cur.close()
conn.close()

from insert_data import create_cursos,create_egressos
l2=[]
for i in range(len(data)):
  l=tuple(data.iloc[i][['curso_nome','nivel','codigo_inep','centro','campus','ds_situacao_curso','ds_grau_academico','turno']])
  if l not in l2:
    l2.append(l)

create_cursos(l2)

l2=[]
for i in range(len(data)):
  l=tuple(data.iloc[i][['key','ano_conclusao',\
        'periodo_conclusao','ano_ingresso',\
        'periodo_ingresso','data_nascimento',\
        'cra','sexo','mun_residen','curso_nome'] ])
  if l not in l2:
    l2.append(l)

create_egressos(l2)