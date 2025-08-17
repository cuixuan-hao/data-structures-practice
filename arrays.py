```python
class MyArray:
    def __init__(self):
        self.data = []

    # 在末尾添加元素
    def append(self, value):
        self.data.append(value)

    # 根据索引获取元素
    def get(self, index):
        return self.data[index] if 0 <= index < len(self.data) else None

    # 在指定位置插入元素
    def insert(self, index, value):
        self.data.insert(index, value)

    # 删除指定位置的元素
    def remove(self, index):
        return self.data.pop(index) if 0 <= index < len(self.data) else None

# 示例使用
arr = MyArray()
arr.append(10)
arr.append(20)
arr.insert(1, 15)

print(arr.get(0))  # 10
print(arr.get(1))  # 15
print(arr.get(2))  # 20

arr.remove(1)
print(arr.get(1))  # 20

```

