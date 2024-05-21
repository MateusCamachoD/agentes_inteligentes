from pyamaze import maze, COLOR, agent

def compute_path(my_maze, my_agent):
    """
    Exercício:
    Implemente um algoritmo de busca por profundidade, que encontre o caminho 
    que o agente deve percorrer para encontrar a saída do labirinto.

    Dicas:
    - Use o atributo my_maze.maze_map para checar os movimentos possíveis.
    - Use o atributo my_agent.position para saber a posição do agente.
    - Verifique os formatos adequados para um caminho nesse post do
    Towards Data Science, feito pelo autor do pacote:
    https://towardsdatascience.com/a-python-module-for-maze-search-algorithms-64e7d1297c96
    """
    print(my_maze.maze_map)
    print(my_agent.position)
    return "NNNN"

if __name__ == "__main__":
    # cria environment
    my_maze = maze(5, 5)
    # lê labirinto do exercício
    my_maze.CreateMaze(theme=COLOR.light)
    # cria agente
    my_agent = agent(my_maze, 5, 5, shape="arrow", filled=True, footprints=True)
    # calcula passos que o agente seguirá para sair do labirinto
    my_path = compute_path(my_maze, my_agent)
    # executa os passos calculados
    my_maze.tracePath({my_agent: my_path}, delay=200, kill=False)
    # roda a animação mostrando o movimento do agente
    my_maze.run()
