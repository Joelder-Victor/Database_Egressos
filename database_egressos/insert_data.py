import psycopg2 as psy


def create_sql(row):
    return "SELECT "+row+"_id FROM "+row+" WHERE nome=(%s)"

def create_str(row):
    return [(row,)]

def create_cursos(l2):
    conn =  psy.connect("dbname=egressos user=joelder")
    cur = conn.cursor()

    schema=['curso','nivel','codigo_inep','centro','campus',\
            'situacao_curso','grau_academico','turno']

    for i in range(len(l2)):
        l3=[]
        for j in range(len(schema)):
            if schema[j] == 'curso':
                l3.append(l2[i][0])
            elif schema[j] == 'codigo_inep':
                if l2[i][2] == 'NA':
                    l3.append(None)
                else:
                    l3.append(l2[i][2])
            else:
                cur.execute(create_sql(schema[j]),create_str(l2[i][j]))
                l3.append(cur.fetchone()[0])
    
        cur.executemany("""
        INSERT INTO curso(nome,nivel_id,codigo_inep,
            centro_id,campus_id,situacao_curso_id,
            grau_academico_id,turno_id) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",[tuple(l3)]
        )
    conn.commit()
    cur.close()
    conn.close()
    return

def create_egressos(l2):
    conn =  psy.connect("dbname=egressos user=joelder")
    cur = conn.cursor()

    schema=['key','ano_conclusao','periodo_conclusao',\
            'ano_ingresso','periodo_ingresso',\
            'data_nascimento','cra','sexo',\
            'mun_residen','curso']

    for i in range(len(l2)):
        l3=[]
        for j in range(len(schema)):
            if l2[i][j] == 'NA':
                l3.append(None)
            elif j< 7:
                l3.append(l2[i][j])
            else:
                cur.execute(create_sql(schema[j]),create_str(l2[i][j]))
                l3.append(cur.fetchone()[0])
        
        cur.executemany("""
        INSERT INTO egresso(cpf,ano_conclusao,periodo_conclusao,
            ano_ingresso,periodo_ingresso,data_nascimento,
            cra,sexo_id,mun_residen_id,curso_id) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",[tuple(l3)]
        )
    conn.commit()
    cur.close()
    conn.close()