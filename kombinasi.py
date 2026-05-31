def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

def kombinasi(n, r):
    if r == 0 or r == n:
        return 1
    return kombinasi(n-1, r-1) + kombinasi(n-1, r)

n = int(input('n: '))
r = int(input('r: '))
print('C(%d,%d) = %d' % (n, r, kombinasi(n, r)))
