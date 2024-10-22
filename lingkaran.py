# dibuat oleh : kiano devaro ridho
# tanggal pengerjaan : 10 oktober 2024
# program menghitung Rumus lingkaran

print("="*40)
print("LINGKARAN")
print("="*40)

r = float(input("masukan jarijari: "))

l =lambda r : 3.14 * r * r
k = lambda r : 2*3.14 * r

print("luas :",l(r),'cm2')
print("keliling :",round(k(r),2), 'cm2')