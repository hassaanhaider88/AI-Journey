## Your 30-day roadmap

### Daily 4-hour structure

Use this every day:

```text
1 hour   → Learn concepts
1 hour   → Write code yourself
1.5 hour → Build/project work
30 min   → Revision + GitHub notes
```

The important rule:

```text
30% Learning
70% Coding and building
```

Do not spend the entire month watching tutorials.

# Week 1: Python for AI + Math Basics

Since you're already learning Python, focus on the parts used in AI and ML.

### Day 1-2: Python fundamentals

Learn and practice:

```text
Variables
Data types
Lists
Tuples
Sets
Dictionaries
Loops
Functions
*args and **kwargs
Lambda
List comprehensions
```

Practice by solving 10 to 15 small problems daily.

### Day 3: Python OOP

You are already learning this.

Focus on:

```text
Classes
Objects
__init__
self
Inheritance
super()
Encapsulation
Polymorphism
@property
@classmethod
@staticmethod
Dunder methods
```

Don't go too deep into advanced OOP. One day is enough for now.

### Day 4: NumPy

Learn:

```python
import numpy as np
```

Important topics:

```text
Arrays
Dimensions
Shape
Indexing
Slicing
Reshaping
Broadcasting
Vectorization
Mean
Median
Standard deviation
Matrix operations
```

Example:

```python
import numpy as np

data = np.array([10, 20, 30, 40])

print(data.mean())
print(data.std())
```

### Day 5-6: Pandas

Learn:

```python
import pandas as pd
```

Important:

```text
Series
DataFrame
read_csv()
head()
tail()
info()
describe()
isnull()
dropna()
fillna()
groupby()
sort_values()
Filtering
Merging datasets
```

Practice using real CSV datasets.

### Day 7: Statistics + Math

You don't need advanced calculus in the first month.

Understand:

```text
Mean
Median
Mode
Variance
Standard deviation
Probability
Correlation
Distribution
Outliers
```

Also understand conceptually:

```text
Vectors
Matrices
Linear algebra basics
Derivatives
Gradient
```

Don't get stuck solving difficult math problems. Focus on understanding how these concepts relate to ML.

---

# Week 2: Machine Learning

This is where you start becoming an ML engineer.

Install:

```bash
pip install scikit-learn pandas numpy matplotlib jupyter
```

Learn the basic ML workflow:

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Prediction
   ↓
Evaluation
   ↓
Improvement
```

### Day 8: Introduction to Machine Learning

Understand:

```text
What is Machine Learning?
Supervised Learning
Unsupervised Learning
Features
Labels
Training Data
Testing Data
```

Example:

```text
House Size → Price

1000 sqft → $100,000
2000 sqft → $200,000
```

Here:

```text
Feature = House Size
Label = Price
```

### Day 9: Linear Regression

Build a project:

```text
House Price Predictor
```

Learn:

```text
LinearRegression
train_test_split
fit()
predict()
MAE
MSE
R² Score
```

### Day 10: Classification

Learn:

```text
Logistic Regression
K-Nearest Neighbors
Decision Tree
Random Forest
```

Project:

```text
Student Pass/Fail Predictor
```

or:

```text
Spam Email Classifier
```

### Day 11: Model Evaluation

Very important concepts:

```text
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
```

You should understand when accuracy is misleading.

For example:

```text
990 normal transactions
10 fraud transactions
```

A model predicting everything as "normal" gets:

```text
99% Accuracy
```

But it is useless for fraud detection.

### Day 12: Data Preprocessing

Learn:

```text
Missing values
Categorical data
Label Encoding
One Hot Encoding
Feature Scaling
StandardScaler
Normalization
```

### Day 13: Overfitting and Underfitting

Understand:

```text
Underfitting
Good Fit
Overfitting
```

Learn:

```text
Cross Validation
Regularization
Bias
Variance
```

### Day 14: Project 1

Build a complete ML project.

Recommended:

```text
Customer Churn Prediction
```

Your project should include:

```text
Dataset
Data cleaning
EDA
Feature engineering
Model training
Evaluation
Model comparison
Saved model
```

Save the model:

```python
import joblib

joblib.dump(model, "model.pkl")
```

---

# Week 3: Deep Learning + AI

Now move into modern AI.

Install:

```bash
pip install torch torchvision
```

I recommend learning **PyTorch**.

Focus on understanding the fundamentals rather than trying to learn every deep learning architecture.

### Day 15: Neural Networks

Understand:

```text
Neuron
Input Layer
Hidden Layer
Output Layer
Weights
Bias
Activation Functions
Loss Function
Epoch
Batch
Learning Rate
```

The basic flow:

```text
Input
  ↓
Neural Network
  ↓
Prediction
  ↓
Calculate Loss
  ↓
Backpropagation
  ↓
Update Weights
```

### Day 16: PyTorch Basics

Learn:

```text
Tensors
Datasets
DataLoader
nn.Module
Forward pass
Loss function
Optimizer
Training loop
```

### Day 17: Build Your First Neural Network

Project:

```text
Handwritten Digit Classifier
```

Use MNIST.

You should understand the training loop:

```python
for epoch in range(epochs):
    for X, y in dataloader:

        prediction = model(X)

        loss = loss_function(prediction, y)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()
```

Understand every line.

### Day 18: CNN Basics

Learn:

```text
Convolution
Filters
Pooling
Feature Maps
```

Build:

```text
Cat vs Dog Classifier
```

You don't need to train huge models from scratch. Use a smaller dataset or transfer learning.

### Day 19: NLP Basics

Learn:

```text
Tokenization
Embeddings
Text Classification
Transformers
LLMs
```

Build:

```text
Sentiment Analysis App
```

Example:

```text
"This movie is amazing"

→ Positive
```

### Day 20-21: Transformers + Hugging Face

This is extremely valuable for current AI development.

Learn:

```text
Pretrained models
Pipelines
Tokenizers
Embeddings
Inference
Model loading
```

Build:

```text
AI Text Summarizer
```

or:

```text
Sentiment Analyzer
```

---

# Week 4: Real AI Engineering

This is where your existing MERN skills become a major advantage.

You should combine:

```text
React / Next.js
        +
Python
        +
FastAPI
        +
Machine Learning
        +
LLMs
        +
Database
```

### Day 22: FastAPI

Learn how to expose your ML model through an API.

Example architecture:

```text
React / Next.js
       │
       ▼
    FastAPI
       │
       ▼
 Machine Learning Model
```

Example:

```python
from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "ML API Running"}
```

Then create prediction endpoints.

### Day 23: Docker

Learn:

```text
Dockerfile
Image
Container
Port mapping
Environment variables
```

Containerize your FastAPI project.

Architecture:

```text
Docker
   │
   ├── FastAPI
   └── ML Model
```

### Day 24-25: Build Project 2

Build an **AI Resume Analyzer**.

Architecture:

```text
React / Next.js
       │
       ▼
    FastAPI
       │
       ├── Resume Text Extraction
       │
       ├── AI/LLM Analysis
       │
       └── Skill Matching
```

Features:

```text
Upload Resume
Extract Text
Analyze Skills
Compare with Job Description
Generate Match Score
Show Missing Skills
AI Suggestions
```

This project fits perfectly with your existing full-stack background.

### Day 26-27: Build Project 3

Build a **Document Chatbot using RAG**.

Architecture:

```text
User uploads PDF
        ↓
Extract text
        ↓
Split into chunks
        ↓
Create embeddings
        ↓
Vector Database
        ↓
User asks question
        ↓
Similarity Search
        ↓
Relevant Context
        ↓
LLM
        ↓
Answer
```

Learn these concepts:

```text
Embeddings
Vector Database
Chunking
Similarity Search
RAG
Prompt Engineering
```

This is probably the most valuable project for your portfolio.

### Day 28: Deployment

Deploy your projects.

Learn:

```text
Environment variables
API deployment
Frontend deployment
Docker deployment
```

Your portfolio should contain live demos and GitHub repositories.

### Day 29: GitHub Cleanup

Your GitHub repositories should have a proper README.

Example structure:

```text
Project Name

Description

Features

Tech Stack

Architecture

Installation

Environment Variables

API Documentation

Screenshots

Demo
```

Don't upload 20 tutorial projects.

Have 3 to 4 serious projects.

### Day 30: Interview Preparation

Prepare for these questions:

```text
What is supervised learning?
What is overfitting?
What is underfitting?
What is train/test split?
What is cross validation?
What is precision and recall?
What is a confusion matrix?
What is gradient descent?
What is backpropagation?
What is an embedding?
What is RAG?
What is a vector database?
What is an LLM?
What is FastAPI?
How do you deploy an ML model?
```

Also be able to explain your own projects deeply.

## Your final skill stack after 30 days

Focus on this stack:

```text
PYTHON
   │
   ├── NumPy
   ├── Pandas
   ├── Matplotlib
   │
   ▼
SCIKIT-LEARN
   │
   ├── Regression
   ├── Classification
   ├── Preprocessing
   └── Evaluation
   │
   ▼
PYTORCH
   │
   ├── Neural Networks
   └── CNN Basics
   │
   ▼
AI / LLMS
   │
   ├── Hugging Face
   ├── Transformers
   ├── Embeddings
   └── RAG
   │
   ▼
DEPLOYMENT
   │
   ├── FastAPI
   ├── Docker
   └── Next.js
```

## The 3 projects I recommend for you

Given your existing full-stack experience, build these:

**1. Customer Churn Prediction System**

```text
Next.js Frontend
+
FastAPI
+
Scikit-learn
+
MongoDB/PostgreSQL
```

**2. AI Resume Analyzer**

```text
Upload Resume
+
Extract Text
+
AI Analysis
+
Job Description Matching
+
Skill Gap Analysis
```

**3. RAG Document Chatbot**

```text
PDF Upload
+
Embeddings
+
Vector Database
+
LLM
+
Chat Interface
```

These are much better for your profile than simple notebook-only projects.

## What to avoid during this month

Don't spend your 30 days trying to learn all of this:

```text
TensorFlow
PyTorch
LangChain
LangGraph
CrewAI
AutoGen
Computer Vision
NLP
Reinforcement Learning
MLOps
Kubernetes
Advanced Mathematics
Research Papers
```

You will end up knowing a little about everything and not being able to build anything properly.

Your fastest path is:

```text
Python
    ↓
NumPy + Pandas
    ↓
Scikit-learn
    ↓
One Deep Learning Framework
    ↓
LLM + RAG
    ↓
FastAPI
    ↓
Deploy Real Projects
```
