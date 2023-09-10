import networkx as nx
from src.Q04 import mfs_greedy

# Samuel Cabral de Luna


def class_order(ddc: nx.DiGraph) -> list[list] or None:

    """
    Agrupamento ordenado de classes indicando uma possível ordem de integração entre elas.
    :param ddc: grafo direcionado.
    :return: lista de listas, cada lista interna representa um grupo de classes que podem ser integradas ao mesmo tempo.
    """

    # Trata entradas inválidas.
    if ddc is None or not ddc.is_directed():
        return None

    # Calcula o conjunto MFS.
    mfs = mfs_greedy(ddc)

    # Seleciona os arcos que não estão em MFS.
    edges = [x for x in ddc.edges if x not in mfs]

    if edges:
        # Cria um grafo auxiliar acíclico a partir do DDC.
        aux = nx.DiGraph(edges)
        # Calcula a ordem topológica inversa no novo grafo.
        result = [generation for generation in nx.topological_generations(aux)]
        result.reverse()
    else:
        # Calcula a ordem topológica no DDC original caso seja um grafo vazio.
        result = [generation for generation in nx.topological_generations(ddc)]

    return result
