# Single-Layer-Perceptron
Implementation of a Single Layer Perceptron in Python using NumPy to perform binary classification on AND, OR, and custom datasets.

## Overview

This project implements a **Single Layer Perceptron** from scratch using **Python** and **NumPy**. The perceptron is one of the simplest neural network models used for binary classification. It learns by adjusting its weights based on prediction errors during training.

The implementation demonstrates the working of a perceptron on:

- AND Logic Gate
- OR Logic Gate
- Custom Binary Classification Dataset

---

## Features

- Perceptron implemented from scratch
- Random weight initialization
- Heaviside Step Activation Function
- Weight updates using Perceptron Learning Rule
- Prediction and Accuracy Calculation
- Multiple dataset testing

---

## Technologies Used

- Python
- NumPy
- Google Colab

---

## Algorithm

1. Initialize weights randomly.
2. Compute the weighted sum.
3. Apply the Heaviside Step Function.
4. Compare prediction with target.
5. Update weights if prediction is incorrect.
6. Repeat for multiple epochs until convergence.

---

## Datasets

### AND Gate

| Input 1 | Input 2 | Output |
|---------|---------|--------|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

---

### OR Gate

| Input 1 | Input 2 | Output |
|---------|---------|--------|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

---

### Custom Dataset

| Feature 1 | Feature 2 | Output |
|-----------|-----------|--------|
|0|0|0|
|0|1|0|
|1|0|1|
|1|1|1|
|1|1|1|
|0|0|0|

---

## Sample Output

```
AND prediction: [0 0 0 1]
AND accuracy: 100.0

OR prediction: [0 1 1 1]
OR accuracy: 100.0

prediction: [0 0 1 1 1 0]
accuracy: 100.0
```

---

## Learning Outcome

This project demonstrates how a single-layer perceptron learns linearly separable patterns by iteratively updating its weights using the perceptron learning algorithm.

---

## Author

Janani K.
Artificial Intelligence and Data Science
