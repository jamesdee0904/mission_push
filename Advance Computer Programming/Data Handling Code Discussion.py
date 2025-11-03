from collections import namedtuple, deque, Counter, defaultdict, OrderedDict, ChainMap

print("=== NamedTuple Examples ===")
# Define namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)

print("Original Point:", p)
print("_make():", Point._make([4, 5]))          # Create from iterable
print("_asdict():", p._asdict())                # Convert to dict
print("_replace():", p._replace(x=10))          # Replace value
print("_fields:", Point._fields)                # Show fields

print("\n=== Deque Examples ===")
d = deque([1, 2, 3])
print("Original deque:", d)
d.append(4)
print("After append:", d)
d.appendleft(0)
print("After appendleft:", d)
d.pop()
print("After pop:", d)
d.popleft()
print("After popleft:", d)
d.extend([5, 6])
print("After extend:", d)
d.rotate(3)
print("After rotate(2):", d)

print("\n=== Counter Examples ===")
# Count numbers in a list
c = Counter(['a', 'b', 'b', 'c', 'c', 'c', 'd'])
print("Counter of numbers:", c)

# Find 2 most common numbers
print("Most common:", c.most_common(1))

# Update with another list
c.update([3, 4, 4, 5, 5])
print("After update with [3, 4, 4, 5]:", c)

# List elements (expanded counts)
print("Elements:", list(c.elements()))

print("\n=== DefaultDict Examples ===")
dd = defaultdict(int)
dd["apples"] += 1
dd["mango"] += 2
dd["grapes"] += 3
print("Defaultdict with int:", dict(dd))

dd_list = defaultdict(list)
dd_list["fruits"].append("apple")
dd_list["fruits"].append("mango")
dd_list["prutas"].append("saging")
print("Defaultdict with list:", dict(dd_list))

print("\n=== OrderedDict Examples ===")
od = OrderedDict()
od["one"] = 1
od["two"] = 2
od["three"] = 3
print("Original OrderedDict:", od)

od.move_to_end("one")   # move to end
print("After move_to_end('one'):", od)

od.popitem(last=False)  # pop from beginning
print("After popitem(last=False):", od)

print("\n=== ChainMap Examples ===")
dict1 = {"a": 1, "b": 2} # index 0
dict2 = {"b": 3, "c": 4} # index 1
cm = ChainMap(dict1, dict2)

print("ChainMap:", cm)
print("cm['b'] (from first dict):", cm["b"])
print("Access second dict directly:", cm.maps[1]["b"])  # Force lookup from dict2
print("All maps inside ChainMap:", cm)

# ----------------------------
# Iterators
# ----------------------------

import sys

num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

it = iter(num)

print(it.__next__())
print(next(it))

# ----------------------------
# Custom Iterators
# ----------------------------

class SquareIterator:
    def __init__(self, max_n):
        self.max_n = max_n # 6
        self.current = 0 # 1 # 2 # 3

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

# Using the custom iterator
square_iter = SquareIterator(7)

for num in square_iter:
    print(num)

# ----------------------------
# Generators
# ----------------------------

class FactorialGen:
    def __init__(self, n):
        self.n = n   # maximum number to compute factorial for

    def generate(self):
        result = 1
        for i in range(1, self.n + 1):
            result *= i
            yield result   # yield each factorial step

fact = FactorialGen(6)

for value in fact.generate():
    print(value)

# ------------------
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)

for num in gen:
    print(num)

# ----------------------------
# Generators -> generator expressions
# ----------------------------

import sys
# gen exp
squares = (x*x for x in range(10)) # represented by () still an example of generators

for sq in squares:
    print(sq)
print(sys.getsizeof(squares))

# ----------------------------
# Context Managers
# ----------------------------

class MyContext:
    def __enter__(self):
        print("Start")       # Runs at the beginning of the with-block
        return self          # Optional: lets you return an object for use inside
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End")         # Runs at the end of the with-block (always)
    
    def process(self):
        print("Processing data...")

# Usage
with MyContext() as ctx:     # ctx will be the object returned by __enter__
    print("Inside with-block")
    ctx.process()

# ------------------------------

with open('student_exam_scores.csv', 'r') as file:
    content = file.read()
    print(content)