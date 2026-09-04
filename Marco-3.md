##  Marco 3 — Aplicação Básica de DFS (Simulação no Exemplo 5x8)

Com base no exemplo de entrada 5x8 fornecido, simulamos a execução de uma Busca em Profundidade (DFS).

**Mapeamento Inicial:**
* Coordenadas (linha, coluna) baseadas em índice 0.
* Ponto de Partida `A`: (1, 2)
* Ponto de Destino `B`: (2, 6)
* **Ordem de prioridade de exploração:** Esquerda, Baixo, Direita, Cima (L, D, R, U).

### 1. Execução Manual e Árvore de Busca
A DFS começa em `A(1,2)` e avança o mais profundo possível na primeira direção válida. Seguindo nossa prioridade (L, D, R, U):
1. De `(1,2)`, o único passo livre é para a Esquerda → (1,1).
2. De `(1,1)`, desce → (2,1).
3. De `(2,1)`, desce → (3,1).
4. A partir de `(3,1)`, o algoritmo segue um "corredor" direto para a Direita: → (3,2) → (3,3) → (3,4) → (3,5) → (3,6).
5. Em `(3,6)`, sobe → (2,6), encontrando o destino `B`.

*Nota de Árvore de Busca:* Mesmo após achar `B`, a DFS clássica continua explorando os vizinhos livres para montar a árvore completa. De `B(2,6)`, ela sobe para (1,6) → (1,5) → (1,4) → (2,4). Ao chegar em (2,4), fica sem saídas (beco sem saída) e inicia o *backtracking* (retorno) até `A`.

### 2. Estados de Visita (`marked`)
Durante a execução, o vetor/matriz `marked` garante que não entremos em loop, registrando `true` para os vértices descobertos. 
* Vértices que são paredes (como o `#` entre conexões inválidas) nunca são acessados e seu `marked` permanece `false`.
* O caminho `(3,4)` possuía uma bifurcação. Como a prioridade "Direita" foi testada primeiro, a célula superior `(2,4)` só teve seu estado `marked` alterado para `true` muito depois, no final da árvore de recursão.

### 3. Rastreamento: marked, edgeTo, d e f
Abaixo detalhamos o estado das principais estruturas do algoritmo ao longo da execução da DFS. O vetor `edgeTo` salva o predecessor exato (a aresta de onde viemos), crucial para reconstruir o caminho no final.

| V (Vértice) | marked | edgeTo  | d (Descoberta) | f (Término) |
| :---        | :---:  | :---:   | :---:          | :---:       |
| `(1,2)` [A] | true   | -       | 1              | 28          |
| `(1,1)`     | true   | `(1,2)` | 2              | 27          |
| `(2,1)`     | true   | `(1,1)` | 3              | 26          |
| `(3,1)`     | true   | `(2,1)` | 4              | 25          |
| `(3,2)`     | true   | `(3,1)` | 5              | 24          |
| `(3,3)`     | true   | `(3,2)` | 6              | 23          |
| `(3,4)`     | true   | `(3,3)` | 7              | 22          |
| `(3,5)`     | true   | `(3,4)` | 8              | 21          |
| `(3,6)`     | true   | `(3,5)` | 9              | 20          |
| `(2,6)` [B] | true   | `(3,6)` | 10             | 19          |
| `(1,6)`     | true   | `(2,6)` | 11             | 18          |
| `(1,5)`     | true   | `(1,6)` | 12             | 17          |
| `(1,4)`     | true   | `(1,5)` | 13             | 16          |
| `(2,4)`     | true   | `(1,4)` | 14             | 15          |

### 4. Alcançabilidade, Predecessores e Aplicabilidade
* **Alcançabilidade:** Como o `marked` do vértice `B(2,6)` virou `true` e os tempos foram registrados, ele é oficialmente alcançável a partir de `A`.
* **Predecessores:** Usando a coluna `edgeTo`, podemos fazer o rastreamento reverso exato de `B` até `A`: (2,6) ← (3,6) ← (3,5) ← (3,4) ... ← (1,2).
* **Aplicabilidade ao Problema:** Coincidentemente, por causa da ordem escolhida, a DFS encontrou o caminho `LDDRRRRRU` (9 passos) de primeira. No entanto, se a prioridade fosse "Cima" antes de "Direita" na bifurcação `(3,4)`, a DFS teria feito uma volta enorme por cima `(1,4)`, resultando em um caminho subótimo de 11 passos. Isso reforça que **a DFS encontra um caminho (alcançabilidade), mas não garante a rota mais curta**, provando que a BFS (Marco 4) é a escolha correta para o CSES.
