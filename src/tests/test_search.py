from src.search_solver import a_star_search, graph, heuristic

def test_a_star_path_found():
    path, cost = a_star_search(graph, 'Keluhan_Masuk', 'Selesai_Refund', heuristic)
    assert path is not None
    assert path[-1] == 'Selesai_Refund'
    assert cost == 9
