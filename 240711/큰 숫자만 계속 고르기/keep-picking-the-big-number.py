import heapq

def find_max_after_operations(numbers, m):
    # Python의 heapq는 최소 힙만을 제공하므로, 음수로 변환하여 최대 힙을 만듭니다.
    max_heap = [-num for num in numbers]
    heapq.heapify(max_heap)
    
    # m번 가장 큰 수에서 1씩 빼는 작업을 합니다.
    for _ in range(m):
        largest = -heapq.heappop(max_heap)  # 가장 큰 수를 꺼내고
        largest -= 1  # 그 수에서 1을 빼고
        heapq.heappush(max_heap, -largest)  # 다시 힙에 넣습니다.
    
    # 최종적으로 남아있는 숫자들 중 가장 큰 수를 반환합니다.
    return -max_heap[0]

# 입력 받기
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 함수 실행
result = find_max_after_operations(numbers, m)
print(result)  # 결과 출력