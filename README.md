# Projeto Vacuum Cleaner https://github.com/shgo/agentes_inteligentes?utm_source=chatgpt.com

## Padrões de Refatoração Aplicados:

### 1. **Composing Methods**:
   - **Objetivo**: Criar métodos pequenos e específicos para separar diferentes responsabilidades dentro de um método complexo. Isso melhora a legibilidade, reutilização e manutenibilidade do código.
   - **Implementação**:
     - O método `act` do agente foi dividido em três métodos: `decide_move_direction`, `move` e `clean`.
     - **`decide_move_direction`**: Define a direção para o movimento do agente.
     - **`move`**: Executa o movimento do agente com base na estratégia escolhida.
     - **`clean`**: Verifica se o agente está em uma posição suja e realiza a limpeza, se necessário.

### 2. **Simplifying Conditional Expressions**:
   - **Objetivo**: Simplificar as expressões condicionais complexas, tornando o código mais legível e fácil de modificar.
   - **Implementação**:
     - A lógica de movimentação foi simplificada no método `decide_move_direction`, que agora determina de maneira mais clara se o agente deve mover para a esquerda ou para a direita.
     - A verificação de se o ambiente está limpo foi simplificada no ambiente com o método `is_clean`, removendo a necessidade de verificações diretas no código principal.

### 3. **Simplifying Method Calls**:
   - **Objetivo**: Tornar a chamada dos métodos mais simples e compreensíveis.
   - **Implementação**:
     - O método `act` agora encapsula a lógica do agente em chamadas claras para `decide_move_direction`, `move` e `clean`, o que torna o código principal mais limpo e a execução mais intuitiva.

## Exemplo de Execução:

```bash
['0', '0', '0', '1', '0', '1', '1', '0', '0', '0']
['-', '-', '-', '-', '-', '-', '-', '-', '-', 'X']
MOVENDO PARA A DIREITA
LIMPANDO O ESPAÇO
```