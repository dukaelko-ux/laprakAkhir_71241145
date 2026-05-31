def palindrom(s):
    s = s.lower().replace(' ', '')
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

kalimat = input('Masukkan kalimat: ')
if palindrom(kalimat):
    print('Palindrom')
else:
    print('Bukan palindrom')
# Contoh: 'katak' -> Palindrom
