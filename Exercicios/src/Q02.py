import networkx as nx
from src.Q01 import class_metrics

# Marcos Antônio


def silent_villains(ddc: nx.DiGraph, threshold: int) -> list or None:
    """
    :param ddc: Grafo a ser passado como paramêtro
    :param threshold: Limiar de tolerância de dependências
    :return: tupla contendo as quebráveis globais (g_br), as borboletas globais (g_bu) e a(as) hub(s) (h)
    """

    g_br = []
    g_bu = []
    h = []

    # Verifica os casos nulos e inválidos
    if ddc is None or not nx.is_directed(ddc) or threshold is None or threshold < 0:
        return None

    for node in ddc.nodes:
        fan_out, fan_in = class_metrics(ddc, node)

        # Se o número de classes que o nó node depende (fan_out) e se o número de classes que dependem
        # do nó node (fan_in) forem maior que o limiar de tolerância, temos um Hub.
        if fan_out > threshold and fan_in > threshold:
            h.append(node)

        # Se o número de classes que o nó depende for maior que o threshold, temos uma quebrável global
        if fan_out > threshold:
            g_br.append(node)

        # Se o número de classes que dependem do nó forem maiores que threshold, temos uma borboleta global.
        if fan_in > threshold:
            g_bu.append(node)

    return g_br, g_bu, h
