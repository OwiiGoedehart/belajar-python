nama=input("nama: ")
umur=int(input("umur: "))
jurusan=input("jurusan: ")

mahasiswa = {
    "nama": nama,
    "umur": umur,
    "jurusan": jurusan
}
for key,value in mahasiswa.items():
    print(key,":",value)