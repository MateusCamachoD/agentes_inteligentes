class Command:
    def execute(self, environment):
        pass

class MoveLeftCommand(Command):
    def execute(self, environment):
        environment.agent_location -= 1
        print("MOVENDO PARA A ESQUERDA")
        
class MoveRightCommand(Command):
    def execute(self, environment):
        environment.agent_location += 1
        print("MOVENDO PARA A DIREITA")
        
class CleanCommand(Command):
    def execute(self, environment):
        environment.room[environment.agent_location] = 0
        print("LIMPANDO O ESPAÇO")