# LSTM-Based Sentiment Analysis

A deep learning project that uses Long Short-Term Memory (LSTM) networks to classify movie reviews as positive or negative based on their textual content.

## Overview

Understanding sentiment in textual data is an important Natural Language Processing (NLP) task. This project explores how recurrent neural networks, particularly LSTMs, can learn sequential patterns in text to identify sentiment.

Using the IMDB Movie Reviews dataset, the model processes review text, learns contextual representations, and predicts the sentiment of unseen reviews.

The project covers the complete workflow, from text preprocessing and sequence generation to model training, evaluation, and inference.

## Key Features

* **Text preprocessing:** Normalizes text and removes punctuation.
* **Tokenization and vectorization:** Builds a vocabulary and converts text into numerical sequences.
* **Sequence padding:** Ensures consistent input dimensions.
* **LSTM architecture:** Learns sequential dependencies in movie reviews.
* **Model evaluation:** Measures performance using accuracy, precision, recall, and F1-score.
* **Performance visualization:** Plots training and validation accuracy and loss.
* **Sentiment inference:** Predicts sentiment for new review samples.
* **Error analysis:** Uses a confusion matrix to examine classification errors.

## Tech Stack

| Technology          | Purpose                               |
| ------------------- | ------------------------------------- |
| Python              | Core programming language             |
| TensorFlow / Keras  | Model development and training        |
| TensorFlow Datasets | Dataset loading                       |
| NumPy               | Numerical operations                  |
| Pandas              | Results organization                  |
| Matplotlib          | Performance visualization             |
| Scikit-learn        | Evaluation metrics                    |
| Google Colab        | Development and execution environment |

## Dataset

**IMDB Movie Reviews**

The project uses the IMDB Movie Reviews dataset, containing 50,000 movie reviews labeled as positive or negative.

| Property            | Description                     |
| ------------------- | ------------------------------- |
| Total reviews       | 50,000                          |
| Training split      | 25,000 reviews                  |
| Test split          | 25,000 reviews                  |
| Classification type | Binary sentiment classification |
| Negative label      | 0                               |
| Positive label      | 1                               |

The training split is further divided into training and validation subsets. The test split is reserved for final model evaluation.

Dataset source: [TensorFlow Datasets — IMDB Reviews](https://www.tensorflow.org/datasets/catalog/imdb_reviews)

## Methodology

The workflow consists of four stages.

### 1. Text Preprocessing

Raw movie reviews are converted into a format suitable for neural network training.

* Convert text to lowercase.
* Remove punctuation.
* Tokenize reviews and construct a vocabulary.
* Map tokens to integer indices.
* Pad or truncate sequences to a fixed length.

The vocabulary is learned from the training data to avoid using test data during preprocessing setup.

### 2. Model Architecture

The model uses an embedding layer followed by an LSTM layer and a binary classification output.

```text
Input Review
     |
     v
Text Vectorization
     |
     v
Embedding Layer
(64-dimensional vectors)
     |
     v
LSTM Layer
(64 units)
     |
     v
Dropout (0.3)
     |
     v
Dense Layer
(Sigmoid Activation)
     |
     v
Positive / Negative
```

**Layer descriptions**

* **Embedding:** Learns dense vector representations for words.
* **LSTM:** Captures sequential information and relationships between words.
* **Dropout:** Helps reduce overfitting during training.
* **Sigmoid output:** Produces a probability used to assign a sentiment label.

The model is compiled with the Adam optimizer and binary cross-entropy loss.

### 3. Training and Validation

The model is trained on the training subset and monitored using the validation subset.

The initial configuration uses a vocabulary limit of 10,000 tokens, a maximum sequence length of 250, an embedding dimension of 64, 64 LSTM units, a batch size of 64, and five training epochs.

These values provide a baseline configuration and can be adjusted through further experimentation.

### 4. Evaluation and Inference

The trained model is evaluated on the separate test dataset using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix

Training and validation curves are used to examine learning behavior and identify potential overfitting.

The model is also tested on new movie reviews to demonstrate how it performs on text outside the training examples.

---
