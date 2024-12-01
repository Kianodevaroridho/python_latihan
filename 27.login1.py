pin = "nimda123"

print ("="*40)
print ("Verifikasi Login Anda")
print ("="*40)

username = input ("Masukkan Username Anda: ")
password = input("Masukkan Password Anda: ")

if password == pin:
    print (f'''-------------------------
Login berhasil
-------------------------''')
else:
    print (f'''-------------------------
Maaf, Password Salah
-------------------------''')