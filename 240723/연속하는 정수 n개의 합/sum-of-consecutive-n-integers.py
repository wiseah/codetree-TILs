n, m = map(int, input().split())
L = list(map(int, input().split()))


def solution(n, m, L):
    count = 0
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += L[end]

        while current_sum > m and start <= end:
            current_sum -= L[start]
            start += 1

        if current_sum == m:
            count += 1

    return count

print(solution(n, m, L))