class HelloWorldCommand:
    def __init__(self):
        self.name = "hello_world_command"
        self.description = "Comando que imprime Olá, Mundo!."
        pass
    
    def run(self):
        print("Olá, Mundo!")
