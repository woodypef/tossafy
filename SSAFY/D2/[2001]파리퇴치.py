T = int(input())
data = []
max = 0
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1) :
    N,M = map(int,input().split())
    for i in range(N) :
        data.append(list(map(int,input().split())))
    for i in range(N-M+1) :
        for j in range(N-M+1) :
            result = 0
            result = data[i:i+M][j:j+M]
            if(result>max) :
                max = result




    print("#%d %d" %(test_case,max))