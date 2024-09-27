class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Createing an iterator that yields the length and width in the required format
        yield {'length': self.length}
        yield {'width': self.width}


rect = Rectangle(15, 10)

# Iterating over the rectangle instance
for attribute in rect:
    print(attribute)
