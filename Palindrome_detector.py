def bul(s):
    if s[::] == s[::-1]:
        print('true')
    else:
        print('false')
s = input()
bul(s)