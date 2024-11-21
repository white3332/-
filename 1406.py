import sys
def input(): return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None


STRING = str(input())

# 연결 리스트의 첫 번째 노드를 생성합니다.
head = Node('dummy')
current = head

for i in range(0, len(STRING)):
    new_node = Node(STRING[i])
    current.next = new_node
    new_node.pre = current
    current = new_node

tail = current
node = tail
N = int(input())

for _ in range(N):
    cmd = str(input().strip())
    if cmd[0] == 'P': # 노드 추가
        new_node = Node(cmd[2])
        # 새로운 노드의 업데이트
        new_node.next = node.next
        new_node.pre = node
        # 다음 노드의 업데이트
        if node.next is not None:
            node.next.pre = new_node
        # 현재 노드의 업데이트
        node.next = new_node
        # 현재 노드를 새로운 노드로 업데이트
        node = new_node
        
    elif cmd[0] == 'L': # 노드 이동
        if node.data != 'dummy':
            node = node.pre
        
    elif cmd[0] == 'D': # 노드 이동
        if node.next is not None:
            node = node.next
        
    else: # 노드 삭제
        if node.data != 'dummy':
            if node.next is not None: # 앞 뒤 모두 노드가 존재함
                node.pre.next = node.next
                node.next.pre = node.pre
            else: # 이전 노드만 있음
                node.pre.next = None
            node = node.pre


# 노드를 가장 앞으로 이동
while node is not None:
    head = node
    node = node.pre
    
node = head
while node is not None:
    if node.data != 'dummy':
        print(node.data, end='')
    node = node.next

# while node is not None:
#     pre_data = node.pre.data if node.pre else None
#     next_data = node.next.data if node.next else None
#     print(f"Node data: {node.data}, Pre: {pre_data}, Next: {next_data}")
#     node = node.next
