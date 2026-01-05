# キュー(待ち行列)とは、最初に入れたデータを最初に取り出す形式のデータ構造
# キューにデータを入れることをenqueue, 取り出すことをdequeueという
# FIFO(First In First Out)方式とも呼ばれる
# キューのデータはリングバッファで管理すると扱いやすい
# データを出し入れする際、記憶領域の終端と戦闘をつなげる計算を行い、役野洋右な状態を実現する

# キューの最大サイズ
MAX = 6

# キュー配列
queue = [0] * MAX

# headポインタ
head = 0

# tailポインタ
tail = 0

def enqueue(d):
    global tail
    next_tail = (tail + 1) % MAX

    if next_tail == head:
        print("Queue Overflow")
    else:
        queue[tail] = d
        tail = next_tail
        print("Enqueued:", d)

def dequeue():
    global head
    if head == tail:
        print("Queue Underflow")
        return None
    else:
        d = queue[head]
        head = (head + 1) % MAX
        return d
    
for i in range(6):
    d = enqueue(i)
for i in range(6):
    d = dequeue()
    print("Dequeued:", d)