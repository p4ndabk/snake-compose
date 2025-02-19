import importlib

class Command:
    def __init__(self, name, description=None):
        self.name = name
        self.description = None
        
    def run(self, *args):
        module = importlib.import_module(f"commands.{self.name}")

        class_name = "".join(word.capitalize() for word in self.name.split("_"))

        command_class = getattr(module, class_name)

        cmd = command_class()

        cmd.run()

