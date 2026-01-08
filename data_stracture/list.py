# 線形リストの処理時間
# 線形リストは、データの追加や削除の計算量がO(1)
# ただし、データの探索にはO(n)の時間がかかる(データを追加する際、空きノードを探のとか)

MAX = 5

data = [None]*MAX

pointer = [None]*MAX

head = 0

# 先頭にデータを追加する関数
def add_list(value):
    n = -1
    for i in range(MAX):
        if data[i] == None:
            n = i
            break
    if n == -1:
        print("List Overflow")
        return False
    for i in range(MAX):
        if data[i] != None and pointer[i] is None:
            pointer[i] = n
            break
    data[n] = value
    pointer[n] = None
    print("Added:", value)
    return True
    
# 指定したデータを削除する関数
def del_list(value):
    global head
    n = -1
    for i in range(MAX):
        if data[i] == value:
            n = i
            break
    if n == -1:
        print("Data not found")
        return False
    if n != head:
        for i in range(MAX):
            if pointer[i] == n:
                pointer[i] = pointer[n]
                break
    else:
        head = pointer[n]
        if head is None:
            head = 0
    data[n] = None
    pointer[n] = None
    print("Deleted:", value)
    return True

# リストの内容を表示する関数
def put_list():
    p = head
    while True:
        print(data[p], end="->")
        if pointer[p] is None:
            print("EOF")
            break
        p = pointer[p]

# テストコード
for i in range(10, 70, 10):
    add_list(i)
del_list(10)
put_list()