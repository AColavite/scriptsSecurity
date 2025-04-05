import os
from dotenv import load_dotenv # type: ignore

def load_env():
    load_dotenv()
    return{
        "mysql":{
            "name": os.getenv("MYSQL_DB"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "host": os.getenv("MYSWL_HOST", "localhost"),
            "dump_cmd": "mysqldump"
        },
        "postgres": {
               "name": os.getenv("POSTGRES_DB"),
            "user": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASSWORD"),
            "host": os.getenv("POSTGRES_HOST", "localhost"),
            "dump_cmd": "pg_dump"
            }
    }