def can_pass_in_time(n, m, times, mid):
    count = 0
    for time in times:
        count += mid // time
        if count >= n:
            return True
    return count >= n

def find_min_time(n, m, times):
    left, right = 1, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_pass_in_time(n, m, times, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer

# 입력 받기
n, m = map(int, input().split())
times = [int(input()) for _ in range(m)]

# 최소 시간 계산
result = find_min_time(n, m, times)
print(result)