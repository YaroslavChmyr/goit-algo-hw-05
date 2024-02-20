class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    self.table[key_hash].remove(pair)
        return None

# Тестуємо функціонал видалення пар ключ значення:
H = HashTable(5)

H.insert("apple", 10) # Додаємо ключ значення

print(H.get("apple")) # Знаходимо ключ значення в хеш таблиці, та виводимо значення в термінал

H.delete("apple") # Видаляємо ключ значення з хеш таблиці по ключу

print(H.get("apple")) # Перевіряємо, якщо отримуємо None, ключ значення були видалені успішно
