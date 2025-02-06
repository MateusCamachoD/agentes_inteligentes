class MoveStrategy:
    def move(self, environment):
        pass

class MoveLeftStrategy(MoveStrategy):
    def move(self, environment):
        environment.agent_location -= 1
        print("MOVENDO PARA A ESQUERDA")
        
class MoveRightStrategy(MoveStrategy):
    def move(self, environment):
        environment.agent_location += 1
        print("MOVENDO PARA A DIREITA")