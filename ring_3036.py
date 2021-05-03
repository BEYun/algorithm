import sys
input = sys.stdin.readline
n = int(input())
ring = list(map(int, input().split()))
for i in range(1, n):
    gcd = 0
    a, b = ring[0], ring[i]
    A, B = a, b
    if a > b:
        while b != 0:
            a = a % b
            a, b = b, a
            gcd = a
    else:
        while a != 0:
            b = b % a
            a, b = b, a
            gcd = b
    print('%d/%d'%(A/gcd, B/gcd))