
# below code works but it's inefficent
def dailyTemperatures(temperatures):
    # [73,74,75,71,69,72,76,73]
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
