import psycopg2
import logger

user = "bksp_user"
password = "django"
host = "127.0.0.1"
port = "5432"
database = "bank_db"


def connect_to_db():
    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        logger.debug("Successfully connect to PostgreSQL")
        return connection
    except (Exception, psycopg2.Error) as error:
        logger.error("Error while connecting to PostgreSQL:", error)
        return None