saldo = 500000

while True:
    print('=== ATM SEDERHANA ===')
    print('1. cek saldo')
    print('2. tarik tunai')
    print('3. setor tunai')
    print('4. keluar')

    pilihan = input('pilih menu: ')

    if pilihan == '1':
        print('saldo kamu:', saldo)

    elif pilihan == '2':
        jumlah = int(input('Masukkan jumlah uang: '))

        if jumlah <= saldo:
            saldo = saldo - jumlah
            print('Penarikan berhasil!')
            print('Saldo kamu:', saldo)
        else:
            print('Saldo tidak cukup!')
        print('Saldo tidak cukup!')
    elif pilihan == '3':
        jumlah = int(input('Masukkan jumlah uang yang ingin disetor: '))
        saldo = saldo + jumlah
        print('Setoran berhasil!')
        print('Saldo kamu:', saldo)
    elif pilihan == '4':
        print('terimakasih sudah menggunakan ATM!')
        break