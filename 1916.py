import heapq
import sys
input = sys.stdin.readline
INF = float('INF')


city = int(input())
bus = int(input())

graph = [[] for _ in range(city+1)]
distance = [INF] * (city+1)

for _ in range(bus):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (start, 0))
    distance[start] = 0
    while heap:
        cur_pos, cur_cost = heapq.heappop(heap)
        if distance[cur_pos] < cur_cost:
            continue
        for tar_pos, tar_cost in graph[cur_pos]:
            cost = cur_cost + tar_cost
            if cost < distance[tar_pos]:
                distance[tar_pos] = cost
                heapq.heappush(heap, (tar_pos, distance[tar_pos]))

start, end = map(int, input().split())

dijkstra(start)
print(distance[end])