def hanoi(n, frm, to, other):
    if n < 2:
        print(frm, to)
        return
    hanoi(n-1, frm, other, to)
    print(frm, to)
    hanoi(n-1, other, to, frm)

n = int(input())
print((2**n)-1)
hanoi(n, 1, 3, 2)