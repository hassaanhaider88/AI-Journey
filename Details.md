## Week 1: Python for AI + Math Basics

### 1. Python Fundamentals (Day 1-2)

**Variables & Data Types**
```python
# Variables — no type declaration needed
name = "Alice"        # str
age = 25               # int
height = 5.6            # float
is_student = True       # bool

print(type(name), type(age), type(height), type(is_student))
```

**Lists** — ordered, mutable collections
```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)          # [1, 2, 3, 4, 5, 6]
numbers.remove(3)          # [1, 2, 4, 5, 6]
print(numbers[0])          # 1 (first element)
print(numbers[-1])         # 6 (last element)
print(numbers[1:3])        # [2, 4] (slicing)

# Advanced: nested lists (used heavily in ML for matrices)
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])        # 2
```

**Tuples** — ordered, immutable
```python
point = (10, 20)
x, y = point                # unpacking
# point[0] = 5              # ERROR — tuples can't be changed
```

**Sets** — unordered, unique elements
```python
tags = {"python", "ai", "python"}   # duplicates removed
print(tags)                          # {'python', 'ai'}
tags.add("ml")
print("ai" in tags)                  # True — fast membership check
```

**Dictionaries** — key-value pairs
```python
student = {"name": "Bob", "age": 22, "grade": "A"}
print(student["name"])          # Bob
student["age"] = 23              # update
student["city"] = "NYC"          # add new key

for key, value in student.items():
    print(key, "->", value)
```

**Loops**
```python
# for loop
for i in range(5):
    print(i)                    # 0 1 2 3 4

# while loop
count = 0
while count < 3:
    print("count:", count)
    count += 1

# looping over data structures (common in ML preprocessing)
scores = [85, 90, 78, 92]
for i, score in enumerate(scores):
    print(f"Index {i}: {score}")
```

**Functions**
```python
def greet(name, greeting="Hello"):     # default parameter
    return f"{greeting}, {name}!"

print(greet("Alice"))                   # Hello, Alice!
print(greet("Bob", "Hi"))               # Hi, Bob!
```

**\*args and \*\*kwargs** — flexible function arguments
```python
def add_numbers(*args):                 # collects positional args as tuple
    return sum(args)

print(add_numbers(1, 2, 3, 4))          # 10

def print_info(**kwargs):               # collects keyword args as dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
```

**Lambda functions** — small anonymous functions
```python
square = lambda x: x ** 2
print(square(5))                        # 25

# common in ML: sorting or applying quick transformations
nums = [1, -2, 3, -4]
sorted_by_abs = sorted(nums, key=lambda x: abs(x))
print(sorted_by_abs)                    # [1, -2, 3, -4]
```

**List comprehensions** — compact way to build lists
```python
squares = [x**2 for x in range(10)]
print(squares)                          # [0, 1, 4, 9, 16, ...]

# with condition
evens = [x for x in range(20) if x % 2 == 0]

# nested (matrix flattening — used in data prep)
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat)                             # [1, 2, 3, 4]
```

---

### 2. Python OOP (Day 3)

```python
class Model:
    # Class attribute — shared across all instances
    model_type = "Generic"

    def __init__(self, name, accuracy):
        self.name = name           # instance attribute
        self.accuracy = accuracy
        self._internal = "hidden"  # convention: "protected"

    def describe(self):
        return f"{self.name} has accuracy {self.accuracy}%"

    @property
    def accuracy_grade(self):
        if self.accuracy > 90:
            return "Excellent"
        return "Needs Improvement"

    @staticmethod
    def is_valid_accuracy(value):
        return 0 <= value <= 100

    @classmethod
    def create_default(cls):
        return cls("DefaultModel", 75)

    def __str__(self):              # dunder method — controls print() output
        return f"<Model: {self.name}>"


m = Model("RandomForest", 94)
print(m.describe())                 # RandomForest has accuracy 94%
print(m.accuracy_grade)             # Excellent (called without parentheses)
print(Model.is_valid_accuracy(150)) # False
print(m)                            # <Model: RandomForest>
```

**Inheritance & Polymorphism**
```python
class NeuralNetworkModel(Model):    # inherits from Model
    model_type = "Deep Learning"

    def __init__(self, name, accuracy, layers):
        super().__init__(name, accuracy)   # call parent constructor
        self.layers = layers

    def describe(self):             # polymorphism — overrides parent method
        return f"{self.name} (NN, {self.layers} layers): {self.accuracy}%"


nn = NeuralNetworkModel("CNN-Classifier", 97, 8)
print(nn.describe())                # CNN-Classifier (NN, 8 layers): 97%
print(isinstance(nn, Model))        # True — inherited relationship
```

**Encapsulation**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # double underscore = "private" (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(100)
acc.deposit(50)
print(acc.get_balance())            # 150
# print(acc.__balance)              # ERROR — not directly accessible
```

---

### 3. NumPy (Day 4)

```python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])      # 2D array (matrix)

print(a.shape)      # (4,)
print(b.shape)      # (2, 2)
print(b.ndim)        # 2 (dimensions)

# Indexing & slicing
print(a[1:3])        # [2 3]
print(b[0, 1])        # 2 — row 0, col 1
print(b[:, 0])        # [1 3] — entire first column

# Reshaping
c = np.arange(12)               # [0,1,2,...,11]
reshaped = c.reshape(3, 4)      # 3 rows, 4 columns
print(reshaped)

# Broadcasting — operate on arrays of different shapes without loops
x = np.array([1, 2, 3])
y = np.array([[10], [20], [30]])
print(x + y)
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

# Vectorization — fast operations instead of Python loops
data = np.array([10, 20, 30, 40])
print(data * 2)             # [20 40 60 80] — no explicit loop needed
print(data.mean())          # 25.0
print(data.std())           # standard deviation
print(np.median(data))      # 25.0

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A + B)                 # element-wise addition
print(A @ B)                 # matrix multiplication (dot product)
print(A.T)                   # transpose
```

**Why vectorization matters (advanced insight):**
```python
import time

big_array = np.arange(1_000_000)

# Slow — Python loop
start = time.time()
result = [x * 2 for x in big_array]
print("Loop time:", time.time() - start)

# Fast — vectorized NumPy
start = time.time()
result = big_array * 2
print("Vectorized time:", time.time() - start)
# Vectorized is typically 10-100x faster
```

---

### 4. Pandas (Day 5-6)

```python
import pandas as pd

# Series — 1D labeled array
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s["b"])                # 20

# DataFrame — 2D labeled table
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85, 90, None]
})

print(df.head())             # first 5 rows
print(df.tail())              # last 5 rows
print(df.info())              # column types, non-null counts
print(df.describe())          # statistical summary (mean, std, etc.)

# Handling missing data
print(df.isnull())            # True/False mask for missing values
print(df.isnull().sum())      # count of missing values per column
df_clean = df.dropna()        # remove rows with any missing value
df_filled = df.fillna(0)      # replace missing values with 0
df["score"] = df["score"].fillna(df["score"].mean())  # fill with column mean

# Filtering
adults = df[df["age"] > 28]
print(adults)

# Sorting
df_sorted = df.sort_values("age", ascending=False)

# GroupBy — aggregate data (core skill for EDA)
sales = pd.DataFrame({
    "region": ["East", "West", "East", "West"],
    "revenue": [100, 150, 200, 120]
})
grouped = sales.groupby("region")["revenue"].sum()
print(grouped)
# East    300
# West    270

# Merging datasets
customers = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
orders = pd.DataFrame({"id": [1, 2], "amount": [250, 400]})
merged = pd.merge(customers, orders, on="id")
print(merged)

# Reading real data
# df = pd.read_csv("data.csv")
```

**Advanced Pandas — method chaining (real-world pattern):**
```python
result = (
    df[df["age"] > 20]
    .sort_values("score", ascending=False)
    .reset_index(drop=True)
)
```

---

### 5. Statistics + Math (Day 7)

```python
import numpy as np

data = [23, 45, 12, 67, 34, 89, 23, 45, 12]

# Central tendency
mean = np.mean(data)
median = np.median(data)
from scipy import stats
mode = stats.mode(data, keepdims=True)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode.mode[0])

# Spread
variance = np.var(data)
std_dev = np.std(data)
print("Variance:", variance)
print("Std Dev:", std_dev)

# Correlation — relationship between two variables
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
correlation = np.corrcoef(x, y)[0, 1]
print("Correlation:", correlation)     # 1.0 — perfect positive relationship

# Outlier detection using standard deviation
threshold = mean + 2 * std_dev
outliers = [x for x in data if x > threshold]
print("Outliers:", outliers)
```

**Vectors, matrices, and gradients (conceptual + code):**
```python
# Vector — a 1D array of numbers (e.g., a data point's features)
vector = np.array([1.5, 2.3, 0.8])   # e.g., [height, weight, age_scaled]

# Matrix — 2D array (e.g., a whole dataset: rows=samples, cols=features)
matrix = np.array([[1.5, 2.3], [0.8, 1.1], [3.2, 0.5]])

# Dot product — foundation of neural network computations
weights = np.array([0.5, 0.3])
prediction = np.dot(vector[:2], weights)   # weighted sum
print(prediction)

# Derivative/gradient concept — the slope of a function at a point
# For f(x) = x^2, derivative is f'(x) = 2x
def f(x):
    return x ** 2

def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

print(numerical_derivative(f, 3))   # ≈ 6.0 (matches 2*3)
# This is the core idea behind gradient descent in ML/DL
```

---