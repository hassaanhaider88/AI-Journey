# 30-Day AI Engineer Roadmap — Full Explanation with Code

A complete walkthrough of every concept in the roadmap, from basics to advanced, with runnable code examples.

---

## Table of Contents

1. [Week 1: Python for AI + Math Basics](#week-1-python-for-ai--math-basics)
2. [Week 2: Machine Learning](#week-2-machine-learning)
3. [Week 3: Deep Learning + AI](#week-3-deep-learning--ai)
4. [Week 4: Real AI Engineering](#week-4-real-ai-engineering)
5. [Interview Prep Answers](#interview-prep-answers)
6. [Final Skill Stack](#final-skill-stack)

---

# Week 1: Python for AI + Math Basics

## Day 1-2: Python Fundamentals

### Variables & Data Types
```python
name = "Alice"        # str
age = 25               # int
height = 5.6            # float
is_student = True       # bool
print(type(name), type(age), type(height), type(is_student))
```

### Lists — ordered, mutable
```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)          # [1, 2, 3, 4, 5, 6]
numbers.remove(3)          # [1, 2, 4, 5, 6]
print(numbers[0])          # 1
print(numbers[-1])         # 6
print(numbers[1:3])        # [2, 4]

# Advanced: nested lists (used for matrices in ML)
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])        # 2
```

### Tuples — ordered, immutable
```python
point = (10, 20)
x, y = point                # unpacking
# point[0] = 5              # ERROR — immutable
```

### Sets — unordered, unique
```python
tags = {"python", "ai", "python"}
print(tags)                          # {'python', 'ai'}
tags.add("ml")
print("ai" in tags)                  # True — O(1) lookup
```

### Dictionaries — key-value pairs
```python
student = {"name": "Bob", "age": 22, "grade": "A"}
print(student["name"])
student["age"] = 23
student["city"] = "NYC"
for key, value in student.items():
    print(key, "->", value)
```

### Loops
```python
for i in range(5):
    print(i)

count = 0
while count < 3:
    print("count:", count)
    count += 1

scores = [85, 90, 78, 92]
for i, score in enumerate(scores):
    print(f"Index {i}: {score}")
```

### Functions
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))                   # Hello, Alice!
print(greet("Bob", "Hi"))               # Hi, Bob!
```

### *args and **kwargs
```python
def add_numbers(*args):
    return sum(args)
print(add_numbers(1, 2, 3, 4))          # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=25)
```

### Lambda
```python
square = lambda x: x ** 2
print(square(5))                        # 25

nums = [1, -2, 3, -4]
sorted_by_abs = sorted(nums, key=lambda x: abs(x))
```

### List Comprehensions
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# nested — flatten a matrix (common in data prep)
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]     # [1, 2, 3, 4]
```

---

## Day 3: Python OOP

```python
class Model:
    model_type = "Generic"          # class attribute

    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy
        self._internal = "hidden"    # convention: protected

    def describe(self):
        return f"{self.name} has accuracy {self.accuracy}%"

    @property
    def accuracy_grade(self):
        return "Excellent" if self.accuracy > 90 else "Needs Improvement"

    @staticmethod
    def is_valid_accuracy(value):
        return 0 <= value <= 100

    @classmethod
    def create_default(cls):
        return cls("DefaultModel", 75)

    def __str__(self):
        return f"<Model: {self.name}>"

m = Model("RandomForest", 94)
print(m.describe())
print(m.accuracy_grade)             # property — no parentheses
print(Model.is_valid_accuracy(150)) # False
print(m)                            # uses __str__
```

### Inheritance & Polymorphism
```python
class NeuralNetworkModel(Model):
    model_type = "Deep Learning"

    def __init__(self, name, accuracy, layers):
        super().__init__(name, accuracy)
        self.layers = layers

    def describe(self):             # overrides parent
        return f"{self.name} (NN, {self.layers} layers): {self.accuracy}%"

nn = NeuralNetworkModel("CNN-Classifier", 97, 8)
print(nn.describe())
print(isinstance(nn, Model))        # True
```

### Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # name-mangled "private"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(100)
acc.deposit(50)
print(acc.get_balance())            # 150
```

---

## Day 4: NumPy

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
print(a.shape)      # (4,)
print(b.shape)      # (2, 2)
print(b.ndim)        # 2

# Indexing & slicing
print(a[1:3])        # [2 3]
print(b[0, 1])        # 2
print(b[:, 0])        # [1 3] — first column

# Reshaping
c = np.arange(12).reshape(3, 4)

# Broadcasting
x = np.array([1, 2, 3])
y = np.array([[10], [20], [30]])
print(x + y)
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

# Vectorization
data = np.array([10, 20, 30, 40])
print(data * 2)             # no explicit loop
print(data.mean())          # 25.0
print(data.std())
print(np.median(data))

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A + B)                 # element-wise
print(A @ B)                 # matrix multiplication
print(A.T)                   # transpose
```

### Advanced: why vectorization matters
```python
import time
big_array = np.arange(1_000_000)

start = time.time()
result = [x * 2 for x in big_array]     # Python loop
print("Loop:", time.time() - start)

start = time.time()
result = big_array * 2                   # vectorized
print("Vectorized:", time.time() - start)  # typically 10-100x faster
```

---

## Day 5-6: Pandas

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s["b"])                # 20

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85, 90, None]
})

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

# Missing data
print(df.isnull().sum())
df_clean = df.dropna()
df_filled = df.fillna(0)
df["score"] = df["score"].fillna(df["score"].mean())

# Filtering
adults = df[df["age"] > 28]

# Sorting
df_sorted = df.sort_values("age", ascending=False)

# GroupBy
sales = pd.DataFrame({
    "region": ["East", "West", "East", "West"],
    "revenue": [100, 150, 200, 120]
})
grouped = sales.groupby("region")["revenue"].sum()
print(grouped)
# East 300, West 270

# Merging
customers = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
orders = pd.DataFrame({"id": [1, 2], "amount": [250, 400]})
merged = pd.merge(customers, orders, on="id")

# df = pd.read_csv("data.csv")
```

### Advanced: method chaining
```python
result = (
    df[df["age"] > 20]
    .sort_values("score", ascending=False)
    .reset_index(drop=True)
)
```

---

## Day 7: Statistics + Math

```python
import numpy as np
from scipy import stats

data = [23, 45, 12, 67, 34, 89, 23, 45, 12]

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=True).mode[0]
variance = np.var(data)
std_dev = np.std(data)

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
correlation = np.corrcoef(x, y)[0, 1]     # 1.0 — perfect positive

threshold = mean + 2 * std_dev
outliers = [v for v in data if v > threshold]
```

### Vectors, matrices, and gradients
```python
vector = np.array([1.5, 2.3, 0.8])          # a data point's features
matrix = np.array([[1.5, 2.3], [0.8, 1.1], [3.2, 0.5]])   # a dataset

weights = np.array([0.5, 0.3])
prediction = np.dot(vector[:2], weights)     # weighted sum — core of a neuron

def f(x):
    return x ** 2

def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

print(numerical_derivative(f, 3))   # ≈ 6.0, matches analytical 2x
# This is the foundation of gradient descent
```

---

# Week 2: Machine Learning

```bash
pip install scikit-learn pandas numpy matplotlib jupyter
```

**Workflow:** Dataset → Cleaning → Feature Selection → Train/Test Split → Training → Prediction → Evaluation → Improvement

## Day 8: Introduction to ML

```python
# Feature = input (House Size), Label = output (Price)
# Supervised learning: model learns from labeled examples (X -> y)
# Unsupervised learning: model finds structure with no labels (clustering)

import pandas as pd
data = pd.DataFrame({
    "size_sqft": [1000, 1500, 2000, 2500],
    "price": [100000, 150000, 200000, 250000]
})
X = data[["size_sqft"]]   # features (2D — sklearn requires this shape)
y = data["price"]          # label (1D)
```

## Day 9: Linear Regression — House Price Predictor

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Sample data
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([100000, 150000, 200000, 250000, 300000])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)             # learn weight & bias

predictions = model.predict(X_test)

print("Coefficient (slope):", model.coef_)
print("Intercept:", model.intercept_)
print("MAE:", mean_absolute_error(y_test, predictions))
print("MSE:", mean_squared_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))   # 1.0 = perfect fit
```

## Day 10: Classification

### Logistic Regression, KNN, Decision Tree, Random Forest — Student Pass/Fail
```python
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Features: [hours_studied, attendance_pct] -> Label: 1=pass, 0=fail
X = np.array([[1,50],[2,60],[3,55],[5,80],[6,85],[8,90],[9,95],[2,40]])
y = np.array([0,0,0,1,1,1,1,0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

models = {
    "Logistic Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(n_neighbors=3),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=100)
}

for name, clf in models.items():
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print(name, "Accuracy:", accuracy_score(y_test, preds))
```

### Spam Email Classifier (text-based alternative project)
```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = ["win free money now", "meeting at 3pm tomorrow",
          "claim your prize today", "project report attached"]
labels = [1, 0, 1, 0]   # 1 = spam, 0 = not spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)     # text -> numeric features

clf = MultinomialNB()
clf.fit(X, labels)

new_email = vectorizer.transform(["win a free prize"])
print(clf.predict(new_email))            # [1] -> spam
```

## Day 11: Model Evaluation

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)

# Fraud example: 990 normal, 10 fraud — accuracy is misleading here
y_true = [0]*990 + [1]*10
y_pred_naive = [0]*1000       # model predicts "normal" every time

print("Accuracy:", accuracy_score(y_true, y_pred_naive))    # 0.99 -- looks great...
print("Recall:", recall_score(y_true, y_pred_naive))        # 0.0  -- catches zero fraud!

# Better evaluation with a real model's predictions
y_pred = [0]*985 + [1]*5 + [0]*5 + [1]*5   # example mixed predictions
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
# [[TN, FP],
#  [FN, TP]]
```

**Concept notes:**
- **Precision** = of everything predicted positive, how much was correct (avoids false alarms)
- **Recall** = of everything actually positive, how much was caught (avoids missed cases)
- **F1** = harmonic mean of precision and recall — useful when classes are imbalanced

## Day 12: Data Preprocessing

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

df = pd.DataFrame({
    "city": ["NYC", "LA", "NYC", "SF"],
    "size": [1000, 1500, 1100, 2000],
    "price": [200000, 300000, 210000, 400000]
})

# Missing values
df["size"] = df["size"].fillna(df["size"].mean())

# Label Encoding — ordinal categories (has an order)
le = LabelEncoder()
df["city_encoded"] = le.fit_transform(df["city"])   # NYC=1, LA=0, SF=2 (alphabetical)

# One-Hot Encoding — nominal categories (no order) — safer for most ML models
df_onehot = pd.get_dummies(df, columns=["city"])
print(df_onehot)

# Feature Scaling — StandardScaler (mean=0, std=1)
scaler = StandardScaler()
df[["size_scaled"]] = scaler.fit_transform(df[["size"]])
print(df)
```

## Day 13: Overfitting and Underfitting

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.random.rand(100, 2)
y = (X[:, 0] + X[:, 1] > 1).astype(int)

# Underfitting: model too simple to capture the pattern
underfit_model = LogisticRegression(C=0.001)   # heavy regularization

# Overfitting: model memorizes training data, fails on new data
overfit_model = DecisionTreeClassifier(max_depth=None)   # unlimited depth

# Good fit: balanced complexity
good_model = DecisionTreeClassifier(max_depth=4)

# Cross-validation — test generalization across multiple folds
scores = cross_val_score(good_model, X, y, cv=5)
print("CV scores:", scores)
print("Mean CV accuracy:", scores.mean())

# Regularization example (Ridge/L2 penalizes large weights to reduce overfitting)
from sklearn.linear_model import Ridge
ridge_model = Ridge(alpha=1.0)   # alpha controls regularization strength
```

**Concept notes:**
- **Bias** = error from overly simple assumptions (underfitting)
- **Variance** = error from sensitivity to training data noise (overfitting)
- Goal: balance the bias-variance tradeoff

## Day 14: Project 1 — Customer Churn Prediction

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# 1. Load & clean data
# df = pd.read_csv("churn.csv")
df = pd.DataFrame({
    "tenure_months": [1, 24, 3, 36, 6, 48, 2, 60],
    "monthly_charge": [70, 50, 90, 40, 85, 30, 95, 25],
    "support_calls": [5, 1, 6, 0, 4, 0, 7, 1],
    "churned": [1, 0, 1, 0, 1, 0, 1, 0]
})

# 2. Feature engineering
df["charge_per_call"] = df["monthly_charge"] / (df["support_calls"] + 1)

# 3. Split features/label
X = df.drop("churned", axis=1)
y = df["churned"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 4. Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train & compare models
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 6. Evaluate
preds = model.predict(X_test_scaled)
print(classification_report(y_test, preds))

# 7. Save model
joblib.dump(model, "churn_model.pkl")
joblib.dump(scaler, "scaler.pkl")
```

---

# Week 3: Deep Learning + AI

```bash
pip install torch torchvision
```

## Day 15: Neural Networks — Concepts

```text
Input -> Neural Network -> Prediction -> Loss -> Backpropagation -> Update Weights
```

```python
import numpy as np

# A single neuron, manually implemented
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

inputs = np.array([0.5, 0.8, 0.2])       # input layer values
weights = np.array([0.4, 0.7, 0.1])      # learned weights
bias = 0.1

z = np.dot(inputs, weights) + bias        # weighted sum
output = sigmoid(z)                       # activation function
print("Neuron output:", output)

# Loss function example — Mean Squared Error
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

y_true = np.array([1.0])
y_pred = np.array([output])
print("Loss:", mse_loss(y_true, y_pred))
```

## Day 16: PyTorch Basics

```python
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Tensors — like NumPy arrays but with GPU + autograd support
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x ** 2
y_sum = y.sum()
y_sum.backward()          # computes gradients automatically
print(x.grad)              # dy/dx = 2x -> [2, 4, 6]

# Custom Dataset
class SimpleDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

X_data = [[1, 2], [3, 4], [5, 6]]
y_data = [3, 7, 11]
dataset = SimpleDataset(X_data, y_data)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# nn.Module — defining a model
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(2, 4)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(4, 1)

    def forward(self, x):
        x = self.relu(self.layer1(x))
        return self.layer2(x)

model = SimpleNet()
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
```

## Day 17: First Neural Network — Handwritten Digit Classifier (MNIST)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([transforms.ToTensor()])
train_data = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
dataloader = DataLoader(train_data, batch_size=64, shuffle=True)

class DigitClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28*28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)   # 10 digit classes

    def forward(self, x):
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        return self.fc2(x)

model = DigitClassifier()
loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 3
for epoch in range(epochs):
    total_loss = 0
    for X, y in dataloader:
        prediction = model(X)                # forward pass
        loss = loss_function(prediction, y)   # compute loss

        optimizer.zero_grad()                  # clear old gradients
        loss.backward()                         # backpropagation
        optimizer.step()                        # update weights

        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")
```

## Day 18: CNN Basics — Cat vs Dog Classifier

```python
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.fc = nn.Linear(32 * 16 * 16, 2)   # 2 classes: cat, dog

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))   # convolution + pooling
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)                   # flatten feature maps
        return self.fc(x)

model = SimpleCNN()
```

### Transfer learning (recommended over training from scratch)
```python
from torchvision import models
import torch.nn as nn

resnet = models.resnet18(pretrained=True)
for param in resnet.parameters():
    param.requires_grad = False       # freeze pretrained layers

resnet.fc = nn.Linear(resnet.fc.in_features, 2)   # replace final layer for our 2 classes
```

**Concept notes:**
- **Convolution**: a small filter slides over the image, detecting patterns (edges, textures)
- **Pooling**: downsamples feature maps, reducing size while keeping important info
- **Feature Maps**: the output of each convolution — increasingly abstract representations

## Day 19: NLP Basics — Sentiment Analysis App

```python
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")
result = sentiment_analyzer("This movie is amazing")
print(result)   # [{'label': 'POSITIVE', 'score': 0.999}]
```

### Manual tokenization + embeddings concept
```python
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

text = "Machine learning is powerful"
tokens = tokenizer(text, return_tensors="pt")
print(tokens["input_ids"])          # numeric token IDs

with torch.no_grad():
    output = model(**tokens)

embeddings = output.last_hidden_state    # dense vector representation of each token
print(embeddings.shape)                   # [1, num_tokens, 768]
```

## Day 20-21: Transformers + Hugging Face — AI Text Summarizer

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """
Machine learning is a subset of artificial intelligence that enables
systems to learn patterns from data without explicit programming.
It powers recommendation engines, fraud detection, and much more...
"""

summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
print(summary[0]["summary_text"])
```

### Using pretrained models directly (pipelines, tokenizers, inference)
```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification")
result = classifier(
    "This is a tutorial about deep learning",
    candidate_labels=["education", "sports", "politics"]
)
print(result["labels"][0])   # most likely label
```

---

# Week 4: Real AI Engineering

```text
React/Next.js -> FastAPI -> Machine Learning Model / LLM -> Database
```

## Day 22: FastAPI — Serving an ML Model

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

class PredictionInput(BaseModel):
    size_sqft: float
    bedrooms: int

@app.get("/")
def home():
    return {"message": "ML API Running"}

@app.post("/predict")
def predict(data: PredictionInput):
    features = np.array([[data.size_sqft, data.bedrooms]])
    prediction = model.predict(features)
    return {"predicted_price": float(prediction[0])}

# Run with: uvicorn main:app --reload
```

## Day 23: Docker

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t ml-api .
docker run -p 8000:8000 -e MODEL_PATH=/app/model.pkl ml-api
```

## Day 24-25: Project 2 — AI Resume Analyzer

```python
from fastapi import FastAPI, UploadFile
import PyPDF2
from transformers import pipeline

app = FastAPI()
skill_matcher = pipeline("zero-shot-classification")

def extract_text_from_pdf(file) -> str:
    reader = PyPDF2.PdfReader(file)
    return " ".join(page.extract_text() for page in reader.pages)

@app.post("/analyze-resume")
async def analyze_resume(resume: UploadFile, job_description: str):
    text = extract_text_from_pdf(resume.file)

    required_skills = ["python", "machine learning", "sql", "react", "docker"]
    result = skill_matcher(text, candidate_labels=required_skills, multi_label=True)

    matched = [label for label, score in zip(result["labels"], result["scores"]) if score > 0.5]
    missing = [s for s in required_skills if s not in matched]

    match_score = len(matched) / len(required_skills) * 100

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_score": round(match_score, 2)
    }
```

## Day 26-27: Project 3 — RAG Document Chatbot

```text
PDF Upload -> Extract Text -> Chunk -> Embed -> Vector DB -> Question -> Similarity Search -> Context -> LLM -> Answer
```

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
import PyPDF2

# 1. Extract text
def extract_text(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    return " ".join(page.extract_text() for page in reader.pages)

raw_text = extract_text("document.pdf")

# 2. Chunking — split into overlapping pieces so context isn't lost at boundaries
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(raw_text)

# 3. Embeddings — turn text into dense numeric vectors
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Vector Database — store chunks for fast similarity search
vector_db = Chroma.from_texts(chunks, embeddings, persist_directory="./chroma_db")

# 5. Similarity Search — retrieve the most relevant chunks for a query
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# 6. RAG chain — retrieved context + question -> LLM -> answer
qa_chain = RetrievalQA.from_chain_type(
    llm=HuggingFacePipeline.from_model_id(model_id="google/flan-t5-base", task="text2text-generation"),
    retriever=retriever
)

answer = qa_chain.run("What is the main topic of this document?")
print(answer)
```

**Concept notes:**
- **Embeddings**: numeric vectors where semantically similar text is close together in vector space
- **Vector Database**: stores embeddings and supports fast nearest-neighbor search (e.g., Chroma, Pinecone, FAISS)
- **RAG (Retrieval-Augmented Generation)**: instead of relying only on the LLM's training data, you retrieve relevant real documents first, then feed them as context — this reduces hallucination and lets the model answer about your own data
- **Prompt Engineering**: crafting the input prompt (including retrieved context) so the LLM produces accurate, well-formatted answers

## Day 28: Deployment

```bash
# Environment variables (.env)
MODEL_PATH=/app/model.pkl
API_KEY=your_key_here

# Backend deployment (example: Railway/Render/Fly.io)
docker build -t my-api .
docker push myregistry/my-api

# Frontend deployment (example: Vercel)
vercel --prod
```

```python
# Loading env vars safely in FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH")
```

## Day 29: GitHub Cleanup

```markdown
# Project Name

## Description
Short, clear summary of what the project does and why.

## Features
- Feature 1
- Feature 2

## Tech Stack
Next.js, FastAPI, scikit-learn, PostgreSQL, Docker

## Architecture
[Diagram or description of how components connect]

## Installation
\`\`\`bash
git clone <repo>
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`

## Environment Variables
| Variable | Description |
|---|---|
| MODEL_PATH | Path to trained model file |

## API Documentation
POST /predict — returns prediction given input features

## Screenshots
[Add images]

## Demo
[Live link]
```

## Day 30: Interview Preparation

See the [Interview Prep Answers](#interview-prep-answers) section below.

---

# Interview Prep Answers

**What is supervised learning?**
Training a model on labeled data (input-output pairs) so it learns to map inputs to correct outputs, then generalizes to new, unseen inputs.

**What is overfitting?**
The model learns the training data too well, including its noise, and performs poorly on new data. Detected by a large gap between training and validation accuracy.

**What is underfitting?**
The model is too simple to capture the underlying pattern, performing poorly on both training and test data.

**What is train/test split?**
Dividing data into a portion used to train the model and a separate portion used to evaluate it on unseen data, so performance metrics reflect real-world generalization.

**What is cross validation?**
Splitting data into k folds, training on k-1 folds and validating on the remaining fold, rotating through all folds — gives a more reliable performance estimate than a single split.

**What is precision and recall?**
Precision = correct positive predictions / all positive predictions (how many flagged items were actually correct). Recall = correct positive predictions / all actual positives (how many real cases were caught).

**What is a confusion matrix?**
A table showing True Positives, True Negatives, False Positives, and False Negatives — the basis for computing accuracy, precision, recall, and F1.

**What is gradient descent?**
An optimization algorithm that iteratively adjusts model parameters in the direction that reduces the loss function, using the gradient (slope) of the loss with respect to each parameter.

**What is backpropagation?**
The algorithm that computes gradients of the loss with respect to every weight in a neural network by applying the chain rule backward through the layers, enabling gradient descent to update weights.

**What is an embedding?**
A dense numeric vector representation of data (text, images, etc.) where semantically similar items are positioned close together in vector space.

**What is RAG?**
Retrieval-Augmented Generation — retrieving relevant documents/context from an external knowledge source before generating an LLM response, so answers are grounded in real data rather than only the model's training knowledge.

**What is a vector database?**
A database optimized for storing embeddings and performing fast similarity (nearest-neighbor) search, used to power semantic search and RAG systems.

**What is an LLM?**
A Large Language Model — a neural network (typically transformer-based) trained on massive text data to understand and generate human language.

**What is FastAPI?**
A modern Python web framework for building APIs quickly, with automatic request validation (via Pydantic) and interactive documentation.

**How do you deploy an ML model?**
Save the trained model (e.g., with joblib/pickle), wrap it in an API (e.g., FastAPI), containerize it (Docker) for consistent environments, then deploy the container to a cloud platform and connect it to a frontend.

---

# Final Skill Stack

```text
PYTHON
   ├── NumPy
   ├── Pandas
   ├── Matplotlib
   ▼
SCIKIT-LEARN
   ├── Regression
   ├── Classification
   ├── Preprocessing
   └── Evaluation
   ▼
PYTORCH
   ├── Neural Networks
   └── CNN Basics
   ▼
AI / LLMS
   ├── Hugging Face
   ├── Transformers
   ├── Embeddings
   └── RAG
   ▼
DEPLOYMENT
   ├── FastAPI
   ├── Docker
   └── Next.js
```

## Recommended Projects

1. **Customer Churn Prediction System** — Next.js + FastAPI + scikit-learn + PostgreSQL/MongoDB
2. **AI Resume Analyzer** — Upload → Extract Text → AI Analysis → Job Matching → Skill Gap Analysis
3. **RAG Document Chatbot** — PDF Upload + Embeddings + Vector Database + LLM + Chat Interface