print("="*30)
print("MENENTUKAN SUATU ZAT")
print("="*30)

inputan_suhu = int(input("masukan suhu = "))
if inputan_suhu <= 0:
    print("ini adalah zat padat")
elif 0 <= inputan_suhu < 100:
    print("ini adalah zat cair")
elif inputan_suhu > 100:
    print("ini adalah zat uap")