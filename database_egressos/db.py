import psycopg2 as psy

connect = psy.connect('dbname=egressos user=joelder')

cursor = connect.cursor()
schema = open('egressos.sql')

schema_as_string=schema.read()
print(schema_as_string)



cursor.execute(schema_as_string)

print('Banco Criado com sucesso')

connect.commit()
cursor.close()

connect.close()