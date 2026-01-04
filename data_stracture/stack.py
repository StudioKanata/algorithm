# Stack
# LIFO(Last In First Out)のデータ構造

# stackの最大サイズ
MAX = 5

# stack配列
stack = [0] * MAX

# stackポインタ
stack_pointer = 0

# stackにデータをpushする関数
def push(d):
    global stack_pointer
    if stack_pointer < MAX:
        stack[stack_pointer] = d
        stack_pointer += 1
        print("Pushed:", d)
    else:
        print("Stack Overflow")

# stackからデータをpopする関数
def pop():
    global stack_pointer
    if stack_pointer > 0:
        stack_pointer -= 1
        return stack[stack_pointer]
    else:
        print("Stack Underflow")
        return None

for i in range(6):
    push(i)
for i in range(6):
    d = pop()
    print("Popped:", d)