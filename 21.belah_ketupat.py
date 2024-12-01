def belahKetupat():
    print('='*40)
    print(' BELAH KETUPAT ')
    print('='*40)

    d1 = float(input('Masukan panjang sisi diagonal pertama : '))
    d2 = float(input('Masukan panjang sisi diagonal kedua : '))

    l = lambda d1,d2 : 1/2 * d1 * d2

    print(f'Luas\t: {l(d1,d2)}')

belahKetupat()