import heapq

# Representasi Graf Masalah Bisnis CS E-Commerce
graph = {
    'Keluhan_Masuk': [('Cek_Status_Resi', 1), ('Tanya_Detail_Barang', 2)],
    'Cek_Status_Resi': [('Terlacak_Sesuai', 1), ('Kendala_Pengiriman', 3)],
    'Tanya_Detail_Barang': [('Klaim_Kerusakan', 4), ('Tukar_Barang', 5)],
    'Terlacak_Sesuai': [('Solusi_Informasi_Pelanggan', 1)],
    'Kendala_Pengiriman': [('Eskalasi_Kurir', 2), ('Ajukan_Pengembalian_Dana', 4)],
    'Klaim_Kerusakan': [('Ajukan_Pengembalian_Dana', 2)],
    'Tukar_Barang': [('Proses_Retur_Stok', 3)],
    'Solusi_Informasi_Pelanggan': [],
    'Eskalasi_Kurir': [('Solusi_Informasi_Pelanggan', 2)],
    'Ajukan_Pengembalian_Dana': [('Selesai_Refund', 1)],
    'Proses_Retur_Stok': [('Selesai_Retur', 1)],
    'Selesai_Refund': [],
    'Selesai_Retur': []
}

# Tabel Heuristik Admissible h(n)
heuristic = {
    'Keluhan_Masuk': 3,
    'Cek_Status_Resi': 3,
    'Tanya_Detail_Barang': 3,
    'Terlacak_Sesuai': 5,
    'Kendala_Pengiriman': 2,
    'Klaim_Kerusakan': 2,
    'Tukar_Barang': 4,
    'Solusi_Informasi_Pelanggan': 5,
    'Eskalasi_Kurir': 3,
    'Ajukan_Pengembalian_Dana': 1,
    'Proses_Retur_Stok': 4,
    'Selesai_Refund': 0,
    'Selesai_Retur': 5
}

def a_star_search(graph, start, goal, h):
    priority_queue = [(h[start], 0, start, [start])]
    visited = {}

    while priority_queue:
        f_score, g_score, current, path = heapq.heappop(priority_queue)

        if current in visited and visited[current] <= g_score:
            continue
        visited[current] = g_score

        if current == goal:
            return path, g_score

        for neighbor, cost in graph.get(current, []):
            new_g = g_score + cost
            new_f = new_g + h.get(neighbor, 0)
            heapq.heappush(priority_queue, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

if __name__ == "__main__":
    path, cost = a_star_search(graph, 'Keluhan_Masuk', 'Selesai_Refund', heuristic)
    print(f"Jalur A* Optimasi: {' -> '.join(path)} | Biaya Riil (g): {cost} Menit")
