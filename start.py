from HashLab.HashAlgorithm import HashTable, Node
import random
import time

start_time = time.time()

SIZE_TABLE = 1000
ht = HashTable(SIZE_TABLE)

for i in range(0, SIZE_TABLE):
    ht.put(random.randint(1, 100000))

print("1-2. Хэш таблица заполнена! %s элементов за %s секунд" % (SIZE_TABLE, time.time() - start_time))

quantity = SIZE_TABLE
min_chain = SIZE_TABLE
max_chain = 0
chains = 0

for i in ht.table:
    if i is None:
        quantity -= 1
    elif type(i) is Node:
        temp = i
        count = 1
        while temp.next is not None:
            count += 1
            temp = temp.next

        if count > max_chain:
            max_chain = count
        elif count < min_chain:
            min_chain = count

        chains += 1

print("3. Коэффицент заполнения: %s\n   Самая длинная цепочка: %s\n   Самая короткая цепочка: %s\n   Количество цепочек: %s" %
      (quantity / SIZE_TABLE, max_chain, min_chain, chains))


