#DIBUAT OLEH:KIANO DEVARO RIDHO
#Tanggal Pengerjaan: 25 Oktober 2024
#Program Menghitung Rumus Tabung



print("="*40)
print("TABUNG")
print("="*40)

R = float(input("Masukan jarijari:"))
T = float(input("Masukan tinggi:"))

PHI = 3.14
V = PHI * R * R * T 
LP = (2 * PHI * R * T) + (2 * (2 * PHI))

print("Volume:",V," cm2")
print("Luas Permukaan:",LP," cm2")