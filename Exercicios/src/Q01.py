import networkx as nx

# Paola Kathrein Moura Marques


def class_metrics(ddc: nx.DiGraph, c: str or int) -> tuple[int, int] or None:

    """
    Calcula métricas de classe em um grafo direcionado.
    :param ddc: grafo direcionado sobre o qual as métricas de classe serão calculadas.
    :param c: nó específico do grafo ddc para o qual as métricas de classe serão calculadas.
    :return: retorna as métricas fan-out e fan-in do nó c no grafo ddc.
    """

    if ddc is None or c is None:  # Verifica se o grafo ou a classe são None.
        return None

    if not isinstance(ddc, nx.DiGraph):  # Verifica se o grafo é direcionado.
        return None

    if not ddc.has_node(c):  # Verifica se o grafo possui o nó (classe) especificado.
        return None

    fan_out = ddc.out_degree(c)  # Calcula o fan_out (grau de saída) da classe c usando out_degree.

    fan_in = ddc.in_degree(c)  # Calcula o fan_in (grau de entrada) da classe c usando in_degree.

    return fan_out, fan_in
