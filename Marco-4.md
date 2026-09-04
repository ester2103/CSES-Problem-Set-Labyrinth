## 🏆 Marco 4 — Aplicação Básica de BFS e Conclusão

Para encontrar o menor caminho no Labyrinth (CSES), substituímos a DFS pela **Busca em Largura (BFS)**. A BFS explora o grafo em "camadas" radiais, garantindo que a primeira vez que o destino for alcançado, o trajeto feito é o mais curto possível.

### 1. Execução Manual e Comportamento da Fila (`Queue`)
Ao contrário da DFS que usa recursão (Pilha/Stack), a BFS utiliza uma estrutura de **Fila (Queue - FIFO)**.
1. O vértice de origem `A(1,2)` entra na fila.
2. Enquanto a fila não estiver vazia, desenfileiramos o primeiro elemento e verificamos seus vizinhos válidos.
3. Seguindo a ordem L, D, R, U, enfileiramos os vizinhos ainda não visitados (`marked = false`), marcando-os imediatamente para evitar duplicação.
4. Quando atingimos o vértice `(3,4)`, a BFS encontra uma bifurcação. Ela enfileira tanto `(3,5)` quanto `(2,4)`. Ambos estão no mesmo **nível de distância** da origem. A BFS processa a fila uniformemente, avançando um passo de cada vez em todas as direções possíveis.

### 2. Níveis, Distâncias e Rastreamento
A tabela abaixo mostra a ordem de descoberta. Adicionamos a matriz `distTo` (nível/distância), além do `marked` e `edgeTo`. O nível de `A` é 0, e a cada expansão, o vizinho recebe `distTo[atual] + 1`.

| V (Vértice) | marked | edgeTo  | distTo (Nível) |
| :---        | :---:  | :---:   | :---:          |
| `(1,2)` [A] | true   | -       | 0              |
| `(1,1)`     | true   | `(1,2)` | 1              |
| `(2,1)`     | true   | `(1,1)` | 2              |
| `(3,1)`     | true   | `(2,1)` | 3              |
| `(3,2)`     | true   | `(3,1)` | 4              |
| `(3,3)`     | true   | `(3,2)` | 5              |
| `(3,4)`     | true   | `(3,3)` | 6              |
| `(3,5)`     | true   | `(3,4)` | 7              |
| `(2,4)`     | true   | `(3,4)` | 7              |
| `(3,6)`     | true   | `(3,5)` | 8              |
| `(1,4)`     | true   | `(2,4)` | 8              |
| `(2,6)` [B] | true   | `(3,6)` | 9              |

*Note que `(3,5)` e `(2,4)` foram descobertos no mesmo nível (distância 7 de A). O vértice destino `B` foi encontrado no nível 9.*

### 3. Comparação entre DFS e BFS
* **DFS (Marco 3):** Explora de forma profunda e errática. Acha caminhos viáveis, mas é altamente dependente da ordem de exploração e frequentemente retorna caminhos mais longos.
* **BFS (Marco 4):** Explora em ondas expansivas (níveis). Ela processa sistematicamente todas as células a 1 passo de distância, depois a 2 passos, etc. O primeiro contato com `B` é o ótimo global.

### 4. Escolha Justificada e Complexidade
* **Escolha:** O enunciado do problema exige estritamente o comprimento do menor caminho e suas direções. Em grafos não ponderados (onde toda aresta/passo custa 1), a BFS é a única abordagem correta para esse requisito.
* **Adaptação e Integração:** A matriz bidimensional (grafo implícito) foi mantida, e implementamos vetores de deslocamento (ex: `dx = {-1, 1, 0, 0}`) para iterar sobre os vizinhos sem estourar os limites da matriz.
* **Complexidade:** $O(V + E)$, que em um grid se traduz para o máximo de $O(N \times M)$ tanto em tempo (visitamos cada célula no máximo uma vez) quanto em espaço (armazenamento das matrizes `marked`, `edgeTo` e da própria `Queue`). Para $N, M \le 1000$, isso é extremamente eficiente e perfeitamente ajustado ao limite de 1.00s.

### 5. Submissão e Ensaio
* **Submissão CSES:** Status `Accepted`.
* **Conclusão:** A modelagem matricial se mostrou excelente para a representação da memória. O uso da Fila para controlar os níveis de profundidade na BFS solucionou o gargalo imposto pela DFS. A reconstrução da resposta, varrendo o `edgeTo` do destino à origem, confirmou de forma prática a teoria por trás da preservação de caminhos em algoritmos de busca.
