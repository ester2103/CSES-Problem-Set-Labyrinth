
# CSES Problem Set — Labyrinth

Repositório destinado ao acompanhamento processual da resolução do problema "Labyrinth" (CSES), documentando as evidências de cada marco da atividade.

---

## 📌 Marco 1 — Modelagem

* **Enunciado:** O objetivo é encontrar um caminho do ponto `A` para o ponto `B` em um labirinto, informando se é possível e, caso seja, o comprimento do menor caminho e a direção dos passos (L, R, U, D).
* **Entrada:** Dois inteiros $n$ e $m$ representando a altura e largura do grid. Em seguida, $n$ linhas com $m$ caracteres cada, onde `.` é piso, `#` é parede, `A` é o início e `B` é o final.
* **Saída:** "YES" se houver caminho e "NO" caso contrário. Se "YES", imprimir também o tamanho do menor caminho e uma string com as direções percorridas.
* **Restrições:** $1 \le n, m \le 1000$. Limite de tempo de 1.00s.
* **Vértices:** Cada célula caminhável (caracteres `.`, `A` ou `B`) do grid representa um vértice do grafo.
* **Arestas:** Conexões adjacentes válidas (cima, baixo, esquerda, direita) entre as células caminháveis.
* **Tipo do Grafo:** Grafo não direcionado (movimento bidirecional), não ponderado e cíclico.
* **Instância Pequena (Exemplo):**
  ```text
  5 5
  #####
  #A..#
  ###.#
  #B..#
  #####

```

* **Resultado Esperado:**
```text
YES
4
RRDD

```


* **Hipótese Inicial de Solução:** Modelar o labirinto como um grafo implícito na matriz e utilizar um algoritmo de busca (como a BFS para garantir o caminho mais curto) para explorar os vértices adjacentes a partir de `A` até encontrar `B`.

---

## 💻 Marco 2 — Representação Computacional

* **Tipo de Representação:** Representação implícita (Matriz de Caracteres). Como o grafo é um grid regular perfeito, criar uma lista de adjacência tradicional consumiria memória excessiva. A própria matriz bidimensional atua como o grafo, utilizando vetores de direção (deslocamentos em $x$ e $y$) para acessar os vizinhos.
* **Leitura da Entrada e Construção:** A leitura é realizada processando a entrada linha por linha para construir a matriz bidimensional. Durante essa varredura inicial, as coordenadas exatas dos pontos de partida (`A`) e destino (`B`) são mapeadas e salvas.
* **Medidas Estruturais (Unidade I):** O grau máximo de qualquer vértice neste grafo é 4 (quando uma célula livre está cercada por outras 4 células livres). O número total de vértices $|V|$ é no máximo $10^6$ ($1000 \times 1000$) e as arestas $|E|$ são no máximo aproximadamente $2 \times 10^6$.
* **Validação:** A representação foi validada carregando a instância pequena do Marco 1 e realizando testes de impressão no console para confirmar se as posições, limites e caracteres foram processados corretamente em memória.

---

## 🔍 Marco 3 — Aplicação Básica de DFS

* **Execução Manual:** A DFS começa no vértice `A` e explora o labirinto avançando o máximo possível em uma direção (ex: sempre tentando ir primeiro para a direita, depois baixo, etc.) até encontrar uma parede (`#`) ou o limite do grid. Quando não há mais opções válidas, o algoritmo realiza o *backtracking*, retornando à bifurcação anterior para testar novos caminhos não explorados.
* **Estados de Visita:** Foi definida uma matriz booleana auxiliar `visited[][]` para marcar os vértices já descobertos, prevenindo loops infinitos em ciclos dentro do labirinto.
* **Árvore de Busca:** A árvore gerada avança em profundidade máxima, criando ramificações longas e estreitas.
* **Tempos de Descoberta e Término:** O tempo de descoberta marca a primeira vez que a célula é alcançada na recursão/pilha, enquanto o tempo de término é registrado apenas quando todos os vizinhos possíveis daquela célula já foram completamente explorados.
* **Alcançabilidade e Predecessores:** Para verificar a alcançabilidade, basta observar se o vértice `B` foi marcado como visitado. A matriz de predecessores registra a direção de onde o algoritmo veio, permitindo refazer o caminho.
* **Aplicabilidade ao Problema:** A DFS é perfeitamente capaz de descobrir se *existe* um caminho (alcançabilidade). No entanto, sua natureza de ir profundo antes de ir largo faz com que ela **não garanta o menor caminho**. Para o problema do CSES em questão, ela não é a solução ideal.

---

## 🏆 Marco 4 — Aplicação Básica de BFS e Conclusão

* **Execução Manual:** A BFS inicializa uma Fila (Queue) com o vértice `A`. Em seguida, desenfileira a posição atual e enfileira todos os seus vizinhos válidos e não visitados (cima, baixo, esquerda, direita). Esse processo de expansão em "ondas" se repete até o vértice `B` ser enfileirado ou a fila esvaziar.
* **Níveis, Distâncias e Predecessores:**
* A BFS processa o grafo em níveis (camadas). O nível do ponto `A` é 0.
* A distância mínima até qualquer célula alcançada é igual ao seu nível na árvore de busca da BFS.
* Uma matriz extra de caminho (`path[][]`) armazena a instrução exata (L, R, U, D) tomada para chegar em cada célula, permitindo reconstruir o trajeto de forma reversa a partir de `B`.


* **Comparação entre DFS e BFS:** Enquanto a DFS explora caminhos longos de forma errática em busca do destino, a BFS se expande de maneira uniforme. Em grafos não ponderados como este grid, o primeiro caminho encontrado pela BFS para o destino é garantidamente o caminho com a menor distância possível.
* **Escolha Justificada:** Como o problema exige explicitamente encontrar o **menor caminho**, a utilização da **BFS** é obrigatória e justificada, pois atende a esse requisito estrutural fundamental em grafos sem peso nas arestas.
* **Adaptação, Integração e Testes:** A matriz construída no Marco 2 integrou perfeitamente com a lógica da BFS. Foram aplicadas verificações constantes de limites de borda ($0 \le x < N$ e $0 \le y < M$) e de viabilidade da célula (não ser parede nem visitada).
* **Complexidade:** A complexidade de tempo é $O(V + E)$, o que, num grid, se traduz em $O(N \times M)$. A complexidade de espaço também é $O(N \times M)$ para armazenar a matriz do labirinto, a matriz de visitação e a Fila. Esses limites garantem a execução segura dentro do teto de 1.00s estabelecido pela plataforma.
* **Submissão:**
* **Status:** `Accepted` *(Anexar print da plataforma opcionalmente)*.
* **Ensaio Final:** O desenvolvimento desta atividade consolidou o entendimento sobre modelagem de grafos implícitos e a aplicação prática de algoritmos de busca. O desafio realççou a importância de escolher a estrutura correta (BFS) baseada nos requisitos do problema (caminho mais curto) e de manipular eficientemente o rastreamento de predecessores para reconstruir rotas.

