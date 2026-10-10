# Text Preprocessing and Word2Vec Word Embeddings

A Natural Language Processing (NLP) implementation exploring how raw text can be cleaned, analyzed, and transformed into numerical word representations using **NLTK and Word2Vec**.

## Overview

Text data often contains punctuation, stop words, and different forms of the same word. Preprocessing helps standardize this text before it is used for NLP tasks.

This project demonstrates a complete text-processing workflow using the **Brown Corpus** and trains a Word2Vec model to learn word embeddings based on contextual relationships between words.

## Objectives

* Perform text preprocessing using NLTK.
* Remove punctuation and stop words and apply lemmatization.
* Analyze word frequencies and vocabulary size.
* Generate word embeddings using the Word2Vec Skip-gram architecture.
* Identify contextually similar words.
* Calculate and interpret cosine similarity between word pairs.

## Technologies Used

* **Python** — Core programming language
* **NLTK** — Tokenization, stop-word removal, lemmatization, and corpus analysis
* **Gensim** — Word2Vec model training
* **NumPy** — Numerical operations
* **Matplotlib** — Visualization of word frequencies and similarity scores
* **Brown Corpus** — Text dataset for training and analysis

## Methodology

### 1. Text Preprocessing

The Brown Corpus is loaded using NLTK. The selected text is then processed through the following steps:

1. Convert text to lowercase.
2. Tokenize sentences into individual words.
3. Remove punctuation and non-alphabetic tokens.
4. Remove common English stop words.
5. Apply WordNet lemmatization to normalize word forms.

The original and preprocessed text can be compared to understand the effect of each step.

### 2. Vocabulary and Frequency Analysis

The preprocessed tokens are analyzed to determine:

* Total number of tokens
* Vocabulary size
* Ten most frequent words

Word frequency distribution is visualized using Matplotlib.

### 3. Word2Vec Embeddings

A Word2Vec model is trained using the **Skip-gram architecture (`sg=1`)**.

The model learns vector representations of words based on the words appearing around them in the training text.

Key configuration:

| Parameter              | Value     |
| ---------------------- | --------- |
| Architecture           | Skip-gram |
| Vector size            | 100       |
| Context window         | 5         |
| Minimum word frequency | 2         |
| Training epochs        | 10        |

The trained model is used to retrieve word vectors and identify words with similar embedding representations.

### 4. Cosine Similarity

Cosine similarity is calculated for selected word pairs to compare their learned vector representations.

The results help examine how words used in similar contexts are represented in the embedding space. Similarity scores depend on the dataset, preprocessing choices, and model training.

---
