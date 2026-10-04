from models.buku_model import BukuModel

model = BukuModel()

print("==========================================")
print("     UJI BUKU MODEL - F5212520056        ")
print("==========================================")

# 1. Menjalankan Update Data
print("\n[>] Memperbarui data buku ID 1...")
model.update_buku(1, "Tugas Modul 4 F5212520056", "Muh. Fikri Fachrezzi", 2026)
print("[+] Status: Data buku ID 1 sukses diubah!")

# 2. Menampilkan Data Setelah Update
print("\n--- Daftar Buku Pasca Update ---")
daftar = model.get_all_buku()
for b in daftar:
    print(f"ID: {b['id_buku']} | Judul: {b['judul']} | Penulis: {b['penulis']} ({b['tahun_terbit']})")

# 3. Menjalankan Delete Data (Menghapus baris terakhir)
if daftar:
    target_id = daftar[-1]['id_buku']
    print(f"\n[>] Menghapus data buku ID {target_id}...")
    model.delete_buku(target_id)
    print(f"[+] Status: Data buku ID {target_id} berhasil dihapus!")

# 4. Tampilan Akhir
print("\n--- Daftar Buku Akhir di Database ---")
for b in model.get_all_buku():
    print(f"ID: {b['id_buku']} | Judul: {b['judul']} | Penulis: {b['penulis']} ({b['tahun_terbit']})")