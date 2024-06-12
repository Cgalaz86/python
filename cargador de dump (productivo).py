import subprocess
import os
import psycopg2

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'clear'
    os.system(command)

def restore_tables(host, port, username, password, dbname, table_schema_pairs, dump_file):
    
    clearConsole()
    
    # Establecer la contraseña como variable de entorno
    os.environ["PGPASSWORD"] = password

    # Conexión a la base de datos para borrar los datos de las tablas
    conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=username, password=password)
    conn.autocommit = True
    cursor = conn.cursor()

    for schema, table in table_schema_pairs:
        # Borra los datos de la tabla actual
        delete_query = f"DELETE FROM {schema}.{table};"
        try:
            print(f"Borrando datos de {schema}.{table}...")
            cursor.execute(delete_query)
            print(f"Datos borrados de {schema}.{table}.")
        except psycopg2.Error as e:
            print(f"Error al borrar datos de {schema}.{table}: {e}")
            continue  # Continuar con la siguiente tabla si hay un error

        # Comando para restaurar la tabla
        command = [
            "/Library/PostgreSQL/16/bin/pg_restore",
            "--host", host,
            "--port", str(port),
            "--username", username,
            "--dbname", dbname,
            "--data-only",
            "--verbose",
            "--schema", schema,
            "--table", table,
            dump_file
        ] 

        print(f"Restaurando {schema}.{table}...")
        result = subprocess.run(command, text=True, capture_output=True)
        if result.returncode != 0:
            print("Error al ejecutar el comando para", schema, table)
            print(result.stderr)
        else:
            print(f"Tabla {schema}.{table} restaurada con éxito.")

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

    # Eliminar la variable de entorno después de usarla
    del os.environ["PGPASSWORD"]

# Configura tus propios valores aquí
host = "localhost"
port = "5433"
username = "postgres"
password = "123456"  # Reemplaza con tu contraseña real
dbname = "dump"
table_schema_pairs = [

("nexus_public" , "sesiones_aulas"),
("weisstein_public" , "firmas_sesiones_aulas"),
("weisstein_public" , "registros_actividades"),
("pangea_public" , "asignaturas"),
("public" , "users"),
("public" , "cursos_aulas"),
("public" , "profile_cursos")

]
dump_file = "/Volumes/Howell_01/dumps/lirmi_cl-20240529_072001.dump"

# Llama a la función para restaurar las tablas
restore_tables(host, port, username, password, dbname, table_schema_pairs, dump_file)

