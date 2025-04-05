import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

def get_db_config(db_type):
    if db_type == "mysql":
        return {
            "host": os.getenv("MYSQL_HOST", "localhost"),
            "user": os.getenv("MYSQL_USER", "root"),
            "password": os.getenv("MYSQL_PASSWORD", ""),
            "name": os.getenv("MYSQL_DATABASE", ""),
            "dump_cmd": os.getenv("MYSQL_DUMP_CMD", "mysqldump")
        }
    elif db_type == "postgres":
        return {
            "host": os.getenv("POSTGRES_HOST", "localhost"),
            "user": os.getenv("POSTGRES_USER", "postgres"),
            "password": os.getenv("POSTGRES_PASSWORD", ""),
            "name": os.getenv("POSTGRES_DATABASE", ""),
            "dump_cmd": os.getenv("POSTGRES_DUMP_CMD", "pg_dump")
        }
    else:
        return None
