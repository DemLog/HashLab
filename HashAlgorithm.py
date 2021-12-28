class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size

    def _get_hash(self, key):
        return key % self.size

    def put(self, key):
        hash_val = self._get_hash(key)

        if self.table[hash_val] is None:
            self.table[hash_val] = key
        else:
            temp = Node(key)
            p = self.table[hash_val]

            if type(p) is Node:
                p = self.table[hash_val]

                while p.next is not None:
                    p = p.next
                p.next = temp
            else:
                self.table[hash_val] = Node(p)
                self.table[hash_val].next = temp

    def get(self, key):
        hash_val = self._get_hash(key)

        if self.table[hash_val] == key:
            return True
        else:
            p = self.table[hash_val]

            try:
                while p is not None and p.value != key:
                    p = p.next
                if p is not None and p.data == key:
                    return True
            except TypeError:
                return False
        return False

    def remove(self, key):
        if not self.get(key):
            return "Ошибка! Элемент отсуствует в таблице."

        hash_val = self._get_hash(key)

        if self.data[hash_val] == key:
            self.table[hash_val] = None
        else:
            p = self.table[hash_val]
            prev = None

            try:
                while p is not None and p.value != key:
                    prev = p
                    p = p.next
                if p is None:  # для обработки непредвиденных ошибок
                    return "Ошибка! Невозможно удалить элемент."
                else:
                    prev.next = p.next
            except TypeError:
                return False
