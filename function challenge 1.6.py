def cek_genap(angka):
    if angka %2 == 0:
        return "genap"
    else:
        return "ganjil"

print(cek_genap(8))