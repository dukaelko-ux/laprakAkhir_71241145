def cek_prima(n, i=2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return cek_prima(n, i + 1)

angka = int(input('Masukkan bilangan: '))
if cek_prima(angka):
    print(angka, 'adalah bilangan prima')
else:
    print(angka, 'bukan bilangan prima')
