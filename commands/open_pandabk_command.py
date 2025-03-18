import os
import subprocess

class OpenPandabkCommand:
    def __init__(self):
        self.name = "open_pandabk_command"
        self.description = "Abre o codigo no vs code"
        pass
    
    def run(self):
        directory = "/Volumes/ssd-david/projects/snake-compose"
        os.chdir(directory)
                
        subprocess.run(['code', '.'], check=True, text=True)