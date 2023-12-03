import psycopg2
from psycopg2 import DatabaseError
from decouple import config
from retrying import retry

@retry(wait_fixed=1000, stop_max_delay=30000)  # espera 1 segundo entre intentos, con un máximo de 30 segundos
def wait_for_db():
    try:
        connection = psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE'),
            connect_timeout=15
        )
        connection.close()
    except DatabaseError:
        raise

def get_connection():
    wait_for_db()  # espera hasta que la base de datos esté lista
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE'),
            connect_timeout=15
        )
    except DatabaseError as ex:
        raise ex