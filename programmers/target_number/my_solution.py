def solution(numbers, target):
    p = []
    answer = []
    def dfs(numbers, target):
        if len(numbers) == 0:
            if sum(p) == target:
                answer.append(p)
                
        else:
            for i in [1,-1]:
                n = numbers[:]
                n.remove(numbers[0])    
                if i == 1:
                    p.append(numbers[0])
                    dfs(n, target)
                    p.pop()
                else :
                    p.append(-1 * numbers[0])
                    dfs(n, target)
                    p.pop()
    dfs(numbers, target)
    
    return len(answer)
