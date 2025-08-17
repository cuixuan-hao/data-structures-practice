```python
class MyArray:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        print("索引越界！")
        return None

    def insert(self, index, value):
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)
        else:
            print("索引越界！")

    def remove(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        print("索引越界！")
        return None

    def length(self):
        return len(self.data)


```

