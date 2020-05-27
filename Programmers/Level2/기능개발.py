# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

# 제한 사항 :
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

# 남은 시간 리스트(time)를 만들어서 해결
import math

def solution(progresses, speeds):
    time = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    answer = []
    cnt = 1
    for i in range(1, len(time)):
        if time[i-1] >= time[i]:
            time[i] = time[i - 1]
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer


print(solution([93,30,55], [1,30,5]))                   #[2,1]
print(solution([40,93,30,55,60,65], [60,1,30,5,10,7]))  #[1,2,3]
print(solution([93,30,55,60,40,65], [1,30,5,10,60,7]))  #[2,4]