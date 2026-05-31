def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

def deret_ganjil(n):
    if n == 1:
        return faktorial(1)
    return faktorial(2*n - 1) + deret_ganjil(n - 1)

n = int(input('Jumlah suku: '))
print('Hasil:', deret_ganjil(n))
