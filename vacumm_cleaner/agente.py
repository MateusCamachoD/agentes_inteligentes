from comando import MoveLeftCommand, MoveRightCommand, CleanCommand
from estrategia import MoveLeftStrategy, MoveRightStrategy

class VaccumCleaner:
    def __init__(self):
        self.move_direction = 0
        self.move_strategy = None

    def set_move_strategy(self, strategy):
        self.move_strategy = strategy

    def decide_move_direction(self, environment):
        if environment.agent_location == 0:
            self.set_move_strategy(MoveRightStrategy())
        elif environment.agent_location == len(environment.room) - 1:
            self.set_move_strategy(MoveLeftStrategy())
        else:
            # Se o agente não estiver nas extremidades, ele escolhe a direção onde há um espaço sujo.
            if environment.room[environment.agent_location - 1] == 1:
                self.set_move_strategy(MoveLeftStrategy())
            elif environment.room[environment.agent_location + 1] == 1:
                self.set_move_strategy(MoveRightStrategy())
            else:
                # Caso não haja espaço sujo para mover, o agente pode ir em qualquer direção
                print("Nenhum espaço sujo à vista, agente se movendo sem razão.")

    def move(self, environment):
        if self.move_strategy:
            self.move_strategy.move(environment)
        else:
            print("Erro: A estratégia de movimento não foi definida!")

    def clean(self, environment):
        if environment.room[environment.agent_location] == 1:
            clean_command = CleanCommand()
            clean_command.execute(environment)
            print("Limpeza realizada no espaço.")
        else:
            print("O espaço já está limpo.")

    def act(self, environment):
        self.decide_move_direction(environment)
        self.move(environment)
        self.clean(environment)

        return environment