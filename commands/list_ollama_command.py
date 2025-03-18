import os
import subprocess

class ListOllamaCommand:
    def __init__(self):
        self.name = "list_ollama_command"
        self.description = "Abre o codigo no vs code"
        pass
    
    def run(self):
                
        subprocess.run(['ollama', 'list'], check=True, text=True)