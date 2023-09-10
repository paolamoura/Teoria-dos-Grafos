import networkx as nx
from src.Q01 import class_metrics

# Marcos Antônio


def mfs_greedy(ddc: nx.DiGraph) -> list[tuple[str or int, str or int]] or None:
    """
    Retorna o conjunto de arcos que ao serem removidos, tornam o grafo acíclico.
    :param ddc: grafo
    :return: lista de arcos
    """
    if isinstance(ddc, nx.DiGraph) and ddc.number_of_nodes() <= 1:
        return []

    if not ddc or not nx.is_directed(ddc):
        return None

    mfs = []
    md_cycles = get_cycles(ddc)
    while md_cycles:
        arc = get_arc(md_cycles, ddc)  # pega o arco que participa de mais ciclos
        if not arc:
            break
        mfs.append(arc)
        md_cycles = [cycle for cycle in md_cycles if arc not in cycle]
    return mfs


def get_cycles(g: nx.DiGraph) -> list[list]:
    """
    Retorna os ciclos como lista de arcos.
    :param g: grafo
    :return: lista de ciclos
    """

    cycles = nx.simple_cycles(g)
    cycles = [cycle for cycle in cycles]
    for cycle in cycles:
        arcos = []
        for i in range(len(cycle) - 1):
            arcos.append((cycle[i], cycle[i + 1]))
        arcos.append((cycle[-1], cycle[0]))
        cycle.clear()
        cycle.extend(arcos)
    return cycles


def get_arc(cycles: list[list], ddc: nx.DiGraph) -> tuple[str or int, str or int] or None:
    """
    Retorna o arco que participa de mais ciclos, caso haja empate, retorna o arco com maior fan_out, caso haja empate,
    retorna o arco com maior fan_in, caso haja empate, retorna o arco em ordem lexicográfica.
    :param cycles: lista de ciclos
    :param ddc: grafo
    :return: arco
    """
    arc_counts = {}
    fan_out = {}
    fan_in = {}

    for cycle in cycles:
        for arc in cycle:
            if arc not in arc_counts:
                arc_counts[arc] = 0
            arc_counts[arc] += 1

            source, target = arc
            if source not in fan_out:
                fan_out[source], _ = class_metrics(ddc, source)
            if target not in fan_in:
                _, fan_in[target] = class_metrics(ddc, target)

    return filter_arcs(arc_counts, fan_out, fan_in)


def filter_arcs(arcs: dict[tuple:int], fan_out: dict, fan_in: dict) -> tuple[str or int, str or int] or None:
    """
    Filtra os arcos que mais participam de ciclos, caso haja empate, filtra os arcos com maior fan_out, caso haja
    empate, filtra os arcos com maior fan_in, caso haja empate, filtra os arcos em ordem lexicográfica.
    :param arcs: dicionário de arcos
    :param fan_out: dicionário de fan_outs
    :param fan_in: dicionário de fan_in
    :return: lista de arcos
    """
    max_count = max(arcs.values())
    arcs = [arc for arc in arcs if arcs[arc] == max_count]
    fan_out = {arc[0]: fan_out[arc[0]] for arc in arcs}
    fan_in = {arc[1]: fan_in[arc[1]] for arc in arcs}
    if len(arcs) == 1:
        return arcs[0]

    max_fan_out = max(fan_out.values())
    arcs = [arc for arc in arcs if fan_out[arc[0]] == max_fan_out]
    fan_in = {arc[1]: fan_in[arc[1]] for arc in arcs}
    if len(arcs) == 1:
        return arcs[0]

    max_fan_in = max(fan_in.values())
    arcs = [arc for arc in arcs if fan_in[arc[1]] == max_fan_in]
    if len(arcs) == 1:
        return arcs[0]

    return sorted(arcs)[-1]
