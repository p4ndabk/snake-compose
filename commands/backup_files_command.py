import time
class BackupFilesCommand:
    def __init__(self):
        self.name = "backup_files_command"
        self.description = "Salvar os arquivos."

    def run(self):
        print("Iniciado backup!")
        time.sleep(1)
        print("Finalizado backup!")
