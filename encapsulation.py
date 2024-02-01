class MyClass:
    def __init__(self, _attribute):
        self._attribute = _attribute

    def get_attribute(self):
        return self._attribute

    def set_attribute(self, new_value):
        self._attribute = new_value


# Usage
obj = MyClass(42)

# Using the getter
value = obj.get_attribute()
print("Initial Value:", value)  # Output: 42

# Using the setter
obj.set_attribute(99)
new_value = obj.get_attribute()
print("Updated Value:", new_value)  # Output: 99
