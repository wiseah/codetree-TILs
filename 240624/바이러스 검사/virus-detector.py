def get_input():
    n = int(input().strip())  # 첫 번째 줄 입력
    c = list(map(int, input().strip().split()))  # 두 번째 줄 입력
    LDR, MBR = map(int, input().strip().split())  # 세 번째 줄 입력
    
    return n, c, LDR, MBR

n, c, LDR, MBR = get_input()  # 함수 호출 및 변수 할당

# c에서 LDR을 뺀 값을 c2에 저장
c2 = [i - LDR for i in c]

# 필요한 팀원 수를 계산하고 결과를 반환
total_team_members = 0
for value in c2:
    if value % MBR == 0:
        M = value // MBR  # 필요한 팀원 수 = 몫
    else:
        M = (value // MBR) + 1  # 필요한 팀원 수 = 몫 + 1
    total_team_members += (1 + M)

result = total_team_members * n

# 결과 출력
print(result)