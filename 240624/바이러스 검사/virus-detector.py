def get_input():
    n = int(input().strip())  # 첫 번째 줄 입력
    c = list(map(int, input().strip().split()))  # 두 번째 줄 입력
    LDR, MBR = map(int, input().strip().split())  # 세 번째 줄 입력
    
    return n, c, LDR, MBR

n, c, LDR, MBR = get_input()  # 함수 호출 및 변수 할당

answer = 1 # 팀장은 무조건 1명이기 때문
for cust in c:
    c2 = cust - LDR # 팀원이 검사해야할 고객 수 
    if c2 % MBR == 0:
        M = c2 // MBR  # 필요한 팀원 수 = 몫
        answer += M
    else:
        M = (c2 // MBR) + 1  # 필요한 팀원 수 = 몫 + 1
        answer += M

result = answer

# 결과 출력
print(result)