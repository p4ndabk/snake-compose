import sys
import time
from commands.command import Command
import importlib.resources

COMMANDS_PACKAGE = "commands"

BANNER = r"""                       __                                                             
  ______ ____ _____  |  | __ ____     ____  ____   _____ ______   ____  ______ ____  
 /  ___//    \\__  \ |  |/ // __ \  _/ ___\/  _ \ /     \\____ \ /  _ \/  ___// __ \ 
 \___ \|   |  \/ __ \|    <\  ___/  \  \__(  <_> )  Y Y  \  |_> >  <_> )___ \\  ___/ 
/____  >___|  (____  /__|_ \\___  >  \___  >____/|__|_|  /   __/ \____/____  >\___  >
     \/     \/     \/     \/    \/       \/            \/|__|              \/     \/ 
"""

def stract_command():
    if len(sys.argv) > 1:
        return sys.argv[1]

    return None

def list_commands_v1():
    return [
        file.stem
        for file in importlib.resources.files(COMMANDS_PACKAGE).iterdir()
        if file.suffix == ".py" and file.stem != "__init__"
    ]

def to_write(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def list_commands():
    commands = []

    for file in importlib.resources.files(COMMANDS_PACKAGE).iterdir():

        if file.suffix == ".py" and file.stem != "__init__" and file.stem != "command" and not file.name.startswith("._"):
            try:
                module = importlib.import_module(f"{COMMANDS_PACKAGE}.{file.stem}")

                class_name = "".join(word.capitalize() for word in file.stem.split("_"))

                command_class = getattr(module, class_name)

                command_instance = command_class()
                commands.append({
                    "name": command_instance.name.replace("_command", ""),
                    "description": command_instance.description
                })

            except (ImportError, AttributeError, Exception) as e:
                print(f"Erro ao carregar o comando {file.stem}: {e}")

    return commands

def start():
    console = stract_command()

    if console == None or console == "help":
        print(BANNER)
        to_write("Bem-vindo ao Snake-Compose!")
        to_write("Um console feito para desenvolvedores destemidos.")
        to_write("Digite 'help' para ver os comandos disponíveis.")
        to_write("Que a cobra do código esteja com você! Lá Ele\n")

        to_write("Comandos Disponíveis:")
        to_write("1. `help` - Exibe esta mensagem de ajuda.")
        to_write("2. `list` - Lista todos os itens ou recursos disponíveis.")

        to_write("\nDica: Use o comando `list` para ver o que você pode gerenciar!")
        to_write("Que a força do código esteja com você! 🐍\n")
        sys.exit()
    
    if console == "list":
        commands = list_commands()
        first_iteration = True
        for command in commands:
            if first_iteration:
                print("-" * 20)
                first_iteration = False 
            print(f"Nome: {command['name']}")
            print(f"Descrição: {command['description']}")
            print("-" * 20)
        sys.exit(0)
    
        
    command = Command(console)
    command.run()
    


if __name__ == "__main__":
    start()