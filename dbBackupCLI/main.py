import tkinter as tk
from gui.app import BackupApp
from dotenv import load_dotenv # type: ignore
import os

def ensure_logs_folder():
    if not os.path.exists("logs"):
        os.makedirs("logs")

def main():
        load_dotenv()

        ensure_logs_folder()

        root = tk.Tk()
        app = BackupApp(root)
        root.mainloop()

if __name__ == "__main__":
    main()