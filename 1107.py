data = """10 
9 
1 2 3 4 5 6 7 8 9
11

101
0
1

99
10
0 1 2 3 4 5 6 7 8 9
1

0
0
1

500000
6
0 1 2 3 4 5
166672

0
2
0 1
3

1555
8
0 1 3 4 5 6 7 9
670

944 
7
2 3 4 5 6 7 9
59

6 
9
0 2 3 4 5 6 7 8 9
6

500000
10
0 1 2 3 4 5 6 7 8 9
499900



101 
10
0 1 2 3 4 5 6 7 8 9
1

1
9
1 2 3 4 5 6 7 8 9
2

99999
1
9
7

10
1
0
2

0
3
0 1 2
4

0
9
0 1 2 3 4 5 6 7 8
10

0
10
0 1 2 3 4 5 6 7 8 9
100

1
9
1 2 3 4 5 6 7 8 9
2

1020
0
4

10 
2
0 1
2

999
1
9
5

9990
8
1 2 3 4 5 6 7 8
4

123
2
2 3
7

199
1 
9
4

9
5
9 8 7 6 5
3

19
1
1
3

5959
4
1 2 3 4 
4

56666
0
5

9999
8
0 1 2 3 4 5 6 7 
4

10
1
1 
2

190000
3
1 2 9 
101117

123
3
1 2 5 
23

1
9
0 1 2 3 4 5 6 7 8 
9

100
10
0 1 2 3 4 5 6 7 8 9 
0

99933
2
3 9 
73

1023
5
1 2 3 4 0 
27

91010
2
1 0 
1016

383399
6
1 2 3 4 5 7 
216607

6711
2
1 2 
6

330
4
0 1 2 3 
117

71923
5
4 5 6 7 9 
8082

123123
3
1 2 3 
23129

499999
2
4 8 
7

1111
9
1 2 3 4 5 6 7 8 9 
1011

1111
9
0 1 2 3 4 5 6 7 8 
115

34311
8
0 1 2 3 4 5 6 7 
24316


49445
7
1 2 3 4 5 6 7 
30560

933
2
1 2 
3

1617
3
1 2 3 
621

856
2
5 6 
10

1023
8
1 2 3 4 5 6 7 8 
27

10900
2
1 0 
905

394344
3
1 2 3 
5662

99
1
8 
1

101
9
0 1 2 3 4 5 6 7 8 
1

2420
6
1 2 3 4 5 6 
1424

991
1
1 
4

30002
3
1 3 4 
8

1698
2
6 9 
6

499998
3
4 8 9 
8

1022
5
1 2 3 4 5 
26
""".split('\n')

import sys
input = sys.stdin.readline

def find_char(char, useable_keys):
    char = int(char)
    nums = set()
    if char in useable_keys:
        nums.add(char)
    if 0 in useable_keys:
        nums.add(0)
    if 9 in useable_keys:
        nums.add(9)
    a11, b11 = char, char
    a22, b22 = True, True
    for _ in range(1, 10):
        a11 = a11 + 1
        b11 = b11 - 1
        if a11 >= 10:
            a11 = 0
        if b11 <= -1:
            b11 = 9
        if a11 in useable_keys and a22:
            nums.add(a11)
            a22 = False
        if b11 in useable_keys and b22:
            nums.add(b11)
            b22 = False
    return list(nums)
    

def sol(N, M, wrong_btn):
    channel = ['0']+list(str(N))
    broken_keys = list(wrong_btn)
    keypad = [None if str(i) in broken_keys else i for i in range(10)]
    useable_keys = sorted([i for i in keypad if i is not None])
    
    from itertools import product

    a0 = abs(int(''.join(channel))-100)
    a2 = []
    if len(useable_keys) == 0:
        answer = a0
    else:
        for cnt in range(3):
            answer = []
            for char in channel[cnt:]:
                answer.append(useable_keys)
            if len(answer) == 7:
                answer[6] = [0]
            if len(answer) == 6:
                n_answer=[]
                for i in answer[0]:
                    if i <= 6:
                        n_answer.append(i)
                answer[0] = n_answer
            for ans in product(*answer):
                if not ans:
                    pass
                else:
                    a1 = int(''.join(map(str, ans)))
                    a2.append(abs(int(''.join(channel)) - int(a1)) + len(str(a1)))
        answer = min(a0, *a2)
        return answer

i = 0
N, M, wrong_btn = None, None, set()
while i != len(data):
    if data[i] == '':
        N, M, wrong_btn = None, None, set()
        i += 1
        continue
    if N is None:
        N = int(data[i])
        i += 1
        M = int(data[i])
        i += 1
        if M != 0:
            wrong_btn = set(data[i].split())
            i += 1
        ans = int(data[i])
        i += 1
        answer = sol(N, M, wrong_btn)
        if answer != ans:
            print()
            print(N, M, wrong_btn)
            print(answer, ans)
            print()
        N, M, wrong_btn = None, None, set()
