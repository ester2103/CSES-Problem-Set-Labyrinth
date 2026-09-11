from collections import deque


class BreadthFirstPaths:

    def __init__(self, labirinto, s):
        self.labirinto = labirinto
        self.n = len(labirinto)
        self.m = len(labirinto[0])

        self._marked = [
            [False for _ in range(self.m)]
            for _ in range(self.n)
        ]

        self.edge_to = [
            [None for _ in range(self.m)]
            for _ in range(self.n)
        ]

        self.s = s

        self.bfs(s)

    def bfs(self, s):
        x, y = s

        self._marked[x][y] = True
        queue = deque([s])

        while queue:
            v = queue.popleft()

            for w in self.adj(v):
                x, y = w

                if not self._marked[x][y]:
                    self.edge_to[x][y] = v
                    self._marked[x][y] = True
                    queue.append(w)

    def adj(self, v):
        x, y = v

        # baixo, direita, cima, esquerda
        direcoes = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        vizinhos = []

        for dx, dy in direcoes:
            nx = x + dx
            ny = y + dy

            # verifica se está dentro da matriz
            if 0 <= nx < self.n and 0 <= ny < self.m:

                # verifica se não é parede
                if self.labirinto[nx][ny] != '#':
                    vizinhos.append((nx, ny))

        return vizinhos

    def has_path_to(self, v):
        x, y = v
        return self._marked[x][y]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        path = []
        x = v

        while x != self.s:
            path.append(x)

            linha, coluna = x
            x = self.edge_to[linha][coluna]

        path.append(self.s)

        return reversed(path)


if __name__ == '__main__':

    n, m = map(int, input().split())

    labirinto = []

    inicio = None
    fim = None

    for i in range(n):
        linha = input()
        labirinto.append(linha)

        for j in range(m):

            if linha[j] == 'A':
                inicio = (i, j)

            elif linha[j] == 'B':
                fim = (i, j)

    bfs = BreadthFirstPaths(labirinto, inicio)

    if bfs.has_path_to(fim):

        caminho = list(bfs.path_to(fim))

        movimentos = ""

        for i in range(1, len(caminho)):

            x1, y1 = caminho[i - 1]
            x2, y2 = caminho[i]

            if x2 == x1 + 1:
                movimentos += 'D'

            elif x2 == x1 - 1:
                movimentos += 'U'

            elif y2 == y1 + 1:
                movimentos += 'R'

            elif y2 == y1 - 1:
                movimentos += 'L'

        print("YES")
        print(len(movimentos))
        print(movimentos)

    else:
        print("NO")
