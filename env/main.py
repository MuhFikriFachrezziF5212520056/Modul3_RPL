belanja = []
print("Program Pengelola Daftar Belanja")
print("Muh. Fikri Fachrezzi (F5212520056)")
while True:
    print()
    print("=========================================")
    print("1. Tampilkan Belanjaan Dan Total Harganya")
    print("2. Tambah Barang")
    print("3. Hapus Barang")
    print("4. Keluar")
    print("=========================================")
    pilihan = input("Pilih menu: ")
    # 1. Tampilkan
    if pilihan == "1":
        print("\nDaftar Belanja:")
        total_semua = 0
        for i in range(len(belanja)):
            nama = belanja[i][0]
            harga = belanja[i][1]
            jumlah = belanja[i][2]
            print(nama, "| Harga:", harga, "| Jumlah:", jumlah)
        total = 0
        for i in range(len(belanja)):
            total += belanja[i][1] * belanja[i][2]
        print("Total belanja:", total)
    # 2. Tambah
    elif pilihan == "2":
        nama = input("Nama barang: ")
        harga = int(input("Harga: "))
        jumlah = int(input("Jumlah: "))
        belanja.append([nama, harga, jumlah])
        print("Barang ditambahkan!")
    # 3. Hapus
    elif pilihan == "3":
        nama = input("Nama barang yang dihapus: ")
        ditemukan = False
        for i in range(len(belanja)):
            if belanja[i][0] == nama:
                belanja.pop(i)
                ditemukan = True
                print("Barang dihapus!")
                break
        if not ditemukan:
            print("Barang tidak ditemukan!")
    # 4. Keluar
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")