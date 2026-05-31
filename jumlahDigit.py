def jumlah_digit(n):
    if n < 10:
        return n
    return (n % 10) + jumlah_digit(n // 10)

angka = int(input('Masukkan bilangan: '))
print('Jumlah digit:', jumlah_digit(angka))
