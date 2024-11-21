import sys
input = sys.stdin.readline

channel = ['0']+list(input().strip())
_ = int(input())
broken_keys = list(map(int, input().split()))

keypad = [None if i in broken_keys else i for i in range(10)]
useable_keys = sorted([i for i in keypad if i is not None])

del _
del broken_keys
del keypad

from itertools import product

a2 = []
if len(useable_keys) == 0:
    a0 = abs(int(''.join(channel))-100)
    print(a0)
else:
    a0 = abs(int(''.join(channel))-100)
    for cnt in range(3):
        answer = []
        for char in channel[cnt:]:
            answer.append(useable_keys)
        for ans in product(*answer):
            if not ans:
                pass
            else:
                a1 = int(''.join(map(str, ans)))
                a2.append(abs(int(''.join(channel)) - int(a1)) + len(str(a1)))
    print(min(a0, *a2))