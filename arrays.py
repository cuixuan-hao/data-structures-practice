```python
class ContactList:
    def __init__(self):
        self.contacts = []

    def add(self, name, phone):
        self.contacts.append((name, phone))

    def get(self, index):
        return self.contacts[index] if 0 <= index < len(self.contacts) else None

    def insert(self, index, name, phone):
        self.contacts.insert(index, (name, phone))

    def remove(self, index):
        return self.contacts.pop(index) if 0 <= index < len(self.contacts) else None


# 使用示例
clist = ContactList()
clist.add("Alice", "123")
clist.add("Bob", "456")
clist.insert(1, "Tom", "789")

print(clist.get(0))  # ('Alice', '123')
print(clist.get(1))  # ('Tom', '789')
print(clist.get(2))  # ('Bob', '456')

clist.remove(1)
print(clist.get(1))  # ('Bob', '456')

```

