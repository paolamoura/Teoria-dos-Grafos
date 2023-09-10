import networkx as nx

# Paola Kathrein Moura Marques


def dependencies(ddc: nx.DiGraph, c: str or int) -> list or None:
    """
    Retorna as dependências diretas e indiretas de um nó em um grafo direcionado.
        :param: ddc (nx.DiGraph): Grafo direcionado representado como um objeto nx.DiGraph.
        :param: c: Nó do qual se deseja obter as dependências.
        :return: Tuple: Uma tupla contendo duas listas ordenadas. A primeira lista contém as
        dependências diretas do nó 'c' e a segunda lista contém as dependências indiretas,
        ou seja, os nós que são alcançáveis a partir de 'c' através de caminhos não diretos.
        Caso 'ddc' seja None, 'c' seja None, 'ddc' não seja um objeto do tipo nx.DiGraph
        ou 'c' não seja um nó válido em 'ddc', retorna None.
    """
    if ddc is None or c is None:  # Verifica se os argumentos ddc e c são None
        return None

    if not isinstance(ddc, nx.DiGraph):  # Verifica se ddc é um objeto do tipo nx.DiGraph
        return None

    if not ddc.has_node(c):  # Verifica se o nó c existe no grafo ddc
        return None

    direct_deps = list(ddc.successors(c))  # Obtém os nós diretamente dependentes do nó c
    indirect_deps = set()  # Conjunto para armazenar as dependências indiretas
    visited = set()  # Conjunto para armazenar os nós visitados durante a busca DFS

    def dfs(current):
        visited.add(current)  # Adiciona o nó atual aos nós visitados
        for neighbor in ddc.successors(current):  # Percorre os vizinhos do nó atual
            if neighbor not in visited:  # Verifica se o vizinho não foi visitado
                indirect_deps.add(neighbor)  # Adiciona o vizinho às dependências indiretas
                dfs(neighbor)  # Chama recursivamente a busca DFS para o vizinho

    dfs(c)  # Inicia a busca DFS a partir do nó c

    indirect_deps.difference_update(direct_deps)  # Remove os nós diretamente dependentes das dependências indiretas

    return sorted(direct_deps), sorted(list(indirect_deps))  # Retorna as dependências diretas e indiretas ordenadas
