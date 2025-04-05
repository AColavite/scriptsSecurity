import argparse
from controllers.backupControllers import run_backup

def handle_cli():
    parser = argparse.ArgumentParser(description="Database Backup CLI Utility")
    parser.add_argument("--mysql", action="store_true", help="Backup MySQL")
    parser.add_argument("--postgres", action="store_true", help="Backup PostgreSQL")
    args = parser.parse_args()

    if args.mysql:
        run_backup("mysql")
    elif args.postgres:
        run_backup("postgres")
    else:
        print("Nenhuma opção válida selecionada. Use --mysql ou --postgres.")