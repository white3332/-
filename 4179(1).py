import sys
from collections import deque

input = sys.stdin.readline



def find_item(graph):
    ret_node = []
    fire_dir = []
    for i, row in enumerate(graph):
        for j, value in enumerate(row):
            if value == 'J':
                ret_node.append((i, j))  # 사람 위치를 리스트에 추가
            elif value == 'F':
                fire_dir.append((i, j))  # 불 위치를 리스트에 추가
    ret_node.extend(fire_dir)  # 사람 위치를 포함한 리스트 반환
    return ret_node

def spread_fire(graph, fire_dir):
    new_fire_dir = []
    
    for i, j in fire_dir:
        # 4방향으로 불 확산
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni <= max_row and 0 <= nj <= max_col and graph[ni][nj] == '.':
                graph[ni][nj] = 'F'  # 불 확산
                new_fire_dir.append((ni, nj))  # 새로운 불 위치 추가
    
    return new_fire_dir  # 새로운 불 위치 반환


def bfs(graph):
    node = find_item(graph)
    person_queue = deque([node[0]])  # 사람의 초기 위치
    visited = set(person_queue)  # 방문한 위치 저장
    fire_dir = node[1:]  # 초기 불 위치
    step = 1
    
    while person_queue:
        # 불 확산
        fire_dir = spread_fire(graph, fire_dir)
        
        # 사람 이동
        for _ in range(len(person_queue)):
            i, j = person_queue.popleft()
            
            # 탈출 조건 확인
            if i == 0 or i == max_row or j == 0 or j == max_col:
                return step
            
            # 4방향으로 이동
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni <= max_row and 0 <= nj <= max_col and graph[ni][nj] == '.' and (ni, nj) not in visited:
                    visited.add((ni, nj))  # 방문 처리
                    person_queue.append((ni, nj))  # 이동할 위치 큐에 추가
        
        step += 1
    
    return 'IMPOSSIBLE'


# 입력 처리
max_row, max_col = map(int, input().split())
max_row -= 1  # 인덱스 조정
max_col -= 1  # 인덱스 조정
graph = [list(input().strip()) for _ in range(max_row + 1)]

# BFS 실행 및 결과 출력
print(bfs(graph))