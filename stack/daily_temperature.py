def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for i,t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            result[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
        stack.append([t,i])
    return result

    # below code works but it's inefficent
    i, j = 0, 1
    answer = []
    while i < len(temperatures) and j < len(temperatures):
        if temperatures[j] > temperatures[i]:
            answer.append(j-i)
            i += 1
            j += 1
        else:
            while temperatures[j] <= temperatures[i]:
                j += 1
                if j == len(temperatures):
                    answer.append(0)
                    break
            if j != len(temperatures):
                answer.append(j-i)
                i += 1
                j = i + 1
            else:
                i += 1
                j = i+1
    answer.append(0)
    return answer


temperatures = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]

print(dailyTemperatures(temperatures))
