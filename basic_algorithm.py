# average_1
scoreList = [70, 98, 92, 88, 64]
total: float = 0
average: float = 0
for score in scoreList:
    total += score
    average = total / len(scoreList)
print("Average score: ", average)


# addup
def addup(n):
    total = 0
    for num in range(1, n + 1):
        total += num
    
    return total

print("Addup", addup(10))

def recursive_addup(n):
    if n == 1:
        return 1
    else:
        return n + recursive_addup(n - 1)
print("Recursive Addup", recursive_addup(10))