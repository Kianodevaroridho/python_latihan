#Dibuat Oleh : KIANO DEVARO RIDHO
#Tanggal Pengerjaan: 24 Oktober 2024
#Program Menghitung Rumus kerucut

print("="*40)
print("PROGRAM KERUCUT")
print("="*40)

r = int(input("Jari-jari\t: "))
s = int(input("Garis Pelukis\t: "))
t = int(input("Tinggi\t\t: "))

lp = 3.14 * r * (r + 5)
ls = 3.14 * r * s
v = 1/3 * 3.13 * r * r * t

print(f"Luad Permukaan\t: {lp}")
print(f"Luas Selimut\t: {ls}")
print(f"Volume\t\t: {v}")

