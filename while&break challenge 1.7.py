while True:
    username = input('masukan username : ')
    password = input('masukan password : ')

    if username == 'admin' and password == 'python':
        break
    else:
        print('username atau password salah!')

print("login berhasil!")
