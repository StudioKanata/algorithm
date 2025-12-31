# pythonの書き方お試し
def average_score():
    scoreList = [70, 98, 92, 88, 64]
    total: float = 0
    average: float = 0
    for score in scoreList:
        total += score
        average = total / len(scoreList)
    print("Average score: ", average)

# 1~nまでの和を求めるアルゴリズム
# addup
def addup(n):
    total = 0
    for num in range(1, n + 1):
        total += num
    
    return total

# 再帰関数は意外と遅いのか！？ - ファイル探索などで使用する場合、読みやすいし、普通のループより早いという結果
def recursive_addup(n):
    if n == 1:
        return 1
    else:
        return n + recursive_addup(n - 1)

# nが大きくなっても高速に計算できる
def addup_2(n):
    total = (1+n) * n/2
    return int(total)

# 九九の式を出力する
def multiplication_table():
    for i in range(1, 10):
        result = ""
        for j in range(1, 10):
            result = result + "{} x {} = {:2d}  ".format(j, i, i*j)
        print(result)

if __name__ == "__main__":
    # average_score()
    # print("Addup", addup(10))
    # print("Recursive Addup", recursive_addup(10))
    # print("Addup_2", addup_2(10))
    print("Multiplication Table", multiplication_table())
