import numpy as np
from agente import VaccumCleaner
from ambiente import Environment

if __name__ == "__main__":
    my_env = Environment(n_cols=10)
    agent = VaccumCleaner()
    
    my_env.add_agent(np.random.randint(len(my_env.room)))

    for i in range(20):
        my_env.render()
        my_env = agent.act(my_env)
        input()

        if my_env.is_clean():
            my_env.render()
            print("SALA LIMPA")
            break