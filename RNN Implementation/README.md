# RNN-Based Text Generation

## Overview

This project explores how a **Recurrent Neural Network (RNN)** can learn sequential patterns in text and generate new text by predicting one word at a time.

The experiment uses the **Tiny Shakespeare** text corpus and implements a word-level Simple RNN using TensorFlow and Keras. The workflow covers text preprocessing, vocabulary creation, sequence generation, model development, training, evaluation, and text generation from different seed inputs.

The main objective is to understand how an RNN uses previously observed words to predict what comes next and how factors such as sequence length and training epochs affect the generated output.

---

## Dataset

**Dataset:** Tiny Shakespeare

The dataset contains Shakespeare's works and provides a relatively compact corpus for experimenting with language modeling and text generation.

The text was:

* Converted to lowercase
* Tokenized into individual words
* Mapped to integer IDs using a vocabulary
* Converted into fixed-length input sequences
* Split into training and validation sets

---

## Workflow

```text
Raw Text
   ↓
Text Preprocessing
   ↓
Word Tokenization
   ↓
Vocabulary Creation
   ↓
Integer Encoding
   ↓
Input Sequence Generation
   ↓
Padding
   ↓
Train / Validation Split
   ↓
Embedding Layer
   ↓
Simple RNN
   ↓
Dense + Softmax
   ↓
Model Training
   ↓
Next-Word Prediction
   ↓
Generated Text
```

---

## Model Architecture

The model consists of three main layers:

| Layer           | Purpose                                                |
| --------------- | ------------------------------------------------------ |
| Embedding       | Converts word IDs into dense numerical representations |
| Simple RNN      | Learns sequential relationships between words          |
| Dense + Softmax | Produces probabilities for the next word               |

The model uses:

* **Embedding dimension:** 128
* **RNN units:** 128
* **Optimizer:** Adam
* **Loss function:** Sparse Categorical Cross-Entropy
* **Output activation:** Softmax
* **Sequence length:** 10
* **Training epochs:** 10
* **Batch size:** 128

---

## Training and Evaluation

The model was trained using the prepared training sequences and evaluated on unseen validation sequences after each epoch.

Training and validation accuracy and loss were recorded to observe the learning behaviour of the model.

### Accuracy

The accuracy plot shows how effectively the model predicts the correct next word during training and validation.

<img width="708" height="470" alt="image" src="https://github.com/user-attachments/assets/93573289-db22-4e21-bbab-4f9b6d3af744" />


### Loss

The loss plot shows the difference between the predicted probability distribution and the actual next word.

<img width="691" height="470" alt="image" src="https://github.com/user-attachments/assets/9b997b60-feb4-4ff7-b9bc-206979f07149" />


### Final Performance

Add the actual values obtained during training:

```text
Training Accuracy   : 24.61%
Validation Accuracy : 7.21%
Training Loss       : 3.9798
Validation Loss     : 7.6164
```

---

## Text Generation

After training, the model was used to generate text from multiple seed inputs.

The generation process repeatedly:

1. Converts the current text into token IDs.
2. Keeps the required sequence length.
3. Passes the sequence through the trained RNN.
4. Predicts the probability of each vocabulary word.
5. Selects the predicted next word.
6. Appends the word to the existing text.
7. Repeats the process to generate a longer sequence.

### Sample Generation

**Seed:** `the king`

```text
the king is dead and all the world is not the dead and by the bright of war i have not the
```

**Seed:** `i am`

```text
i am ready to be revenged on him that i have not to the crown king richard ii we shall be satisfied
```

**Seed:** `my lord`

```text
my lord wherein i not speak of thy speech and i have heard the face of him first servingman what is the
```

**Seed:** `this is`

```text
this is death within the world that slew me gaunt in this my tongue is my lord king richard iii what is
```

**Seed:** `when the`

```text
when the nobles was not to the court cupboard i have been in the house of york that i have done to
```

---

## Observations

The generated text showed vocabulary and word patterns similar to the Shakespeare training corpus. Different seed inputs produced different continuations, with several outputs containing contextually related words such as *king, lord, crown, court, nobles, war,* and *death*.

The model demonstrated reasonable local word relationships, but some generated sequences contained grammatical inconsistencies, repetition, and incomplete phrases. This indicates that the Simple RNN learned patterns from the training corpus but had limitations in maintaining longer-term context.

---

## Key Learning

This experiment demonstrates the basic pipeline of a word-level RNN language model:

**Text → Sequences → RNN → Next-word prediction → Generated text**

It also highlights the importance of preprocessing, sequence length, training duration, and validation performance when building sequence-based deep learning models.

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib
* Google Colab
* Hugging Face / Tiny Shakespeare dataset

---
## Conclusion

A Simple RNN was successfully implemented for word-level text generation. The model learned sequential word patterns from the Tiny Shakespeare corpus and generated text from multiple seed inputs. Although the generated text was not consistently grammatically correct, it demonstrated that the model could learn and reproduce patterns present in the training data.
