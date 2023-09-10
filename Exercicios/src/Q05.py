import networkx as nx

# Samuel Cabral de Luna


def change_costs_factor(ddc: nx.DiGraph, c: str or int) -> int or None:

    """
    Calcula um fator que representa o custo estimado de modificação de uma determinada classe em um programa.
    :param ddc: Digrafo que representa as classes de um programa e a relação de dependência entre elas.
    :param c: a classe de comparação.
    :return: valor de custo estimado para modificar a classe c.
    """

    # Trata entradas inválidas.
    if ddc is None or len(ddc.nodes) == 0 or c is None or (c not in ddc.nodes) or not ddc.is_directed():
        return None

    custo = 1  # Custo padrão.
    dependentes = len(nx.ancestors(ddc, c))  # Número de dependentes de c.
    cycles = nx.simple_cycles(ddc)
    tangled = False
    tangles = nx.strongly_connected_components(ddc)
    cycles_containing_c = 0
    
    for tangle in tangles:  # True se c pertence à algum tangle.
        if len(tangle) > 3:
            if c in tangle:
                tangled = True

    for cycle in cycles:  # Calcula o número de ciclos que c pertence.
        if c in cycle:
            cycles_containing_c += 1
            
    return custo + (dependentes * 1) + (tangled * 50) + (cycles_containing_c * 10)
