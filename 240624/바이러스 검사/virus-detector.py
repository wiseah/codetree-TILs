def get_input():
    n = int(input().strip())  # 첫 번째 줄 입력
    c = list(map(int, input().strip().split()))  # 두 번째 줄 입력
    LDR, MBR = map(int, input().strip().split())  # 세 번째 줄 입력
    
    return n, c, LDR, MBR

n, c, LDR, MBR = get_input()  # 함수 호출 및 변수 할당

answer = 0 # 여기서 1이 아닌 이유는 각 팀마다 팀장이 1명씩이기 때문.(1로 정해버리면 팀 수에 상관없이 팀장이 총 1명이 되버림)
for cust in c:
    c2 = cust - LDR  # 팀장이 처리한 후 남은 고객 수
    answer += 1  # 팀장은 무조건 한 명 필요
    if c2 % MBR == 0:
        M = c2 // MBR  # 필요한 팀원 수 = 몫
        answer += M
    else:
        M = (c2 // MBR) + 1  # 필요한 팀원 수 = 몫 + 1
        answer += M

result = answer

# 결과 출력
print(result)