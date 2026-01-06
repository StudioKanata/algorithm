# 線形リスト
# 片方向リスト
# 双方向リスト
# 循環リスト

MAX = 5

data = [None]*MAX

pointer = [None]*MAX

head = 0

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

def put_list():
    p = head
    while True:
        print(data[p], end="->")
        if pointer[p] is None:
            print("EOF")
            break
        p = pointer[p]

for i in range(10, 70, 10):
    add_list(i)
del_list(10)
put_list()