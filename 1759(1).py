def combinations(iterable, r):
    # iterable을 리스트로 변환하여 튜플로 반환
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return  # r이 n보다 크면 조합을 생성할 수 없음
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)

# 예제 사용
items = {'a', 'b', 'c', 'd', 'e'}
items_list = list(items)
L = len(items_list)

result = []
for i in range(3, L):
    answers = list(combinations(items_list, i))
    
    for answer in answers:
        if any(char in {'a', 'e', 'i', 'o', 'u'} for char in answer):
            result.append(answer)

for element in result:
    print(''.join(element))