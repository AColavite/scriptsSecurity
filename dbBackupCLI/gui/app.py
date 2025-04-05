import tkinter as tk 
from tkinter import ttk, messagebox
from threading import Timer
from datetime import datetime, timedelta
from controllers.backupControllers import run_backup

class backupApp:
    def __init__(self, master):
        self.master = master
        master.title("DB Backup utility")
        master.geometry("1024x768")

        self.db_type = tk.StringVar()
        self.password = tk.StringVar()

    def create_widgets(self):
        ttk.Label(self.master, text="Tipo de banco: ").pack(pady=5)
        ttk.Combobox(
            self.master, textvariable=self.db_type, values=["mysql", "postgres"]
        ).pack()

        ttk.Label(self.master, text="Admin password: ").pack(pady=5)
        ttk.Entry(self.master, textvariable=self.password, show="*").pack()
        
        
        ttk.Button(self.master, text="Make backup now", command=self.backup_now).pack(pady=5)
        ttk.Button(self.master, text="Schedule daily back to 03:00 AM", command=self.schedule_backup).pack(pady=5)

    def backup_now(self):
        if not self.db_type.get():
            messagebox.showerror("Error!", "Please choose the DataBase type.")
            return
        
        run_backup(self.db_type.get(), password=self.password.get())

    def schedule_backup(self):
        now = datetime.now()
        scheduled_time = now.replace(hour=3, minute=0, second=0, microsecond=0)

        if scheduled_time <= now:
            scheduled_time += timedelta(days=1)

        delay = (scheduled_time - now).total_seconds()

        def task():
            run_backup(self.db_type.get(), password=self.password.get())
            self.schedule_backup()

        Timer(delay, task).start()
        messagebox.showinfo("Scheduled.", "Daily backup scheduled to 03:00 AM")

# Standalone
if __name__ == "__main__":
    root = tk.Tk()
    app = BackupApp(root) # type: ignore
    root.mainloop()