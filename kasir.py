def tampilkan_menu(daftar_barang):
    print("\n=== DAFTAR BARANG ===")
    for kode, data in daftar_barang.items():
        print(f"{kode}. {data['nama']} - Rp{data['harga']:,}")
    print("======================")


def proses_transaksi(daftar_barang):
    keranjang = {}
    total_belanja = 0

    while True:
        tampilkan_menu(daftar_barang)
        kode = input("\nMasukkan kode barang (atau ketik 'selesai' untuk bayar): ").strip()

        if kode.lower() == "selesai":
            break

        if kode not in daftar_barang:
            print("Kode barang tidak ditemukan. Coba lagi.")
            continue

        try:
            jumlah = int(input(f"Jumlah {daftar_barang[kode]['nama']} yang dibeli: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")
            continue

        subtotal = daftar_barang[kode]['harga'] * jumlah

        if kode in keranjang:
            keranjang[kode]['jumlah'] += jumlah
            keranjang[kode]['subtotal'] += subtotal
        else:
            keranjang[kode] = {
                'nama': daftar_barang[kode]['nama'],
                'harga': daftar_barang[kode]['harga'],
                'jumlah': jumlah,
                'subtotal': subtotal
            }

        total_belanja += subtotal
        print(f"-> {jumlah} {daftar_barang[kode]['nama']} ditambahkan ke keranjang.")

    return keranjang, total_belanja


def cetak_struk(keranjang, total_belanja):
    if not keranjang:
        print("\nTidak ada barang yang dibeli. Transaksi dibatalkan.")
        return

    print("\n========== STRUK BELANJA ==========")
    for data in keranjang.values():
        print(f"{data['nama']:<15} {data['jumlah']} x Rp{data['harga']:,} = Rp{data['subtotal']:,}")
    print("------------------------------------")
    print(f"TOTAL: Rp{total_belanja:,}")
    print("====================================")

    while True:
        try:
            uang_bayar = int(input("Masukkan jumlah uang pembayaran: Rp"))
            if uang_bayar < total_belanja:
                print("Uang tidak cukup! Masukkan jumlah yang sesuai atau lebih.")
                continue
            break
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")

    kembalian = uang_bayar - total_belanja
    print(f"Kembalian: Rp{kembalian:,}")
    print("\nTerima kasih telah berbelanja!")


def main():
    daftar_barang = {
        "1": {"nama": "Roti", "harga": 8000},
        "2": {"nama": "Susu", "harga": 12000},
        "3": {"nama": "Kopi", "harga": 15000},
        "4": {"nama": "Mie Instan", "harga": 3500},
        "5": {"nama": "Air Mineral", "harga": 4000},
    }

    print("SELAMAT DATANG DI KASIR SEDERHANA")
    keranjang, total_belanja = proses_transaksi(daftar_barang)
    cetak_struk(keranjang, total_belanja)


if __name__ == "__main__":
    main()