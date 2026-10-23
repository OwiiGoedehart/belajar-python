password = ""
percobaan= 0

while password != 'jungenstrasse' and percobaan <3:
    password = input("Masukkan password: ")

    if password != 'jungenstrasse':
        print("Password salah!")
        percobaan += 1

if password == 'jungenstrasse':
    print("selamat datang!")
else :
    print("kesempatan habis!")

