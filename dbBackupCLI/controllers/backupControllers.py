import os
import subprocess
import datetime
import sys
from models.db_config import get_db_config # type: ignore
from middlewares.auth import require_authentication # type: ignore

LOG_PATH = "logs/backup.log"

def log(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_PATH, "a") as f:
        f.write(f"{timestamp} {message}\n")

def get_backup_filename(db_type, db_name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"backup_{db_type}_{db_name}_{timestamp}.sql"

def create_backup_command(db_type, config, backup_file):
    if db_type == "mysql":
        return f"{config['dump_cmd']} -h {config['host']} -u {config['user']} -p{config['password']} {config['name']} > {backup_file}"
    elif db_type == "postgres":
        os.environ["PGPASSWORD"] = config["password"]
        return f"{config['dump_cmd']} -h {config['host']} -U {config['user']} -F c {config['name']} -f {backup_file}"
    else:
        return None

def run_backup(db_type, password=None):
    try:
        require_authentication(password)
        config = get_db_config(db_type)

        if not config:
            log(f"Erro: Configuração inválida para {db_type}")
            print(f"Erro: Configuração inválida para {db_type}")
            return

        backup_file = get_backup_filename(db_type, config["name"])
        command = create_backup_command(db_type, config, backup_file)

        if not command:
            log("Erro: Tipo de banco não suportado.")
            print("Erro: Tipo de banco não suportado.")
            return

        subprocess.run(command, shell=True, check=True)
        log(f"Backup {db_type} concluído com sucesso: {backup_file}")
        print(f"✔️ Backup {db_type} feito: {backup_file}")

    except subprocess.CalledProcessError as e:
        log(f"Erro ao executar backup: {e}")
        print(f"❌ Erro ao executar backup: {e}")
    except SystemExit:
        log("Autenticação falhou.")
    finally:
        if db_type == "postgres":
            del os.environ["PGPASSWORD"]
